import os
import time
import json
import sys
import traceback
import threading
import click

from lib import ip_helper
from lib.osp import output as osp_output

from menu import progress
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("img")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--name", "image_name", default='', callback=validations.empty_string_to_none, help="Image name")
@click.option("--src", "source_filename", default='', callback=validations.empty_string_to_none, help="Source filename (upload)")
@click.option("--dst", "destination_filename", default='', callback=validations.empty_string_to_none, help="Destination filename (download)")
@click.option("--disk", "disk_format", type=click.Choice(['qcow2', 'raw'], case_sensitive=False), default='qcow2', help="Upload disk format")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_osp_img_command(
        ctx,
        cluster_name,
        image_name,
        source_filename,
        destination_filename,
        disk_format,
        devel
        ):
    """Create osp img"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if source_filename is None and destination_filename is None:
            ctx.my_output.error('Define souce (upload) filename or destination (download) filename')
            raise ErrorExit

        if source_filename is not None and destination_filename is not None:
            ctx.my_output.error('Define souce (upload) filename or destination (download) filename')
            raise ErrorExit

        if source_filename is not None:
            if not os.path.isfile(source_filename):
                ctx.my_output.error('File not found: %s' % (source_filename))
                raise ErrorExit

        if destination_filename is not None:
            if os.path.isfile(destination_filename):
                ctx.my_output.default('Overwrite existing file?')
                if not common.get_confirmation():
                    raise ErrorExit

        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster_name)
        if osp_handlers is None:
            raise ErrorExit

        if source_filename is not None:
            if image_name is None:
                image_name = input('Target image name: ')
                if len(image_name) == 0:
                    raise ErrorExit

                if len(image_name.split(' ')) > 1:
                    ctx.my_output.error('Image name cannot have white spaces')
                    raise ErrorExit

            if osp_handlers.is_image(image_name=image_name):
                ctx.my_output.error('Image exists: %s' % (image_name))
                raise ErrorExit

            ctx.my_output.default(
                'Create image %s from file %s with disk format %s' % (
                    image_name,
                    source_filename,
                    disk_format
                )
            )

            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            new_image_id = osp_handlers.create_image_mo(
                image_name,
                source_filename,
                disk_format=disk_format
            )

            ctx.busy = False

            if new_image_id is None:
                ctx.my_output.error('Create image failed')
                raise ErrorExit

            ctx.my_output.default('New image created: %s' % (new_image_id))

        if destination_filename is not None:
            if image_name is None:
                images = osp_handlers.get_images()
                image_info = osp_output_handler.select_image(images)
                if image_info is None:
                    raise ErrorExit
            else:
                image_info = osp_handlers.get_image(image_name=image_name)
                if image_info is None:
                    ctx.my_output.error('Image does not exist: %s' % (image_name))
                    raise ErrorExit

            ctx.my_output.default(
                'Image %s download to file %s' % (
                    image_info['name'],
                    destination_filename
                )
            )

            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

            success = osp_handlers.download_image(
                image_info['id'],
                destination_filename
            )

            ctx.busy = False

            if not success:
                ctx.my_output.error('Image download failed')
                raise ErrorExit

            ctx.my_output.default('Image downloaded')

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
