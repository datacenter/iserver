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


@click.command("sub")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--network-name", default='', callback=validations.empty_string_to_none, help="Network name")
@click.option("--network-id", default='', callback=validations.empty_string_to_none, help="Network id")
@click.option("--name", "subnet_name", default='', callback=validations.empty_string_to_none, help="Subnet name")
@click.option("--cidr", default='', callback=validations.empty_string_to_none, help="Subnet cidr")
@click.option("--gateway", default='', callback=validations.empty_string_to_none, help="Subnet gateway")
@click.option("--dns", multiple=True, help="Subnet dns")
@click.option("--dhcp", type=click.Choice(['enabled', 'disabled'], case_sensitive=False), help="DHCP")
@click.option("--start", "start_ip", default='', callback=validations.empty_string_to_none, help="DHCP start")
@click.option("--end", "end_ip", default='', callback=validations.empty_string_to_none, help="DHCP end")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_subnet_command(
        ctx,
        cluster_name,
        network_name,
        network_id,
        subnet_name,
        cidr,
        gateway,
        dns,
        dhcp,
        start_ip,
        end_ip,
        devel
        ):
    """Create osp subnet"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        user_input_mode = False

        if network_name is None and network_id is None:
            user_input_mode = True
            networks = osp_handlers.get_networks(tenant_info=True, subnet_info=True, router_info=True)
            if networks is None:
                ctx.my_output.error('Failed to get networks')
                raise ErrorExit

            network_info = osp_output_handler.select_network(networks)
            if network_info is None:
                raise ErrorExit

            network_id = network_info['id']
            network_name = network_info['name']
            tenant_id = network_info['tenant_id']
            tenant_name = network_info['tenant_name']
        else:
            if network_name is not None:
                network_info = osp_handlers.get_network(network_name=network_name, tenant_info=True)
                if network_info is None:
                    ctx.my_output.error('Network not found: %s' % (network_name))
                    raise ErrorExit

                network_id = network_info['id']
                tenant_id = network_info['tenant_id']
                tenant_name = network_info['tenant_name']

            if network_id is not None:
                network_info = osp_handlers.get_network(network_id=network_id, tenant_info=True)
                if network_info is None:
                    ctx.my_output.error('Network not found: %s' % (network_id))
                    raise ErrorExit

                network_name = network_info['name']
                tenant_id = network_info['tenant_id']
                tenant_name = network_info['tenant_name']

        if subnet_name is None:
            user_input_mode = True
            subnet_name = input('New subnet name (default %s-subnet): ' % (network_name))
            if subnet_name is None or len(subnet_name) == 0:
                subnet_name = '%s-subnet' % (network_name)

            if osp_handlers.is_subnet_name(subnet_name):
                ctx.my_output.error('Subnet already defined: %s' % (subnet_name))
                raise ErrorExit

        if cidr is None:
            user_input_mode = True
            cidr = input('Subnet cidr: ')
            if cidr is None or len(cidr) == 0 or not ip_helper.is_valid_ipv4_cidr(cidr):
                raise ErrorExit

        if user_input_mode:
            if gateway is None:
                gateway = input('Subnet gateway: ')
                if gateway is None or len(gateway) == 0:
                    gateway = None

        if gateway is not None:
            if not ip_helper.is_ipv4_in_cidr(gateway, cidr):
                ctx.my_output.error('Gateway not in cidr')
                raise ErrorExit

        if user_input_mode:
            if len(dns) == 0:
                dns_servers = input('DNS servers comma separated: ')
                if dns_servers is not None and len(dns_servers) > 0:
                    dns = dns_servers.split(',')

        for dns_entry in dns:
            if not ip_helper.is_valid_ipv4_address(dns_entry):
                ctx.my_output.error('Invalid dns ipv4 address: %s' % (dns_entry))
                raise ErrorExit

        if user_input_mode or len(dhcp) == 0:
            ctx.my_output.default('DHCP enabled')
            if common.get_confirmation(title=False):
                dhcp = 'enabled'
            else:
                dhcp = 'disabled'

        if dhcp == 'disabled':
            dhcp_enabled = False
            start_ip = None
            end_ip = None

        if dhcp == 'enabled':
            dhcp_enabled = True
            if user_input_mode:
                if start_ip is None:
                    start_ip = input('DHCP start ip: ')
                    if start_ip is None or len(start_ip) == 0:
                        start_ip = None

                    if start_ip is not None and not ip_helper.is_ipv4_in_cidr(start_ip, cidr):
                        raise ErrorExit

                if start_ip is not None and end_ip is None:
                    end_ip = input('DHCP end ip: ')
                    if end_ip is None or len(end_ip) == 0:
                        end_ip = None

                    if end_ip and not ip_helper.is_ipv4_in_cidr(end_ip, cidr):
                        raise ErrorExit

        new_subnet = osp_handlers.create_subnet_mo(
            network_id,
            cidr,
            tenant_id=tenant_id,
            subnet_name=subnet_name,
            gateway=gateway,
            dns=dns,
            dhcp=dhcp_enabled,
            start_ip=start_ip,
            end_ip=end_ip
        )
        if new_subnet is None:
            ctx.my_output.error('Create failed')
            raise ErrorExit

        ctx.my_output.default('New subnet created: %s' % (new_subnet['id']))

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
