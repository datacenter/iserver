# Useful links
# https://cloudcult.dev/creating-openshift-clusters-with-the-assisted-service-api/
# https://cloudcult.dev/static-networking-with-assisted-installer/
# https://cloudcult.dev/calico-installation-openshift-assisted-installer/
# https://cloudcult.dev/cilium-installation-openshift-assisted-installer/
# https://api.openshift.com/?urls.primaryName=assisted-service%20service#/

import os
import json
import time
import uuid
import base64
from progress.bar import Bar

from lib import file_helper
from lib import ip_helper
from lib import log_helper
from lib import output_helper
from lib import ssh
from lib import template
from lib.openshift import console
from lib.openshift import output as openshift_output
from lib.ocp import settings as ocp_settings
from lib.redfish import endpoint as redfish_endpoint
from lib.imc.cli import endpoint as imc_endpoint

from menu import common


def get_data(user_settings, my_output):
    data = {}

    mandatory_keys = [
        'name',
        'openshift_version',
        'base_dns_domain',
        'ssh_public_key'
    ]
    for key in mandatory_keys:
        if key not in user_settings:
            my_output.error('Key %s missing' % (key))
            return None, None

    data['name'] = '%s-%s' % (
        user_settings['name'],
        str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1]
    )

    data['openshift_version'] = user_settings['openshift_version']
    data['base_dns_domain'] = user_settings['base_dns_domain']
    data['ssh_public_key'] = user_settings['ssh_public_key']

    if 'cpu_architecture' in user_settings:
        data['cpu_architecture'] = user_settings['cpu_architecture']
    else:
        data['cpu_architecture'] = 'x86_64'

    if 'cpu_architecture' in user_settings:
        data['cluster_network_cidr'] = user_settings['cluster_network_cidr']
    else:
        data['cluster_network_cidr'] = '10.128.0.0/14'

    if 'cluster_network_host_prefix' in user_settings:
        data['cluster_network_host_prefix'] = user_settings['cluster_network_host_prefix']
    else:
        data['cluster_network_host_prefix'] = 23

    if 'service_network_cidr' in user_settings:
        data['service_network_cidr'] = user_settings['service_network_cidr']
    else:
        data['service_network_cidr'] = '172.30.0.0/16'

    if 'server' not in user_settings or len(user_settings['server']) == 0:
        my_output.error('Servers key missing or empty')
        return None, None

    if len(user_settings['server']) == 2:
        my_output.error('Invalid server count')
        return None, None

    if len(user_settings['server']) == 1:
        data['high_availability_mode'] = "None"
        user_settings['api'] = user_settings['server'][0]['ssh']['ip']
        user_settings['ingress'] = user_settings['server'][0]['ssh']['ip']
    else:
        data['high_availability_mode'] = "Full"
        for key in ['api', 'ingress']:
            if key not in user_settings:
                my_output.error('Key %s missing' % (key))
                return None, None

    if 'http_proxy' in user_settings:
        data['http_proxy'] = user_settings['http_proxy']
    else:
        data['http_proxy'] = None

    if 'https_proxy' in user_settings:
        data['https_proxy'] = user_settings['https_proxy']
    else:
        data['https_proxy'] = None

    if 'no_proxy' in user_settings:
        data['no_proxy'] = user_settings['no_proxy']
    else:
        data['no_proxy'] = None

    if 'olm_operators' in user_settings:
        data['olm_operators'] = user_settings['olm_operators']
    else:
        data['olm_operators'] = []

    if 'network_type' in user_settings:
        data['network_type'] = user_settings['network_type']
    else:
        data['network_type'] = 'OVNKubernetes'

    return user_settings, data

