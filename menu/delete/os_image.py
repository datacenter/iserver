import sys
import traceback
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
@click.option("--id", "image_id", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Image object Moid")
@click.option("--name", "image_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Image object Name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_os_image_command(ctx, image_id, image_name, iaccount, devel):
    """Delete operating system image metadata"""

    # iwectl delete os-image

    ctx.developer = devel

    try:
        image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
        images = image_handler.get_all()

        if image_id == '' and image_name == '':
            image_handler.print(images)
            ctx.my_output.error('Define --id or --name parameters')
            raise ErrorExit

        if len(image_name) > 0:
            image_attributes = image_handler.get_by_name(image_name)
            if image_attributes is None:
                image_handler.print(images)
                ctx.my_output.error('Name not found: %s' % (image_name))
                raise ErrorExit
            image_id = image_attributes['Moid']

        if not image_handler.is_moid(image_id):
            image_handler.print(images)
            ctx.my_output.error('Object not found: %s' % (image_id))
            raise ErrorExit

        success = image_handler.delete(image_id)
        if not success:
            ctx.my_output.error('Object delete failed: %s' % (image_id))
            raise ErrorExit

        ctx.my_output.default('Object deleted: %s\n' % (image_id))

        images = image_handler.get_all()
        image_handler.print(images)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
