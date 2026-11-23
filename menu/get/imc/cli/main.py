import click

from menu.get.imc.cli.adapter import get_imc_cli_adapter_command
from menu.get.imc.cli.admin import get_imc_cli_admin_command
from menu.get.imc.cli.bbu import get_imc_cli_bbu_command
from menu.get.imc.cli.bios import get_imc_cli_bios_command
from menu.get.imc.cli.boot import get_imc_cli_boot_command
from menu.get.imc.cli.chassis import get_imc_cli_chassis_command
from menu.get.imc.cli.cpu import get_imc_cli_cpu_command
from menu.get.imc.cli.dimm import get_imc_cli_dimm_command
from menu.get.imc.cli.fault import get_imc_cli_fault_command
from menu.get.imc.cli.flex import get_imc_cli_flex_command
from menu.get.imc.cli.fw import get_imc_cli_fw_command
from menu.get.imc.cli.hdd import get_imc_cli_hdd_command
from menu.get.imc.cli.http import get_imc_cli_http_command
from menu.get.imc.cli.hw import get_imc_cli_hw_command
from menu.get.imc.cli.endpoint import get_imc_cli_endpoint_command
from menu.get.imc.cli.ip import get_imc_cli_ip_command
from menu.get.imc.cli.ipmi import get_imc_cli_ipmi_command
from menu.get.imc.cli.kvm import get_imc_cli_kvm_command
from menu.get.imc.cli.led import get_imc_cli_led_command
from menu.get.imc.cli.memory import get_imc_cli_memory_command
from menu.get.imc.cli.net import get_imc_cli_net_command
from menu.get.imc.cli.ntp import get_imc_cli_ntp_command
from menu.get.imc.cli.pci import get_imc_cli_pci_command
from menu.get.imc.cli.psu import get_imc_cli_psu_command
from menu.get.imc.cli.redfish import get_imc_cli_redfish_command
from menu.get.imc.cli.sel import get_imc_cli_sel_command
from menu.get.imc.cli.sensor import get_imc_cli_sensor_command
from menu.get.imc.cli.smtp import get_imc_cli_smtp_command
from menu.get.imc.cli.snmp import get_imc_cli_snmp_command
from menu.get.imc.cli.sol import get_imc_cli_sol_command
from menu.get.imc.cli.ssh import get_imc_cli_ssh_command
from menu.get.imc.cli.storageadapter import get_imc_cli_storageadapter_command
from menu.get.imc.cli.syslog import get_imc_cli_syslog_command
from menu.get.imc.cli.tls import get_imc_cli_tls_command
from menu.get.imc.cli.tpm import get_imc_cli_tpm_command
from menu.get.imc.cli.utilization import get_imc_cli_utilization_command
from menu.get.imc.cli.version import get_imc_cli_version_command
from menu.get.imc.cli.vmedia import get_imc_cli_vmedia_command
from menu.get.imc.cli.xml import get_imc_cli_xml_command


class Failure(Exception):
    pass


@click.group("cli")
@click.pass_obj
def get_imc_cli_menu(ctx):
    """Get imc commands"""


get_imc_cli_menu.add_command(get_imc_cli_adapter_command)
get_imc_cli_menu.add_command(get_imc_cli_admin_command)
get_imc_cli_menu.add_command(get_imc_cli_bbu_command)
get_imc_cli_menu.add_command(get_imc_cli_bios_command)
get_imc_cli_menu.add_command(get_imc_cli_boot_command)
get_imc_cli_menu.add_command(get_imc_cli_chassis_command)
get_imc_cli_menu.add_command(get_imc_cli_cpu_command)
get_imc_cli_menu.add_command(get_imc_cli_dimm_command)
get_imc_cli_menu.add_command(get_imc_cli_fault_command)
get_imc_cli_menu.add_command(get_imc_cli_flex_command)
get_imc_cli_menu.add_command(get_imc_cli_fw_command)
get_imc_cli_menu.add_command(get_imc_cli_hdd_command)
get_imc_cli_menu.add_command(get_imc_cli_http_command)
get_imc_cli_menu.add_command(get_imc_cli_hw_command)
get_imc_cli_menu.add_command(get_imc_cli_endpoint_command)
get_imc_cli_menu.add_command(get_imc_cli_ip_command)
get_imc_cli_menu.add_command(get_imc_cli_ipmi_command)
get_imc_cli_menu.add_command(get_imc_cli_kvm_command)
get_imc_cli_menu.add_command(get_imc_cli_led_command)
get_imc_cli_menu.add_command(get_imc_cli_memory_command)
get_imc_cli_menu.add_command(get_imc_cli_net_command)
get_imc_cli_menu.add_command(get_imc_cli_ntp_command)
get_imc_cli_menu.add_command(get_imc_cli_pci_command)
get_imc_cli_menu.add_command(get_imc_cli_psu_command)
get_imc_cli_menu.add_command(get_imc_cli_redfish_command)
get_imc_cli_menu.add_command(get_imc_cli_sel_command)
get_imc_cli_menu.add_command(get_imc_cli_sensor_command)
get_imc_cli_menu.add_command(get_imc_cli_smtp_command)
get_imc_cli_menu.add_command(get_imc_cli_snmp_command)
get_imc_cli_menu.add_command(get_imc_cli_sol_command)
get_imc_cli_menu.add_command(get_imc_cli_ssh_command)
get_imc_cli_menu.add_command(get_imc_cli_storageadapter_command)
get_imc_cli_menu.add_command(get_imc_cli_syslog_command)
get_imc_cli_menu.add_command(get_imc_cli_tls_command)
get_imc_cli_menu.add_command(get_imc_cli_tpm_command)
get_imc_cli_menu.add_command(get_imc_cli_utilization_command)
get_imc_cli_menu.add_command(get_imc_cli_version_command)
get_imc_cli_menu.add_command(get_imc_cli_vmedia_command)
get_imc_cli_menu.add_command(get_imc_cli_xml_command)