def get_infra(user_settings, data, directory, my_output, log_id):
    template_handler = template.Template(log_id=log_id)
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

        nmstate_filename = os.path.join(
            directory,
            server['nmstate']
        )
        if not os.path.isfile(nmstate_filename):
            my_output.error('nmstate file not found: %s' % (nmstate_filename))
            return None

        content = file_helper.get_file_text(
            nmstate_filename
        )
        if content is None:
            my_output.error('nmstate file read failed: %s' % (nmstate_filename))
            return None

        if 'variables' in server and len(server['variables']) > 0:
            content = template_handler.replace_attributes(
                content,
                server['variables']
            )
            if content is None:
                my_output.error('nmstate variables replacemet failed for server %s' % (server['redfish']['endpoint_ip']))
                return None

            if template_handler.is_template_attributes(content):
                my_output.error('nmstate variables replacemet missing for server %s' % (server['redfish']['endpoint_ip']))
                return None

        network_config['network_yaml'] = '\r\n'.join(content.split('\n'))

        infra['static_network_config'].append(
            network_config
        )

    infra['additional_trust_bundle'] = ''
    infra['image_type'] = 'minimal-iso'

    return infra

def get_manifests(user_settings, directory, my_output, log_id):
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

            encoded_content = base64.b64encode(
                content.encode('utf-8')
            ).decode('utf-8')

            manifests[file_basename] = encoded_content

    return manifests

def get_input_files(directory, log_id=None):
    console_handler = console.Console(log_id=log_id)
    my_output = output_helper.OutputHelper(log_id=log_id)
    log = log_helper.Log(log_id=log_id)

    my_output.default('Checking openshift API...')
    if not console_handler.is_ready():
        my_output.error('OpenShift API not configured')
        return False, None, None, None, None

    if len(directory) == 0:
        my_output.error('Cluster definition directory required')
        return False, None, None, None, None

    my_output.default('Checking user input...')

    filename = os.path.join(directory, 'cluster.json')
    user_settings = file_helper.get_file_json(filename)
    if user_settings is None:
        my_output.error('Failed to read cluster.json')
        return False, None, None, None, None

    user_settings, data = get_data(user_settings, my_output)
    if data is None:
        return False, None, None, None, None

    data['pull_secret'] = console_handler.get_pull_secret()
    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            data,
            indent=4
        )
    )

    infra = get_infra(user_settings, data, directory, my_output, log_id)
    if infra is None:
        return False, None, None, None, None

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
        return False, None, None, None, None

    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            manifests,
            indent=4
        )
    )

    return True, user_settings, data, infra, manifests

def create_cluster(data, infra, manifests, console_handler, my_output, log):
    if data['network_type'] in ['OpenShiftSDN', 'OVNKubernetes']:
        cluster_id = console_handler.create_assisted_install_cluster(data)
        if cluster_id is None:
            my_output.error('Cluster create failed')
            return None, None

        my_output.default('Cluster created: %s [%s]' % (data['name'], cluster_id))
    else:
        target_cni = data['network_type']
        data['network_type'] = 'OVNKubernetes'

        cluster_id = console_handler.create_assisted_install_cluster(data)
        if cluster_id is None:
            my_output.error('Cluster create failed')
            return None, None

        my_output.default('Cluster created: %s [%s]' % (data['name'], cluster_id))

        patch_data_text = '"{\\\"networking\\\":{\\\"networkType\\\":\\\"%s\\\"}}"' % (target_cni)
        response = console_handler.patch_assisted_install_cluster_install_config(cluster_id, patch_data_text)
        if response is None:
            my_output.error('Cluster install config patch with target cni failed')
            return None, None

        my_output.default('Cluster install config cni patched: %s' % (target_cni))

    infra['cluster_id'] = cluster_id
    infra_id = console_handler.create_assisted_install_infra(infra)
    if infra_id is None:
        my_output.error('Infra create failed')
        return None, None

    my_output.default('Infra created: %s' % (infra_id))

    if len(manifests) > 0:
        for manifest in manifests:
            success = console_handler.create_assisted_install_manifest(
                cluster_id,
                manifest,
                manifests[manifest]
            )
            if not success:
                my_output.error('Manifest create failed')
                return None, None

            my_output.default('Manifest created: %s' % (manifest))

    cluster_info = console_handler.get_assisted_install_cluster(
        cluster_id=cluster_id,
        config_info=True,
        credentials_info=True,
        infra_info=True,
        manifest_info=True,
        kubeconfig_info=True,
        cache_enabled=False
    )
    if cluster_info is None:
        my_output.error('Failed to get newly created cluster information')
        return None, None

    log.debug(
        'workflow_ocp_bm_installation',
        json.dumps(
            cluster_info,
            indent=4
        )
    )

    return cluster_id, cluster_info

