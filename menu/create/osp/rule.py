import sys
import traceback
import click

from lib.osp import output as osp_output

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("rule")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--name", "security_group_name", default='', callback=validations.empty_string_to_none, help="Security group name")
@click.option("--type", "ethertype", type=click.Choice(['ipv4', 'ipv6'], case_sensitive=False), help="EtherType")
@click.option("--direction", type=click.Choice(['ingress', 'egress'], case_sensitive=False), help="Direction")
@click.option("--protocol", type=click.Choice(['icmp', 'sctp', 'tcp', 'udp'], case_sensitive=False), help="Protocol")
@click.option("--sport", "start_port", default=-1, type=click.INT, help="Start port range")
@click.option("--eport", "end_port", default=-1, type=click.INT, help="End port range")
@click.option("--prefix", "remote_ip_prefix", default='0.0.0.0/0', callback=validations.validate_subnet, help="Remote prefix")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_rule_command(
        ctx,
        cluster_name,
        tenant_name,
        security_group_name,
        ethertype,
        direction,
        protocol,
        start_port,
        end_port,
        remote_ip_prefix,
        devel
        ):
    """Create osp security group rule"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
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

        if ethertype is None:
            ethertype = common.get_value_from_list('EtherType', ['ipv4', 'ipv6'], before_newline=True)
            if ethertype is None:
                raise ErrorExit

        if direction is None:
            direction = common.get_value_from_list('Direction', ['ingress', 'egress'], before_newline=True)
            if direction is None:
                raise ErrorExit

        if protocol is None:
            protocol = common.get_value_from_list('Protocol', ['icmp', 'sctp', 'tcp', 'udp'], before_newline=True)
            if protocol is None:
                raise ErrorExit

        if protocol != 'icmp':
            if start_port < 0:
                start_port = common.get_integer('Start port: ', before_newline=True)
                if start_port is None:
                    raise ErrorExit

            if end_port < 0:
                end_port = common.get_integer('End port: ', before_newline=True)
                if end_port is None:
                    raise ErrorExit

        if len(security_group_name.split('/')) == 2:
            (security_group_name, tenant_name) = security_group_name.split('/')

        if start_port > 0 and end_port > 1:
            rule_id = osp_handlers.create_security_group_rule_mo(
                security_group_id=security_group_id,
                ethertype=ethertype,
                protocol=protocol,
                direction=direction,
                port_range_min=start_port,
                port_range_max=end_port,
                remote_ip_prefix=remote_ip_prefix
            )
        else:
            rule_id = osp_handlers.create_security_group_rule_mo(
                security_group_id=security_group_id,
                ethertype=ethertype,
                protocol=protocol,
                direction=direction,
                remote_ip_prefix=remote_ip_prefix
            )

        if rule_id is None:
            ctx.my_output.error('Security group rule create failed')
            raise ErrorExit

        ctx.my_output.default('Security group rule created: %s' % (rule_id))

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
