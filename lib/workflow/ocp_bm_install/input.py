import os
import json
import uuid
import base64
import yaml
from lib.openshift import console
from lib import file_helper
from lib import log_helper
from lib import output_helper
from lib import template
from lib.workflow.ocp_bm_install import cilium
from lib.workflow.ocp_bm_install import validations
from lib.workflow.ocp_bm_install import common as install_common
from lib.workflow.ocp_bm_install import install
from lib.workflow.aci_interface import check as aci_check


def get_input(directory, my_output):
    if len(directory) == 0:
        my_output.error('Cluster definition directory required')
        return None

    filename = os.path.join(directory, 'cluster.json')
    user_settings = file_helper.get_file_json(filename)
    if user_settings is None:
        my_output.error('Failed to read cluster.json')
        return None

    user_settings['directory'] = directory

    if 'server' not in user_settings:
        filename = os.path.join(user_settings['directory'], 'server.json')
        if not os.path.isfile(filename):
            my_output.error('Servers key missing or empty')
            return None

        user_settings['server'] = file_helper.get_file_json(filename)
        if user_settings['server'] is None:
            my_output.error('File server.json read failed')
            return None

    filename = os.path.join(user_settings['directory'], 'redfish.json')
    if os.path.isfile(filename):
        user_settings['redfish_credentials'] = file_helper.get_file_json(filename)
        if user_settings['redfish_credentials'] is None:
            my_output.error('redfish.json read failed')
            return None
        
    filename = os.path.join(user_settings['directory'], 'proxy.json')
    if os.path.isfile(filename):
        content = file_helper.get_file_json(filename)
        if content is None:
            my_output.error('File read failed: proxy.json')
            return None

        proxy_keys = [
            'http_proxy',
            'https_proxy',
            'no_proxy',
        ]
        for key in proxy_keys:
            if key in content:
                user_settings[key] = content[key]

    if 'ssh_public_key' not in user_settings:
        filename = os.path.join(user_settings['directory'], 'ssh.pub')
        if not os.path.isfile(filename):
            my_output.error('Key ssh_public_key missing or ssh.pub file missing')
            return None

        user_settings['ssh_public_key'] = file_helper.get_file_text(filename)
        if user_settings['ssh_public_key'] is None:
            my_output.error('File ssh.pub read failed')
            return None

        user_settings['ssh_public_key'] = user_settings['ssh_public_key'].strip().split('\n')[0]

    if 'web_server' not in user_settings:
        filename = os.path.join(user_settings['directory'], 'web.json')
        if os.path.isfile(filename):
            content = file_helper.get_file_json(filename)
            if content is None:
                my_output.error('Failed to read web.json: %s' % (filename))
                return None

            if isinstance(content, dict):
                if 'web-server' in content:
                    user_settings['web_server'] = content['web-server']
                else:
                    user_settings['web_server'] = content

    filename = os.path.join(user_settings['directory'], 'cilium.json')
    if os.path.isfile(filename):
        content = file_helper.get_file_json(filename)
        if content is None:
            my_output.error('File read failed: cilium.json')
            return None

        user_settings['cilium'] = content

    if 'tasks' not in user_settings:
        user_settings['tasks'] = []
        filename = os.path.join(user_settings['directory'], 'tasks.json')
        if os.path.isfile(filename):
            content = file_helper.get_file_json(filename)
            if content is None:
                my_output.error('Failed to read tasks.json')
                return None

            if isinstance(content, list):
                user_settings['tasks'] = content

            if isinstance(content, dict):
                if 'tasks' not in content:
                    my_output.error('Invalid tasks.json')
                    return None

                user_settings['tasks'] = content['tasks']

    if 'settings' not in user_settings:
        filename = os.path.join(user_settings['directory'], 'settings.json')
        if os.path.isfile(filename):
            user_settings['settings'] = file_helper.get_file_json(filename)
            if user_settings['settings'] is None:
                my_output.error('Failed to read settings.json')
                return None
            
    return user_settings


def get_data(user_settings):
    data = {}

    data['name'] = user_settings['name']
    if user_settings['randomize']:
        data['name'] = '%s-%s' % (
            user_settings['name'],
            str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1]
        )

    data['openshift_version'] = user_settings['openshift_version']
    data['base_dns_domain'] = user_settings['base_dns_domain']
    data['ssh_public_key'] = user_settings['ssh_public_key']
    data['cpu_architecture'] = user_settings['cpu_architecture']
    data['cluster_network_cidr'] = user_settings['cluster_network_cidr']
    data['cluster_network_host_prefix'] = user_settings['cluster_network_host_prefix']
    data['service_network_cidr'] = user_settings['service_network_cidr']
    data['high_availability_mode'] = user_settings['high_availability_mode']
    data['http_proxy'] = user_settings['http_proxy']
    data['https_proxy'] = user_settings['https_proxy']
    data['no_proxy'] = user_settings['no_proxy']
    data['network_type'] = user_settings['network_type']
    data['disk_encryption'] = {}
    data['disk_encryption']['enable_on'] = user_settings['disk_encryption']
    data['disk_encryption']['mode'] = user_settings['encryption_mode']
    
    return data


def get_infra(user_settings, data):
    infra = {}

    infra['cpu_architecture'] = data['cpu_architecture']
    infra['openshift_version'] = data['openshift_version']
    infra['proxy'] = {}
    infra['proxy']['http_proxy'] = data['http_proxy']
    infra['proxy']['https_proxy'] = data['https_proxy']
    infra['proxy']['no_proxy'] = data['no_proxy']
    infra['ssh_authorized_key'] = data['ssh_public_key']

    infra['static_network_config'] = []
    for server in user_settings['server']:
        network_config = {}
        network_config['mac_interface_map'] = []
        for interface in server['interface']:
            mac_interface_map = {}
            mac_interface_map['logical_nic_name'] = interface['name']
            mac_interface_map['mac_address'] = interface['mac']
            network_config['mac_interface_map'].append(
                mac_interface_map
            )

        network_config['network_yaml'] = server['network_yaml']
        infra['static_network_config'].append(
            network_config
        )

    infra['additional_trust_bundle'] = ''

    infra['image_type'] = '%s-iso' % (user_settings['iso']['mode'])

    return infra


