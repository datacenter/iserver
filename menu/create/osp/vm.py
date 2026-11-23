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


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--name", "vm_name", default='', callback=validations.empty_string_to_none, help="Virtual machine name")
@click.option("--img", "image_name", default='', callback=validations.empty_string_to_none, help="Image name")
@click.option("--flv", "flavor_name", default='', callback=validations.empty_string_to_none, help="Flavor name")
@click.option("--net", "networks_info", multiple=True, help="Network name[:subnet][:ip]")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_vm_command(
        ctx,
        cluster_name,
        tenant_name,
        vm_name,
        image_name,
        flavor_name,
        networks_info,
        devel
        ):
    """Create osp vm"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        if tenant_name is None:
            tenants = osp_handlers.get_tenants()
            if tenants is None:
                ctx.my_output.error('Failed to get tenants')
                raise ErrorExit

            selected_tenant = osp_output_handler.select_tenant(tenants)
            if selected_tenant is None:
                raise ErrorExit

            tenant_id = selected_tenant['id']
            tenant_name = selected_tenant['name']
        else:
            tenant_info = osp_handlers.get_tenant(tenant_name=tenant_name)
            if tenant_info is None:
                ctx.my_output.error(
                    'Tenant not found: %s' % (tenant_name)
                )
                raise ErrorExit

            tenant_id = tenant_info['id']

        if vm_name is None:
            vm_name = input('New virtual machine name: ')
            if vm_name is None or len(vm_name) == 0:
                raise ErrorExit

        if osp_handlers.is_virtual_machine_by_name(vm_name, tenant_id=tenant_id):
            ctx.my_output.error(
                'Virtual machine already defined: %s/%s' % (
                    tenant_name,
                    vm_name
                )
            )
            raise ErrorExit

        ctx.my_output.default(
            'Virtual machine does not exist yet: %s/%s' % (
                tenant_name,
                vm_name
            )
        )

        if image_name is None:
            images = osp_handlers.get_images()
            if images is None:
                ctx.my_output.error('Failed to get images')
                raise ErrorExit

            image_info = osp_output_handler.select_image(images)
            if image_info is None:
                raise ErrorExit

            image_id = image_info['id']
            image_name = image_info['name']
        else:
            image_info = osp_handlers.get_image(image_name=image_name)
            if image_info is None:
                ctx.my_output.error('Image does not exist: %s' % (image_name))
                raise ErrorExit
            image_id = image_info['id']

        if flavor_name is None:
            flavors = osp_handlers.get_flavors()
            if flavors is None:
                ctx.my_output.error('Failed to get flavors')
                raise ErrorExit

            flavor_info = osp_output_handler.select_flavor(flavors)
            if flavor_info is None:
                raise ErrorExit

            flavor_id = flavor_info['id']
            flavor_name = flavor_info['name']
        else:
            flavor_info = osp_handlers.get_flavor(flavor_name=flavor_name)
            if flavor_info is None:
                ctx.my_output.error('Image does not exist: %s' % (flavor_name))
                raise ErrorExit
            flavor_id = flavor_info['id']

        nics = []
        nics_info = []

        if len(networks_info) > 0:
            for user_network_info in networks_info:
                network_name = user_network_info.split(':')[0]
                network_info = osp_handlers.get_network(network_name=network_name, subnet_info=True)
                if network_info is None:
                    ctx.my_output.error('Network not found: %s' % (network_name))
                    raise ErrorExit

                subnet_name = None
                ip_address = None
                if len(user_network_info.split(':')) == 2:
                    user_input = user_network_info.split(':')[1]
                    if ip_helper.is_valid_ipv4_address(user_input):
                        ip_address = user_input
                    else:
                        subnet_name = user_input
                if len(user_network_info.split(':')) == 3:
                    user_input = user_network_info.split(':')[2]
                    if ip_helper.is_valid_ipv4_address(user_input):
                        ip_address = user_input
                    else:
                        subnet_name = user_input

                if subnet_name is not None:
                    network_subnet_info = None
                    for subnet_info in network_info['subnet_info']:
                        if subnet_info['name'] == subnet_name:
                            network_subnet_info = subnet_info
                            break

                    if network_subnet_info is None:
                        ctx.my_output.error('Invalid subnet %s for network %s' % (subnet_name, network_name))
                        raise ErrorExit

                if subnet_name is None:
                    if len(network_info['subnet_info']) > 1:
                        ctx.my_output.error('Define subnet as multiple subnets defined for network: %s' % (network_name))
                        raise ErrorExit

                    network_subnet_info = network_info['subnet_info'][0]

                if ip_address is not None:
                    if not ip_helper.is_ipv4_in_cidr(ip_address, network_subnet_info['cidr']):
                        ctx.my_output.error('Selected IP %s not in subnet cidr %s' % ip_address, network_subnet_info['cidr'])
                        raise ErrorExit

                nic = {}
                nic['net-id'] = network_info['id']
                if subnet_name is not None:
                    nic['subnet-id'] = network_subnet_info['id']
                if ip_address is not None:
                    nic['v4-fixed-ip'] = ip_address
                nics.append(
                    nic
                )

                nic_info = {}
                nic_info['net-id'] = network_info['id']
                nic_info['net-name'] = network_info['name']
                nic_info['subnet-id'] = network_subnet_info['id']
                nic_info['subnet-name'] = network_subnet_info['name']
                if ip_address is not None:
                    nic_info['ip'] = ip_address
                else:
                    nic_info['ip'] = 'dhcp'

                nics_info.append(
                    nic_info
                )

        if len(networks_info) == 0:
            nic_index = 1
            networks = osp_handlers.get_networks(tenant_info=True, subnet_info=True, router_info=True)
            if networks is None:
                ctx.my_output.error('Failed to get networks')
                raise ErrorExit

            while True:
                network_info = osp_output_handler.select_network(networks)
                if network_info is None and nic_index == 1:
                    raise ErrorExit

                if network_info is None:
                    break

                network_subnet_info = None
                if len(network_info['subnet_info']) == 1:
                    network_subnet_info = network_info['subnet_info'][0]
                if len(network_info['subnet_info']) > 1:
                    network_subnet_info = osp_output_handler.select_subnet(network_info['subnet_info'])
                    if network_subnet_info is None:
                        raise ErrorExit

                if network_subnet_info is None:
                    subnet_name = None

                if network_subnet_info is not None:
                    subnet_name = network_subnet_info['name']
                    ip_address = input('IPv4 address (empty for DHCP): ')
                    if len(ip_address) == 0:
                        ip_address = None
                    else:
                        if network_subnet_info is None:
                            ctx.my_output.error('Network has no subnet')
                            raise ErrorExit

                        if not ip_helper.is_ipv4_in_cidr(ip_address, network_subnet_info['cidr']):
                            ctx.my_output.error('IP addess %s is not in network subnet cidr %s' % (ip_address, network_subnet_info['cidr']))
                            raise ErrorExit


                nic = {}
                nic['net-id'] = network_info['id']
                if subnet_name is not None:
                    nic['subnet-id'] = network_subnet_info['id']
                if ip_address is not None:
                    nic['v4-fixed-ip'] = ip_address
                nics.append(
                    nic
                )

                nic_info = {}
                nic_info['net-id'] = network_info['id']
                nic_info['net-name'] = network_info['name']
                nic_info['subnet-id'] = network_subnet_info['id']
                nic_info['subnet-name'] = network_subnet_info['name']
                if ip_address is not None:
                    nic_info['ip'] = ip_address
                else:
                    nic_info['ip'] = 'dhcp'

                nics_info.append(
                    nic_info
                )

                nic_index = nic_index + 1

        ctx.my_output.default('Create virtual machine')
        ctx.my_output.default('- tenant: %s [%s]' % (tenant_name, tenant_id))
        ctx.my_output.default('- name: %s' % (vm_name))
        ctx.my_output.default('- image: %s [%s]' % (image_name, image_id))
        ctx.my_output.default('- flavor: %s [%s]' % (flavor_name, flavor_id))
        for nic_info in nics_info:
            ctx.my_output.default(
                '- network %s [%s] subnet %s [%s] ip %s' % (
                    nic_info['net-name'],
                    nic_info['net-id'],
                    nic_info['subnet-name'],
                    nic_info['subnet-id'],
                    nic_info['ip']
                )
            )

        new_virtual_machine_id = osp_handlers.create_virtual_machine_mo(
            vm_name,
            image_id,
            flavor_id,
            nics=nics
        )
        if new_virtual_machine_id is None:
            ctx.my_output.error('Create failed')
            raise ErrorExit

        ctx.my_output.default('New virtual machine created: %s' % (new_virtual_machine_id))

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
