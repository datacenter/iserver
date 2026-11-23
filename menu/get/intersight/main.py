import click

from menu.get.intersight.alarm import get_intersight_alarm_command
from menu.get.intersight.iaccount import get_intersight_iaccount_command
from menu.get.intersight.os_image import get_intersight_os_image_command
from menu.get.intersight.os_vendor import get_intersight_os_vendor_command
from menu.get.intersight.os_version import get_intersight_os_version_command
from menu.get.intersight.os_config import get_intersight_os_config_command
from menu.get.intersight.scu import get_intersight_scu_command
from menu.get.intersight.settings import get_intersight_settings_command
from menu.get.intersight.workflows import get_intersight_workflows_command
from menu.get.intersight.workflow import get_intersight_workflow_command


class Failure(Exception):
    pass


@click.group("is")
@click.pass_obj
def get_intersight_menu(ctx):
    """Get intersight commands"""


get_intersight_menu.add_command(get_intersight_alarm_command)
get_intersight_menu.add_command(get_intersight_iaccount_command)
get_intersight_menu.add_command(get_intersight_os_image_command)
get_intersight_menu.add_command(get_intersight_os_vendor_command)
get_intersight_menu.add_command(get_intersight_os_version_command)
get_intersight_menu.add_command(get_intersight_os_config_command)
get_intersight_menu.add_command(get_intersight_scu_command)
get_intersight_menu.add_command(get_intersight_settings_command)
get_intersight_menu.add_command(get_intersight_workflows_command)
get_intersight_menu.add_command(get_intersight_workflow_command)
