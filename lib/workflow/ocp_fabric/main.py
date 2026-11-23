import copy
import json
from lib import output_helper
from lib import ssh
from lib.ocp import settings as ocp_settings
from lib.workflow.ocp_fabric.aci import main as aci_task
from lib.workflow.aci_interface import check as aci_interface_check
from lib.workflow.aci_policy import check as aci_policy_check
from menu import common


def get_fabric_configuration(connector, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(connector):
        return None

    content = ocp_settings_handler.set_ocp_cluster_file(
        connector,
        'fabric.json'
    )
    return content


def save_fabric_configuration(connector, fabric, log_id):
    my_output = output_helper.OutputHelper(log_id=log_id)

    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(connector):
        return True

    success = ocp_settings_handler.set_ocp_cluster_file(
        connector,
        'fabric.json',
        json.dumps(fabric, indent=4)
    )
    if not success:
        my_output.error('Failed to save fabric information')
        return False

    my_output.default('Fabric information saved locally')

    management_ip = ocp_settings_handler.get_ocp_cluster_file(
        connector,
        'management_ip'
    )
    if management_ip is None:
        my_output.default('[WARNING] Management ip not found')
        return True

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        connector,
        'ssh.pub'
    )
    if filename is None:
        my_output.default('[WARNING] ssh.pub not found')
        return True

    ssh_handler = ssh.Ssh(
        management_ip,
        'core',
        key_filename=filename,
        log_id=log_id
    )
    success = ssh_handler.create_directory('/home/core/.itool')
    if not success:
        my_output.default('[WARNING] Directory .itool create failed')
        return True

    success = ssh_handler.create_file(
        json.dumps(fabric, indent=4),
        '.itool/fabric.json'
    )
    if not success:
        my_output.default('[WARNING] File .itool/fabric.json create failed on the cluster management host')
        return True

    my_output.default('Fabric information uploaded to management host [%s]' % (management_ip))
    return True


def run(data, fabric_mode, my_output, log_id, confirmation_on_check_failed=True):
    for fabric in data['controller']:
        if fabric['type'] == 'aci':
            success = aci_task.run(
                fabric_mode,
                fabric,
                data['server'],
                my_output,
                log_id
            )
            if success:
                continue

            if fabric_mode == 'check':
                if confirmation_on_check_failed:
                    my_output.default('Fabric state mismatch detected. Continue?')
                    if common.get_confirmation():
                        continue
                return False

            if fabric_mode == 'patch':
                my_output.default('Fabric configuration failed. Continue?')
                if common.get_confirmation():
                    continue
                return False

            if fabric_mode == 'delete':
                my_output.default('Fabric unconfiguration failed. Continue?')
                if common.get_confirmation():
                    continue
                return False

    return True

def run_check(data, log_id):
    success = True

    for controller in data['controller']:
        if controller['type'] == 'aci':
            controller_success = aci_policy_check.run(
                controller,
                log_id
            )
            success = success and controller_success

            controller_interfaces = []
            for server in data['server']:
                for interface in server['interface']:
                    if interface['domain'] == controller['domain']:
                        controller_interface = copy.deepcopy(interface)
                        controller_interface['context'] = '%s:%s' % (server['hostname'], interface['name'])
                        controller_interfaces.append(controller_interface)

            if len(controller_interfaces) == 0:
                continue

            # params = {}
            # params['apic'] = controller['apic']
            # params['interface'] = controller_interfaces
            
            # controller_success = aci_interface_check.run(
            #     params,
            #     log_id
            # )
            # success = success and controller_success

    return success

def run_patch(data, log_id):
    return True