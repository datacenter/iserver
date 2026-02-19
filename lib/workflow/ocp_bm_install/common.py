import json
import stat
import os
import uuid
import shutil
import requests
import subprocess
from lib import ssh
from lib import file_helper
from lib import filter_helper
from lib.ocp import settings as ocp_settings
from lib.redfish import endpoint as redfish_endpoint


def get_etc_hosts(user_settings, cluster_info):
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
        'alertmanager-main-openshift-monitoring',
        'hyperconverged-cluster-cli-download-openshift-cnv'
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
    return etc_hosts


def get_server_redfish_handler(server, log_id):
    redfish_handler = redfish_endpoint.RedfishEndpoint(
        server['endpoint_type'],
        server['endpoint_ip'],
        server['endpoint_port'],
        server['username'],
        server['password'],
        auto_connect=True,
        ssl_verify=False,
        log_id=log_id
    )

    if server['endpoint_type'] == 'fi':
        redfish_handler.endpoint_handler.set_inventory(
            server['inventory_type'],
            server['inventory_id']
        )
        
    return redfish_handler


def get_server_ssh_handler(server_settings, log_id=None):
    if server_settings['password'] is not None:
        ssh_handler = ssh.Ssh(
            server_settings['ip'],
            server_settings['username'],
            password=server_settings['password'],
            log_id=log_id
        )
        return ssh_handler

    key_filename = file_helper.set_tmp_file(
        server_settings['ssh_public_key']
    )
    ssh_handler = ssh.Ssh(
        server_settings['ip'],
        server_settings['username'],
        key_filename=key_filename,
        log_id=log_id
    )
    return ssh_handler


def check_ssh_acccess(server_settings, my_output, log_id=None):
    my_output.default('Check ssh access [%s]...' % (server_settings['ip']))

    ssh_handler = get_server_ssh_handler(server_settings, log_id=log_id)
    success, output, error = ssh_handler.run_cmd('pwd')
    if not success:
        my_output.error('Failed to run pwd command over ssh')
        return False

    return True


