import click

from menu.get.openshift.ai.main import get_openshift_ai_menu
from menu.get.openshift.login import get_openshift_login_command


class Failure(Exception):
    pass


@click.group("openshift")
@click.pass_obj
def get_openshift_menu(ctx):
    """Get rh openshift api commands"""


get_openshift_menu.add_command(get_openshift_ai_menu)
get_openshift_menu.add_command(get_openshift_login_command)
