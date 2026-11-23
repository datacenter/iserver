import sys
import traceback
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import common
from menu import validations



class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("rule")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Security group tenant")
@click.option("--name", "security_group_name", default='', callback=validations.empty_string_to_none, help="Security group name")
@click.option("--id", "security_group_rule_id", default='', callback=validations.empty_string_to_none, help="Rule id")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_rule_command(
        ctx,
        cluster,
        tenant_name,
        security_group_name,
        security_group_rule_id,
        no_confirm
        ):
    """Delete osp security group rule"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        if security_group_name is not None:
            if len(security_group_name.split('/')) == 2:
                (tenant_name, security_group_name) = security_group_name.split('/')

        if tenant_name is None:
            tenants = osp_handlers.get_tenants()
            selected_tenant = osp_output_handler.select_tenant(tenants)
            if selected_tenant is None:
                raise ErrorExit

            tenant_id = selected_tenant['id']
            tenant_name = selected_tenant['name']
        else:
            tenant_info = osp_handlers.get_tenant(
                tenant_name=tenant_name
            )
            if tenant_info is None:
                ctx.my_output.error('Tenant not found: %s' % (tenant_name))
                raise ErrorExit

            tenant_id = tenant_info['id']

        if security_group_name is None:
            object_filter = []
            object_filter.append(
                'tenant_name:%s' % (tenant_name)
            )
            security_groups = osp_handlers.get_security_groups(
                object_filter=object_filter,
                tenant_info=True
            )

            security_group_info = osp_output_handler.select_security_group(
                security_groups
            )
            if security_group_info is None:
                raise ErrorExit

            security_group_id = security_group_info['id']
            security_group_name = security_group_info['name']
        else:
            security_group_info = osp_handlers.get_security_group(
                tenant_id=tenant_id,
                security_group_name=security_group_name
            )
            if security_group_info is None:
                raise ErrorExit

            security_group_id = security_group_info['id']

        if security_group_rule_id is None:
            security_group_info = osp_handlers.get_security_group(
                security_group_id=security_group_id,
                tenant_info=True,
                rule_info=True
            )

            rule_info = osp_output_handler.select_security_group_rule(
                [security_group_info]
            )

            security_group_rule_id = rule_info['id']
        else:
            if not osp_handlers.is_security_group_rule(security_group_rule_id):
                ctx.my_output.error('Security group rule id not found: %s' % (security_group_rule_id))
                raise ErrorExit

        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        if not osp_handlers.delete_security_group_rule_mo(security_group_rule_id):
            ctx.my_output.error('Failed to delete security group rule: %s' % (security_group_rule_id))
            raise ErrorExit

        ctx.my_output.default('Security group rule deleted: %s' % (security_group_rule_id))

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
