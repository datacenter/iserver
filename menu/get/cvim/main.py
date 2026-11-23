import click

from menu.get.cvim.cluster import get_cvim_cluster


class Failure(Exception):
    pass


@click.group("cvim")
@click.pass_obj
def get_cvim_menu(ctx):
    """Get cvim commands (alpha)"""


get_cvim_menu.add_command(get_cvim_cluster)
