import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_intersight_operator import operator_create
from lib.workflow.ocp_intersight_operator import instance_create
from lib.workflow.ocp_intersight_operator import enable_plugin
from lib.workflow.ocp_intersight_operator import register

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("intersight")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['operator', 'instance', 'ui', 'register', 'all'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--channel", default='__default__', show_default=True, help="Operator channel")
@click.option("--ucs-tool", is_flag=True, show_default=True, default=False, help="Enable OsDiscoveryToolInstall")
@click.option("--client-id", default='', callback=validations.empty_string_to_none, help="Intersight client id")
@click.option("--client-secret", default='', callback=validations.empty_string_to_none, help="Intersight client secret")
@click.option("--location", type=click.Choice(['us', 'eu', 'va'], case_sensitive=False), default='us', show_default=True, help="Intersight server location")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_intersight_command(ctx, cluster_name, channel, mode, ucs_tool, client_id, client_secret, location, no_confirm):
    """Set intersight operator in openshift cluster"""

    try:
        if mode in ['operator', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['channel'] = channel
            params['confirmation'] = not no_confirm

            success = operator_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['instance', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['ucs-tool'] = ucs_tool
            params['confirmation'] = not no_confirm

            success = instance_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['ui', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['confirmation'] = not no_confirm

            success = enable_plugin.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode in ['register', 'all']:
            params = {}
            params['cluster'] = cluster_name
            params['client-id'] = client_id
            params['client-secret'] = client_secret
            params['location'] = location
            params['confirmation'] = not no_confirm

            success = register.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit
                                    
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
