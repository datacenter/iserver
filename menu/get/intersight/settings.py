import click

from lib.intersight import settings


@click.command("settings")
@click.pass_obj
def get_intersight_settings_command(ctx):
    """Get intersight settings"""

    settings_handler = settings.IntersightSettings(
        log_id=ctx.run_id
    )

    settings_handler.print_intersight_settings()
