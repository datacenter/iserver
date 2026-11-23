import json
import click

from lib import self_testing


@click.command("name")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_test_get_name_command(ctx, name, directory):
    """get iserver test name"""

    # iserver utils test get name

    test = self_testing.get_test(name, directory)
    if test is None:
        print('Test not found')
        return

    print(json.dumps(test, indent=4))
