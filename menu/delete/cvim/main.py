import click

from menu.delete.cvim.cluster import delete_cvim_cluster


class Failure(Exception):
    pass


@click.group("cvim")
@click.pass_obj
def delete_cvim_menu(ctx):
    """Delete cvim commands"""


delete_cvim_menu.add_command(delete_cvim_cluster)
