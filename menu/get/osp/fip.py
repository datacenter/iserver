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


@click.command("fip")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--floating", "floating_ip", default='', callback=validations.validate_ip_subnet, help="Filter by floating ip address")
@click.option("--fixed", "fixed_ip", default='', callback=validations.validate_ip_subnet, help="Filter by fixed ip address")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by mac address")
@click.option("--router", default='', callback=validations.empty_string_to_none, help="Filter by router name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--floating-net", "floating_net", default='', callback=validations.empty_string_to_none, help="Filter by floating network name")
@click.option("--fixed-net", "fixed_net", default='', callback=validations.empty_string_to_none, help="Filter by fixed network name")
@click.option("--vm", "vm_name", default='', callback=validations.empty_string_to_none, help="Filter by vm name")
@click.option("--view", "-v", default=['state'], help="[state|id|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_fip_command(
        ctx,
        cluster,
        floating_ip,
        fixed_ip,
        mac,
        router,
        tenant,
        floating_net,
        fixed_net,
        vm_name,
        view,
        output,
        devel
        ):
    """Get osp floating ip"""

    # iserver get osp fip

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|all',
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
        router_info = False
        port_info = False

        if 'state' in view:
            tenant_info = True
            network_info = True
            router_info = True
            port_info = True

        object_filter = []

        if len(floating_ip) > 0:
            object_filter.append(
                'floating-ip:%s' % (floating_ip)
            )

        if len(fixed_ip) > 0:
            object_filter.append(
                'fixed-ip:%s' % (fixed_ip)
            )

        if mac is not None:
            object_filter.append(
                'mac:%s' % (mac)
            )

        if router is not None:
            router_info = True
            object_filter.append(
                'router:%s' % (router)
            )

        if tenant is not None:
            tenant_info = True
            object_filter.append(
                'tenant:%s' % (tenant)
            )

        if floating_net is not None:
            network_info = True
            object_filter.append(
                'floating-network:%s' % (floating_net)
            )

        if fixed_net is not None:
            port_info = True
            object_filter.append(
                'fixed-network:%s' % (fixed_net)
            )

        if vm_name is not None:
            port_info = True
            object_filter.append(
                'vm:%s' % (vm_name)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        fips = osp_handlers.get_floating_ips(
            object_filter=object_filter,
            tenant_info=tenant_info,
            network_info=network_info,
            router_info=router_info,
            port_info=port_info
        )

        ctx.busy = False

        if fips is None:
            ctx.my_output.error(
                'Failed to get floating ips'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    fips,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(fips)

        if 'state' in view:
            osp_output_handler.print_floating_ips(
                fips,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_floating_ips_id(
                fips,
                title=True
            )

        ctx.my_output.default('Filter: floating, fixed, mac, router, tenant, floating-net, fixed-net, vm', before_newline=True)
        ctx.my_output.default('View:   state (def), id, all')

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
