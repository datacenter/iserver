import os
import json
import uuid

from lib import ssh
from lib import file_helper


class OcpVsphereIpiCreate():
    def __init__(self):
        self.ocp_parameters = None
        self.input_location = None
        self.installer_parameters = None

    def is_vsphere_ipi_ocp_ready(self):
        ssh_handler = ssh.Ssh(
            self.installer_parameters['vm']['ssh']['ip'],
            self.installer_parameters['vm']['ssh']['username'],
            password=self.installer_parameters['vm']['ssh']['password'],
            log_id=self.log_id
        )
        filename = '/root/install/.openshift_install_state.json'
        return ssh_handler.is_file(filename)

    def vsphere_ipi_ocp_install(self):
        filename = self.get_template_filename('packages.sh')
        if not self.vcenter_handler.run_task_script(filename):
            return False

        if 'dhcp' in self.ocp_parameters:
            if self.ocp_parameters['dhcp']['managed']:
                file_info = {}
                file_info['source'] = self.get_template_filename('dhcpd.leases')
                file_info['template'] = False
                file_info['destination'] = '/var/lib/dhcpd/dhcpd.leases'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                file_info = {}
                file_info['source'] = self.get_template_filename('dhcpd.conf')
                file_info['template'] = True
                file_info['destination'] = '/etc/dhcp/dhcpd.conf'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                commands = [
                    'dos2unix /etc/dhcp/dhcpd.conf',
                    'dos2unix /var/lib/dhcpd/dhcpd.leases',
                    'chown dhcpd:dhcpd /var/lib/dhcpd/dhcpd.leases',
                    'systemctl restart dhcpd',
                    'systemctl status dhcpd'
                ]
                for command in commands:
                    if not self.vcenter_handler.run_task_command(command):
                        return False

        if 'dns' in self.ocp_parameters:
            if self.ocp_parameters['dns']['managed']:
                command = 'mkdir -p /etc/named/zones'
                if not self.vcenter_handler.run_task_command(command):
                    return False

                file_info = {}
                file_info['source'] = self.get_template_filename('dns_a')
                file_info['template'] = True
                file_info['destination'] = '/etc/named/zones/db.%s' % (self.ocp_parameters['ocp']['cluster']['domain'])
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                file_info = {}
                file_info['source'] = self.get_template_filename('dns_arpa')
                file_info['template'] = True
                file_info['destination'] = '/etc/named/zones/db.reverse'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                file_info = {}
                file_info['source'] = self.get_template_filename('named.conf')
                file_info['template'] = True
                file_info['destination'] = '/etc/named.conf'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                commands = [
                    'dos2unix /etc/named.conf',
                    'dos2unix /etc/named/zones/db.reverse',
                    'dos2unix /etc/named/zones/db.%s' % (self.ocp_parameters['ocp']['cluster']['domain']),
                    'systemctl restart named',
                    'systemctl status named',
                    'rm /etc/resolv.conf'
                ]
                for command in commands:
                    if not self.vcenter_handler.run_task_command(command):
                        return False

                file_info = {}
                file_info['source'] = self.get_template_filename('resolv.conf')
                file_info['template'] = True
                file_info['destination'] = '/etc/resolv.conf'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

                command = 'dos2unix /etc/resolv.conf'
                if not self.vcenter_handler.run_task_command(command):
                    return False

        filename = self.get_template_filename('ssh-key-generation.sh')
        if not self.vcenter_handler.run_task_script(filename):
            return False

        file_info = {}
        if self.is_source_local(self.ocp_parameters['sources']['ocp']):
            delete_file = False
            file_info['source'] = self.ocp_parameters['sources']['ocp']
        else:
            delete_file = True
            file_info['source'] = self.download_source_file(self.ocp_parameters['sources']['ocp'])
            if file_info['source'] is None:
                return False

        file_info['template'] = False
        file_info['destination'] = '/root/openshift-install-linux.tar.gz'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            return False

        if delete_file:
            try:
                os.remove(file_info['source'])
                self.my_output.info('File removed after successful upload: %s' % (file_info['source']))
            except BaseException:
                self.my_output.info('File delete failed: %s' % (file_info['source']))

        file_info = {}
        if self.is_source_local(self.ocp_parameters['sources']['oc']):
            delete_file = False
            file_info['source'] = self.ocp_parameters['sources']['oc']
        else:
            delete_file = True
            file_info['source'] = self.download_source_file(self.ocp_parameters['sources']['oc'])
            if file_info['source'] is None:
                return False

        file_info['template'] = False
        file_info['destination'] = '/root/oc.tar.gz'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            return False

        if delete_file:
            try:
                os.remove(file_info['source'])
                self.my_output.info('File removed after successful upload: %s' % (file_info['source']))
            except BaseException:
                self.my_output.info('File delete failed: %s' % (file_info['source']))

        if self.ocp_parameters['cni']['type'] == 'Calico':
            file_info = {}
            delete_file = True
            file_info['source'] = self.download_source_file(self.ocp_parameters['calico']['calicoctl'])
            if file_info['source'] is None:
                return False

            file_info['template'] = False
            file_info['destination'] = '/usr/local/bin/calicoctl'
            file_info['chmod'] = 744
            if not self.vcenter_handler.run_task_file(file_info):
                return False

            if delete_file:
                try:
                    os.remove(file_info['source'])
                    self.my_output.info('File removed after successful upload: %s' % (file_info['source']))
                except BaseException:
                    self.my_output.info('File delete failed: %s' % (file_info['source']))

        file_info = {}
        file_info['source'] = self.ocp_parameters['sources']['secret']
        file_info['template'] = False
        file_info['destination'] = '/root/pull-secret.txt'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            return False

        file_info = {}
        if self.installer_parameters['variables']['HTTP_PROXY_ENABLED'] == "True":
            file_info['source'] = self.get_template_filename('config_proxy.yaml')
        else:
            file_info['source'] = self.get_template_filename('config_no_proxy.yaml')
        file_info['template'] = True
        file_info['destination'] = '/root/config.yaml'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            return False

        if self.ocp_parameters['cni']['type'] == 'Calico':
            file_info = {}
            file_info['source'] = self.get_template_filename('calico_manifests.sh')
            file_info['template'] = True
            file_info['destination'] = '/root/calico_manifests.sh'
            file_info['chmod'] = 744
            if not self.vcenter_handler.run_task_file(file_info):
                return False

        if self.ocp_parameters['cni']['type'] == 'Cilium':
            file_info = {}
            file_info['source'] = self.get_template_filename('cilium_manifests.sh')
            file_info['template'] = True
            file_info['destination'] = '/root/cilium_manifests.sh'
            file_info['chmod'] = 744
            if not self.vcenter_handler.run_task_file(file_info):
                return False

            file_info = {}
            file_info['source'] = self.get_template_filename('cilium_agent.sh')
            file_info['template'] = True
            file_info['destination'] = '/root/cilium_agent.sh'
            file_info['chmod'] = 744
            if not self.vcenter_handler.run_task_file(file_info):
                return False

            file_info = {}
            file_info['source'] = os.path.join(
                self.input_location,
                'cilium_config.yaml'
            )
            file_info['template'] = False
            file_info['destination'] = '/root/cilium_config.yaml'
            file_info['chmod'] = 644
            if not self.vcenter_handler.run_task_file(file_info):
                return False

            if self.ocp_parameters['cilium']['extras']:
                file_info = {}
                file_info['source'] = os.path.join(
                    self.input_location,
                    'cilium_extras.yaml'
                )
                file_info['template'] = False
                file_info['destination'] = '/root/cilium_extras.yaml'
                file_info['chmod'] = 644
                if not self.vcenter_handler.run_task_file(file_info):
                    return False

        if 'bgp' in self.ocp_parameters:
            file_info = {}
            file_info['source'] = self.get_template_filename('bgp.yaml')
            file_info['template'] = True
            file_info['destination'] = '/root/bgp_configuration.yaml'
            file_info['chmod'] = 744
            if not self.vcenter_handler.run_task_file(file_info):
                return False

        file_info = {}
        file_info['source'] = self.get_template_filename('patch.py')
        file_info['template'] = True
        file_info['destination'] = '/root/patch.py'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            return False

        commands = [
            'dos2unix /root/config.yaml',
            'dos2unix /root/patch.py',
            'dos2unix /root/pull-secret.txt',
            'tar xzvf /root/openshift-install-linux.tar.gz',
            'tar xzvf /root/oc.tar.gz',
            'mv /root/kubectl /usr/local/bin',
            'mv /root/oc /usr/local/bin',
            'rm -f README.md',
            'rm -f /root/openshift-install-linux.tar.gz',
            'rm -f /root/oc.tar.gz',
            'python3 /root/patch.py',
            'rm -f /root/patch.py'
        ]
        if self.ocp_parameters['cni']['type'] == 'Calico':
            commands.append(
                'dos2unix /root/calico_manifests.sh'
            )

        if self.ocp_parameters['cni']['type'] == 'Cilium':
            commands.append(
                'dos2unix /root/cilium_manifests.sh'
            )
            commands.append(
                'dos2unix /root/cilium_config.yaml'
            )
            if self.ocp_parameters['cilium']['extras']:
                commands.append(
                    'dos2unix /root/cilium_extras.yaml'
                )

        if 'bgp' in self.ocp_parameters:
            commands.append(
                'dos2unix /root/bgp_configuration.yaml'
            )

        for command in commands:
            if not self.vcenter_handler.run_task_command(command):
                return False

        filename = self.get_template_filename('certs.sh')
        if not self.vcenter_handler.run_task_script(filename):
            return False

        filename = self.get_template_filename('install.sh')
        if not self.vcenter_handler.run_task_script(filename, live_output=True):
            return False

        filename = self.get_template_filename('prepare_export.sh')
        if not self.vcenter_handler.run_task_script(filename):
            return False

        return True

    def is_vsphere_ipi_ocp_working(self):
        filename = self.get_template_filename('check-ocp-nodes.sh')
        if not self.vcenter_handler.run_task_script(filename):
            self.my_output.error('OCP does not seem to be working fine')
            return False
        return True

    def is_vsphere_ipi_ocp_post_install_finished(self):
        ssh_handler = ssh.Ssh(
            self.installer_parameters['vm']['ssh']['ip'],
            self.installer_parameters['vm']['ssh']['username'],
            password=self.installer_parameters['vm']['ssh']['password'],
            log_id=self.log_id
        )
        filename = '/root/.post_install_finished'
        return ssh_handler.is_file(filename)

    def set_vsphere_ipi_ocp_post_install_finished(self):
        ssh_handler = ssh.Ssh(
            self.installer_parameters['vm']['ssh']['ip'],
            self.installer_parameters['vm']['ssh']['username'],
            password=self.installer_parameters['vm']['ssh']['password'],
            log_id=self.log_id
        )
        filename = '/root/.post_install_finished'
        if not ssh_handler.touch_file(filename):
            self.my_output.error('Post installation flag create failed')
            return False

        self.my_output.info('Post installation flag created')
        return True

    def vsphere_ipi_ocp_post_install_upload(self, upload_filename, post_directory):
        try:
            with open(upload_filename, 'r', encoding='utf-8') as file_handler:
                uploads = json.loads(file_handler.read())

        except BaseException:
            self.my_output.debug('Failed to read file: %s' % (upload_filename))
            return False

        for file_info in uploads:
            file_info['source'] = os.path.join(
                post_directory,
                file_info['source']
            )
            if not self.vcenter_handler.run_task_file(file_info, create_directory=True):
                return False

        return True

    def vsphere_ipi_ocp_post_install_commands(self, commands_filename):
        try:
            with open(commands_filename, 'r', encoding='utf-8') as file_handler:
                commands = json.loads(file_handler.read())

        except BaseException:
            self.my_output.debug('Failed to read file: %s' % (commands_filename))
            return False

        for command in commands:
            if not self.vcenter_handler.run_task_command(command):
                return False

        return True

    def vsphere_ipi_ocp_post_install(self):
        if self.is_vsphere_ipi_ocp_post_install_finished():
            self.my_output.info('Post install already completed')
            return True

        post_directory = os.path.join(
            self.input_location,
            'post'
        )

        if not os.path.isdir(post_directory):
            self.my_output.info('No post installation tasks defined')
            self.set_vsphere_ipi_ocp_post_install_finished()
            return True

        upload_filename = os.path.join(post_directory, 'upload.json')
        if os.path.isfile(upload_filename):
            if not self.vsphere_ipi_ocp_post_install_upload(upload_filename, post_directory):
                return False

        commands_filename = os.path.join(post_directory, 'commands.json')
        if os.path.isfile(commands_filename):
            if not self.vsphere_ipi_ocp_post_install_commands(commands_filename):
                return False

        self.set_vsphere_ipi_ocp_post_install_finished()
        return True

    def is_vsphere_ipi_ocp_parameters_ready(self):
        ssh_handler = ssh.Ssh(
            self.installer_parameters['vm']['ssh']['ip'],
            self.installer_parameters['vm']['ssh']['username'],
            password=self.installer_parameters['vm']['ssh']['password'],
            log_id=self.log_id
        )
        filename = '/root/.ocp_parameters.json'
        return ssh_handler.is_file(filename)

    def vsphere_ipi_ocp_parameters_upload(self):
        parameters_filename = '/tmp/%s.json' % (str(uuid.uuid4()))
        try:
            with open(parameters_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(self.ocp_parameters, indent=4))

        except BaseException:
            self.log.error(
                'vsphere_ipi_ocp_parameters_upload',
                'Local file write failed'
            )
            return False

        file_info = {}
        file_info['source'] = parameters_filename
        file_info['template'] = False
        file_info['destination'] = '/root/.ocp_parameters.json'
        file_info['chmod'] = 644
        if not self.vcenter_handler.run_task_file(file_info):
            os.remove(parameters_filename)
            return False

        os.remove(parameters_filename)
        return True

    def vsphere_ipi_ocp_create(self, ocp_parameters, input_location):
        self.my_output.default('vsphere-ipi ocp creation workflow...')

        self.ocp_parameters = ocp_parameters
        self.input_location = input_location
        self.installer_parameters = self.get_vsphere_ipi_installer_parameters()
        if self.installer_parameters is None:
            return False

        self.my_output.info(
            json.dumps(
                self.installer_parameters,
                indent=4
            )
        )

        success = self.vcenter_handler.create_vm_deployment(
            self.installer_parameters,
            dry_run=False
        )
        if not success:
            return False

        if self.is_vsphere_ipi_ocp_ready():
            self.my_output.default('OCP already installed')
        else:
            if not self.vcenter_handler.check_vm_network_devices():
                return False

            if not self.vsphere_ipi_ocp_install():
                return False

        if self.is_vsphere_ipi_ocp_post_install_finished():
            self.my_output.default('OCP post installation steps already completed')
        else:
            if not self.is_vsphere_ipi_ocp_working():
                return False
            self.my_output.default('OCP functional')

            if not self.vsphere_ipi_ocp_post_install():
                return False

        if not self.is_vsphere_ipi_ocp_parameters_ready():
            if not self.vsphere_ipi_ocp_parameters_upload():
                return False

        return True
