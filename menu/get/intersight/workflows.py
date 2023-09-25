import json
import sys
import traceback
import yaml
import click

from lib.intersight import compute_info
from menu import common
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("workflows")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--type", "server_type", type=click.Choice(['all', 'blade', 'rack'], case_sensitive=False), default='rack', show_default=True)
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
@click.option("--failed", "failed_filter", is_flag=True, default=False, help="Filter failed")
@click.option("--completed", "completed_filter", is_flag=True, default=False, help="Filter completed")
@click.option("--power", "power_filter", is_flag=True, default=False, help="Filter power related")
@click.option("--os", "os_filter", is_flag=True, default=False, help="Filter OS related")
@click.option("--fw", "fw_filter", is_flag=True, default=False, help="Filter firmware related")
@click.option("--count", default=-1, show_default=True, help="Last <n> count")
@click.option("--days", default=1, help="Last <n> days")
@click.option("--order", "sorted_by", type=click.Choice(['server', 'workflow', 'date'], case_sensitive=False), default='date', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_workflows_command(
        ctx,
        iaccount,
        group,
        server_type,
        ip_filter,
        name_filter,
        model_filter,
        serial_filter,
        failed_filter,
        completed_filter,
        power_filter,
        os_filter,
        fw_filter,
        count,
        days,
        sorted_by,
        output,
        devel
        ):
    """Get workflows"""

    # iserver get is workflows

    ctx.developer = devel

    try:
        if output == 'default':
            ctx.my_output.default('Get servers info...')

        seconds = 86400 * days
        settings = common.get_server_selection_settings(
            iaccount,
            workflow=seconds,
            action=False,
            registration=False
        )
        if server_type.lower() == 'blade':
            settings['rack'] = False
        if server_type.lower() == 'rack':
            settings['blade'] = False

        match_rules = common.get_no_match_definition()
        match_rules['name'] = name_filter
        match_rules['model'] = model_filter
        match_rules['ip'] = ip_filter
        match_rules['serials'] = group
        if len(serial_filter) > 0:
            match_rules['serials'] = serial_filter

        computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=ctx.run_id)
        servers = computes_handler.get(match_rules=match_rules)
        if servers is None or len(servers) == 0:
            ctx.my_output.error('No servers found')
            raise ErrorExit

        if output == 'default':
            ctx.my_output.default('Get workflows info...')

        workflows_settings = {}
        workflows_settings['failed'] = failed_filter
        workflows_settings['completed'] = completed_filter
        workflows_settings['power'] = power_filter
        workflows_settings['os'] = os_filter
        workflows_settings['fw'] = fw_filter
        workflows_settings['count'] = count
        workflows_settings['days'] = days
        workflows_settings['sorted'] = sorted_by

        workflows = computes_handler.get_servers_workflows(servers, workflows_settings)
        if len(workflows) == 0:
            ctx.my_output.default('No workflows found')
            return

        if output == 'json':
            ctx.my_output.default(json.dumps(workflows, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                workflows,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        computes_handler.print_workflows(workflows)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
