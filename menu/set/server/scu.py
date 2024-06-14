import sys
import json
import traceback
import click

from progress.bar import Bar

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
@click.option("--file", "filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Input yaml file")
@click.option("--id", "moid", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Id")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Name")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Version")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="Link")
@click.option("--interactive", is_flag=True, show_default=True, default=False, help="Interactive mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_server_scu_command(ctx, filename, iaccount, moid, name, version, link, interactive, devel):
    """Set software configuration utilities"""

    # iwectl set server scu

    ctx.developer = devel

    try:
        scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)

        if len(filename) > 0:
            ctx.my_output.default('Input file verification...')
            scus = validations.validate_yaml_file(ctx, filename)
            if scus is None:
                raise ErrorExit

        if len(filename) == 0:
            if len(moid) == 0:
                interactive = True

            if interactive:
                scus = scu_handler.get_all()
                scu_handler.print(scus)

                moid = user_inputs.get_value(ctx, 'SCU ID')

                ctx.my_output.default('Parameters to be modified (leave empty for no change)')
                name = user_inputs.get_value(ctx, '- name', empty=True)
                version = user_inputs.get_value(ctx, '- version', empty=True)
                link = user_inputs.get_value(ctx, '- link', empty=True)

            scus = []
            item = {}
            item['Moid'] = moid
            item['Name'] = name
            item['Version'] = version
            item['Link'] = link
            item['Type'] = ''
            scus.append(item)

        ctx.my_output.default('Input parameters verification...')
        ctx.my_output.debug(
            json.dumps(
                scus,
                indent=4
            )
        )

        success, reason = scu_handler.validate_set(scus)
        if not success:
            ctx.my_output.error('Input parameters validation failed')
            ctx.my_output.default(reason)
            raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(scus))
        bar_handler.goto(0)
        failed = []
        for item in scus:
            if not scu_handler.update(item['Moid'], item):
                failed.append(item['Moid'])
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some updates failed')
            for item in failed:
                ctx.my_output.default('- %s' % (item))
            raise ErrorExit

        scus = scu_handler.get_all()
        scu_handler.print(scus)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
