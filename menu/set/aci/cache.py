import sys
import traceback
import click

from menu import common
from menu import validations

from lib.aci import apic
from lib.aci import cache
from lib.aci import settings
from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cache")
@click.pass_obj
@click.option("--apic", "name", default='', callback=validations.empty_string_to_none, help="APIC specific settings")
@click.option("--on", "cache_on", is_flag=True, show_default=True, default=False, help="Set cache on")
@click.option("--off", "cache_off", is_flag=True, show_default=True, default=False, help="Set cache off")
@click.option("--ttl", "cache_ttl", default=0, type=click.INT, help="Set cache ttl in seconds")
@click.option("--populate", "cache_populate", is_flag=True, show_default=True, default=False, help="Populate cache")
@click.option("--clear", "cache_clear", is_flag=True, show_default=True, default=False, help="Clear cache")
def set_aci_cache_command(
        ctx,
        name,
        cache_on,
        cache_off,
        cache_ttl,
        cache_populate,
        cache_clear
        ):
    """Set aci cache"""

    # iserver set aci cache

    ctx.developer = False
    common.flags_fixup(ctx, False, False, False)

    try:
        if cache_on and cache_off:
            ctx.my_output.error('Select either --on or --off')
            raise ErrorExit

        if cache_populate and cache_clear:
            ctx.my_output.error('Select either --populte or --clear')
            raise ErrorExit

        settings_handler = settings.ApicSettings(log_id=ctx.run_id)
        if name is None:
            apic_names = settings_handler.get_apic_controller_names()
            if len(apic_names) == 0:
                ctx.my_output.error('No api controllers defined')
                raise ErrorExit
        else:
            if settings_handler.get_apic_controller(name) is None:
                ctx.my_output.error('Unknown apic name: %s' % (name))
                raise ErrorExit
            apic_names = [name]

        if cache_on:
            for apic_name in apic_names:
                if not settings_handler.set_apic_cache_on(apic_name=apic_name):
                    ctx.my_output.error('Failed to set cache on: %s' % (apic_name))
                    raise ErrorExit
                ctx.my_output.default('Cache enabled: %s' % (apic_name))

        if cache_off:
            for apic_name in apic_names:
                if not settings_handler.set_apic_cache_off(apic_name=apic_name):
                    ctx.my_output.error('Failed to set cache off: %s' % (apic_name))
                    raise ErrorExit
                ctx.my_output.default('Cache disabled: %s' % (apic_name))

        if cache_ttl > 0:
            for apic_name in apic_names:
                if not settings_handler.set_apic_cache_ttl(cache_ttl, apic_name=apic_name):
                    ctx.my_output.error('Failed to set cache ttl: %s' % (apic_name))
                    raise ErrorExit
                ctx.my_output.default('Cache ttl set to %s seconds: %s' % (cache_ttl, apic_name))

        if cache_clear:
            for apic_name in apic_names:
                cache_handler = cache.Cache(
                    apic_name
                )
                if not cache_handler.clear_cache(bar_enabled=True):
                    ctx.my_output.error('Failed to clear cache: %s' % (apic_name))
                    raise ErrorExit
                ctx.my_output.default('Cache cleared: %s' % (apic_name))

        if cache_populate:
            for apic_name in apic_names:
                controller = settings_handler.get_apic_controller(apic_name)
                apic_handler = apic.Apic(
                    controller['ip'],
                    controller['port'],
                    controller['username'],
                    controller['password'],
                    apic_name=apic_name,
                    log_id=ctx.run_id
                )
                apic_handler.get_mos(bar_enabled=True)

        if len(apic_names) == 1:
            controllers = [settings_handler.get_apic_controller(apic_name)]
        else:
            controllers = settings_handler.get_apic_controllers()

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