def boot_from_iso(user_settings, cluster_id, cluster_info, console_handler, my_output, log, log_id):
    if cluster_info['iso_url'] is None:
        my_output.error('ISO URL not found...')
        return False

    iso_filename = '/tmp/%s.iso' % (cluster_id)
    my_output.default('Download ISO...')
    log.debug(
        'workflow_ocp_bm_installation',
        'Downloading %s to %s' % (cluster_info['iso_url'], iso_filename)
    )
    if not ip_helper.download_url(cluster_info['iso_url'], iso_filename):
        my_output.error('ISO download failed')
        return False, False

    web_server_supported = True
    if user_settings['web_server']['ssh_public_key'] is None:
        ssh_handler = ssh.Ssh(
            user_settings['web_server']['ip'],
            user_settings['web_server']['username'],
            password=user_settings['web_server']['password']
        )
    else:
        key_filename = file_helper.set_tmp_file(
            user_settings['web_server']['ssh_public_key']
        )
        ssh_handler = ssh.Ssh(
            user_settings['web_server']['ip'],
            user_settings['web_server']['username'],
            key_filename=key_filename
        )

    if not ssh_handler.is_ssh():
        my_output.error('SSH access to web server failed')
        web_server_supported = False
    else:
        my_output.default('Upload iso to web server...')
        target_iso_filename = '%s/%s.iso' % (
            user_settings['web_server']['image_upload_directory'],
            cluster_id
        )
        success = ssh_handler.scp_file(
            iso_filename,
            target_iso_filename
        )
        log.debug(
            'workflow_ocp_bm_installation',
            'ISO upload: %s => %s' % (
                iso_filename,
                target_iso_filename
            )
        )

        if success:
            my_output.default('ISO uploaded')
        else:
            my_output.error('ISO upload failed')
            web_server_supported = False

    if not web_server_supported:
        my_output.default('Continue with manual mount and boot from iso: %s' % (iso_filename))
        if not common.get_confirmation():
            return False, False

    if web_server_supported:
        for server in user_settings['server']:
            redfish_handler = redfish_endpoint.RedfishEndpoint(
                server['redfish']['endpoint_type'],
                server['redfish']['endpoint_ip'],
                server['redfish']['endpoint_port'],
                server['redfish']['username'],
                server['redfish']['password'],
                auto_connect=True,
                ssl_verify=False,
                log_id=log_id
            )

            if not redfish_handler.is_connected():
                my_output.error('Redfish connection to server failed: %s' % (server['redfish']['endpoint_ip']))
                return False, False

            success = redfish_handler.endpoint_handler.insert_media_http('%s/%s.iso' % (user_settings['web_server']['image_base_url'], cluster_id))
            if not success:
                my_output.error('Redfish vmedia insert failed: %s' % (server['redfish']['endpoint_ip']))
                return False, False

            success = redfish_handler.endpoint_handler.wait_virtual_media_inserted()
            if not success:
                my_output.error('Redfish vmedia mapping failed: %s' % (server['redfish']['endpoint_ip']))
                return False, False

            my_output.default('Redfish vmedia mapping created successfuly: %s' % (server['redfish']['endpoint_ip']))

            success = redfish_handler.endpoint_handler.set_one_time_boot_source('Cd')
            if not success:
                my_output.error('Redfish boot source set to cd failed: %s' % (server['redfish']['endpoint_ip']))
                return False, False

            my_output.default('Redfish boot source set to cd successful: %s' % (server['redfish']['endpoint_ip']))

            success = redfish_handler.endpoint_handler.power_cycle()
            if not success:
                my_output.error('Server power cycle failed: %s' % (server['redfish']['endpoint_ip']))
                return False, False

            my_output.default('Server booted: %s' % (server['redfish']['endpoint_ip']))

    my_output.default('Wait for all the servers discovered...')

    bmc_addresses = []
    for server in user_settings['server']:
        bmc_addresses.append(
            server['redfish']['endpoint_ip']
        )

    success = console_handler.wait_assisted_install_cluster_hosts_discovered(
        cluster_id,
        bmc_addresses
    )
    if not success:
        my_output.error('Servers discovery failed')
        return False

    return True, web_server_supported

