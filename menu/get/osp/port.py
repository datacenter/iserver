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


@click.command("port")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by port name")
@click.option("--state", type=click.Choice(['active', 'down', 'any'], case_sensitive=False), default='any', show_default=True)
@click.option("--type", "port_type", type=click.Choice(['compute', 'dhcp', 'floating', 'gateway', 'ha', 'any'], case_sensitive=False), default='any', show_default=True)
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--net", "network", default='', callback=validations.empty_string_to_none, help="Filter by network name")
@click.option("--subnet", "subnet", default='', callback=validations.empty_string_to_none, help="Filter by subnet name")
@click.option("--address", default='', callback=validations.validate_ip_subnet, help="Filter by ip address")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--hv", "hypervisor", default='', callback=validations.empty_string_to_none, help="Filter by hypervisor")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine")
@click.option("--sg", "security_group", default='', callback=validations.empty_string_to_none, help="Filter by security group")
@click.option("--view", "-v", default=['state'], help="[state|id|sec|hv|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_port_command(
        ctx,
        cluster,
        name,
        state,
        port_type,
        tenant,
        network,
        subnet,
        address,
        mac,
        hypervisor,
        virtual_machine,
        security_group,
        view,
        output,
        devel
        ):
    """Get osp port"""

    # iserver get osp port

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|sec|hv|all',
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
        network_info = False
        subnet_info = False
        security_info = False
        vm_info = False
        fip_info = False

        if 'state' in view:
            tenant_info = True
            network_info = True
            subnet_info = True
            fip_info = True

        if 'sec' in view:
            security_info = True
            vm_info = True

        if 'hv' in view:
            vm_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if state != 'any':
            object_filter.append(
                'state:%s' % (state)
            )

        if port_type != 'any':
            object_filter.append(
                'type:%s' % (port_type)
            )

        if tenant is not None:
            tenant_info = True
            object_filter.append(
                'tenant_name:%s' % (tenant)
            )

        if network is not None:
            network_info = True
            object_filter.append(
                'network_name:%s' % (network)
            )

        if subnet is not None:
            subnet_info = True
            object_filter.append(
                'subnet_name:%s' % (subnet)
            )

        if address is not None:
            object_filter.append(
                'address:%s' % (address)
            )

        if mac is not None:
            object_filter.append(
                'mac:%s' % (mac)
            )

        if hypervisor is not None:
            object_filter.append(
                'hv:%s' % (hypervisor)
            )

        if virtual_machine is not None:
            vm_info = True
            object_filter.append(
                'vm_name:%s' % (virtual_machine)
            )

        if security_group is not None:
            security_info = True
            object_filter.append(
                'sg:%s' % (security_group)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ports = osp_handlers.get_ports(
            object_filter=object_filter,
            tenant_info=tenant_info,
            network_info=network_info,
            subnet_info=subnet_info,
            security_info=security_info,
            vm_info=vm_info,
            fip_info=fip_info
        )

        ctx.busy = False

        if ports is None:
            ctx.my_output.error(
                'Failed to get ports'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    ports,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(ports)

        if 'state' in view:
            osp_output_handler.print_ports(
                ports,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_ports_id(
                ports,
                title=True
            )

        if 'sec' in view:
            osp_output_handler.print_ports_security(
                ports,
                title=True
            )

        if 'hv' in view:
            osp_output_handler.print_ports_hv(
                ports,
                title=True
            )

        ctx.my_output.default('Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg', before_newline=True)
        ctx.my_output.default('View:   state (def), id, sec, hv, all')

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
