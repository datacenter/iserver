import click

from menu.get.openshift.ai.cluster import get_openshift_ai_cluster_command
from menu.get.openshift.ai.version import get_openshift_ai_version_command


class Failure(Exception):
    pass


@click.group("ai")
@click.pass_obj
def get_openshift_ai_menu(ctx):
    """Get openshift assisted installer commands"""


get_openshift_ai_menu.add_command(get_openshift_ai_cluster_command)
get_openshift_ai_menu.add_command(get_openshift_ai_version_command)