def update_cluster_settings(user_settings, cluster_id, console_handler, my_output):
    my_output.default('Change hostnames...')

    server_hostname = {}
    for server in user_settings['server']:
        server_hostname[server['redfish']['endpoint_ip']] = server['hostname']

    success = console_handler.update_assisted_install_cluster_hosts_hostname(
        cluster_id,
        server_hostname
    )
    if not success:
        my_output.error('Hostname update failed')
        return False

    if 'ntp' in user_settings and user_settings['ntp'] is not None:
        ntp_data = {}
        ntp_data['additional_ntp_source'] = user_settings['ntp']

        my_output.default('Update ntp with %s...' % (ntp_data['additional_ntp_source']))
        response = console_handler.patch_assisted_install_cluster(cluster_id, ntp_data)
        if response is None:
            my_output.error('NTP source update failed')
            return False

    if len(user_settings['server']) > 1:
        # 'api_vips': [{'cluster_id': '7200331f-ff22-467b-861f-f7a84dc77483', 'ip': '<ip>'}]
        api_vip = {}
        api_vip['cluster_id'] = cluster_id
        api_vip['ip'] = user_settings['api']
        api_vips = []
        api_vips.append(
            api_vip
        )

        # 'ingress_vips': [{'cluster_id': '7200331f-ff22-467b-861f-f7a84dc77483', 'ip': '<ip>'}]
        ingress_vip = {}
        ingress_vip['cluster_id'] = cluster_id
        ingress_vip['ip'] = user_settings['ingress']
        ingress_vips = []
        ingress_vips.append(
            ingress_vip
        )

        data = {}
        data['api_vips'] = api_vips
        data['ingress_vips'] = ingress_vips

        my_output.default('Update api %s and ingress vip %s' % (user_settings['api'], user_settings['ingress']))
        response = console_handler.patch_assisted_install_cluster(cluster_id, data)
        if response is None:
            my_output.error('API/Ingress VIP update failed')
            return False

    my_output.default('Wait for cluster ready to be installed...')

    return True

def wait_installation_started(cluster_id, console_handler, my_output):
    success = console_handler.wait_assisted_install_cluster_status(
        cluster_id,
        'ready'
    )
    if not success:
        my_output.error('Cluster has not reached ready state')
        return False

    my_output.default('Start installation request...')

    success = console_handler.action_assisted_install_cluster_install(
        cluster_id
    )
    if not success:
        my_output.error('Cluster installation start request failed')
        return False

    my_output.default('Wait for installation started...')

    success = console_handler.wait_assisted_install_cluster_status(
        cluster_id,
        'installing'
    )
    if not success:
        my_output.error('Cluster has not reached installation in progress state')
        return False

    return True

def boot_from_hdd(user_settings, my_output, log_id):
    for server in user_settings['server']:
        redfish_handler = redfish_endpoint.RedfishEndpoint(
            server['redfish']['endpoint_type'],
            server['redfish']['endpoint_ip'],
            server['redfish']['endpoint_port'],
            server['redfish']['username'],
            server['redfish']['password'],
            auto_connect=True,
            ssl_verify=False,
            log_id=log_id
        )

        if not redfish_handler.is_connected():
            my_output.error('Redfish connection to server failed: %s' % (server['redfish']['endpoint_ip']))
            return False

        success = redfish_handler.endpoint_handler.eject_media()
        if not success:
            my_output.error('Redfish vmedia eject failed: %s' % (server['redfish']['endpoint_ip']))
        else:
            my_output.default('Redfish vmedia eject successful: %s' % (server['redfish']['endpoint_ip']))

        imc_handler = imc_endpoint.ImcCliEndpoint(
            server['redfish']['endpoint_ip'],
            22,
            server['redfish']['username'],
            server['redfish']['password']
        )
        success = imc_handler.set_boot_order(['hdd'])
        if not success:
            my_output.error('Imc boot source set to hdd failed: %s' % (server['redfish']['endpoint_ip']))
            return False

        my_output.default('Imc boot source set to hdd successful: %s' % (server['redfish']['endpoint_ip']))

    return True

