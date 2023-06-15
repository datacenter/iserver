import click

from lib import log_helper


@click.command("bug")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
def utils_cli_bug_command(ctx, name):
    """Submit bug report"""

    # iserver utils devel cli bug

    log_handler = log_helper.Log()
    log_handler.bug_report(name)
