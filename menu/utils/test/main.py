import click

from menu.utils.test.get.main import utils_test_get_menu
from menu.utils.test.run import utils_test_run_command


class Failure(Exception):
    pass


@click.group("test")
@click.pass_obj
def utils_test_menu(ctx):
    """Self Testing"""


utils_test_menu.add_command(utils_test_get_menu)
utils_test_menu.add_command(utils_test_run_command)
