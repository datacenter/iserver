import sys
import traceback
import click
from lib.workflow.k8s import dv_create as workflow
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("dv")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Name")
@click.option("--sc", "storage_class", default='', callback=validations.empty_string_to_none, help="Storage class")
@click.option("--source", "source_filename", default='', callback=validations.empty_string_to_none, help="Source filename")
@click.option("--secret", default='', callback=validations.empty_string_to_none, help="Secret reference")
@click.option("--size", default='', callback=validations.empty_string_to_none, help="Target PVC size")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def create_k8s_dv_command(
        ctx,
        cluster_name,
        namespace,
        name,
        storage_class,
        secret,
        size,
        source_filename,
        no_confirm
        ):
    """Create k8s dv"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['storage_class'] = storage_class
        params['source'] = source_filename
        params['secret'] = secret
        params['size'] = size
        params['confirmation'] = not no_confirm

        success = workflow.run(
            params,
            log_id=ctx.run_id
        )
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
