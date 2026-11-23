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


@click.command("net")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--name", "network_name", default='', callback=validations.empty_string_to_none, help="Network name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--type", "network_type", type=click.Choice(['tenant', 'provider', 'external'], case_sensitive=False), default='tenant', help="Network type")
@click.option("--phy", "physical_network", default='', callback=validations.empty_string_to_none, help="Physical network")
@click.option("--prov", "provider_network_type", default='', callback=validations.empty_string_to_none, help="Provider network type")
@click.option("--vlan", "provider_segmentation_id", default='', callback=validations.empty_string_to_none, help="Provider segmentation id")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_net_command(
        ctx,
        cluster_name,
        network_name,
        tenant_name,
        network_type,
        physical_network,
        provider_network_type,
        provider_segmentation_id,
        devel
        ):
    """Create osp net"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        user_input_mode = False

        if network_name is None:
            user_input_mode = True
            network_name = input('New network name: ')
            if network_name is None or len(network_name) == 0:
                raise ErrorExit

            if osp_handlers.is_network_name(network_name):
                ctx.my_output.error('Network already defined: %s' % (network_name))
                raise ErrorExit

        if tenant_name is None:
            user_input_mode = True
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
            tenant = osp_handlers.get_tenant(tenant_name=tenant_name)
            if tenant is None:
                ctx.my_output.error('Tenant not found: %s' % (tenant_name))
                raise ErrorExit

            tenant_id = tenant['id']

        if user_input_mode:
            network_type = input('Network type (tenant, provider, external): ')
            if network_type is None or len(network_type) == 0 or network_type not in ['tenant', 'provider', 'external']:
                raise ErrorExit

        if network_type == 'tenant':
            new_network_id = osp_handlers.create_tenant_network_mo(
                tenant_id,
                network_name
            )
            if new_network_id is None:
                ctx.my_output.error('Create failed')
                raise ErrorExit

            ctx.my_output.default('New tenant network created: %s' % (new_network_id))
            return

        if network_type == 'external':
            if physical_network is None:
                physical_network = input('Physical network name: ')
                if physical_network is None or len(physical_network) == 0:
                    raise ErrorExit

            new_network_id = osp_handlers.create_external_network_mo(
                network_name,
                physical_network
            )
            if new_network_id is None:
                ctx.my_output.error('Create failed')
                raise ErrorExit

            ctx.my_output.default('New external network created: %s' % (new_network_id))
            return

        if network_type == 'provider':
            if physical_network is None:
                physical_network = input('Physical network name: ')
                if physical_network is None or len(physical_network) == 0:
                    raise ErrorExit

            if provider_network_type is None:
                provider_network_type = input('Provider network type: ')
                if provider_network_type is None or len(provider_network_type) == 0:
                    raise ErrorExit

            if provider_segmentation_id is None:
                provider_segmentation_id = common.get_integer('Provider segmentation id: ')
                if provider_segmentation_id is None:
                    raise ErrorExit

            new_network_id = osp_handlers.create_provider_network_mo(
                tenant_id,
                network_name,
                physical_network,
                provider_network_type,
                provider_segmentation_id
            )
            if new_network_id is None:
                ctx.my_output.error('Create failed')
                raise ErrorExit

            ctx.my_output.default('New provider network created: %s' % (new_network_id))
            return

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
