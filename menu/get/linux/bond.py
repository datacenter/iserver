import sys
import json
import threading
import traceback
import click

from lib import ip_helper
from lib.linux import output as linux_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("bond")
@click.pass_obj
@click.option("--server", multiple=True, help="Linux server name")
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--nexus", "nexus", default='', callback=validations.validate_nexus_any_name, help="Nexus name")
@click.option("--view", "-v", default=['state'], help="[state|member|aci|nexus|all]", show_default=True, multiple=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_linux_bond_command(
        ctx,
        server,
        controller,
        nexus,
        view,
        no_cache,
        output,
        devel
        ):
    """Get linux bond state"""

    # iserver get linux bond

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|member|aci|nexus|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        if 'aci' in view and controller is None:
            ctx.my_output.default(
                '[WARNING] Define APIC for aci view'
            )

        if 'nexus' in view and len(nexus) == 0:
            ctx.my_output.default(
                '[WARNING] Define nexus devices for nexus view'
            )

        linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
        linux_handlers = validations.validate_linux_names(
            ctx,
            server,
            no_cache=no_cache
        )
        if linux_handlers is None:
            raise ErrorExit

        if 'aci' in view and controller is not None:
            apic_handler = validations.validate_apic_controller(
                ctx,
                controller,
                '',
                '',
                '',
                '',
                no_cache=True,
                show_selected=False
            )
            if apic_handler is None:
                raise ErrorExit

            nodes_info = validations.validate_apic_node_names(
                ctx,
                apic_handler,
                ['any'],
                'any',
                pod_id=''
            )
            if nodes_info is None:
                raise ErrorExit

        if 'nexus' in view and len(nexus) > 0:
            nexus_handlers = validations.validate_nexus_devices(
                ctx,
                nexus,
                '',
                '',
                ''
            )
            if nexus_handlers is None:
                raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        bonds = []
        for linux_handler in linux_handlers:
            server_bond_info = linux_handler.get_bond()
            if server_bond_info is not None:
                bonds = bonds + server_bond_info

        if 'aci' in view and controller is not None:
            mac_address = []
            for bond in bonds:
                for member in bond['member']:
                    mac_address.append(
                        member['mac']
                    )

            aci_lacp_infos = apic_handler.get_macs_lacp(
                mac_address,
                nodes_info
            )
            if aci_lacp_infos is not None:
                for aci_lacp_info in aci_lacp_infos:
                    aci_lacp_info['server'] = '--'
                    aci_lacp_info['interface'] = '--'
                    for bond in bonds:
                        for member in bond['member']:
                            if ip_helper.is_mac_equal(aci_lacp_info['adjacency']['sysId'], member['mac']):
                                aci_lacp_info['server'] = bond['server']
                                aci_lacp_info['interface'] = member['name']


        if 'nexus' in view and len(nexus) > 0:
            mac_address = []
            for bond in bonds:
                for member in bond['member']:
                    mac_address.append(
                        member['mac']
                    )

            nexus_lacp_infos = []
            for nexus_handler in nexus_handlers:
                nexus_lacp_info = nexus_handler['handler'].get_macs_lacp(
                    mac_address
                )
                if nexus_lacp_info is not None:
                    for lacp_info in nexus_lacp_info:
                        lacp_info['server'] = '--'
                        lacp_info['interface'] = '--'
                        for port in lacp_info['port']:
                            for bond in bonds:
                                for member in bond['member']:
                                    if ip_helper.is_mac_equal(port['partner_mac'], member['mac']):
                                        lacp_info['server'] = bond['server']
                                        lacp_info['interface'] = member['name']

                    nexus_lacp_infos = nexus_lacp_infos + nexus_lacp_info

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    bond,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(bonds)

        if 'state' in view:
            linux_output_handler.print_linux_bond(
                bonds,
                title=True
            )

        if 'member' in view:
            linux_output_handler.print_linux_bond_member(
                bonds,
                title=True
            )

        if 'aci' in view and controller is not None:
            linux_output_handler.print_linux_bond_aci(
                aci_lacp_infos,
                title=True
            )

        if 'nexus' in view and len(nexus) > 0:
            linux_output_handler.print_linux_bond_nexus(
                nexus_lacp_infos,
                title=True
            )

        ctx.my_output.default('\nViews: state (def), member, aci, all')

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
