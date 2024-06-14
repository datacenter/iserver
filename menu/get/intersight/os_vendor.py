import json
import sys
import traceback
import yaml
import click

from lib.intersight import hcl_operating_system_vendor
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-vendor")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_os_vendor_command(ctx, iaccount, output, devel):
    """Get operating system vendors"""

    # iserver get is os-vendor

    ctx.developer = devel

    try:
        handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount, log_id=ctx.run_id)
        vendors = handler.get_all()
        ctx.my_output.json_output(vendors)

        if output == 'json':
            ctx.my_output.default(json.dumps(vendors, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                vendors,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        handler.print(vendors)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
