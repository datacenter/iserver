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


@click.command("nondefault")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Storage class name")
def set_k8s_sc_nondefault_command(
        ctx,
        cluster,
        name,
        ):
    """Set k8s storage class as non-default"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        if name is None:
            ctx.my_output.error(
                'Define storage class name'
            )
            raise ErrorExit
        
        k8s_handler = validations.validate_kubernetes_name(ctx, cluster, log_id=ctx.run_id)
        if k8s_handler is None:
            raise ErrorExit

        if k8s_handler.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit
        
        success = k8s_handler.unset_storage_class_default(name, my_output=ctx.my_output)
        if not success:
            raise ErrorExit

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
