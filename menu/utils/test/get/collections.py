import click

from lib import self_testing


@click.command("test-collections")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_test_get_collections_command(ctx, directory):
    """get iserver test collections"""

    # iserver utils test get collections

    tests = self_testing.get_tests_collections(directory, names=True)
    for test in tests:
        print(test)
