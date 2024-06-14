import click

from lib import self_testing


@click.command("summary")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_test_get_summary_command(ctx, directory):
    """get iserver test summary"""

    # iserver utils test get summary

    self_testing.get_summary(directory, replace=True)
