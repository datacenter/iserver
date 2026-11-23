import json

from lib import ssh
from lib.vc import vcenter


class OcpClusterVcenter():
    def __init__(self):
        self.ocp_vcenter_handler = None

    def get_vc_handler(self):
        if self.ocp_vcenter_handler is not None:
            return self.ocp_vcenter_handler

        if 'vcenter' not in self.ocp_cluster_settings['parameters']:
            return None

        ocp_vcenter_settings = self.ocp_cluster_settings['parameters']['vcenter']
        self.ocp_vcenter_handler = vcenter.Vcenter(
            ocp_vcenter_settings['ip'],
            ocp_vcenter_settings['username'],
            ocp_vcenter_settings['password'],
            port=ocp_vcenter_settings['port'],
            log_id=self.log_id
        )
        return self.ocp_vcenter_handler

    def get_terraform_cluster_id(self):
        if 'cluster_id' in self.ocp_cluster_settings:
            return self.ocp_cluster_settings['cluster_id']

        try:
            key_filename = self.ocp_cluster_settings['parameters']['installer']['vm']['key_filename']
        except BaseException:
            key_filename = None

        ssh_handler = ssh.Ssh(
            self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            key_filename=key_filename,
            log_id=self.log_id
        )
        if ssh_handler is None:
            self.log.error(
                'get_terraform_cluster_id',
                'Installation VM ssh failed'
            )
            return None

        tfvars = ssh_handler.get_file(
            '/root/install/terraform.tfvars.json',
            convert_json=True
        )
        if tfvars is None:
            self.log.error(
                'get_terraform_cluster_id',
                'Failed to get /root/install/terraform.tfvars.json'
            )
            return None

        self.log.debug(
            'get_terraform_cluster_id',
            json.dumps(tfvars, indent=4)
        )

        if 'cluster_id' not in tfvars:
            self.log.error(
                'get_terraform_cluster_id',
                'Unexpected tfvars'
            )
            return None

        success = self.settings_handler.set_ocp_cluster_parameter(
            self.ocp_cluster_settings['name'],
            'cluster_id',
            tfvars['cluster_id']
        )
        if not success:
            self.log.error(
                'get_terraform_cluster_id',
                'OCP cluster settings update failed'
            )

        self.ocp_cluster_settings['cluster_id'] = tfvars['cluster_id']
        return tfvars['cluster_id']

    def get_ocp_cluster_vcenter_info(self):
        ocp_vcenter_handler = self.get_vc_handler()
        if ocp_vcenter_handler is None:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = self.ocp_cluster_settings['name']
        info['vcenter'] = self.ocp_cluster_settings['parameters']['vcenter']
        info['installer_vm_name'] = self.ocp_cluster_settings['parameters']['installer']['vm']['name']
        info['cluster_id'] = self.get_terraform_cluster_id()
        if info['cluster_id'] is None:
            return None

        vm_filter = []
        vm_filter.append(
            'name:%s' % (info['cluster_id'])
        )
        vm_filter.append(
            'name:%s' % (info['installer_vm_name'])
        )

        info['vms'] = ocp_vcenter_handler.get_vms(
            vm_filter=vm_filter
        )

        return info
