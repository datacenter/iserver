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


@click.command("adapter")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="IMC IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['state'], help="[state|ext|fc|host|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'compare', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_imc_cli_adapter_command(
        ctx,
        endpoint_ip,
        username,
        password,
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get imc adapter"""

    # iserver get imc adapter

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|ext|fc|host|all',
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

        response = {}
        response['state'] = []
        response['ext'] = []
        response['fc'] = []
        response['host'] = []

        if output != 'json':
            bar_handler = Bar('Progress', max=len(endpoints))
            bar_handler.goto(0)

        for item in endpoints:
            endpoint_handler = endpoint.ImcCliEndpoint(
                item['ip'],
                item['port'],
                item['username'],
                item['password'],
                cache_ttl=cache_ttl,
                log_id=ctx.run_id
            )

            if 'state' in view:
                adapter = endpoint_handler.get_adapter()
                if adapter is None:
                    ctx.my_output.error('Failed to get adapter from: %s' % (item['ip']))
                else:
                    response['state'] = response['state'] + adapter

            if 'ext' in view:
                adapter_ext = endpoint_handler.get_adapter_ext()
                if adapter_ext is None:
                    ctx.my_output.error('Failed to get adapter ext interfaces from: %s' % (item['ip']))
                else:
                    response['ext'] = response['ext'] + adapter_ext

            if 'fc' in view:
                adapter_fc = endpoint_handler.get_adapter_fc()
                if adapter_fc is None:
                    ctx.my_output.error('Failed to get adapter fc interfaces from: %s' % (item['ip']))
                else:
                    response['fc'] = response['fc'] + adapter_fc

            if 'host' in view:
                adapter_host = endpoint_handler.get_adapter_host()
                if adapter_host is None:
                    ctx.my_output.error('Failed to get adapter host interfaces from: %s' % (item['ip']))
                else:
                    response['host'] = response['host'] + adapter_host

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
                imc_output_handler.print_imc_adapter(response['state'])

            if output == 'compare':
                imc_output_handler.print_imc_adapter_compare(response['state'])

        if 'ext' in view:
            if output == 'default':
                imc_output_handler.print_imc_adapter_ext(response['ext'])

        if 'fc' in view:
            if output == 'default':
                imc_output_handler.print_imc_adapter_fc(response['fc'])

        if 'host' in view:
            if output == 'default':
                imc_output_handler.print_imc_adapter_host(response['host'])

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   state, ext, fc, host, all')
        ctx.my_output.default('Output: default (def), compare, json')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
