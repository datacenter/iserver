import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("vlan")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "pool_name", default='', callback=validations.empty_string_to_none, help="Filter by pool name")
@click.option("--vlan", "vlan_id", default='', callback=validations.empty_string_to_none, help="Filter by vlan")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--view", "-v", type=click.Choice(['default', 'verbose'], case_sensitive=False), multiple=False, default='default')
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_pool_vlan_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        pool_name,
        vlan_id,
        domain_name,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci pool vlan"""

    # iserver get aci pool vlan

    ctx.developer = devel
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        pool_vlan_filter = []
        if pool_name is not None:
            pool_vlan_filter.append(
                'name:%s' % (pool_name)
            )

        if vlan_id is not None:
            pool_vlan_filter.append(
                'vlan:%s' % (vlan_id)
            )

        if domain_name is not None:
            pool_vlan_filter.append(
                'domain:%s' % (domain_name)
            )

        vlans = apic_handler.get_pool_vlans(
            pool_vlan_filter=pool_vlan_filter,
            vlan_usage_info=True
        )

        ctx.busy = False

        if vlans is None or len(vlans) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    vlans,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(vlans)

        if view == 'default':
            aci_output_handler.print_pool_vlans(
                vlans
            )

        if view == 'verbose':
            for vlan in vlans:
                aci_output_handler.print_pool_vlan(
                    vlan
                )

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