def host_pending_user_action_fixup(host_ip, user_settings, my_output):
    for server in user_settings['server']:
        if server['redfish']['endpoint_ip'] == host_ip:
            imc_handler = imc_endpoint.ImcCliEndpoint(
                server['redfish']['endpoint_ip'],
                22,
                server['redfish']['username'],
                server['redfish']['password']
            )

            if not imc_handler.is_boot_device_type('LOCALHDD'):
                my_output.default(
                    'Creating hdd boot device type: %s' % (host_ip)
                )
                success = imc_handler.create_boot_device('hdd', 'LOCALHDD', device_order=1)
                if not success:
                    my_output.error(
                        'Failed to create localhdd boot device type: %s' % (host_ip)
                    )
                    return

            if imc_handler.is_top_boot_order_from_device_type('HDD'):
                my_output.default('HDD already top priority for boot order: %s' % (host_ip))
            else:
                success = imc_handler.set_boot_order(['hdd'])
                if not success:
                    my_output.error(
                        'Failed to set boot order to hdd: %s' % (host_ip)
                    )
                    return

                my_output.default('Boot order set to hdd: %s' % (server['redfish']['endpoint_ip']))

            if not imc_handler.power_cycle():
                my_output.error('Imc power cycle failed: %s' % (server['redfish']['endpoint_ip']))
                return

            my_output.default('Power cycle successful: %s' % (server['redfish']['endpoint_ip']))

def wait_installation_finished(user_settings, cluster_id, console_handler, my_output, log):
    last_hosts_status = {}
    pending_fixup = {}
    for server in user_settings['server']:
        last_hosts_status[server['redfish']['endpoint_ip']] = None
        pending_fixup[server['redfish']['endpoint_ip']] = False

    bar_handler = Bar('Progress', max=100)
    bar_handler.goto(0)
    while True:
        progress = console_handler.get_assisted_install_cluster_progress(
            cluster_id
        )
        if progress is None:
            time.sleep(10)
            continue

        bar_handler.goto(progress)

        if progress == 100:
            break

        hosts_status = console_handler.get_assisted_install_cluster_host_status(
            cluster_id
        )
        if hosts_status is not None:
            for host_ip in last_hosts_status:
                if host_ip in hosts_status:
                    if hosts_status[host_ip] is not None:
                        if last_hosts_status[host_ip] is None or last_hosts_status[host_ip] != hosts_status[host_ip]:
                            last_hosts_status[host_ip] = hosts_status[host_ip]
                            log.debug(
                                'workflow_ocp_bm_installation',
                                'Host %s status changed to %s' % (
                                    host_ip,
                                    last_hosts_status[host_ip]
                                )
                            )
                            my_output.default(
                                'Host %s status changed to %s' % (
                                    host_ip,
                                    last_hosts_status[host_ip]
                                ),
                                before_newline=True
                            )

                            if last_hosts_status[host_ip] == 'error':
                                return False

                            if last_hosts_status[host_ip] == 'installing-pending-user-action':
                                if not pending_fixup[host_ip]:
                                    host_pending_user_action_fixup(host_ip, user_settings, my_output)
                                    pending_fixup[host_ip] = True

        time.sleep(10)

    my_output.default('Installation finished...', before_newline=True)
    return True

def delete_iso(user_settings, cluster_id, my_output):
    if user_settings['web_server']['ssh_public_key'] is None:
        ssh_handler = ssh.Ssh(
            user_settings['web_server']['ip'],
            user_settings['web_server']['username'],
            password=user_settings['web_server']['password']
        )
    else:
        key_filename = file_helper.set_tmp_file(
            user_settings['web_server']['ssh_public_key']
        )
        ssh_handler = ssh.Ssh(
            user_settings['web_server']['ip'],
            user_settings['web_server']['username'],
            key_filename=key_filename
        )

    if not ssh_handler.is_ssh():
        my_output.error('SSH access to web server failed')
        return False

    my_output.default('Delete iso from web server...')
    success = ssh_handler.delete_file(
        '%s/%s.iso' % (user_settings['web_server']['image_upload_directory'], cluster_id)
    )
    if not success:
        my_output.error('Delete failed')

    return True

