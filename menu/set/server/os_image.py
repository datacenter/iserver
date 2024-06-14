import sys
import traceback
import click

from progress.bar import Bar

from lib.intersight import os_image

from menu import user_inputs
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-image")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--file", "filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Input yaml file")
@click.option("--id", "moid", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Id")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Name")
@click.option("--vendor", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Vendor")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Version")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="OS HTTP Link")
@click.option("--interactive", is_flag=True, show_default=True, default=False, help="Interactive mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_server_os_image_command(ctx, filename, iaccount, moid, name, vendor, version, link, interactive, devel):
    """Set os image objects from input yaml file"""

    # iwectl set server os-image

    ctx.developer = devel

    try:
        image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)

        if len(filename) > 0:
            ctx.my_output.default('Input file verification...')
            images = validations.validate_yaml_file(ctx, filename)
            if images is None:
                raise ErrorExit

        if len(filename) == 0:
            if len(moid) == 0:
                interactive = True

            if interactive:
                items = image_handler.get_all()
                image_handler.print(items)

                moid = user_inputs.get_value(ctx, 'Image ID')

                ctx.my_output.default('Parameters to be modified (leave empty for no change)')
                name = user_inputs.get_value(ctx, 'Image name', empty=True)
                vendor = user_inputs.get_os_image_vendor(ctx, iaccount, empty=True)
                if len(vendor) == 0:
                    for item in items:
                        if item['Moid'] == moid:
                            vendor = item['Vendor']

                if len(vendor) == 0:
                    ctx.my_output.error('Image vendor not found: %s' % (moid))
                    raise ErrorExit

                version = user_inputs.get_os_image_version(ctx, iaccount, vendor, empty=True)
                if len(version) == 0:
                    for item in items:
                        if item['Moid'] == moid:
                            version = item['Version']

                if len(version) == 0:
                    ctx.my_output.error('Image versions not found: %s' % (moid))
                    raise ErrorExit

                link = user_inputs.get_value(ctx, 'Link', empty=True)

            images = []
            item = {}
            item['Moid'] = moid
            item['Name'] = name
            item['Vendor'] = vendor
            item['Version'] = version
            item['Link'] = link
            item['Type'] = 'url'
            images.append(item)

        ctx.my_output.default('Input parameters verification...')

        success, reason = image_handler.validate_set(images)
        if not success:
            ctx.my_output.error('Input parameters validation failed')
            ctx.my_output.default(reason)
            raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(images))
        bar_handler.goto(0)
        failed = []
        for item in images:
            if not image_handler.update(item['Moid'], item):
                failed.append(item['Moid'])
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some updates failed')
            for item in failed:
                ctx.my_output.default('- %s' % (item))
            raise ErrorExit

        images = image_handler.get_all()
        image_handler.print(images)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
