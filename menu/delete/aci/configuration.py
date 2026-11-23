import os
import sys
import json
import traceback
import click

from lib import file_helper
from lib import log_helper
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("config")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--node", "node_name", default='', help="Node name")
@click.option("--id", "interface_id", default='', help="Interface id")
def delete_aci_configuration(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        node_name,
        interface_id
        ):
    """Delete aci interface configuration"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password
        )
        if apic_handler is None:
            raise ErrorExit

        node_filter = []
        node_filter.append(
            'name:*%s*' % (node_name)
        )

        nodes_info = apic_handler.get_nodes(
            node_filter=node_filter
        )

        if len(nodes_info) == 0:
            ctx.my_output.error(
                'Node not found'
            )
            raise ErrorExit

        if len(nodes_info) > 1:
            ctx.my_output.error(
                'Multiple nodes found'
            )
            raise ErrorExit

        if len(interface_id.split('/')) not in [2,3]:
            ctx.my_output.error(
                'Invalid interface id'
            )
            raise ErrorExit

        for item in interface_id.split('/'):
            try:
                item_int = int(item)
            except BaseException:
                ctx.my_output.error(
                    'Invalid interface id'
                )
                raise ErrorExit

        success, error = apic_handler.delete_leaf_interface_configuration(
            nodes_info[0]['id'],
            interface_id
        )

        if not success:
            ctx.my_output.error(
                'Configuration change failed: %s' % (error)
            )
            raise ErrorExit

        ctx.my_output.default(
            'Configuration successful'
        )

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
