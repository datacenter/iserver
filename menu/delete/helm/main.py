import click

from menu.delete.helm.chart import delete_helm_chart_command
from menu.delete.helm.release import delete_helm_release_command


class Failure(Exception):
    pass


@click.group("helm")
@click.pass_obj
def delete_helm_menu(ctx):
    """Delete helm commands"""


delete_helm_menu.add_command(delete_helm_chart_command)
delete_helm_menu.add_command(delete_helm_release_command)
