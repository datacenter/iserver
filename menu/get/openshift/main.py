import click

from menu.get.openshift.ai.main import get_openshift_ai_menu


class Failure(Exception):
    pass


@click.group("openshift")
@click.pass_obj
def get_openshift_menu(ctx):
    """Get rh openshift api commands"""


get_openshift_menu.add_command(get_openshift_ai_menu)
