import sys
import traceback
import click

from lib.intersight.os_configuration_file import main as os_configuration_file

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
@click.option("--id", "config_id", is_flag=False, show_default=False, default='', type=click.STRING, help="OS config object moid")
@click.option("--name", "config_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS config object name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_intersight_os_config_command(ctx, config_id, config_name, iaccount, devel):
    """Delete operating system configuration template"""

    # iwectl delete is os-config

    ctx.developer = devel

    try:
        config_handler = os_configuration_file.OsConfigurationFile(iaccount, log_id=ctx.run_id)

        ctx.my_output.default('Get configs...')
        configs = config_handler.get_all()

        if config_id == '' and config_name == '':
            config_handler.print(configs)
            config_id = user_inputs.get_value(ctx, 'OS Config ID')

        if len(config_name) > 0:
            config_attributes = config_handler.get_by_name(config_name)
            if config_attributes is None:
                ctx.my_output.error('OS configuration file not found: %s' % (config_name))
                raise ErrorExit

            config_id = config_attributes['Moid']

        if not config_handler.is_moid(config_id):
            config_handler.print(configs)
            ctx.my_output.error('Object not found: %s' % (config_id))
            raise ErrorExit

        success = config_handler.delete(config_id)
        if not success:
            ctx.my_output.error('Object delete failed: %s' % (config_id))
            raise ErrorExit

        ctx.my_output.default('Object deleted: %s\n' % (config_id))

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
