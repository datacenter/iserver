import sys
import traceback
import click

from lib import file_helper
from lib.intersight.os_configuration_file import main as os_configuration_file

from menu import main as menu_main
from menu import user_inputs
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-config")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--config", "filename", is_flag=False, show_default=False, default='', type=click.STRING, help="OS configuration file")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS configuration name")
@click.option("--image", "image_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS image name")
@click.option("--organization", "organization_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Organization name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_intersight_os_config_command(ctx, iaccount, filename, name, image_name, organization_name, devel):
    """Create os config"""

    # iserver create is os-config

    ctx.developer = devel

    try:
        ctx.my_output.default('Check isctl version...')
        isctl_success, isctl_output = menu_main.check_isctl()
        if not isctl_success:
            ctx.my_output.error('isctl command execution failed')
            raise ErrorExit

        if not menu_main.check_isctl_version(isctl_output, '0.2.6'):
            ctx.my_output.error('Minimum isctl version 0.2.6 is required')
            raise ErrorExit

        config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)

        if len(filename) == 0:
            filename = user_inputs.get_value(ctx, 'OS configuration file location')
            if len(filename) == 0:
                raise ErrorExit

        file_content = file_helper.get_file_text(filename)
        if file_content is None:
            raise ErrorExit

        if len(image_name) == 0:
            image_name = user_inputs.get_os_image_name(ctx, iaccount)
            if len(image_name) == 0:
                raise ErrorExit

        if len(name) == 0:
            name = user_inputs.get_os_config_file(ctx, iaccount, new=True)
            if len(name) == 0:
                raise ErrorExit

        if len(organization_name) == 0:
            organization_name = user_inputs.get_organization_name(ctx, iaccount)
            if len(organization_name) == 0:
                raise ErrorExit

        attributes = {}
        attributes['Name'] = name
        attributes['Internal'] = False
        attributes['FileContent'] = file_content
        attributes['OsImageName'] = image_name
        attributes['Organization'] = organization_name

        ctx.my_output.default('Input parameters verification...')

        success, reason = config_handler.validate_add(attributes)
        if not success:
            ctx.my_output.error('Input parameters validation failed')
            ctx.my_output.default(reason)
            raise ErrorExit

        ctx.my_output.default('Create OS configuration file...')
        if not config_handler.add(attributes):
            ctx.my_output.error('Create request failed')
            raise ErrorExit

        ctx.my_output.default('OS configuration file created')

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
