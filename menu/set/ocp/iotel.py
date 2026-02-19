import sys
import traceback
import click

from menu import defaults
from menu import validations
from lib.workflow.ocp_iotel import instance_create
from lib.workflow.ocp_iotel import poller_create


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iotel")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--mode", type=click.Choice(['instance', 'poller'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--iaccount", default='', callback=validations.empty_string_to_none, help="Intersight account")
@click.option("--key", default='', callback=validations.empty_string_to_none, help="Intersight key id")
@click.option("--pem", default='', callback=validations.empty_string_to_none, help="Intersight pem filename")
@click.option("--suffix", default='', callback=validations.empty_string_to_none, help="Resources name suffix")
@click.option("--pollers", default='', callback=validations.empty_string_to_none, help="Pollers definition file")
@click.option("--dir", default='', callback=validations.empty_string_to_none, help="Template directory")
@click.option("--template", "ptemplate", multiple=True, help="Poller template")
@click.option("--target", "ptarget", multiple=True, help="Target server")
@click.option("--attribute", "pattribute", multiple=True, help="Extra metric attributes")
@click.option("--pmode", type=click.Choice(['add', 'set'], case_sensitive=False), default='add', show_default=True, help="Pollers modification mode")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_iotel_command(ctx, cluster_name, mode, iaccount, key, pem, suffix, pollers, dir, ptemplate, ptarget, pattribute, pmode, verbose, no_confirm):
    """Set openshift intersight open telemetry collector"""

    try:
        if mode == 'instance':
            params = {}
            params['cluster'] = cluster_name
            params['iaccount'] = iaccount
            params['key'] = key
            params['pem'] = pem
            params['suffix'] = suffix
            params['pollers'] = pollers
            params['verbose'] = verbose
            params['confirmation'] = not no_confirm

            success = instance_create.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit

        if mode == 'poller':
            params = {}
            params['cluster'] = cluster_name
            params['suffix'] = suffix
            params['pollers'] = pollers
            params['dir'] = dir
            params['mode'] = pmode
            params['template'] = []
            for item in ptemplate:
                params['template'].append(item)
            params['target'] = []
            for item in ptarget:
                params['target'].append(item)
            params['attribute'] = []
            for item in pattribute:
                params['attribute'].append(item)
            params['verbose'] = verbose
            params['confirmation'] = not no_confirm

            success = poller_create.run(
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
