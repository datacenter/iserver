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


@click.command("vm")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant")
@click.option("--img", "image", default='', callback=validations.empty_string_to_none, help="Filter by image")
@click.option("--flv", "flavor", default='', callback=validations.empty_string_to_none, help="Filter by flavor")
@click.option("--net", "network", default='', callback=validations.empty_string_to_none, help="Filter by network")
@click.option("--address", default='', callback=validations.validate_ip_subnet, help="Filter by ip address")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--hv", "hypervisor", default='', callback=validations.empty_string_to_none, help="Filter by hypervisor")
@click.option("--view", "-v", default=['state'], help="[state|id|net|sec|console|logs|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_vm_command(
        ctx,
        cluster,
        name,
        tenant,
        image,
        flavor,
        network,
        address,
        mac,
        hypervisor,
        view,
        output,
        devel
        ):
    """Get osp virtual machine"""

    # iserver get osp vm

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|net|sec|console|logs|all',
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
        flavor_info = False
        image_info = False
        volume_info = False
        network_info = False
        subnet_info = False
        port_info = False
        security_info = False
        console_info = False
        logs_info = False

        object_filter = []

        if name is not None:
            if len(name.split('/')) == 2:
                (tenant, name) = name.split('/')
            object_filter.append('name:%s' % (name))

        if tenant is not None:
            tenant_info = True
            object_filter.append('tenant_name:%s' % (tenant))

        if image is not None:
            image_info = True
            object_filter.append('image_name:%s' % (image))

        if flavor is not None:
            flavor_info = True
            object_filter.append('flavor_name:%s' % (flavor))

        if network is not None:
            object_filter.append('network_name:%s' % (network))

        if len(address) > 0:
            network_info = True
            subnet_info = True
            object_filter.append('address:%s' % (address))

        if mac is not None:
            network_info = True
            subnet_info = True
            object_filter.append('mac:%s' % (mac))

        if hypervisor is not None:
            object_filter.append('hypervisor:%s' % (hypervisor))

        if 'state' in view:
            tenant_info = True
            flavor_info = True
            image_info = True
            volume_info = True

        if 'net' in view:
            tenant_info = True
            network_info = True
            subnet_info = True

        if 'sec' in view:
            tenant_info = True
            network_info = True
            subnet_info = True
            port_info = True
            security_info = True

        if 'console' in view:
            tenant_info = True
            console_info = True

        if 'logs' in view:
            logs_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        vms = osp_handlers.get_virtual_machines(
            object_filter=object_filter,
            tenant_info=tenant_info,
            flavor_info=flavor_info,
            image_info=image_info,
            volume_info=volume_info,
            network_info=network_info,
            subnet_info=subnet_info,
            port_info=port_info,
            security_info=security_info,
            console_info=console_info,
            logs_info=logs_info
        )

        if 'sec' in view:
            security_group_names = []
            for vm_info in vms:
                for interface_info in vm_info['interface']:
                    for security_group_name in interface_info['port_info']['security_group_names']:
                        if security_group_name not in security_group_names:
                            security_group_names.append(
                                security_group_name
                            )

            if len(security_group_names) == 0:
                security_groups = []

            if len(security_group_names) > 0:
                object_filter = []
                object_filter.append(
                    'names:%s' % (','.join(security_group_names))
                )

                security_groups = osp_handlers.get_security_groups(
                    object_filter=object_filter,
                    tenant_info=True,
                    rule_info=True,
                    port_info=False
                )

        ctx.busy = False

        if vms is None:
            ctx.my_output.error(
                'Failed to get virtual machines'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    vms,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(vms)

        if 'state' in view:
            osp_output_handler.print_virtual_machines(
                vms,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_virtual_machines_id(
                vms,
                title=True
            )

        if 'net' in view:
            osp_output_handler.print_virtual_machines_net(
                vms,
                title=True
            )

        if 'sec' in view:
            osp_output_handler.print_virtual_machines_sec(
                vms,
                title=True
            )

            osp_output_handler.print_security_groups_rule(
                security_groups,
                title=True
            )

        if 'console' in view:
            osp_output_handler.print_virtual_machines_console(
                vms,
                title=True
            )

        if 'logs' in view:
            osp_output_handler.print_virtual_machines_logs(
                vms
            )

        ctx.my_output.default('Filter: name, tenant, img, flv, net, address, mac, hv', before_newline=True)
        ctx.my_output.default('View:   state (def), id, net, sec, console, logs, all')

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
