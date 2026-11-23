import sys
import traceback
import click
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("is")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_is_command(
        ctx,
        cluster,
        namespace,
        name,
        no_confirm
        ):
    """Delete k8s image stream (ocp)"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
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

        k8s_handlers.delete_image_streams(
            object_filter=object_filter, 
            my_output=ctx.my_output,
            confirmation=not no_confirm
        )

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
