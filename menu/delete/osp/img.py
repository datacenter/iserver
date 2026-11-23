import sys
import traceback
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import common
from menu import validations



class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("img")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--id", "image_id", default='', callback=validations.empty_string_to_none, help="Image id")
@click.option("--name", "image_name", default='', callback=validations.empty_string_to_none, help="Image name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_img_command(
        ctx,
        cluster,
        image_id,
        image_name,
        no_confirm
        ):
    """Delete osp image"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        if image_id is None and image_name is None:
            images = osp_handlers.get_images()
            image_info = osp_output_handler.select_image(images)
            if image_info is None:
                raise ErrorExit

        if image_id is not None:
            image_info = osp_handlers.get_image(
                image_id=image_id
            )
            if image_info is None:
                ctx.my_output.error('Image not found by id')
                raise ErrorExit

        if image_name is not None:
            image_info = osp_handlers.get_image(
                image_name=image_name
            )
            if image_info is None:
                ctx.my_output.error('Image not found by name')
                raise ErrorExit

        ctx.my_output.default('Delete image %s [%s]' % (image_info['name'], image_info['id']))
        if not no_confirm:
            if not common.get_confirmation():
                raise ErrorExit

        success = osp_handlers.delete_image_mo(image_info['id'])
        if not success:
            ctx.my_output.error('Failed')
            raise ErrorExit

        ctx.my_output.default('Deleted')

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
