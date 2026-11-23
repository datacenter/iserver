import click

from lib import self_testing


@click.command("names")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_test_get_names_command(ctx, directory):
    """get iserver test names"""

    # iserver utils test get names

    names = self_testing.get_tests(directory, names=True)
    if names is None:
        print('No tests found')
        return

    for name in names:
        print(name)
