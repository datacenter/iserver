import platform
import traceback
import xml.dom.minidom
import webbrowser
import yaml

from ncclient import manager as nc_manager

from lib import file_helper
from lib import ssh
from lib.xd import ocp2fabric


class OcpVmReport():
    def __init__(self):
        self.report_html = None
        self.report_vm_name = None
        self.report_vm_namespace = None

    def get_report_html_textarea(self, output):
        lines = min(len(output.split('\n')) + 1, 30)
        max_col = 0
        for line in output.split('\n'):
            max_col = max(max_col, len(line))
        columns = min(max_col + 3, 256)

        textarea = '<textarea rows="%s" cols="%s" disabled>\n%s\n</textarea>' % (
            lines,
            columns,
            output
        )

        return textarea

    def get_vm_state_report_oc_commands(self, commands):
        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            key_filename=self.ocp_cluster_settings['parameters']['installer']['vm']['key_filename'],
            log_id=self.log_id
        )

        for key in commands:
            if key == 'oc.vmi':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Virtual Machine Instance</u></h3>' % (self.report_html)

            if key == 'oc.vm':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Virtual Machine</u></h3>' % (self.report_html)

            if key == 'oc.pod':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift POD</u></h3>' % (self.report_html)

            if key == 'oc.svc':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Service</u></h3>' % (self.report_html)

            if key == 'oc.dv':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Data Volume</u></h3>' % (self.report_html)

            if key == 'oc.pvc':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Persistent Volume Claim</u></h3>' % (self.report_html)

            if key == 'oc.pv':
                self.report_html = '%s\n<br><h3><u>Section: OpenShift Persistent Volume</u></h3>' % (self.report_html)

            if key == 'oc.pv':
                self.report_html = '%s\n<br><h3><u>Section: KVM</u></h3>' % (self.report_html)

            for command in commands[key]:
                success, output, error = ssh_handler.run_cmd(command, max_attempts=3)
                if success:
                    report = '# %s\n%s\n\n' % (
                        command,
                        output
                    )
                    self.log.adhoc(
                        'report.%s' % (key),
                        report
                    )

                    self.report_html = '%s\nCommand: %s<br><br>%s<br><br>' % (
                        self.report_html,
                        command,
                        self.get_report_html_textarea(output)
                    )

                else:
                    self.my_output.error(
                        'Command failed: %s' % (command)
                    )
                    self.log.error(
                        'get_vm_state_report_oc_commands',
                        error
                    )
                    return False

        return True

    def create_vm_state_report_oc_dv(self):
        # DVS
        # oc get dvs -n <namespace> <name>
        # oc get dvs -n <namespace> <name> -o yaml

        self.my_output.default('Report: oc dv')

        commands = {}
        report_name = 'oc.dv'
        commands[report_name] = []

        disks_info = self.get_ocp_vm_disks_info(
            self.report_vm_namespace,
            self.report_vm_name
        )
        for disk in disks_info['disks']:
            if disk['volume']['type'] == 'dataVolume':
                dv_name = disk['volume']['info']['name']

                if self.k8s_handler.is_data_volume(self.report_vm_namespace, dv_name):
                    commands[report_name].append(
                        'oc get dvs -n %s %s' % (
                            self.report_vm_namespace,
                            dv_name
                        )
                    )
                    commands[report_name].append(
                        'oc get dvs -n %s %s -o yaml' % (
                            self.report_vm_namespace,
                            dv_name
                        )
                    )

        if not self.get_vm_state_report_oc_commands(commands):
            return False

        return True

    def create_vm_state_report_oc_pvc(self):
        self.my_output.default('Report: oc pvc')

        commands = {}
        report_name = 'oc.pvc'
        commands[report_name] = []

        disks_info = self.get_ocp_vm_disks_info(
            self.report_vm_namespace,
            self.report_vm_name
        )

        for disk in disks_info['disks']:
            if 'persistent_volume_claim_info' in disk and disk['persistent_volume_claim_info'] is not None:

                # PVC
                # oc get pvc -n <namespace> <name>
                # oc get pvc -n <namespace> <name> -o yaml

                pvc_namespace = disk['persistent_volume_claim_info']['namespace']
                pvc_name = disk['persistent_volume_claim_info']['name']

                if self.k8s_handler.is_pvc(pvc_namespace, pvc_name):
                    commands[report_name].append(
                        'oc get pvc -n %s %s' % (
                            pvc_namespace,
                            pvc_name
                        )
                    )
                    commands[report_name].append(
                        'oc get pvc -n %s %s -o yaml' % (
                            pvc_namespace,
                            pvc_name
                        )
                    )

        if not self.get_vm_state_report_oc_commands(commands):
            return False

        return True

    def create_vm_state_report_oc_pv(self):
        self.my_output.default('Report: oc pv')

        commands = {}
        report_name = 'oc.pv'
        commands[report_name] = []

        disks_info = self.get_ocp_vm_disks_info(
            self.report_vm_namespace,
            self.report_vm_name
        )

        for disk in disks_info['disks']:
            if 'persistent_volume_claim_info' in disk and disk['persistent_volume_claim_info'] is not None:

                # PV
                # oc get pv -n <namespace> <name>
                # oc get pv -n <namespace> <name> -o yaml

                pv_namespace = disk['persistent_volume_claim_info']['namespace']
                pv_name = disk['persistent_volume_claim_info']['volume_name']

                if self.k8s_handler.is_pvc(pv_namespace, pv_name):
                    commands[report_name].append(
                        'oc get pv -n %s %s' % (
                            pv_namespace,
                            pv_name
                        )
                    )
                    commands[report_name].append(
                        'oc get pv -n %s %s -o yaml' % (
                            pv_namespace,
                            pv_name
                        )
                    )

        if not self.get_vm_state_report_oc_commands(commands):
            return False

        return True

    def create_vm_state_report_oc_pod(self):
        # POD (Launcher) - matedata.labels.kubevirt.io/domain
        # oc get pod -n <namespace> <name>
        # oc get pod -n <namespace> <name> -o yaml

        self.my_output.default('Report: oc pod')

        pod_mo = self.k8s_handler.get_pod_with_label(
            'kubevirt.io/domain',
            self.report_vm_name,
            namespace=self.report_vm_namespace
        )
        if pod_mo is not None:
            pod_namespace = pod_mo['metadata']['namespace']
            pod_name = pod_mo['metadata']['name']

            report_name = 'oc.pod'

            commands = {}
            commands[report_name] = []
            commands[report_name].append(
                'oc get pod -n %s %s -o wide' % (
                    pod_namespace,
                    pod_name
                )
            )
            commands[report_name].append(
                'oc get pod -n %s %s -o yaml' % (
                    pod_namespace,
                    pod_name
                )
            )

            if not self.get_vm_state_report_oc_commands(commands):
                return False

        return True

    def create_vm_state_report_oc_srv(self, deployment):
        # oc get service -n <namespace> <name>
        # oc get service -n <namespace> <name> -o yaml
        if deployment['deployment']['service'] is not None:
            self.my_output.default('Report: oc service')
            report_name = 'oc.svc'
            commands = {}
            commands[report_name] = []

            for key in deployment['deployment']['service']:
                yaml_content = deployment['deployment']['service'][key]
                if yaml_content is None:
                    continue

                content = yaml.safe_load(yaml_content)
                namespace = content['metadata']['namespace']
                name = content['metadata']['name']

                commands[report_name].append(
                    'oc get service -n %s %s' % (
                        namespace,
                        name
                    )
                )
                commands[report_name].append(
                    'oc get service -n %s %s -o yaml' % (
                        namespace,
                        name
                    )
                )

            if not self.get_vm_state_report_oc_commands(commands):
                return False

        return True

    def create_vm_state_report_oc_vm(self):
        self.my_output.default('Report: oc vm')

        commands = {}
        report_name = 'oc.vm'

        commands[report_name] = []
        commands[report_name].append(
            'oc get vm -n %s %s' % (
                self.report_vm_namespace,
                self.report_vm_name
            )
        )
        commands[report_name].append(
            'oc get vm -n %s %s -o yaml' % (
                self.report_vm_namespace,
                self.report_vm_name
            )
        )

        if not self.get_vm_state_report_oc_commands(commands):
            return False

        return True

    def create_vm_state_report_oc_vmi(self):
        self.my_output.default('Report: oc vmi')

        commands = {}
        report_name = 'oc.vmi'

        commands[report_name] = []
        commands[report_name].append(
            'oc get vmi -n %s %s' % (
                self.report_vm_namespace,
                self.report_vm_name
            )
        )
        commands[report_name].append(
            'oc get vmi -n %s %s -o yaml' % (
                self.report_vm_namespace,
                self.report_vm_name
            )
        )

        if not self.get_vm_state_report_oc_commands(commands):
            return False

        return True

    def create_vm_state_report_oc(self, deployment):
        if not self.create_vm_state_report_oc_vmi():
            return False

        if not self.create_vm_state_report_oc_vm():
            return False

        if not self.create_vm_state_report_oc_srv(deployment):
            return False

        if not self.create_vm_state_report_oc_pod():
            return False

        if not self.create_vm_state_report_oc_dv():
            return False

        if not self.create_vm_state_report_oc_pvc():
            return False

        if not self.create_vm_state_report_oc_pv():
            return False

        return True

    def create_vm_state_report_kvm(self):
        # KVM - via installer => node
        # /var/lib/kubelet/pods/<pod.metadata.uid>/volumes/kubernetes.io~empty-dir/private/libvirt/qemu/<namespace>_<name>.xml

        self.my_output.default('Report: kvm')

        pod_mo = self.k8s_handler.get_pod_with_label(
            'kubevirt.io/domain',
            self.report_vm_name,
            namespace=self.report_vm_namespace
        )
        if pod_mo is not None:
            pod_uid = pod_mo['metadata']['uid']
            host_ip = pod_mo['status']['host_ip']

            report_name = 'oc.kvm'

            commands = {}
            commands[report_name] = []
            if self.ocp_cluster_settings['parameters']['installer']['vm']['ip'] == host_ip:
                commands[report_name].append(
                    'sudo cat /var/lib/kubelet/pods/%s/volumes/kubernetes.io~empty-dir/private/libvirt/qemu/%s_%s.xml' % (
                        pod_uid,
                        self.report_vm_namespace,
                        self.report_vm_name
                    )
                )
            else:
                commands[report_name].append(
                    'ssh core@%s sudo cat /var/lib/kubelet/pods/%s/volumes/kubernetes.io~empty-dir/private/libvirt/qemu/%s_%s.xml' % (
                        host_ip,
                        pod_uid,
                        self.report_vm_namespace,
                        self.report_vm_name
                    )
                )

            if not self.get_vm_state_report_oc_commands(commands):
                return False

        return True

    def create_vm_state_report_ssh(self, deployment):
        ssh_handler = self.get_ocp_vm_ssh_handler(deployment)
        if ssh_handler is None:
            return False

        self.report_html = '%s\n<br><h3><u>Section: Virtual Machine SSH Commands</u></h3>' % (self.report_html)

        for key in deployment['report']['ssh']:
            commands_output = ''
            for command in deployment['report']['ssh'][key]:
                self.my_output.default('Command: %s' % (command))
                success, output, error = ssh_handler.run_cmd(command, max_attempts=3)
                if not success:
                    self.my_output.error(
                        'Command failed: %s' % (command)
                    )
                    self.log.error(
                        'create_vm_state_report_ssh',
                        error
                    )
                    return False

                output = output.replace('\r\n', '\n').lstrip('\n')

                self.report_html = '%s\nCommand: %s<br><br>%s<br><br>' % (
                    self.report_html,
                    command,
                    self.get_report_html_textarea(output)
                )

                commands_output = '%s# %s%s\n\n' % (
                    commands_output,
                    command,
                    output
                )

            self.log.adhoc(
                'report.ssh.%s' % (key),
                commands_output
            )

        return True

    def create_vm_state_report_snmp(self, deployment):
        if deployment['tools'] is not None and deployment['tools']['enabled']:
            ssh_handler = ssh.Ssh(
                deployment['tools']['ip'],
                deployment['tools']['username'],
                password=deployment['tools']['password'],
                key_filename=deployment['tools']['key_filename'],
                log_id=self.log_id
            )
        else:
            ssh_handler = ssh.Ssh(
                self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
                self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
                password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
                key_filename=self.ocp_cluster_settings['parameters']['installer']['vm']['key_filename'],
                log_id=self.log_id
            )

        filename = deployment['deployment']['service']['snmp']
        service_yaml = yaml.safe_load(
            deployment['files'][filename]
        )

        node_ip, node_port = self.k8s_handler.get_service_node_ip_port(
            service_yaml['metadata']['namespace'],
            service_yaml['metadata']['name']
        )
        if node_ip is None or node_port is None:
            return False

        self.report_html = '%s\n<br><h3><u>Section: SNMP</u></h3>' % (self.report_html)

        for key in deployment['report']['snmp']:
            commands_output = ''
            for oid in deployment['report']['snmp'][key]:
                command = 'snmpwalk -v %s -c %s %s:%s %s' % (
                    deployment['snmp']['version'],
                    deployment['snmp']['community'],
                    node_ip,
                    node_port,
                    oid
                )
                self.my_output.default('Command: %s' % (command))
                success, output, error = ssh_handler.run_cmd(command, max_attempts=3)
                if not success:
                    self.my_output.error(
                        'Command failed: %s' % (command)
                    )
                    self.log.error(
                        'create_vm_state_report_snmp',
                        error
                    )
                    return False

                commands_output = '%s# %s%s\n\n' % (
                    commands_output,
                    command,
                    output
                )

                self.log.adhoc(
                    'report.snmp.%s' % (key),
                    commands_output
                )

                self.report_html = '%s\n%s<br><br>' % (
                    self.report_html,
                    self.get_report_html_textarea(commands_output)
                )

        return True

    def create_vm_state_report_netconf(self, deployment):
        filename = deployment['deployment']['service']['netconf']
        service_yaml = yaml.safe_load(
            deployment['files'][filename]
        )
        if service_yaml is None:
            self.log.error(
                'create_vm_state_report_netconf',
                'File read failed: %s' % (deployment['files'][filename])
            )
            return False

        node_ip, node_port = self.k8s_handler.get_service_node_ip_port(
            service_yaml['metadata']['namespace'],
            service_yaml['metadata']['name']
        )

        if node_ip is None or node_port is None:
            return False

        self.my_output.default(
            'Netconf %s:%s with (%s,%s)' % (
                node_ip,
                node_port,
                deployment['netconf']['username'],
                deployment['netconf']['password']
            )
        )

        self.report_html = '%s\n<h3><u>Section: Netconf</u></h3>' % (self.report_html)

        try:
            nc_handler = nc_manager.connect(
                host=node_ip,
                port=node_port,
                username=deployment['netconf']['username'],
                password=deployment['netconf']['password'],
                hostkey_verify=False,
                allow_agent=False,
                look_for_keys=False
            )
        except BaseException:
            self.my_output.error(
                'Netconf connection failed'
            )
            self.my_output.error(
                traceback.format_exc()
            )
            return False

        if 'capabilities' in deployment['report']['netconf']:
            capabilities = ''
            for capability in nc_handler.server_capabilities:
                capabilities = '%s%s\n' % (
                    capabilities,
                    capability
                )

            self.log.adhoc(
                'report.netconf.capabilities',
                capabilities
            )

            self.report_html = '%s\nCapabilities<br><br>%s<br><br>' % (
                self.report_html,
                self.get_report_html_textarea(capabilities)
            )

        if 'configuration' in deployment['report']['netconf']:
            xml_config = nc_handler.get_config(source='running').data_xml
            output = xml.dom.minidom.parseString(xml_config).toprettyxml()
            self.log.adhoc(
                'report.netconf.configuration',
                output
            )

            self.report_html = '%s\nConfiguration<br><br>%s<br><br>' % (
                self.report_html,
                self.get_report_html_textarea(output)
            )

        return True

    def create_vm_state_report_info(self):
        info = self.get_ocp_vms_info(
            name=self.report_vm_name,
            namespace=self.report_vm_namespace
        )

        self.my_output.clear_output()
        self.print_ocp_vm_info(
            info,
            stream='output'
        )

        self.report_html = '%s\n<br><h3><u>Section: Virtual Machine State Information</u></h3>' % (self.report_html)
        self.report_html = '%s\n<br>%s<br><br>' % (
            self.report_html,
            self.get_report_html_textarea(
                self.my_output.get_output()
            )
        )

    def create_vm_state_report_disk(self):
        info = self.get_ocp_vm_disks_info(
            self.report_vm_namespace,
            self.report_vm_name
        )

        self.my_output.clear_output()
        self.print_ocp_vm_disks_info(
            info,
            show_vm_info=False,
            stream='output'
        )

        self.report_html = '%s\n<br><h3><u>Section: Virtual Machine Disks</u></h3>' % (self.report_html)
        self.report_html = '%s\n<br>%s<br><br>' % (
            self.report_html,
            self.get_report_html_textarea(
                self.my_output.get_output()
            )
        )

    def create_vm_state_report_net(self):
        info = self.get_ocp_vm_net_info(
            self.report_vm_namespace,
            self.report_vm_name
        )

        self.my_output.clear_output()

        self.print_ocp_vm_net_info(
            info,
            show_vm_info=False,
            stream='output'
        )

        self.my_output.my_print(
            ocp2fabric.print_ocp_vm_net_fabric_info(
                info['interfaces'],
                stream='output'
            )
        )

        self.report_html = '%s\n<br><h3><u>Section: Virtual Machine Interfaces</u></h3>' % (self.report_html)
        self.report_html = '%s\n<br>%s<br><br>' % (
            self.report_html,
            self.get_report_html_textarea(
                self.my_output.get_output()
            )
        )

    def create_vm_state_report(self, deployment, sections=['all']):
        if not deployment['report']['enabled']:
            return True

        vm_filename = deployment['deployment']['vm']
        filename = deployment['files'][vm_filename]
        vm_yaml = yaml.safe_load(
            filename
        )
        if vm_yaml is None:
            self.log.error(
                'create_vm_state_report',
                'File read failed: %s' % (filename)
            )
            return False

        self.report_vm_namespace = vm_yaml['metadata']['namespace']
        self.report_vm_name = vm_yaml['metadata']['name']

        self.report_html = '<!DOCTYPE html>'
        self.report_html = '%s\n<html>' % (self.report_html)
        self.report_html = '%s\n<head><meta charset="utf-8"><title>VM Report</title></head>' % (self.report_html)
        self.report_html = '%s\n<body>' % (self.report_html)
        self.report_html = '%s\n<h2>OCP Virtual Machine State Report</h2>' % (self.report_html)

        self.my_output.default('Collect virtual machine report data...')
        if 'all' in sections:
            sections = ['oc', 'kvm', 'ssh', 'snmp', 'netconf']

        self.create_vm_state_report_info()
        self.create_vm_state_report_disk()
        self.create_vm_state_report_net()

        if 'oc' in sections:
            if not self.create_vm_state_report_oc(deployment):
                return False

        if 'kvm' in sections:
            if not self.create_vm_state_report_kvm():
                return False

        if 'ssh' in sections:
            if 'ssh' in deployment['report']:
                self.my_output.default('Collect virtual machine ssh/cli data...')
                if not self.create_vm_state_report_ssh(deployment):
                    return False

        if 'snmp' in sections:
            if 'snmp' in deployment['report']:
                self.my_output.default('Collect virtual machine snmp data...')
                if not self.create_vm_state_report_snmp(deployment):
                    return False

        if 'netconf' in sections:
            if 'netconf' in deployment['report']:
                self.my_output.default('Collect virtual machine netconf data...')
                if not self.create_vm_state_report_netconf(deployment):
                    return False

        self.report_html = '%s</body>' % (self.report_html)
        self.report_html = '%s</html>' % (self.report_html)

        filename = self.log.adhoc(
            'report.html',
            self.report_html
        )

        my_os = platform.system()
        if my_os == 'Windows':
            link = 'file://C:%s' % (filename)
        else:
            link = 'file://%s' % (filename)

        self.my_output.default('Report: %s' % (link))
        webbrowser.open(link)

        return True
