import click

from menu.utils.test.get.name import utils_test_get_name_command
from menu.utils.test.get.names import utils_test_get_names_command
from menu.utils.test.get.collection import utils_test_get_collection_command
from menu.utils.test.get.collections import utils_test_get_collections_command
from menu.utils.test.get.summary import utils_test_get_summary_command


class Failure(Exception):
    pass


@click.group("get")
@click.pass_obj
def utils_test_get_menu(ctx):
    """Test"""


utils_test_get_menu.add_command(utils_test_get_name_command)
utils_test_get_menu.add_command(utils_test_get_names_command)
utils_test_get_menu.add_command(utils_test_get_collection_command)
utils_test_get_menu.add_command(utils_test_get_collections_command)
utils_test_get_menu.add_command(utils_test_get_summary_command)
