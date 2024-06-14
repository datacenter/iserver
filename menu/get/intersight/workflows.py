import json
import sys
import traceback
import yaml
import click

from progress.bar import Bar

from lib.intersight import compute
from lib.intersight import computes_worfklow
from lib.intersight import validations as intersight_validations

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
@click.option("--ip", "ip_filter", multiple=True, help="Select by IP or subnet")
@click.option("--name", "name_filter", multiple=True, callback=intersight_validations.name_filter, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, callback=intersight_validations.serial_filter, help="Select by serial")
@click.option("--model", "model_filter", multiple=True, callback=intersight_validations.model_filter, help="Select by model")
@click.option("--type", "type_filter", type=click.Choice(['any', 'blade', 'rack'], case_sensitive=False), default='any', show_default=True, help="Select by type")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Select by group name")
@click.option("--failed", "failed_filter", is_flag=True, default=False, help="Filter failed")
@click.option("--completed", "completed_filter", is_flag=True, default=False, help="Filter completed")
@click.option("--power", "power_filter", is_flag=True, default=False, help="Filter power related")
@click.option("--os", "os_filter", is_flag=True, default=False, help="Filter OS related")
@click.option("--fw", "fw_filter", is_flag=True, default=False, help="Filter firmware related")
@click.option("--count", default=-1, show_default=True, help="Last <n> count")
@click.option("--days", default=1, help="Last <n> days")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--order", "sorted_by", type=click.Choice(['server', 'workflow', 'date'], case_sensitive=False), default='date', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_workflows_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
        model_filter,
        type_filter,
        group_filter,
        failed_filter,
        completed_filter,
        power_filter,
        os_filter,
        fw_filter,
        count,
        days,
        user_cache_ttl,
        sorted_by,
        output,
        devel
        ):
    """Get workflows"""

    # iserver get is workflows

    ctx.developer = devel

    try:
        # default vs. user-defined cache_ttl
        cache_ttl = intersight_validations.validate_cache_ttl(user_cache_ttl, log_id=ctx.run_id)
        if cache_ttl is not None and cache_ttl < 0:
            ctx.my_output.error('Cache TTL must be gt 0')
            raise ErrorExit

        # Server details collection settings

        settings = {}
        settings['state'] = True
        settings['workflow'] = 86400 * days

        if output == 'default':
            ctx.my_output.default('Get servers info...')

        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        mo_match_rules = compute_handler.get_mo_match_rules(
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=intersight_validations.add_group_filter(serial_filter, group_filter),
            model_filter=model_filter
        )

        include_rack = True
        include_blade = True
        if type_filter == 'rack':
            include_blade = False
        if type_filter == 'blade':
            include_rack = False

        servers_mo = compute_handler.get_mo(
            match_rules=mo_match_rules,
            include_rack=include_rack,
            include_blade=include_blade,
            cache_ttl=None
        )

        compute_handler.set_cache(
            servers_mo,
            settings,
            cache_ttl,
            ctx=ctx
        )

        bar_handler = None
        if output == 'default':
            bar_handler = Bar('Collect server information', max=len(servers_mo))
            bar_handler.goto(0)

        match_rules = {}
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            match_rules,
            cache_ttl,
            prepare_cache=False,
            bar_handler=bar_handler
        )

        workflows_settings = {}
        workflows_settings['failed'] = failed_filter
        workflows_settings['completed'] = completed_filter
        workflows_settings['power'] = power_filter
        workflows_settings['os'] = os_filter
        workflows_settings['fw'] = fw_filter
        workflows_settings['count'] = count
        workflows_settings['days'] = days
        workflows_settings['sorted'] = sorted_by

        workflows = compute_handler.get_servers_workflows(servers_info, workflows_settings)
        if len(workflows) == 0:
            ctx.my_output.default('No workflows found', before_newline=True)
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

        compute_output_handler = computes_worfklow.ComputesWorkflow(log_id=ctx.run_id)
        compute_output_handler.print_workflows(workflows)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
