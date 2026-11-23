import click

from menu.create.helm.chart import create_helm_chart_command
from menu.create.helm.release import create_helm_release_command


class Failure(Exception):
    pass


@click.group("helm")
@click.pass_obj
def create_helm_menu(ctx):
    """Create helm commands"""


create_helm_menu.add_command(create_helm_chart_command)
create_helm_menu.add_command(create_helm_release_command)
