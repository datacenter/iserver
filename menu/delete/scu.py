import sys
import traceback
import click

from lib.intersight import scu

from menu import user_inputs
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("scu")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--id", "scu_id", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU object Moid")
@click.option("--name", "scu_name", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU object Name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_scu_command(ctx, scu_id, scu_name, iaccount, devel):
    """Delete software configuration utilities"""

    # iwectl delete scu

    ctx.developer = devel

    try:
        scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)

        ctx.my_output.default('Get scus...')
        scus = scu_handler.get_all()

        if scu_id == '' and scu_name == '':
            scu_handler.print(scus)
            scu_id = user_inputs.get_value(ctx, 'SCU ID')

        if len(scu_name) > 0:
            scu_attributes = scu_handler.get_by_name(scu_name)
            if scu_attributes is None:
                scu_handler.print(scus)
                ctx.my_output.error('SCU Name not found: %s' % (scu_name))
                raise ErrorExit
            scu_id = scu_attributes['Moid']

        if not scu_handler.is_moid(scu_id):
            scu_handler.print(scus)
            ctx.my_output.error('Object not found: %s' % (scu_id))
            raise ErrorExit

        success = scu_handler.delete(scu_id)
        if not success:
            ctx.my_output.error('Object delete failed: %s' % (scu_id))
            raise ErrorExit

        ctx.my_output.default('Object deleted: %s\n' % (scu_id))

        scus = scu_handler.get_all()
        scu_handler.print(scus)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
