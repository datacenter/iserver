import click


from menu.get.iwo.action import get_iwo_action_command
from menu.get.iwo.application import get_iwo_application_command
from menu.get.iwo.chassis import get_iwo_chassis_command
from menu.get.iwo.cluster import get_iwo_cluster_command
from menu.get.iwo.container import get_iwo_container_command
from menu.get.iwo.dc import get_iwo_dc_command
from menu.get.iwo.disk import get_iwo_disk_command
from menu.get.iwo.namespace import get_iwo_namespace_command
from menu.get.iwo.network import get_iwo_network_command
from menu.get.iwo.phy import get_iwo_phy_command
from menu.get.iwo.pod import get_iwo_pod_command
from menu.get.iwo.region import get_iwo_region_command
from menu.get.iwo.service import get_iwo_service_command
from menu.get.iwo.spec import get_iwo_spec_command
from menu.get.iwo.storage import get_iwo_storage_command
from menu.get.iwo.switch import get_iwo_switch_command
from menu.get.iwo.target import get_iwo_target_command
from menu.get.iwo.workload import get_iwo_workload_command
from menu.get.iwo.vdc import get_iwo_vdc_command
from menu.get.iwo.vm import get_iwo_vm_command
from menu.get.iwo.volume import get_iwo_volume_command
from menu.get.iwo.zone import get_iwo_zone_command


class Failure(Exception):
    pass


@click.group("iwo")
@click.pass_obj
def get_iwo_menu(ctx):
    """Get iwo commands"""


get_iwo_menu.add_command(get_iwo_action_command)
get_iwo_menu.add_command(get_iwo_application_command)
get_iwo_menu.add_command(get_iwo_chassis_command)
get_iwo_menu.add_command(get_iwo_cluster_command)
get_iwo_menu.add_command(get_iwo_container_command)
get_iwo_menu.add_command(get_iwo_dc_command)
get_iwo_menu.add_command(get_iwo_disk_command)
get_iwo_menu.add_command(get_iwo_namespace_command)
get_iwo_menu.add_command(get_iwo_network_command)
get_iwo_menu.add_command(get_iwo_phy_command)
get_iwo_menu.add_command(get_iwo_pod_command)
get_iwo_menu.add_command(get_iwo_region_command)
get_iwo_menu.add_command(get_iwo_service_command)
get_iwo_menu.add_command(get_iwo_spec_command)
get_iwo_menu.add_command(get_iwo_storage_command)
get_iwo_menu.add_command(get_iwo_switch_command)
get_iwo_menu.add_command(get_iwo_target_command)
get_iwo_menu.add_command(get_iwo_workload_command)
get_iwo_menu.add_command(get_iwo_vdc_command)
get_iwo_menu.add_command(get_iwo_vm_command)
get_iwo_menu.add_command(get_iwo_volume_command)
get_iwo_menu.add_command(get_iwo_zone_command)
