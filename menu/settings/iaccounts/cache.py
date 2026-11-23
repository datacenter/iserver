import json
import click

from lib.intersight import settings


@click.command("cache")
@click.pass_obj
@click.option("--enabled", default=None, help="Enable cache")
@click.option("--ttl", default=0, type=click.INT, help="Cache ttl in seconds")
def settings_iaccount_cache_command(ctx, enabled, ttl):
    """Cache settings"""

    settings_handler = settings.IntersightSettings()

    if enabled is not None:
        if enabled.lower() not in ['true', 'false']:
            ctx.my_output.error(
                'enabled must be true or false'
            )
            return

        if enabled.lower() == 'true':
            if not settings_handler.set_cache_enabled():
                ctx.my_output.error(
                    'cache enable failed'
                )
                return

        if enabled.lower() == 'false':
            if not settings_handler.set_cache_disabled():
                ctx.my_output.error(
                    'cache disable failed'
                )
                return

    if ttl > 0:
        if not settings_handler.set_cache_ttl(ttl):
            ctx.my_output.error(
                'cache ttl set failed'
            )
            return

    settings_handler.print_intersight_settings()
