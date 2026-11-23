import click

from menu.set.k8s.sc.default import set_k8s_sc_default_command
from menu.set.k8s.sc.nondefault import set_k8s_sc_nondefault_command


class Failure(Exception):
    pass


@click.group("sc")
@click.pass_obj
def set_k8s_sc_menu(ctx):
    """K8s storage class actions and settings"""


set_k8s_sc_menu.add_command(set_k8s_sc_default_command)
set_k8s_sc_menu.add_command(set_k8s_sc_nondefault_command)
