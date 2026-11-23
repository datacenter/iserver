import click

from menu.get.helm.chart import get_helm_chart_command
from menu.get.helm.release import get_helm_release_command


class Failure(Exception):
    pass


@click.group("helm")
@click.pass_obj
def get_helm_menu(ctx):
    """Get helm commands"""


get_helm_menu.add_command(get_helm_chart_command)
get_helm_menu.add_command(get_helm_release_command)
