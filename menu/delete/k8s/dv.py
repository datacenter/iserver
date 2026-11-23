import sys
import traceback
import click
from lib.workflow.k8s import dv_delete as workflow
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
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--force", is_flag=True, show_default=True, default=False, help="Force delete even if used")
@click.option("--unused", is_flag=True, show_default=True, default=False, help="Select unused data volumes")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_k8s_dv_command(
        ctx,
        cluster_name,
        namespace,
        name,
        force,
        unused,
        no_confirm
        ):
    """Delete k8s dv (ocp)"""

    # iserver delete k8s dv

    ctx.developer = False
    ctx.output = 'default'

    try:
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id)
        if k8s_handlers is None:
            raise ErrorExit

        params = {}
        params['cluster'] = cluster_name
        params['namespace'] = namespace
        params['name'] = name
        params['force'] = force
        params['unused'] = unused
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
