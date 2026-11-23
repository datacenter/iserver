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


@click.command("sg")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant")
@click.option("--mac", default='', callback=validations.empty_string_to_none, help="Filter by port mac address")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine")
@click.option("--view", "-v", default=['state'], help="[state|id|rule|port|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_sg_command(
        ctx,
        cluster,
        name,
        tenant,
        mac,
        virtual_machine,
        view,
        output,
        devel
        ):
    """Get osp security group"""

    # iserver get osp sg

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|rule|port|all',
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
        rule_info = False
        port_info = False

        if 'state' in view:
            tenant_info = True

        if 'id' in view:
            rule_info = True

        if 'rule' in view:
            tenant_info = True
            rule_info = True

        if 'port' in view:
            tenant_info = True
            rule_info = True
            port_info = True

        object_filter = []

        if name is not None:
            if len(name.split('/')) == 2:
                (tenant, name) = name.split('/')

            tenant_info = True
            object_filter.append(
                'name:%s' % (name)
            )

        if tenant is not None:
            tenant_info = True
            object_filter.append(
                'tenant_name:%s' % (tenant)
            )

        if mac is not None:
            tenant_info = True
            port_info = True
            object_filter.append(
                'mac:%s' % (mac)
            )

        if virtual_machine is not None:
            tenant_info = True
            port_info = True
            object_filter.append(
                'vm_name:%s' % (virtual_machine)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        security_groups = osp_handlers.get_security_groups(
            object_filter=object_filter,
            tenant_info=tenant_info,
            rule_info=rule_info,
            port_info=port_info
        )

        ctx.busy = False

        if security_groups is None:
            ctx.my_output.error(
                'Failed to get security groups'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    security_groups,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(security_groups)

        if 'state' in view:
            osp_output_handler.print_security_groups(
                security_groups,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_security_groups_id(
                security_groups,
                title=True
            )

        if 'rule' in view:
            osp_output_handler.print_security_groups_rule(
                security_groups,
                title=True
            )

        if 'port' in view:
            osp_output_handler.print_security_groups_port(
                security_groups,
                title=True
            )

        ctx.my_output.default('Filter: name, tenant, mac, vm', before_newline=True)
        ctx.my_output.default('View:   state (def), id, rule, port, all')

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
