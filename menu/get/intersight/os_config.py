import sys
import json
import traceback
import click

from lib.intersight.hcl_operating_system_vendor import main as hcl_operating_system_vendor
from lib.intersight.os_configuration_file import main as os_configuration_file
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-config")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Configration Name")
@click.option("--vendor", "vendor_name", is_flag=False, show_default=False, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Vendor Name")
@click.option("--version", "version_name", is_flag=False, show_default=False, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Version Name")
@click.option("--moid", "version_id", is_flag=False, show_default=False, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Version ID")
@click.option("--content", "show_content", is_flag=True, show_default=True, default=False, help="Show file content")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_os_config_command(ctx, iaccount, name, vendor_name, version_name, version_id, show_content, devel):
    """Get operating system configuration template"""

    # iserver get is os-config

    ctx.developer = devel

    try:
        vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
        vendors = vendor_handler.get_all()

        config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)
        config_files = config_handler.get_infos(
            vendors,
            moid_filter=version_id,
            name_filter=name,
            vendor_filter=vendor_name,
            version_filter=version_name
        )

        if config_files is None:
            ctx.my_output.error('No configuration file found')
            raise ErrorExit

        config_handler.print(
            config_files,
            title=True,
            show_content=show_content
        )
        ctx.my_output.json_output(config_files)

        ctx.my_output.default('Filter: name, vendor, version, moid', before_newline=True)
        ctx.my_output.default('Options: content')

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
