import sys
import traceback
import click

from menu import common
from menu import validations

from lib.aci import settings
from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("mode")
@click.pass_obj
@click.option("--apic", "apic_name", default='', callback=validations.empty_string_to_none, help="APIC specific settings")
@click.option("--online", "online_mode", is_flag=True, show_default=True, default=False, help="Set online mode")
@click.option("--offline", "offline_mode", is_flag=True, show_default=True, default=False, help="Set offline mode")
def set_aci_mode_command(
        ctx,
        apic_name,
        online_mode,
        offline_mode
        ):
    """Set aci mode"""

    # iserver set aci mode

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        settings_handler = settings.ApicSettings(log_id=ctx.run_id)

        if apic_name is not None:
            if settings_handler.get_apic_controller(apic_name) is None:
                ctx.my_output.error('Unknown apic name: %s' % (apic_name))
                raise ErrorExit

        if not online_mode and not offline_mode:
            ctx.my_output.error('Select either --online or --offline')
            raise ErrorExit

        if online_mode and offline_mode:
            ctx.my_output.error('Select either --online or --offline')
            raise ErrorExit

        if online_mode:
            if not settings_handler.set_apic_mode_online(apic_name=apic_name):
                ctx.my_output.error('Failed to set online mode')
                raise ErrorExit

        if offline_mode:
            if not settings_handler.set_apic_mode_offline(apic_name=apic_name):
                ctx.my_output.error('Failed to set offline mode')
                raise ErrorExit

        if apic_name is None:
            controllers = settings_handler.get_apic_controllers()
        else:
            controllers = [settings_handler.get_apic_controller(apic_name)]

        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        aci_output_handler.print_apic_controllers(
            controllers,
            show_password=False
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
