# Useful links
# https://cloudcult.dev/creating-openshift-clusters-with-the-assisted-service-api/
# https://cloudcult.dev/static-networking-with-assisted-installer/
# https://cloudcult.dev/calico-installation-openshift-assisted-installer/
# https://cloudcult.dev/cilium-installation-openshift-assisted-installer/
# https://api.openshift.com/?urls.primaryName=assisted-service%20service#/
# https://api.openshift.com/api/assisted-install/v2/openapi

import os
import shutil
import json
import time
import subprocess
import traceback
from progress.bar import Bar

from lib import file_helper
from lib import ip_helper
from lib import log_helper
from lib import output_helper
from lib.openshift import console
from lib.openshift import output as openshift_output
from lib.workflow.ocp_bm_install import common as install_common
from menu import common


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


def modify_boot_iso_locally(iso_filename, image_name, exec, core_password, my_output, destination=None):
    my_output.default('ISO manipulation locally', before_newline=True, underline=True)
    my_output.default('Iso filename: %s' % (iso_filename))

    directory = os.path.dirname(iso_filename)
    filename = os.path.basename(iso_filename)
    if destination is None:
        new_filename = 'new-%s' % (filename)
    else:
        new_filename = os.path.basename(destination)
    
    ignition_filename = 'ignition-%s' % (filename)
    ignition_filepath = os.path.join(directory, ignition_filename)

    command = 'sudo %s run -v %s:/data:Z --rm %s iso ignition show /data/%s' % (
        exec,
        directory,
        image_name,
        filename
    )
    my_output.default('Run: %s' % (command))
    try:
        output = subprocess.run(command.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        my_output.default(traceback.format_exc())
        success = False

    if not success:
        my_output.error('Failed to run command')
        return False

    try:
        ignition = json.loads(output.stdout)
    except BaseException:
        my_output.error('Failed to load ignition json output')
        my_output.default(output)
        return False

    my_output.default('Ignition output loaded')

    command = 'openssl passwd -6 %s' % (core_password)
    my_output.default('Run: %s' % (command))
    try:
        output = subprocess.run(command.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        my_output.default(traceback.format_exc())
        success = False

    if not success:
        my_output.error('Failed to run command')
        return False

    try:
        ignition['passwd']['users'][0]['passwordHash'] = output.stdout.strip('\n')
    except BaseException:
        my_output.error('Failed to update core user password in ingition data')
        my_output.default(json.dumps(ignition, indent=4))
        return False

    my_output.default('Core password updated in ignition')
    my_output.default(json.dumps(ignition['passwd']['users'][0], indent=4))

    if not file_helper.set_file_json(ignition_filepath, ignition):
        my_output.error('Failed to save ignition data to file: %s' % (ignition_filepath))
        return False

    command = 'sudo %s run -v %s:/data:Z --rm %s iso customize --output /data/%s --force /data/%s --live-ignition /data/%s' % (
        exec,
        directory,
        image_name,
        new_filename,
        filename,
        ignition_filename
    )
    my_output.default('Run: %s' % (command))
    try:
        output = subprocess.run(command.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        my_output.default(traceback.format_exc())
        success = False

    if not success:
        my_output.error('Failed to run command')
        return False

    my_output.default('New iso generated: %s' % (os.path.join(directory, new_filename)))

    command = 'sudo chmod 644 %s' % (
        os.path.join(directory, new_filename)
    )
    try:
        output = subprocess.run(command.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        my_output.default(traceback.format_exc())
        success = False

    if not success:
        my_output.error('Failed to run command')
        return False

    if destination is None:
        my_output.default('Copy %s/%s => %s' % (directory, new_filename, iso_filename))
        shutil.copy(
            os.path.join(directory, new_filename),
            iso_filename
        )

    return True


def modify_boot_iso_remotely(user_settings, local_iso_filename, my_output, log_id):
    my_output.default('ISO manipulation remotely', before_newline=True, underline=True)
    my_output.default('Local iso filename: %s' % (local_iso_filename))

    ssh_handler = install_common.get_server_ssh_handler(user_settings['iso'], log_id=log_id)
    success, exception_name, error = ssh_handler.is_ssh()
    if not success:
        my_output.error('SSH access to iso manipulation server failed: %s' % (error))
        return False
    
    my_output.default('SSH access to iso manipulation server successful')

    remote_iso_filename = '/tmp/%s' % (os.path.basename(local_iso_filename))
    directory = os.path.dirname(remote_iso_filename)
    filename = os.path.basename(remote_iso_filename)
    new_filename = 'new-%s' % (filename)
    ignition_filename = 'ignition-%s' % (filename)
    ignition_filepath = os.path.join(directory, ignition_filename)

    my_output.default('Upload %s => %s' % (local_iso_filename, remote_iso_filename))
    if not ssh_handler.scp_file(local_iso_filename, remote_iso_filename):
        my_output.error('Failed to upload iso')
        return False
    
    command = 'sudo docker run -v %s:/data:Z --rm %s iso ignition show /data/%s' % (
        directory,
        user_settings['iso']['image'],
        filename
    )

    my_output.default('Run: %s' % (command))
    success, output, error = ssh_handler.run_cmd(command)
    if not success:
        my_output.error('Failed to run command')
        my_output.default(str(output))
        my_output.default(str(error))
        return False
    
    try:
        ignition = json.loads(output)
    except BaseException:
        my_output.error('Failed to load ignition json output')
        my_output.default(output)
        return False
    
    my_output.default('Ignition output loaded')

    command = 'openssl passwd -6 %s' % (user_settings['iso']['core'])
    success, output, error = ssh_handler.run_cmd(command)
    if not success:
        my_output.error('Failed to run command')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    try:
        ignition['passwd']['users'][0]['passwordHash'] = output
    except BaseException:
        my_output.error('Failed to update core user password in ingition data')
        my_output.default(json.dumps(ignition, indent=4))
        return False
    
    my_output.default('Core password updated in ignition')
    my_output.default(json.dumps(ignition['passwd']['users'][0]))

    if ssh_handler.create_file(json.dumps(ignition, indent=4), filename=ignition_filepath) is None:
        my_output.default('Failed to save ignition data remotely')
        return False
    
    my_output.default('Ignition data saved remotely: %s ' % (ignition_filepath))

    command = 'sudo docker run -v %s:/data:Z --rm %s iso customize --output /data/%s --force /data/%s --live-ignition /data/%s' % (
        directory,
        user_settings['iso']['image'],
        new_filename,
        filename,
        ignition_filename
    )
    success, output, error = ssh_handler.run_cmd(command)
    if not success:
        my_output.error('Failed to run command')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default('New iso generated remotely: %s' % (os.path.join(directory, new_filename)))

    command = 'sudo chmod 644 %s' % (
        os.path.join(directory, new_filename)
    )
    success, output, error = ssh_handler.run_cmd(command)
    if not success:
        my_output.error('Failed to run command')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default('Download %s => %s' % (os.path.join(directory, new_filename), local_iso_filename))
    if not ssh_handler.scp_file(os.path.join(directory, new_filename), local_iso_filename, put=False):
        my_output.error('Failed to download iso')
        return False
    
    return True


def modify_boot_iso(user_settings, iso_filename, my_output, log_id):
    if user_settings['iso']['manual']:
        my_output.default('Manual iso modification mode', before_newline=True, underline=True)
        my_output.default('- file: %s' % (iso_filename))

        my_output.default('Modify iso file as needed...')
        return common.get_confirmation()
    
    if user_settings['iso']['core'] is None:
        return True
    
    my_output.default('Core user password override', before_newline=True, underline=True)
    my_output.default('- core password: %s' % (user_settings['iso']['core']))
    my_output.default('- container: %s' % (user_settings['iso']['exec']))
    my_output.default('- ip: %s' % (user_settings['iso']['ip']))

    if user_settings['iso']['ip'] == 'localhost':
        return modify_boot_iso_locally(
            iso_filename, 
            user_settings['iso']['image'],
            user_settings['iso']['exec'],
            user_settings['iso']['core'],
            my_output
        )
        
    my_output.default('- username: %s' % (user_settings['iso']['username']))
    return modify_boot_iso_remotely(user_settings, iso_filename, my_output, log_id)


def boot_from_iso(user_settings, cluster_id, cluster_info, my_output, log, log_id):
    if cluster_info['iso_url'] is None:
        my_output.error('ISO URL not found...')
        return False, None

    iso_filename = '/tmp/%s.iso' % (cluster_id)
    my_output.default('Download ISO', before_newline=True, underline=True)
    my_output.default('- url: %s' % (cluster_info['iso_url']))
    my_output.default('- ssl verify: %s' % (user_settings['iso']['check_ssl']))
    my_output.default('- timeout: %s' % (user_settings['iso']['timeout']))
    my_output.default('- target filename: %s' % (iso_filename))
    log.debug(
        'workflow_ocp_bm_installation',
        'Downloading %s to %s' % (cluster_info['iso_url'], iso_filename)
    )
    success = ip_helper.download_large_url(
        cluster_info['iso_url'], 
        iso_filename, 
        verify=user_settings['iso']['check_ssl'],
        timeout=user_settings['iso']['timeout']
    )
    if not success:
        my_output.error('ISO download failed')
        return False, None

    success = modify_boot_iso(user_settings, iso_filename, my_output, log_id)
    if not success:
        return False, None
    
    web_server_supported = True

    if user_settings['web_server']['ip'] == 'localhost':
        target_filename = os.path.join(
            user_settings['web_server']['image_upload_directory'],
            os.path.basename(iso_filename)
        )
        try:
            shutil.copy(
                iso_filename,
                target_filename
            )
        except BaseException:
            pass

        if not os.path.isfile(target_filename):
            my_output.error('Local copy of ISO failed')
            return False, None

    if user_settings['web_server']['ip'] != 'localhost':
        ssh_handler = install_common.get_server_ssh_handler(user_settings['web_server'], log_id=log_id)

        success, exception_name, error = ssh_handler.is_ssh()
        if not success:
            my_output.error('SSH access to web server failed: %s' % (error))
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
                return False, None

    if web_server_supported:
        for server in user_settings['server']:
            redfish_handler = install_common.get_server_redfish_handler(
                server['redfish'],
                log_id
            )

            my_output.default('Server: %s' % (server['hostname']), before_newline=True, underline=True)
            my_output.default('- endpoint ip: %s' % (server['redfish']['endpoint_ip']))
            my_output.default('- endpoint type:%s' % (server['redfish']['endpoint_type']))
            if server['redfish']['endpoint_type'] == 'fi':
                my_output.default('- inventory id: %s' % (server['redfish']['inventory_id']))

            if not redfish_handler.is_connected():
                my_output.error('Redfish connection to server failed: %s' % (server['redfish']['endpoint_ip']))
                return False, None

            my_output.default('- redfish connection successful')

            response = redfish_handler.endpoint_handler.get_boot_properties()
            if response is not None:
                my_output.default(
                    json.dumps(response, indent=4),
                    wrap='~~~'
                )

            url = '%s/%s.iso' % (user_settings['web_server']['image_base_url'], cluster_id)
            my_output.default('- vmedia url: %s' % (url))
            my_output.default('- vmedia id: %s' % (server['redfish']['virtual_media_id']))

            success = redfish_handler.endpoint_handler.insert_media_http(
                url,
                virtual_media_id=server['redfish']['virtual_media_id']
            )
            if not success:
                my_output.error('Redfish vmedia insert failed')
                return False, None

            success = redfish_handler.endpoint_handler.wait_virtual_media_inserted(
                virtual_media_id=server['redfish']['virtual_media_id']
            )
            if not success:
                my_output.error('Redfish vmedia mapping failed')
                return False, None

            my_output.default('- vmedia mapping created successfuly')

            success = redfish_handler.endpoint_handler.set_one_time_boot_source('Cd')
            if not success:
                my_output.error('Redfish boot source set to cd failed: %s' % (server['redfish']['endpoint_ip']))
                return False, None

            my_output.default('- boot source set to cd')

            if redfish_handler.endpoint_handler.is_power_on():
                my_output.default('- sending power cycle request')
                success = redfish_handler.endpoint_handler.power_cycle()
                if not success:
                    my_output.error('Server power cycle failed...')
                    return False, None
            else:
                my_output.default('- sending power on request')
                success = redfish_handler.endpoint_handler.power_on()
                if not success:
                    my_output.error('Server power on failed...')
                    return False, None

            my_output.default('- server booted')
            time.sleep(10)

            redfish_handler.reconnect()

            my_output.default('- redfish reconnected')

            response = redfish_handler.endpoint_handler.get_boot_properties()
            if response is not None:
                my_output.default(
                    json.dumps(response, indent=4)
                )

            redfish_handler.endpoint_handler.disconnect()
            my_output.default('- redfish disconnected')

    return True, web_server_supported


def wait_boot_from_iso(user_settings, cluster_id, console_handler, my_output, log_id):
    openshift_output_handler = openshift_output.OpenshiftOutput(log_id=log_id)

    bmc_addresses = None
    serial_numbers = None

    if user_settings['server'][0]['redfish']['endpoint_type'] == 'ucsc':
        bmc_addresses = []
        for server in user_settings['server']:
            bmc_addresses.append(
                server['redfish']['endpoint_ip']
            )

    if user_settings['server'][0]['redfish']['endpoint_type'] == 'fi':
        serial_numbers = []
        for server in user_settings['server']:
            serial_numbers.append(
                server['serial']
            )

    success = console_handler.wait_assisted_install_cluster_hosts_discovered(
        cluster_id,
        bmc_addresses=bmc_addresses,
        serial_numbers=serial_numbers,
        my_output=my_output,
        openshift_output=openshift_output_handler
    )
    if not success:
        return False

    return True


def update_cluster_settings(user_settings, cluster_id, console_handler, my_output):
    my_output.default('Change hostnames and roles')

    server_hostname = {}
    server_role = {}
    if user_settings['server'][0]['redfish']['endpoint_type'] == 'ucsc':
        server_key = 'bmc'
        for server in user_settings['server']:
            key = server['redfish']['endpoint_ip']
            server_hostname[key] = server['hostname']
            server_role[key] = server['role']
            my_output.default(
                '- Server [%s] hostname [%s] role [%s]' % (
                    key,
                    server['hostname'],
                    server['role']
                )
            )

    if user_settings['server'][0]['redfish']['endpoint_type'] == 'fi':
        server_key = 'serial'
        for server in user_settings['server']:
            key = server['serial']
            server_hostname[key] = server['hostname']
            server_role[key] = server['role']
            my_output.default(
                '- Server [%s] hostname [%s] role [%s]' % (
                    key,
                    server['hostname'],
                    server['role']
                )
            )

    success = console_handler.update_assisted_install_cluster_hosts_hostname(
        cluster_id,
        server_key,
        server_hostname,
        server_role
    )
    if not success:
        my_output.error('Hostname/role update failed')
        my_output.default('Continue once it is fixed manually via UI?')
        if not common.get_confirmation():
            return False

    my_output.default('REST API successful')

    ntp_data = {}
    ntp_data['additional_ntp_source'] = user_settings['ntp']

    my_output.default('Update ntp [%s]' % (ntp_data['additional_ntp_source']))
    response = console_handler.patch_assisted_install_cluster(cluster_id, ntp_data)
    if response is not None:
        my_output.default('REST API successful')
    else:
        my_output.error('NTP source update failed')
        my_output.default('Continue once it is fixed manually via UI?')
        if not common.get_confirmation():
            return False

    if len(user_settings['server']) > 1:
        api_vip = {}
        api_vip['cluster_id'] = cluster_id
        api_vip['ip'] = user_settings['api']
        api_vips = []
        api_vips.append(
            api_vip
        )

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
        if response is not None:
            my_output.default('REST API successful')
        else:
            my_output.error('API/Ingress VIP update failed')
            my_output.default('Continue once it is fixed manually via UI?')
            if not common.get_confirmation():
                return False

    return True


def wait_installation_started(cluster_id, console_handler, my_output):
    success = console_handler.wait_assisted_install_cluster_status(
        cluster_id,
        'ready'
    )
    if not success:
        my_output.error('Cluster has not reached ready state')
        my_output.default('Continue once it is fixed manually via UI?')
        if not common.get_confirmation():
            return False

    my_output.default('Start installation request...')

    success = console_handler.action_assisted_install_cluster_install(
        cluster_id
    )
    if not success:
        my_output.error('Cluster installation start request failed')
        my_output.default('Continue once it is fixed manually via UI?')
        if not common.get_confirmation():
            return False

    my_output.default('Wait for installation started [%s]...' % (cluster_id))

    success = console_handler.wait_assisted_install_cluster_status(
        cluster_id,
        'installing',
        install_action_on_ready_state=True,
        my_output=my_output
    )
    if not success:
        my_output.error('Cluster has not reached installation in progress state')
        my_output.default('Continue once it is fixed manually via UI?')
        if not common.get_confirmation():
            return False

    return True


def boot_from_hdd(user_settings, my_output, log_id):
    my_output.default('Changing servers to boot from hdd with optional vmedia eject')
    for server in user_settings['server']:
        my_output.default('- %s' % (server['redfish']['endpoint_ip']))

        redfish_handler = install_common.get_server_redfish_handler(
            server['redfish'],
            log_id
        )

        if user_settings['iso']['mode'] == 'full':
            my_output.default('\tSkipping vmedia eject for full iso')
        else:
            if not redfish_handler.is_connected():
                my_output.error('\tRedfish connection to server failed')
                return False

            my_output.default('\tRedfish connection successful')

            success = redfish_handler.endpoint_handler.eject_media(
                virtual_media_id=server['redfish']['virtual_media_id']
            )
            if not success:
                my_output.error('\tRedfish vmedia eject failed [id:%s]' % (server['redfish']['virtual_media_id'] ))
            else:
                my_output.default('\tRedfish vmedia eject successful [id:%s]' % (server['redfish']['virtual_media_id'] ))

        success = redfish_handler.endpoint_handler.set_one_time_boot_source('Hdd')
        if not success:
            my_output.error('\tServer boot source overrided to hdd failed')
            return False

        my_output.default('\tServer boot source override set to hdd successful')

    return True


def host_pending_user_action_fixup(host_ip, user_settings, my_output, log_id):
    for server in user_settings['server']:
        if server['redfish']['endpoint_ip'] == host_ip:
            redfish_handler = install_common.get_server_redfish_handler(
                server['redfish'],
                log_id
            )

            if not redfish_handler.is_connected():
                my_output.error('\tRedfish connection to server failed')
                return False

            my_output.default('\tRedfish connection successful')

            success = redfish_handler.endpoint_handler.set_one_time_boot_source('Hdd')
            if not success:
                my_output.error('\tServer boot source overrided to hdd failed')
                return False

            my_output.default('\tServer boot source override set to hdd successful')

            success = redfish_handler.endpoint_handler.power_cycle()
            if not success:
                my_output.error('Server power cycle failed: %s' % (server['redfish']['endpoint_ip']))
                return

            my_output.default('\tPower cycle successful: %s' % (server['redfish']['endpoint_ip']))

    return True


def wait_installation_finished(user_settings, cluster_id, console_handler, my_output, log, log_id):
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
                                    host_pending_user_action_fixup(host_ip, user_settings, my_output, log_id)
                                    pending_fixup[host_ip] = True

        time.sleep(10)

    my_output.default('Installation finished...', before_newline=True)
    return True


def delete_iso(user_settings, cluster_id, my_output, log_id=None):
    if user_settings['web_server']['ip'] == 'localhost':
        success = True

        filename = os.path.join(user_settings['web_server']['image_upload_directory'], '%s.iso' % (cluster_id))
        if os.path.isfile(filename):
            try:
                os.remove(filename)
            except BaseException:
                my_output.error('Failed to delete local file: %s' % (filename))
                success = False

        filename = os.path.join('/tmp', '%s.iso' % (cluster_id))
        if os.path.isfile(filename):
            try:
                os.remove(filename)
            except BaseException:
                my_output.error('Failed to delete local file: %s' % (filename))
                success = False

        return success

    ssh_handler = install_common.get_server_ssh_handler(user_settings['web_server'], log_id=log_id)
    success, exception_name, error = ssh_handler.is_ssh()
    if not success:
        my_output.error('SSH access to web server failed: %s' % (error))
        return False

    my_output.default('Delete iso from web server...')
    success = ssh_handler.delete_file(
        '%s/%s.iso' % (user_settings['web_server']['image_upload_directory'], cluster_id)
    )
    if not success:
        my_output.error('Delete failed')

    return True


def run(user_settings, data, infra, manifests, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    log = log_helper.Log(log_id=log_id)

    console_handler = console.Console(
        log_id=log_id,
        do_strip=user_settings['strip_token'],
        check_ssl=user_settings['iso']['check_ssl'],
        timeout=user_settings['iso']['timeout']
    )

    cluster_id, cluster_info = create_cluster(
        data,
        infra,
        manifests,
        console_handler,
        my_output,
        log
    )
    if cluster_info is None:
        return None

    success, web_server_supported = boot_from_iso(
        user_settings,
        cluster_id,
        cluster_info,
        my_output,
        log,
        log_id
    )
    if not success:
        my_output.default('Continue with manual mount and boot from iso')
        if not common.get_confirmation():
            return None

    success = wait_boot_from_iso(
        user_settings, 
        cluster_id, 
        console_handler, 
        my_output, 
        log_id
    )
    if not success:
        my_output.default('Press Y only if all servers are discovered and N to exit')
        if not common.get_confirmation():
            return None

    success = update_cluster_settings(
        user_settings,
        cluster_id,
        console_handler,
        my_output
    )
    if not success:
        return None

    my_output.default('Wait for cluster ready to be installed...')
    success = wait_installation_started(
        cluster_id,
        console_handler,
        my_output
    )
    if not success:
        return None

    if web_server_supported:
        try:
            success = boot_from_hdd(
                user_settings,
                my_output,
                log_id
            )
        except BaseException:
            my_output.error('Boot from hdd configuration may have failed...')
            print(traceback.format_exc())
            success = False

        if not success:
            my_output.default('Continue once the servers boot from hdd?')
            if not common.get_confirmation():
                return None

    success = wait_installation_finished(
        user_settings,
        cluster_id,
        console_handler,
        my_output,
        log,
        log_id
    )

    if web_server_supported:
        if user_settings['iso']['mode'] == 'full':
            for server in user_settings['server']:
                redfish_handler = install_common.get_server_redfish_handler(
                    server['redfish'],
                    log_id
                )

                success = redfish_handler.endpoint_handler.eject_media(
                    virtual_media_id=server['redfish']['virtual_media_id']
                )
                if not success:
                    my_output.error('Redfish vmedia eject failed: %s' % (server['redfish']['endpoint_ip']))
                else:
                    my_output.default('Redfish vmedia eject successful: %s' % (server['redfish']['endpoint_ip']))

        delete_iso(
            user_settings,
            cluster_id,
            my_output,
            log_id=log_id
        )

    if not success:
        my_output.error('Installation failed')
        return None

    return cluster_id
