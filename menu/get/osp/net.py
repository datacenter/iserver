import sys
import json
import threading
import traceback
import click

from lib.osp import output as osp_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("net")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by network name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--ext", "external", is_flag=True, show_default=True, default=False, help="Filter external network")
@click.option("--address", default='', callback=validations.validate_ip, help="Filter by ip address")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by port mac address")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine")
@click.option("--hv", "hypervisor", default='', callback=validations.empty_string_to_none, help="Filter by hypervisor")
@click.option("--vlan", default='', callback=validations.empty_string_to_none, help="Filter by vlan")
@click.option("--view", "-v", default=['state'], help="[state|id|port|phy|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_net_command(
        ctx,
        cluster,
        name,
        tenant,
        external,
        address,
        mac,
        virtual_machine,
        hypervisor,
        vlan,
        view,
        output,
        devel
        ):
    """Get osp network"""

    # iserver get osp net

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|port|phy|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        tenant_info = False
        port_info = False
        subnet_info = False
        router_info = False

        if 'state' in view:
            tenant_info = True
            subnet_info = True
            router_info = True

        if 'port' in view:
            tenant_info = True
            subnet_info = True
            port_info = True

        if 'phy' in view:
            tenant_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if tenant is not None:
            tenant_info = True
            object_filter.append(
                'tenant_name:%s' % (tenant)
            )

        if external:
            object_filter.append(
                'external:true'
            )

        if address is not None and len(address) > 0:
            subnet_info = True
            object_filter.append(
                'address:%s' % (address)
            )

        if mac is not None:
            port_info = True
            object_filter.append(
                'mac:%s' % (mac)
            )

        if virtual_machine is not None:
            port_info = True
            object_filter.append(
                'vm_name:%s' % (virtual_machine)
            )

        if hypervisor is not None:
            port_info = True
            object_filter.append(
                'hv:%s' % (hypervisor)
            )

        if vlan is not None:
            object_filter.append(
                'vlan:%s' % (vlan)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        networks = osp_handlers.get_networks(
            object_filter=object_filter,
            tenant_info=tenant_info,
            subnet_info=subnet_info,
            port_info=port_info,
            router_info=router_info
        )

        ctx.busy = False

        if networks is None:
            ctx.my_output.error(
                'Failed to get networks'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    networks,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(networks)

        if 'state' in view:
            osp_output_handler.print_networks(
                networks,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_networks_id(
                networks,
                title=True
            )

        if 'port' in view:
            osp_output_handler.print_networks_port(
                networks,
                title=True
            )

        if 'phy' in view:
            osp_output_handler.print_networks_phy(
                networks,
                title=True
            )

        ctx.my_output.default('Filter: name, tenant, address, mac, vm, hv, vlan', before_newline=True)
        ctx.my_output.default('View:   state (def), id, port, phy, all')

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
