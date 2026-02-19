import os
import sys
import traceback
import click

from lib.workflow.ocp_nfs_helm import install as nfs

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("nfs")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Helm chart url")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Helm chart namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Helm chart name")
@click.option("--version", default='', callback=validations.empty_string_to_none, help="Helm chart version")
def set_ocp_nfs_command(
        ctx,
        cluster_name,
        url,
        namespace,
        name,
        version
        ):
    """Set ocp cluster nfs"""

    # iserver set ocp nfs

    ctx.developer = False

    try:
        params = {}
        params['cluster'] = cluster_name
        params['helm_repo'] = url
        params['helm_namespace'] = namespace
        params['helm_name'] = name
        params['helm_version'] = version

        success = nfs.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
