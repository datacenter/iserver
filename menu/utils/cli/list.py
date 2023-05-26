import click

from lib import log_helper


@click.command("list")
@click.pass_obj
def utils_cli_list_command(ctx):
    """Show last commands history"""

    # iserver utils cli list

    log_handler = log_helper.Log()
    log_handler.show_last_logs()
