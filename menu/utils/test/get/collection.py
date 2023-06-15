import click

from lib import self_testing


@click.command("collection")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_test_get_collection_command(ctx, name, directory):
    """get iserver test collection info"""

    # iserver utils test get collection

    self_testing.get_tests_collection_info(name, directory)
