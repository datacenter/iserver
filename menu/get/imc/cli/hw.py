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


@click.command("hw")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="IMC IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['all'], help="[bbu|cpu|dimm|flex|hdd|memory|net|pci|psu|sc|tpm|vic|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_imc_cli_hw_command(
        ctx,
        endpoint_ip,
        username,
        password,
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get imc hardware"""

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'bbu|cpu|dimm|flex|hdd|memory|net|pci|psu|sc|tpm|vic|all',
        'all',
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

        bbu_info = False
        if 'bbu' in view:
            bbu_info = True

        cpu_info = False
        if 'cpu' in view:
            cpu_info = True

        dimm_info = False
        if 'dimm' in view:
            dimm_info = True

        flex_info = False
        if 'flex' in view:
            flex_info = True

        hdd_info = False
        if 'hdd' in view:
            hdd_info = True

        memory_info = False
        if 'memory' in view:
            memory_info = True

        net_info = False
        if 'net' in view:
            net_info = True

        pci_info = False
        if 'pci' in view:
            pci_info = True

        psu_info = False
        if 'psu' in view:
            psu_info = True

        sc_info = False
        if 'sc' in view:
            sc_info = True

        tpm_info = False
        if 'tpm' in view:
            tpm_info = True

        vic_info = False
        if 'vic' in view:
            vic_info = True

        response = []

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

            admin = endpoint_handler.get_hardware(
                bbu_info=bbu_info,
                cpu_info=cpu_info,
                dimm_info=dimm_info,
                flex_info=flex_info,
                hdd_info=hdd_info,
                memory_info=memory_info,
                net_info=net_info,
                pci_info=pci_info,
                psu_info=psu_info,
                sc_info=sc_info,
                tpm_info=tpm_info,
                vic_info=vic_info
            )
            if admin is None:
                ctx.my_output.error('Failed to get hardware settings from: %s' % (item['ip']))
            else:
                response.append(
                    admin
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

        if output == 'default':
            imc_output_handler.print_imc_hardware(response)

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   bbu, cpu, dimm, flex, hdd, memory, net, pci, psu, sc, tpm, vic, all')
        ctx.my_output.default('Output: default, compare, json')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