def check_iso_server_local(user_settings, my_output, log_id=None):
    openssl_command = 'openssl version'
    my_output.default('Run: %s' % (openssl_command))
    try:
        output = subprocess.run(openssl_command.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        success = False

    if not success:
        my_output.error('Failed to run openssl cli')
        return False

    my_output.default('~~~\n%s\n~~~' % (str(output)))

    podman_command = 'sudo podman -v'
    docker_command = 'sudo docker -v'
    exec_command = user_settings['iso']['exec']

    if exec_command == 'podman':
        my_output.default('Run: %s' % (podman_command))
        try:
            output = subprocess.run(podman_command.split(' '), capture_output=True, text=True, check=True)
            success = True
        except BaseException:
            success = False

        if not success:
            my_output.error('Failed to run podman cli')
            return False

        my_output.default('~~~\n%s\n~~~' % (str(output)))

    if exec_command == 'docker':
        my_output.default('Run: %s' % (docker_command))
        try:
            output = subprocess.run(docker_command.split(' '), capture_output=True, text=True, check=True)
            success = True
        except BaseException:
            success = False

        if not success:
            my_output.error('Failed to run docker cli')
            return False

        my_output.default('~~~\n%s\n~~~' % (str(output)))

    if exec_command == 'detect':
        my_output.default('Run: %s' % (podman_command))
        try:
            output = subprocess.run(podman_command.split(' '), capture_output=True, text=True, check=True)
            success = True
        except BaseException:
            success = False

        if success:
            exec_command = 'podman'
            my_output.default('~~~\n%s\n~~~' % (str(output)))
        else:
            my_output.default('Run: %s' % (docker_command))
            try:
                output = subprocess.run(docker_command.split(' '), capture_output=True, text=True, check=True)
                success = True
            except BaseException:
                success = False

            if success:
                exec_command = 'docker'
                my_output.default('~~~\n%s\n~~~' % (str(output)))

        if exec_command == 'detect':
            my_output.error('Failed to detect exec mode for containers')
            return False

        my_output.default('Container mode detected: %s' % (exec_command))
        user_settings['iso']['exec'] = exec_command

    my_output.default('Pull coreos installer container image: %s' % (user_settings['iso']['image']))
    try:
        cmd = 'sudo %s pull %s' % (exec_command, user_settings['iso']['image'])
        my_output.default('Run: %s' % (cmd))
        output = subprocess.run(cmd.split(' '), capture_output=True, text=True, check=True)
        success = True
    except BaseException:
        success = False

    if not success:
        my_output.error('Image pull failed')
        return False

    my_output.default('~~~\n%s\n~~~' % (str(output)))

    return True


def check_iso_server_remote(user_settings, my_output, log_id=None):
    ssh_handler = get_server_ssh_handler(user_settings['iso'], log_id=log_id)
    success, exception_name, error = ssh_handler.is_ssh()
    if not success:
        my_output.error('SSH access to iso manipulation server failed: %s' % (error))
        return False

    openssl_command = 'openssl version'
    my_output.default('Run: %s' % (openssl_command))
    success, output, error = ssh_handler.run_cmd(openssl_command)
    if not success:
        my_output.error('Failed to run openssl cli')
        return False
    
    my_output.default('~~~\n%s\n~~~' % (str(output)))

    podman_command = 'sudo podman -v'
    docker_command = 'sudo docker -v'
    exec_command = user_settings['iso']['exec']

    if exec_command == 'podman':
        my_output.default('Run: %s' % (podman_command))
        success, output, error = ssh_handler.run_cmd(podman_command)
        if not success:
            my_output.error('Failed to run podman cli')
            return False
        
        my_output.default('~~~\n%s\n~~~' % (str(output)))

    if exec_command == 'docker':
        my_output.default('Run: %s' % (docker_command))
        success, output, error = ssh_handler.run_cmd(docker_command)
        if not success:
            my_output.error('Failed to run docker cli')
            return False
        
        my_output.default('~~~\n%s\n~~~' % (str(output)))

    if exec_command == 'detect':
        my_output.default('Run: %s' % (podman_command))
        success, output, error = ssh_handler.run_cmd(podman_command)
        if success:
            exec_command = 'podman'
            my_output.default('~~~\n%s\n~~~' % (str(output)))
        else:
            my_output.default('Run: %s' % (docker_command))
            success, output, error = ssh_handler.run_cmd(docker_command)
            if success:
                exec_command = 'docker'
                my_output.default('~~~\n%s\n~~~' % (str(output)))

        if exec_command == 'detect':
            my_output.error('Failed to detect exec mode for containers')
            return False

        my_output.default('Container mode detected: %s' % (exec_command))
        user_settings['iso']['exec'] = exec_command

    my_output.default('Pull coreos installer container image')
    success, output, error = ssh_handler.run_cmd('sudo %s pull %s' % (exec_command, user_settings['iso']['image']))
    if not success:
        my_output.error('Image pull failed')
        return False

    my_output.default('~~~\n%s%s~~~' % (str(output), str(error)))
    return True


def check_iso_server(user_settings, my_output, log_id=None):
    if user_settings['iso']['ip'] is None:
        return user_settings

    my_output.default(
        'Check iso manipulation server [%s]...' % (user_settings['iso']['ip']),
        before_newline=True,
        underline=True
    )

    if user_settings['iso']['ip'] == 'localhost':
        my_output.default('Iso manipulation server is local')
        if not check_iso_server_local(user_settings, my_output, log_id=log_id):
            return None
    
    if user_settings['iso']['ip'] != 'localhost':
        my_output.default('Iso manipulation server is remote')
        if not check_ssh_acccess(user_settings['iso'], my_output, log_id=log_id):
            return None

        if not check_iso_server_remote(user_settings, my_output, log_id=log_id):
            return None

    return user_settings


def check_web_server_http_acccess(user_settings, my_output, log_id=None):
    my_output.default('Check web server http access...')

    try:
        response = requests.get(
            user_settings['web_server']['image_base_url'],
            timeout=5
        )
    except BaseException:
        my_output.error('Web server http access failed')
        return False

    if response.status_code >= 300:
        my_output.error('Web server http access failed')
        return False

    ssh_handler = get_server_ssh_handler(user_settings['web_server'], log_id=log_id)

    source_filename = file_helper.set_tmp_file('test')
    target_filename = '%s/%s' % (
        user_settings['web_server']['image_upload_directory'],
        os.path.basename(source_filename)
    )
    success = ssh_handler.scp_file(
        source_filename,
        target_filename
    )
    if not success:
        my_output.error('Web server file upload failed')
        return False

    success = True
    try:
        response = requests.get(
            '%s/%s' % (
                user_settings['web_server']['image_base_url'],
                os.path.basename(source_filename)
            ),
            timeout=5
        )
    except BaseException:
        my_output.error('Web server http access failed')
        success = False

    my_output.default('Test file uploaded to web server via ssh and then downloaded successfully via http')
    ssh_handler.delete_file(target_filename)

    return success


def check_local_web_server_http_acccess(user_settings, my_output, log_id=None):
    my_output.default('Check local web server http access...')

    try:
        response = requests.get(
            user_settings['web_server']['image_base_url'],
            timeout=5
        )
    except BaseException:
        my_output.error('Web server http access failed')
        return False

    if response.status_code >= 300:
        my_output.error('Web server http access failed')
        return False

    source_filename = file_helper.set_tmp_file('test')
    target_filename = os.path.join(
        user_settings['web_server']['image_upload_directory'],
        os.path.basename(source_filename)
    )
    try:
        shutil.copy(source_filename, target_filename)
    except BaseException:
        my_output.error('File copy failed: %s => %s' % (source_filename, target_filename))
        return False

    success = True
    try:
        response = requests.get(
            '%s/%s' % (
                user_settings['web_server']['image_base_url'],
                os.path.basename(source_filename)
            ),
            timeout=5
        )
    except BaseException:
        my_output.error('Web server http access failed')
        success = False

    my_output.default('Test file uploaded locally to web server and then downloaded successfully via http')
    return success


def check_web_server(user_settings, my_output, log_id=None):
    if not 'web_server' in user_settings:
        return False

    my_output.default('Check web server', before_newline=True, underline=True)

    if user_settings['web_server']['ip'] == 'localhost':
        my_output.default('Web server is local')
        if not os.path.isdir(user_settings['web_server']['image_upload_directory']):
            my_output.error('Upload directory not found: %s' % (user_settings['web_server']['image_upload_directory']))
            return False

        my_output.default('Upload directory found: %s' % (user_settings['web_server']['image_upload_directory']))

        if not check_local_web_server_http_acccess(user_settings, my_output, log_id=log_id):
            return False

        return True

    if not check_ssh_acccess(user_settings['web_server'], my_output, log_id=log_id):
        return False

    if not check_web_server_http_acccess(user_settings, my_output, log_id=log_id):
        return False

    return True


def create_web_server_file(user_settings, filename, my_output, log_id):
    if not 'web_server' in user_settings:
        return None

    if user_settings['web_server']['ip'] == 'localhost':
        my_output.default('Creating file in local web server: %s' % (filename))
        source_filename = file_helper.get_local_file_location('sample.iso', 'templates')
        target_filename = os.path.join(
            user_settings['web_server']['image_upload_directory'],
            filename
        )
        try:
            shutil.copy(source_filename, target_filename)
        except BaseException:
            my_output.error('File copy failed: %s => %s' % (source_filename, target_filename))
            return None

        try:
            os.chmod(target_filename, stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)
        except BaseException:
            my_output.default('[WARNING] Failed to set file ownership: %s' % (target_filename))

    else:
        ssh_handler = get_server_ssh_handler(user_settings['web_server'], log_id=log_id)

        source_filename = file_helper.get_local_file_location('sample.iso', 'templates')
        if source_filename is None:
            my_output.error('sample.iso file not found')
            return None

        target_filename = '%s/%s' % (
            user_settings['web_server']['image_upload_directory'],
            filename
        )
        success = ssh_handler.scp_file(
            source_filename,
            target_filename
        )
        if not success:
            my_output.error('Web server file upload failed')
            return None

    return '%s/%s' % (user_settings['web_server']['image_base_url'], filename)


def delete_web_server_file(user_settings, filename, my_output, log_id):
    if not 'web_server' in user_settings:
        return None

    if user_settings['web_server']['ip'] == 'localhost':
        my_output.default('Deleting file in local web server: %s' % (filename))
        target_filename = os.path.join(
            user_settings['web_server']['image_upload_directory'],
            filename
        )
        try:
            if os.path.isfile(filename):
                os.remove(target_filename)
        except BaseException:
            my_output.error('File delete failed: %s' % (target_filename))

    else:
        ssh_handler = get_server_ssh_handler(user_settings['web_server'], log_id=log_id)

        target_filename = '%s/%s' % (
            user_settings['web_server']['image_upload_directory'],
            filename
        )
        success = ssh_handler.delete_file(
            target_filename
        )
        if not success:
            my_output.error('Web server file delete failed')

    my_output.default('- web server file deleted')
    return True


def check_cluster_server_ssh_acccess(user_settings, my_output):
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
        success, exception_name, error = ssh_handler.is_ssh()
        if not success:
            my_output.error(error)
            return False

    return True


def print_virtual_media_info(virtual_media_details, my_output):
    my_output.default('Virtual Media [%s]' % (virtual_media_details['Id']))
    my_output.default('- Name: %s' % (filter_helper.get_attr(virtual_media_details, 'Name', cast='---')))
    my_output.default('- Inserted: %s' % (filter_helper.get_attr(virtual_media_details, 'Inserted', cast='---')))
    my_output.default('- MediaTypes: %s' % (filter_helper.get_attr(virtual_media_details, 'MediaTypes', cast='---')))
    my_output.default('- ConnectedVia: %s' % (filter_helper.get_attr(virtual_media_details, 'ConnectedVia', cast='---')))
    my_output.default('- State: %s' % (filter_helper.get_attr(virtual_media_details, 'Status:State', cast='---')))
    my_output.default('- Health: %s' % (filter_helper.get_attr(virtual_media_details, 'Status:Health', cast='---')))
    extended_info = filter_helper.get_attr(virtual_media_details, 'Status:Health@Message.ExtendedInfo')
    if extended_info is not None:
        for item in extended_info:
            my_output.default('- Info: %s' % (filter_helper.get_attr(item, 'Message', cast='---')))


def list_virtual_media_info(redfish_handler, my_output):
    my_output.default('All available virtual media', before_newline=True, underline=True)
    for virtual_media_id in range(10):
        virtual_media_details = redfish_handler.endpoint_handler.get_virtual_media(
            virtual_media_id
        )
        if virtual_media_details is None:
            my_output.default('Virtual Media [%s]' % (virtual_media_id))
            my_output.default('- Not found')
        else:
            print_virtual_media_info(virtual_media_details, my_output)


def test_server_redfish_virtual_media(user_settings, redfish_handler, server, virtual_media_id, my_output, log_id):
    virtual_media_details = redfish_handler.endpoint_handler.get_virtual_media(
        virtual_media_id
    )
    if virtual_media_details is None:
        my_output.error(
            'Failed to get virtual media [%s] state via redfish: %s' % (
                server['redfish']['virtual_media_id'],
                server['redfish']['endpoint_ip']
            )
        )

        return False

    print_virtual_media_info(virtual_media_details, my_output)

    if 'DVD' not in virtual_media_details['MediaTypes']:
        my_output.error(
            'Virtual media [#%s] does not support DVD media type: %s' % (
                server['redfish']['virtual_media_id'],
                server['redfish']['endpoint_ip']
            )
        )
        return False

    if virtual_media_details['Status']['State'] != 'Disabled':
        if not user_settings['settings']['server_force_virtual_media_eject']:
            my_output.default(
                'Virtual media id is currently used. It must be ejected to be tested.',
                before_newline=True
            )
            return False

        success = redfish_handler.endpoint_handler.eject_media(
            virtual_media_id=server['redfish']['virtual_media_id']
        )
        if not success:
            my_output.error('Failed to eject virtual media via redfish: %s' % (server['redfish']['endpoint_ip']))
            return False

        my_output.default('Virtual media ejected via redfish')

    my_output.default('Virtual media test')
    filename = 'image-%s.iso' % (str(uuid.uuid4()))
    my_output.default('- filename to be uploaded to web server: %s' % (filename))
    url = create_web_server_file(user_settings, filename, my_output, log_id)
    if url is None:
        my_output.error('Failed to prepare test file in web server')
        return False

    my_output.default('- url: %s' % (url))

    success = redfish_handler.endpoint_handler.insert_media_http(
        url,
        virtual_media_id=server['redfish']['virtual_media_id']
    )
    if not success:
        my_output.error('Redfish vmedia insert failed: %s' % (server['redfish']['endpoint_ip']))
        delete_web_server_file(user_settings, filename, my_output, log_id)
        return False

    my_output.default('- virtual media inserted [id:%s]' % (server['redfish']['virtual_media_id']))

    success = redfish_handler.endpoint_handler.wait_virtual_media_inserted(
        virtual_media_id=server['redfish']['virtual_media_id']
    )
    if not success:
        my_output.error('Redfish vmedia mapping failed: %s' % (server['redfish']['endpoint_ip']))
        response = redfish_handler.endpoint_handler.get_virtual_media(virtual_media_id=server['redfish']['virtual_media_id'])
        if response is None:
            my_output.error('Failed to get virtual media state')
        else:
            my_output.default('Virtual Media State (on error)', underline=True, before_newline=True)
            my_output.default(json.dumps(response, indent=4))

        delete_web_server_file(user_settings, filename, my_output, log_id)
        return False

    my_output.default('- virtual media mapped')

    response = redfish_handler.endpoint_handler.get_virtual_media(virtual_media_id=server['redfish']['virtual_media_id'])
    if response is None:
        my_output.error('Failed to get virtual media state - continue with the workflow')
    else:
        my_output.debug('Virtual Media State', underline=True, before_newline=True)
        my_output.debug(json.dumps(response, indent=4))

    success = redfish_handler.endpoint_handler.eject_media(
        virtual_media_id=server['redfish']['virtual_media_id']
    )
    if not success:
        my_output.error('Failed to eject virtual media via redfish: %s' % (server['redfish']['endpoint_ip']))
        delete_web_server_file(user_settings, filename, my_output, log_id)
        return user_settings

    my_output.default('- virtual media ejected')
    delete_web_server_file(user_settings, filename, my_output, log_id)

    return True


def test_server_redfish_boot_properties(redfish_handler, my_output):
    boot_properties = redfish_handler.endpoint_handler.get_boot_properties()
    if boot_properties is None:
        my_output.error('Failed to get boot settings via redfish')
        return False

    target_values = filter_helper.get_attr(boot_properties, 'BootSourceOverrideTarget@Redfish.AllowableValues')
    enabled_values = filter_helper.get_attr(boot_properties, 'BootSourceOverrideEnabled@Redfish.AllowableValues')
    my_output.default('Boot settings')
    my_output.default('- boot source override enabled: %s' % (filter_helper.get_attr(boot_properties, 'BootSourceOverrideEnabled', cast='---')))
    my_output.default('- boot source override target: %s' % (filter_helper.get_attr(boot_properties, 'BootSourceOverrideTarget', cast='---')))
    my_output.default('- target values: %s' % (target_values))
    my_output.default('- enabled values: %s' % (enabled_values))

    if target_values is None:
        my_output.error('Target values missing')
        return False

    if 'Cd' not in target_values:
        my_output.error('Cd not in target values')
        return False

    if 'Hdd' not in target_values:
        my_output.error('Hdd not in target values')
        return False

    if 'None' not in target_values:
        my_output.error('None not in target values')
        return False

    my_output.default('- Cd, Hdd and None found in target values')

    if enabled_values is None:
        my_output.error('Enabled values missing')
        return False

    if 'Disabled' not in enabled_values:
        my_output.error('Disabled not in enabled values')
        return False

    if 'Once' not in enabled_values:
        my_output.error('Once not in enabled values')
        return False

    my_output.default('- Once and Disabled found in enabled values')

    success = redfish_handler.endpoint_handler.set_one_time_boot_source('Cd')
    if not success:
        my_output.error('Failed to enable boot from Cd')
        return False

    my_output.default('- Boot from Cd override enabled successfully')

    success = redfish_handler.endpoint_handler.set_one_time_boot_source('None', enabled='Disabled')
    if not success:
        my_output.error('Failed to disable boot overrived')
        return False

    my_output.default('- Boot override disabled successfully')

    return True


def test_server_redfish_actions(redfish_handler, my_output):
    my_output.default('System power actions')

    actions = redfish_handler.endpoint_handler.get_system_actions()
    if actions is None:
        my_output.error('Failed to get actions via redfish')
        return False

    if '#ComputerSystem.Reset' not in actions:
        my_output.error('Missing #ComputerSystem.Reset in actions')
        return False

    my_output.default('- ComputerSystem.Reset action found')

    allowed = filter_helper.get_attr(actions, '#ComputerSystem.Reset:ResetType@Redfish.AllowableValues')
    if allowed is None:
        my_output.error('Missing ResetType@Redfish.AllowableValues')
        return False

    my_output.default('- Allowed values: %s' % (allowed))

    keys = [
        'PowerCycle',
        'GracefulRestart',
        'ForceRestart',
        'GracefulShutdown',
        'ForceOff'
    ]
    for key in keys:
        if key not in allowed:
            my_output.error('Missing reset type support: %s' % (key))
            return False

    my_output.default('- Compute reset actions check successful')
    return True


def check_server_redfish_access(user_settings, my_output, log_id, include_vmedia=False, include_boot_source=False, include_actions=False):
    for server in user_settings['server']:
        my_output.default('Check server redfish [%s]' % (server['hostname']), before_newline=True, underline=True)
        redfish_handler = get_server_redfish_handler(
            server['redfish'],
            log_id
        )

        if not redfish_handler.is_connected():
            my_output.error('Redfish connection to server failed: %s' % (server['redfish']['endpoint_ip']))
            return None

        chassis_uri = redfish_handler.endpoint_handler.get_chassis_uri()
        if chassis_uri is None:
            my_output.error('Getting redfish chassis uri failed: %s' % (server['redfish']['endpoint_ip']))
            return None

        my_output.default('Redfish endpoint: %s' % (server['redfish']['endpoint_ip']))
        values = redfish_handler.get_properties(chassis_uri)
        if values is not None:
            keys = [
                'ChassisType',
                'Model',
                'SerialNumber',
                'PowerState'
            ]
            for key in keys:
                if key in values:
                    my_output.default('- %s: %s' % (key, values[key]))
            
            server['serial'] = values['SerialNumber']

        server['redfish']['chassis_type'] = redfish_handler.endpoint_handler.get_chassis_type()
        if server['redfish']['chassis_type'] is None:
            my_output.error('Failed to detect chassis type of server: %s' % (server['redfish']['endpoint_ip']))
            return None

        my_output.default('- Detected chassis type: %s' % (server['redfish']['chassis_type']))

        if server['redfish']['chassis_type'] == 'Rack':
            server['redfish']['virtual_media_id'] = 0
        else:
            server['redfish']['virtual_media_id'] = 3

        if include_vmedia:
            success = test_server_redfish_virtual_media(
                user_settings,
                redfish_handler,
                server,
                server['redfish']['virtual_media_id'],
                my_output,
                log_id
            )
            if not success:
                if user_settings['settings']['server_list_virtual_media_on_failure']:
                    list_virtual_media_info(redfish_handler, my_output)

                return None

        if include_boot_source:
            success = test_server_redfish_boot_properties(
                redfish_handler,
                my_output
            )
            if not success:
                return None

        if include_actions:
            success = test_server_redfish_actions(
                redfish_handler,
                my_output
            )
            if not success:
                return None

    return user_settings


def get_management_host_ip(user_settings):
    for server in user_settings['server']:
        if server['kube']:
            return server['ssh']['ip']
    return None


def save_management_ip(connector, management_ip, log_id):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(connector):
        return True

    success = ocp_settings_handler.set_management_ip(
        connector,
        management_ip
    )
    if not success:
        return False

    return True
