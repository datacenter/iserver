import sys
import json
import traceback
import click

from menu import common
from menu import defaults
from menu import validations
from menu import main as menu_main
from menu.create.intersight.os import validations as os_install_validations
from menu.create.intersight.os import common as os_install_common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("static")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--serial", "serial_filter", default='', help="Serial number")
@click.option("--scu", "scu_name", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Name")
@click.option("--image", "image_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Image Name")
@click.option("--interface", "interface_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Interface name")
@click.option("--mac", "interface_mac", is_flag=False, show_default=False, default='', type=click.STRING, help="Interface mac address")
@click.option("--address", is_flag=False, show_default=False, default='', callback=validations.validate_ip, type=click.STRING, help="IP address")
@click.option("--netmask", is_flag=False, show_default=False, default='', callback=validations.validate_ip, type=click.STRING, help="Netmask")
@click.option("--gateway", is_flag=False, show_default=False, default='', callback=validations.validate_ip, type=click.STRING, help="IP gateway")
@click.option("--nameserver", is_flag=False, show_default=False, default='', callback=validations.validate_ip, type=click.STRING, help="Nameserver")
@click.option("--hostname", is_flag=False, show_default=False, default='', type=click.STRING, help="Hostname")
@click.option("--password", is_flag=False, show_default=False, default='', type=click.STRING, help="Password")
@click.option("--organization", "organization_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Organization name")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait disabled")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_os_install_static_command(
    ctx,
    iaccount,
    name_filter,
    ip_filter,
    serial_filter,
    scu_name,
    image_name,
    interface_name,
    interface_mac,
    address,
    netmask,
    gateway,
    nameserver,
    hostname,
    password,
    organization_name,
    dry_run,
    no_wait,
    verbose,
    devel
    ):
    """OS installation with static"""

    # iserver create os-install static

    ctx.developer = devel
    silent = False
    debug = False
    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        ctx.my_output.default('Check isctl version...')
        isctl_success, isctl_output = menu_main.check_isctl()
        if not isctl_success:
            ctx.my_output.error('isctl command execution failed')
            raise ErrorExit

        if not menu_main.check_isctl_version(isctl_output, '0.1.18'):
            ctx.my_output.error('Minimum isctl version 0.1.18 is required')
            raise ErrorExit

        attributes = os_install_validations.get_static_attributes(
            ctx,
            iaccount,
            name_filter,
            ip_filter,
            serial_filter,
            scu_name,
            image_name,
            interface_name,
            interface_mac,
            address,
            netmask,
            gateway,
            nameserver,
            hostname,
            password,
            organization_name
        )
        if attributes is None:
            raise ErrorExit

        ctx.my_output.info(
            json.dumps(
                attributes,
                indent=4
            )
        )

        if common.get_confirmation():
            if not os_install_common.run(ctx, iaccount, attributes, dry_run=dry_run, wait=not no_wait, verbose=verbose):
                raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
