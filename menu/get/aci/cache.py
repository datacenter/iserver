import sys
import traceback
import click

from menu import validations

from lib.aci import settings
from lib.aci import cache
from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cache")
@click.pass_obj
@click.option("--apic", "apic_name", default='', callback=validations.empty_string_to_none, help="APIC name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_cache_command(
        ctx,
        apic_name,
        devel
        ):
    """Get aci cache"""

    # iserver get aci cache

    ctx.developer = devel

    try:
        settings_handler = settings.ApicSettings(log_id=ctx.run_id)
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)

        if apic_name is None:
            controllers = settings_handler.get_apic_controllers()
            if controllers is None:
                ctx.my_output.error('Failed to get ACI controllers')
                raise ErrorExit
        else:
            controller = settings_handler.get_apic_controller(apic_name)
            if controller is None:
                ctx.my_output.error('Failed to get ACI controller: %s' % (apic_name))
                raise ErrorExit

            controllers = [controller]

        aci_output_handler.print_apic_controllers(
            controllers,
            show_password=False
        )

        for controller in controllers:
            if apic_name is None or controller['name'] == apic_name:
                if controller['cache']['enabled']:
                    cache_handler = cache.Cache(
                        controller['name']
                    )
                    stats = cache_handler.get_cache_stats()

                    ctx.my_output.default(
                        'Cache: %s' % (controller['name']),
                        underline=True,
                        before_newline=True
                    )

                    aci_output_handler.print_cache_stats(stats)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
