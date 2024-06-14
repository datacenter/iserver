import json
import sys
import traceback
import yaml
import click

from lib.intersight import hcl_operating_system
from lib.intersight import hcl_operating_system_vendor
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-version")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--vendor", "vendor_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Vendor Name")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_os_version_command(ctx, iaccount, vendor_name, output, devel):
    """Get operating system versions"""

    # iserver get is os-version

    ctx.developer = devel

    try:
        version_handler = hcl_operating_system.HclOperatingSystem(iaccount, log_id=ctx.run_id)
        if vendor_name == '':
            versions = version_handler.get_all()
        else:
            vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
            vendor_attributes = vendor_handler.get_by_name(vendor_name)
            if vendor_attributes is None:
                ctx.my_output.error('Vendor not found: %s' % (vendor_name))
                raise ErrorExit
            versions = version_handler.get_vendor_versions(vendor_attributes['Moid'])

        ctx.my_output.json_output(versions)

        if output == 'json':
            ctx.my_output.default(json.dumps(versions, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                versions,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        version_handler.print(versions)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