def create_connector(user_settings, cluster_info, my_output, log_id):
    if 'connector' not in user_settings:
        return None

    connector_name = user_settings['connector']
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if ocp_settings_handler.is_ocp_cluster(connector_name):
        success = ocp_settings_handler.delete_ocp_cluster(
            connector_name
        )
        if not success:
            my_output.default('Existing ocp connector delete failed: %s' % (connector_name))
            return None

    my_output.default('Create ocp connector: %s' % (connector_name))
    success = ocp_settings_handler.create_ocp_cluster(
        connector_name,
        cluster_info['kubeconfig']
    )
    if not success:
        my_output.error('Ocp connector create failed')
        return None

    my_output.default('Ocp connector created')

    success = ocp_settings_handler.set_ocp_cluster_kubeadmin(
        connector_name,
        cluster_info['credentials']['password']
    )
    if not success:
        my_output.error('Kubeadmin updated failed')
        return None

    my_output.default('Kubeadmin updated')

    success = ocp_settings_handler.set_ocp_cluster_file(
        connector_name,
        'ssh.pub',
        user_settings['ssh_public_key']
    )
    if not success:
        my_output.error('SSH public key update failed')
        return None

    my_output.default('SSH public key updated')

    ssh_settings = {}
    ssh_settings['username'] = 'core'
    ssh_settings['password'] = None
    ssh_settings['key_filename'] = os.path.join(
        ocp_settings_handler.get_ocp_cluster_directory(connector_name),
        'ssh.pub'
    )
    ocp_settings_handler.set_ocp_cluster_parameter(
        connector_name,
        'ssh',
        ssh_settings
    )

    my_output.default('SSH access configured in connector')

    server_ip = None
    for server in user_settings['server']:
        if server['kube']:
            server_ip = server['ssh']['ip']

    if server_ip is not None:
        server_settings = {}
        server_settings['ip'] = server_ip
        server_settings['username'] = 'core'
        server_settings['password'] = None
        server_settings['key_filename'] = os.path.join(
            ocp_settings_handler.get_ocp_cluster_directory(connector_name),
            'ssh.pub'
        )
        ocp_settings_handler.set_ocp_cluster_parameter(
            connector_name,
            'helm',
            ssh_settings
        )
        ocp_settings_handler.set_ocp_cluster_parameter(
            connector_name,
            'virtctl',
            ssh_settings
        )
        my_output.default('Helm and virtcl access configured in connector')

    # <ip>	api.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	oauth-openshift.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	console-openshift-console.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	grafana-openshift-monitoring.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	thanos-querier-openshift-monitoring.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	prometheus-k8s-openshift-monitoring.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan
    # <ip>	alertmanager-main-openshift-monitoring.apps.ocp-bm3-cilium-8858d4f50002.ocp.lan

    etc_hosts = []
    etc_hosts.append(
        '%s\tapi.%s.%s' % (
            user_settings['api'],
            cluster_info['name'],
            cluster_info['base_dns_domain']
        )
    )
    apps = [
        'oauth-openshift',
        'console-openshift-console',
        'grafana-openshift-monitoring',
        'thanos-querier-openshift-monitoring',
        'prometheus-k8s-openshift-monitoring',
        'alertmanager-main-openshift-monitoring'
    ]
    for app in apps:
        etc_hosts.append(
            '%s\t%s.apps.%s.%s' % (
                user_settings['ingress'],
                app,
                cluster_info['name'],
                cluster_info['base_dns_domain']
            )
        )

    my_output.default('Required /etc/hosts entries')
    for entry in etc_hosts:
        my_output.default(entry)

    success = ocp_settings_handler.set_ocp_cluster_file(
        connector_name,
        'etc_hosts',
        '\n'.join(etc_hosts)
    )
    if not success:
        my_output.error('etc_hosts update failed')

    return connector_name

def check_ssh_acccess(user_settings, my_output):
    my_output.default('Check ssh access...')

    for server in user_settings['server']:
        key_filename = file_helper.set_tmp_file(
            user_settings['ssh_public_key']
        )
        ssh_handler = ssh.Ssh(
            server['ssh']['ip'],
            server['ssh']['username'],
            key_filename=key_filename
        )
        if not ssh_handler.is_ssh():
            my_output.error('SSH access to cluster node failed: %s' % (server['ssh']['ip']))
            return False

    return True

