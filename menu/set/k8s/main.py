import click

from menu.set.k8s.cluster import set_k8s_cluster


class Failure(Exception):
    pass


@click.group("k8s")
@click.pass_obj
def set_k8s_menu(ctx):
    """K8s actions and settings"""


set_k8s_menu.add_command(set_k8s_cluster)