def get_manifests(user_settings, directory, my_output, log_id, silent=False):
    manifests = {}
    manifests_directory = os.path.join(directory, 'manifests')
    if os.path.isdir(manifests_directory):
        template_handler = template.Template(log_id=log_id)
        for file_basename in os.listdir(manifests_directory):
            filename = os.path.join(
                manifests_directory,
                file_basename
            )
            content = file_helper.get_file_text(
                filename
            )
            if content is None:
                my_output.error('manifest file read failed: %s' % (filename))
                return None

            if 'variables' in user_settings and len(user_settings['variables']) > 0:
                content = template_handler.replace_attributes(
                    content,
                    user_settings['variables']
                )
                if content is None:
                    my_output.error('manifest variables replacemet failed for file %s' % (filename))
                    return None

                if template_handler.is_template_attributes(content):
                    my_output.error('manifest variables replacemet missing for file %s' % (filename))
                    return None
            else:
                if template_handler.is_template_attributes(content):
                    my_output.error('manifest variables replacemet missing for file %s' % (filename))
                    return None

            try:
                jcontent = yaml.safe_load(
                    content
                )
            except BaseException:
                my_output.error('manifest yaml read failed %s' % (filename))
                return None

            manifests[file_basename] = content

    if user_settings['network_type'] == 'Cilium':
        if len(manifests) == 0:
            my_output.error('Cilium manifests required')
            return None

        manifests = cilium.get_cilium_manifests(user_settings, manifests, my_output, silent=silent)
        if manifests is None:
            return None

    for file_basename in manifests:
        manifests[file_basename] = base64.b64encode(
            manifests[file_basename].replace('QUOTE', '"').encode('utf-8')
        ).decode('utf-8')

    return manifests


def check_fabric(user_settings, log_id):
    apic_names = []

    for server in user_settings['server']:
        for interface in server['interface']:
            if 'aci' not in interface:
                continue

            if interface['aci']['apic'] not in apic_names:
                apic_names.append(
                    interface['aci']['apic']
                )

    for apic_name in apic_names:
        params = {}
        params['apic'] = apic_name

        params['interface'] = []
        for server in user_settings['server']:
            for interface in server['interface']:
                if 'aci' not in interface:
                    continue

                if interface['aci']['apic'] == apic_name:
                    apic_interface = {}
                    apic_interface['context'] = '%s:%s' % (server['hostname'], interface['name'])
                    apic_interface['node'] = interface['aci']['node']
                    apic_interface['port'] = interface['aci']['port']
                    apic_interface['mac'] = interface['mac']
                    apic_interface['ip'] = server['ssh']['ip']
                    apic_interface['gateway'] = user_settings['machine_network_gateway']
                    if 'vlan' in server:
                        apic_interface['vlan'] = server['vlan']
                        apic_interface['trunk'] = True
                    if server['kube_interface_count'] > 1:
                        apic_interface['bond'] = True
                    params['interface'].append(apic_interface)

        success = aci_check.run(params, log_id)
        if not success:
            return False
        
    return True


def run(directory, install_mode, log_id=None, offline=False):
    my_output = output_helper.OutputHelper(log_id=log_id)
    log = log_helper.Log(log_id=log_id)

    my_output.default('Checking user input', before_newline=True, underline=True)
    user_settings = get_input(directory, my_output)
    if user_settings is None:
        return None, None, None, None
    
    my_output.default('- input files loaded')
    user_settings['mode'] = install_mode

    user_settings = validations.run(user_settings, my_output, log_id)
    if user_settings is None:
        return None, None, None, None

    console_handler = console.Console(
        log_id=log_id,
        do_strip=user_settings['strip_token'],
        check_ssl=user_settings['iso']['check_ssl'],
        timeout=user_settings['iso']['timeout']
    )

    my_output.default('Checking openshift API', before_newline=True, underline=True)
    if not console_handler.check_token(my_output, user_settings['strip_token']):
        if install_mode == 'install':
            return None, None, None, None

    data = get_data(user_settings)
    data['pull_secret'] = console_handler.get_pull_secret()
    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            data,
            indent=4
        )
    )

    infra = get_infra(user_settings, data)
    if infra is None:
        return None, None, None, None

    infra['name'] = '%s_infra-env' % (data['name'])
    infra['pull_secret'] = console_handler.get_pull_secret()

    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            infra,
            indent=4
        )
    )

    manifests = get_manifests(user_settings, directory, my_output, log_id)
    if manifests is None:
        return None, None, None, None
    
    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            manifests,
            indent=4
        )
    )

    if not check_fabric(user_settings, log_id):
        return None, None, None, None
    
    user_settings = install_common.check_iso_server(user_settings, my_output, log_id=log_id)
    if user_settings is None:
        return None, None, None, None

    if not offline:
        if not install_common.check_web_server(user_settings, my_output, log_id=log_id):
            return None, None, None, None

    if not offline:
        user_settings = install_common.check_server_redfish_access(
            user_settings,
            my_output,
            log_id,
            include_vmedia=True,
            include_boot_source=True,
            include_actions=True
        )
        if user_settings is None:
            return None, None, None, None

    return user_settings, data, infra, manifests