def prepare_kubeconfig(user_settings, cluster_info, my_output):
    my_output.default('Prepare kubeconfig...')
    for server in user_settings['server']:
        if server['kube']:
            key_filename = file_helper.set_tmp_file(
                user_settings['ssh_public_key']
            )
            ssh_handler = ssh.Ssh(
                server['ssh']['ip'],
                server['ssh']['username'],
                key_filename=key_filename
            )

            success = ssh_handler.create_directory('.kube')
            if not success:
                my_output.error('Directory .kube create failed')
                return False

            success = ssh_handler.scp_file(
                cluster_info['kubeconfig'],
                '.kube/config'
            )
            if not success:
                my_output.error('Kubeconfig upload failed')
                return False

            my_output.default('Kubeconfig upload successful')

            success = ssh_handler.set_file_chmod(
                '.kube/config',
                '600'
            )
            if not success:
                my_output.error('Kubeconfig chmod failed')
                return False

            my_output.default('Kubeconfig chmod successful')

    return True

def run_tasks(user_settings, my_output):
    my_output.default('Run tasks...')
    for server in user_settings['server']:
        if server['kube']:
            key_filename = file_helper.set_tmp_file(
                user_settings['ssh_public_key']
            )
            ssh_handler = ssh.Ssh(
                server['ssh']['ip'],
                server['ssh']['username'],
                key_filename=key_filename
            )

            if 'tasks' in user_settings:
                for task in user_settings['tasks']:
                    if 'command' in task:
                        for command in task['command']:
                            my_output.default('Run command: %s' % command, before_newline=True)
                            success, output, error = ssh_handler.run_cmd(command)
                            if not success:
                                my_output.error('Failed')
                            else:
                                my_output.default(output)

    return True

def post_install(user_settings, cluster_info, my_output, log_id):
    success = False
    connector_name = create_connector(user_settings, cluster_info, my_output, log_id)
    if check_ssh_acccess(user_settings, my_output):
        if prepare_kubeconfig(user_settings, cluster_info, my_output):
            if run_tasks(user_settings, my_output):
                success = True
    return success

def run(user_settings, data, infra, manifests, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    log = log_helper.Log(log_id=log_id)

    openshift_output_handler = openshift_output.OpenshiftOutput(log_id=log_id)
    console_handler = console.Console(log_id=log_id)

    cluster_id, cluster_info = create_cluster(
        data,
        infra,
        manifests,
        console_handler,
        my_output,
        log
    )
    if cluster_info is None:
        return False

    success, web_server_supported = boot_from_iso(
        user_settings,
        cluster_id,
        cluster_info,
        console_handler,
        my_output,
        log,
        log_id
    )
    if not success:
        return False

    success = update_cluster_settings(
        user_settings,
        cluster_id,
        console_handler,
        my_output
    )
    if not success:
        return False

    success = wait_installation_started(
        cluster_id,
        console_handler,
        my_output
    )

    if web_server_supported:
        success = boot_from_hdd(
            user_settings,
            my_output,
            log_id
        )
        if not success:
            return False

    success = wait_installation_finished(
        user_settings,
        cluster_id,
        console_handler,
        my_output,
        log
    )

    if web_server_supported:
        delete_iso(
            user_settings,
            cluster_id,
            my_output
        )

    if not success:
        my_output.error('Installation failed')
        return False

    my_output.default('Collecting cluster information...')

    cluster_info = console_handler.get_assisted_install_cluster(
        cluster_id=cluster_id,
        credentials_info=True,
        kubeconfig_info=True,
        cache_enabled=False
    )
    if cluster_info is None:
        my_output.error('Failed to get newly installed cluster information')
        return False

    openshift_output_handler.print_assisted_install_cluster_credentials(
        cluster_info
    )
    openshift_output_handler.print_assisted_install_cluster_kubeconfig(
        cluster_info
    )

    success = post_install(
        user_settings,
        cluster_info,
        my_output,
        log_id
    )
    if not success:
        return False

    my_output.default('OpenShift bare metal installation completed successfully')

    return True
