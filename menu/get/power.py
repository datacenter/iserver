import json
import sys
import time
import threading
import traceback
import yaml
import click

from lib.intersight import compute_info

from menu import defaults
from menu import common
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("power")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--empty", is_flag=True, show_default=True, default=False, help="Show servers with no power info")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_power_command(
        ctx,
        iaccount,
        group,
        ip_filter,
        name_filter,
        model_filter,
        empty,
        output,
        devel
        ):
    """Get servers' power info"""

    # iserver get power

    ctx.developer = devel

    try:
        if output not in ['json', 'yaml']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        settings = common.get_server_selection_settings(
            iaccount,
            workflow=None,
            enabled=['locator', 'power']
        )

        match_rules = common.get_no_match_definition()
        match_rules['name'] = name_filter
        match_rules['model'] = model_filter
        match_rules['ip'] = ip_filter
        match_rules['serials'] = group

        computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=ctx.run_id)
        servers = computes_handler.get(match_rules=match_rules)

        skipped = 0
        if not empty:
            non_empty = []
            for server in servers:
                if server['PowerSource'] != 'N/A':
                    non_empty.append(server)

            skipped = len(servers) - len(non_empty)
            servers = non_empty

        ctx.my_output.json_output(servers)

        if output == 'json':
            ctx.my_output.default(json.dumps(servers, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                servers,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.busy = False
        time.sleep(.1)

        computes_handler.print_power(servers)

        if skipped > 0:
            ctx.my_output.default('Skipped servers count: %s' % (skipped))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
