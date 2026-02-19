import os
from lib import output_helper
from lib import file_helper
from lib import ssh
from lib.ocp import settings as ocp_settings
from lib.openshift import console
from lib.openshift import output as openshift_output
from lib.workflow.ocp_bm_install import common as install_common
from lib.workflow.ocp_cilium_cni import approve


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

    my_output.default('Create ocp connector: %s [kubeconfig:%s] [domain:%s]' % (connector_name, cluster_info['kubeconfig'], user_settings['domain']))
    success = ocp_settings_handler.create_ocp_cluster(
        connector_name,
        cluster_info['kubeconfig'],
        domain=user_settings['domain']
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
        my_output.default('Helm and virtctl access configured in connector')

    etc_hosts = install_common.get_etc_hosts(user_settings, cluster_info)
    success = ocp_settings_handler.set_ocp_cluster_file(
        connector_name,
        'etc_hosts',
        '\n'.join(etc_hosts)
    )
    if not success:
        my_output.error('etc_hosts update failed')

    return connector_name


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


def post_install(user_settings, cluster_info, my_output, log_id):
    success = False
    create_connector(user_settings, cluster_info, my_output, log_id)
    if install_common.check_cluster_server_ssh_acccess(user_settings, my_output):
        if prepare_kubeconfig(user_settings, cluster_info, my_output):
            success = True
    return success


def print_etc_hosts_requirements(my_output, etc_hosts):
    my_output.default('Required /etc/hosts entries')
    for entry in etc_hosts:
        my_output.default(entry)


def run(user_settings, cluster_id, log_id):
    my_output = output_helper.OutputHelper(log_id=log_id)
    openshift_output_handler = openshift_output.OpenshiftOutput(log_id=log_id)
    console_handler = console.Console(
        log_id=log_id,
        do_strip=user_settings['strip_token'],
        check_ssl=user_settings['iso']['check_ssl'],
        timeout=user_settings['iso']['timeout']
    )

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

    if user_settings['network_type'] == 'Cilium':
        params = {}
        params['cluster'] = user_settings['connector']
        approve.run(
            params,
            log_id=log_id
        )

    print_etc_hosts_requirements(
        my_output,
        install_common.get_etc_hosts(user_settings, cluster_info)
    )

    my_output.default('OpenShift bare metal installation completed successfully')

    return True
