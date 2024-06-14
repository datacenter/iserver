import sys
import traceback
import click

from lib.intersight import hcl_operating_system
from lib.intersight import hcl_operating_system_vendor
from lib.intersight import os_configuration_file
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-config")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--vendor", "vendor_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Vendor Name")
@click.option("--version", "version_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Version Name")
@click.option("--id", "version_id", is_flag=False, show_default=False, default='', type=click.STRING, help="Version ID")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_os_config_command(ctx, iaccount, vendor_name, version_name, version_id, devel):
    """Get operating system configuration template"""

    # iserver get is os-config

    ctx.developer = devel

    try:
        ctx.my_output.default('Validate input parameters...')

        if vendor_name == '' and version_name == '' and version_id == '':
            ctx.my_output.error('Define os version using vendor and version names or version id')
            raise ErrorExit

        if version_id == '':
            if vendor_name == '' or version_name == '':
                ctx.my_output.error('Define os version using vendor and version names or version id')
                raise ErrorExit

        if version_id == '':
            vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
            vendor_id = vendor_handler.get_moid(vendor_name)
            if vendor_id is None:
                ctx.my_output.error('Vendor not found: %s' % (vendor_name))
                raise ErrorExit

            version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=ctx.run_id)
            version_id = version_handler.get_vendor_version_id(vendor_id, version_name)
            if version_id is None:
                ctx.my_output.error('Version not found: %s' % (version_name))
                raise ErrorExit

        config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
        config_files = config_handler.get_file_for_os(version_id)

        if config_files is None:
            ctx.my_output.error('No configuration file found')
            raise ErrorExit

        for config_file in config_files:
            ctx.my_output.default('Configuration file: %s [%s]\n' % (config_file['Name'], config_file['Moid']))
            ctx.my_output.default(config_file['FileContent'])

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
