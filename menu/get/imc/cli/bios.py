import sys
import json
import traceback
import click

from progress.bar import Bar

from lib.imc.cli import endpoint
from lib.imc.cli import output as imc_output

from menu import validations

from menu.get.imc.cli import common as imc_common
from menu.get.imc.cli import validations as imc_validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bios")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="IMC IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--key", "key_filter", multiple=True, help="Key filter")
@click.option("--type", "type_filter", multiple=True, help="Type filter")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['state'], help="[state|params|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'compare', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_imc_cli_bios_command(
        ctx,
        endpoint_ip,
        username,
        password,
        key_filter,
        type_filter,
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get imc bios"""

    # iserver get imc bios

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|params|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    cache_ttl = imc_validations.validate_cache_ttl(user_cache_ttl, log_id=ctx.run_id)
    imc_common.print_cache_ttl(ctx, output, cache_ttl)

    try:
        endpoints = imc_validations.get_imc_cli_endpoints(
            ctx,
            endpoint_ip,
            username,
            password
        )

        if endpoints is None:
            raise ErrorExit

        if len(endpoints) == 0:
            ctx.my_output.error('Define imc endpoints')
            raise ErrorExit

        response = []

        if output != 'json':
            bar_handler = Bar('Progress', max=len(endpoints))
            bar_handler.goto(0)

        state_info = False
        params_info = False

        if 'state' in view:
            state_info = True

        if 'params' in view:
            params_info = True

        for item in endpoints:
            endpoint_handler = endpoint.ImcCliEndpoint(
                item['ip'],
                item['port'],
                item['username'],
                item['password'],
                cache_ttl=cache_ttl,
                log_id=ctx.run_id
            )

            bios = endpoint_handler.get_bios(
                key_filter=key_filter,
                type_filter=type_filter,
                state_info=state_info,
                params_info=params_info
            )
            if bios is None:
                ctx.my_output.error('Failed to get bios from: %s' % (item['ip']))
            else:
                response.append(
                    bios
                )

            if output != 'json':
                bar_handler.next()

        if output != 'json':
            bar_handler.finish()

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    response,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(response)

        imc_output_handler = imc_output.ImcCliOutput(
            log_id=ctx.run_id
        )

        if 'state' in view:
            if output == 'default':
                imc_output_handler.print_imc_bios(response)

            if output == 'compare':
                imc_output_handler.print_imc_bios_compare(response)

        if 'params' in view:
            if output == 'default':
                imc_output_handler.print_imc_bios_params(response)

            if output == 'compare':
                imc_output_handler.print_imc_bios_params_compare(response)

        ctx.my_output.default('Filter: key, type', before_newline=True)
        ctx.my_output.default('View:   state, params, all')
        ctx.my_output.default('Output: default (def), compare, json')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
