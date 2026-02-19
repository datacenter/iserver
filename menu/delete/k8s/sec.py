import sys
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress
from progress.bar import Bar


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("sec")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_sec_command(
        ctx,
        cluster,
        namespace,
        name,
        no_confirm
        ):
    """Delete k8s secret"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []
        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        secrets = k8s_handlers.get_secrets(
            object_filter=object_filter,
            cache_enabled=False
        )

        ctx.busy = False

        if len(secrets) == 0:
            ctx.my_output.default('No object found')
            return

        k8s_output_handler.print_secrets(secrets)

        if not no_confirm:
            value = input('Confirm (Y/N) ')
            if value.lower() != 'y':
                return

        bar_handler = Bar('Delete objects', max=len(secrets))
        bar_handler.goto(0)

        success = True
        for secret in secrets:
            success = success and k8s_handlers.delete_secret_mo(secret['namespace'], secret['name'])
            bar_handler.next()

        bar_handler.finish()

        if not success:
            ctx.my_output.error('Some delete api calls failed')
            raise ErrorExit

        ctx.my_output.default('Done')

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
