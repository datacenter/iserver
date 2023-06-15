import json
import sys
import traceback
import yaml
import click

from lib.intersight import os_image
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-image")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml', 'set'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_os_image_command(ctx, iaccount, output, devel):
    """Get operating system image"""

    # iserver get is image

    ctx.developer = devel

    try:
        image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
        images = image_handler.get_all()

        if output == 'json':
            ctx.my_output.default(json.dumps(images, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                images,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        if output == 'set':
            yaml_output = image_handler.get_set_output(images)
            if yaml_output is None:
                ctx.my_output.error('Failed to get set output type')
                raise ErrorExit

            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        image_handler.print(images)
        ctx.my_output.json_output(images)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
