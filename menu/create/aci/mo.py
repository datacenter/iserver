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


@click.command("mo")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--mo", "mo_dn", default='', help="Target object")
@click.option("--node", is_flag=True, show_default=True, default=False, help="Node specific")
@click.option("--body", "filename", default='', help="File with JSON body")
def create_aci_mo_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        mo_dn,
        node,
        filename
        ):
    """Create aci managed object"""

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

        if len(mo_dn) == 0:
            ctx.my_output.error(
                'Define mo name'
            )
            raise ErrorExit

        if not os.path.isfile(filename):
            ctx.my_output.error(
                'File not found: %s' % (filename)
            )
            raise ErrorExit

        body = file_helper.get_file_json(filename)
        if body is None:
            ctx.my_output.error(
                'File json read failed: %s' % (filename)
            )
            raise ErrorExit

        if node:
            uri = 'node/mo/%s' % (mo_dn)
        else:
            uri = 'mo/%s' % (mo_dn)

        success, error = apic_handler.create_managed_object(
            uri,
            body
        )

        if not success:
            ctx.my_output.error(error)
            raise ErrorExit

        ctx.my_output.default(
            'Configuration change successful'
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
