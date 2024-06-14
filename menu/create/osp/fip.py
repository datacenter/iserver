import os
import time
import json
import sys
import traceback
import threading
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import progress
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("fip")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--port", "port_id", default='', callback=validations.empty_string_to_none, help="Port id")
@click.option("--network", "network_name", default='', callback=validations.empty_string_to_none, help="Floating network name")
@click.option("--ip", "floating_ip", default='', callback=validations.empty_string_to_none, help="Floating IP address")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_fip_command(
        ctx,
        cluster_name,
        tenant_name,
        port_id,
        network_name,
        floating_ip,
        devel
        ):
    """Create osp fip"""

    # iserver create osp fip

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        tenant_id = None
        if port_id is None:
            object_filter = []
            if tenant_name is not None:
                object_filter.append(
                    'tenant_name:%s' % (tenant_name)
                )

            vms = osp_handlers.get_virtual_machines(
                object_filter=object_filter,
                tenant_info=True,
                flavor_info=True,
                image_info=True,
                volume_info=True,
                network_info=True,
                subnet_info=True
            )
            selected_vm = osp_output_handler.select_virtual_machine(vms)
            if selected_vm is None:
                raise ErrorExit

            tenant_id = selected_vm['tenant_id']
            tenant_name = selected_vm['tenant_name']
            ctx.my_output.default('Tenant id: %s' % (tenant_id))
            ctx.my_output.default('Tenant name: %s' % (tenant_name))

            object_filter = []
            object_filter.append(
                'vm_id:%s' % (selected_vm['id'])
            )
            ports = osp_handlers.get_ports(
                object_filter=object_filter,
                tenant_info=True,
                network_info=True,
                subnet_info=True,
                fip_info=True
            )
            selected_port = osp_output_handler.select_port(ports)
            if selected_port is None:
                raise ErrorExit

            port_id = selected_port['id']
            ctx.my_output.default('Port id: %s' % (selected_port['id']))

        if network_name is not None:
            network_info = osp_handlers.get_network(
                network_name=network_name
            )
            if network_info is None:
                ctx.my_output.error('Network not found: %s' % (network_name))
                raise ErrorExit

            if not network_info['external']:
                ctx.my_output.error('Network must be external: %s' % (network_name))
                raise ErrorExit

            network_id = network_info['id']

        if network_name is None:
            object_filter = []
            object_filter.append(
                'external:true'
            )

            networks = osp_handlers.get_networks(
                object_filter=object_filter,
                tenant_info=True,
                subnet_info=True,
                port_info=False,
                router_info=True
            )
            selected_network = osp_output_handler.select_network(networks)
            if selected_network is None:
                raise ErrorExit

            network_id = selected_network['id']
            network_name = selected_network['name']

        ctx.my_output.default('External network id: %s' % (network_id))
        ctx.my_output.default('External network name: %s' % (network_name))

        object_filter = []
        object_filter.append(
            'network_id:%s' % (network_id)
        )
        subnets = osp_handlers.get_subnets(
            object_filter=object_filter,
            tenant_info=True,
            network_info=True
        )
        if subnets is None:
            ctx.my_output.error('Network subnet info failed: %s' % (network_name))
            raise ErrorExit

        if len(subnets) == 0:
            ctx.my_output.error('Network must have subnet: %s' % (network_name))
            raise ErrorExit

        if len(subnets) == 1:
            selected_subnet = subnets[0]
        else:
            selected_subnet = osp_output_handler.select_subnet(subnets)
            if selected_subnet is None:
                raise ErrorExit

        subnet_id = selected_subnet['id']
        subnet_name = selected_subnet['name']
        subnet_cidr = selected_subnet['cidr']
        ctx.my_output.default('External subnet id: %s' % (subnet_id))
        ctx.my_output.default('External subnet name: %s' % (subnet_name))
        ctx.my_output.default('External subnet cidr: %s' % (subnet_cidr))

        if tenant_id is None:
            tenants = osp_handlers.get_tenants()
            selected_tenant = osp_output_handler.select_tenant(tenants)
            if selected_tenant is None:
                raise ErrorExit

            tenant_id = selected_tenant['id']

        if floating_ip is None:
            ctx.my_output.default('Automatic allocation of floating IP?')
            if not common.get_confirmation(title=False):
                object_filter = []
                object_filter.append(
                    'subnet_id:%s' % (subnet_id)
                )
                ports = osp_handlers.get_ports(
                    object_filter=object_filter,
                    tenant_info=True,
                    network_info=True,
                    subnet_info=True,
                    fip_info=True
                )

                ctx.my_output.default('Floating IP usage', underline=True)
                osp_output_handler.print_ports(ports, title=False)

                floating_ip = input("Define new floating IP: ")
                if not ip_helper.is_valid_ipv4_address(floating_ip):
                    ctx.my_output.error('Invalid IPv4 address')
                    raise ErrorExit

        if floating_ip is not None:
            if not ip_helper.is_ipv4_in_cidr(floating_ip, subnet_cidr):
                ctx.my_output.error('Floating IP %s not in subnet %s' % (floating_ip, subnet_cidr))
                raise ErrorExit

            if osp_handlers.is_floating_ip(floating_ip):
                ctx.my_output.error('Floating IP already used')

                floating_ip_info = osp_handlers.get_floating_ip(
                    floating_ip=floating_ip,
                    tenant_info=True,
                    network_info=True,
                    port_info=True,
                    router_info=True
                )
                if floating_ip_info is None:
                    ctx.my_output.error('Floating IP not found')
                    raise ErrorExit

                osp_output_handler.print_floating_ips(
                    [floating_ip_info],
                    title=False
                )

                raise ErrorExit

        floating_ip_id = osp_handlers.create_floating_ip_mo(
            tenant_id,
            port_id,
            network_id,
            subnet_id,
            floating_ip_address=floating_ip
        )
        if floating_ip_id is None:
            ctx.my_output.error('Floating IP create failed')
            raise ErrorExit

        ctx.my_output.default('Floating IP created: %s' % (floating_ip_id))

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
