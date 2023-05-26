import json

from lib import ssh
from lib import filter_helper

from lib.vc import vcenter
from lib.ocp import settings as ocp_settings


class OcpVcenterInfo():
    def __init__(self):
        self.ocp_settings_handler = ocp_settings.OcpSettings(
            log_id=self.log_id
        )
        self.vc_handler = {}

    def get_vc_handler(self, ocp_vcenter_settings):
        if ocp_vcenter_settings['ip'] in self.vc_handler:
            return self.vc_handler[ocp_vcenter_settings['ip']]

        self.vc_handler[ocp_vcenter_settings['ip']] = vcenter.Vcenter(
            ocp_vcenter_settings['ip'],
            ocp_vcenter_settings['username'],
            ocp_vcenter_settings['password'],
            port=ocp_vcenter_settings['port'],
            log_id=self.log_id
        )
        return self.vc_handler[ocp_vcenter_settings['ip']]

    def get_terraform_cluster_id(self, ocp_cluster_settings):
        if 'cluster_id' in ocp_cluster_settings:
            return ocp_cluster_settings['cluster_id']

        ssh_handler = ssh.Ssh(
            ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=ocp_cluster_settings['parameters']['installer']['vm']['password']
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

        success = self.ocp_settings_handler.set_ocp_cluster_parameter(
            ocp_cluster_settings['name'],
            'cluster_id',
            tfvars['cluster_id']
        )
        if not success:
            self.log.error(
                'get_terraform_cluster_id',
                'OCP cluster settings update failed'
            )

        ocp_cluster_settings['cluster_id'] = tfvars['cluster_id']
        return tfvars['cluster_id']

    def get_ocp_cluster_vcenter_info(self, cluster_name):
        cluster = self.ocp_settings_handler.get_ocp_cluster(
            cluster_name
        )
        if cluster is None:
            self.log.error(
                'get_ocp_cluster_vcenter_info',
                'No cluster settings: %s' % (cluster_name)
            )
            return None

        if cluster['parameters']['ocp']['installation'] not in ['vsphere-ipi']:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = cluster_name
        info['vcenter'] = cluster['parameters']['vcenter']
        info['installer_vm_name'] = cluster['parameters']['installer']['vm']['name']
        info['cluster_id'] = self.get_terraform_cluster_id(cluster)
        if info['cluster_id'] is None:
            return None

        return info

    def get_ocp_clusters_vcenter_info(self):
        cluster_names = self.ocp_settings_handler.get_ocp_cluster_names()
        if cluster_names is None:
            return None

        clusters = []
        for cluster_name in cluster_names:
            cluster_info = self.get_ocp_cluster_vcenter_info(
                cluster_name
            )
            if cluster_info is not None:
                clusters.append(
                    cluster_info
                )

        return clusters

    def get_ocp_cluster_vm_info(self, cluster_info):
        vc_handler = self.get_vc_handler(cluster_info['vcenter'])
        if vc_handler is None:
            self.log.error(
                'get_vcenter_state',
                'vcenter access failed for cluster: %s' % (cluster_info['name'])
            )
            return None

        vm_filter = []
        vm_filter.append(
            'name:%s' % (cluster_info['cluster_id'])
        )
        vm_filter.append(
            'name:%s' % (cluster_info['installer_vm_name'])
        )

        info = vc_handler.get_vms(
            vm_filter=vm_filter
        )

        return info

    def match_ocp_cluster_vcenter(self, cluster_info, cluster_filter):
        if cluster_filter is None or len(cluster_filter) == 0:
            return True

        for ap_rule in cluster_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, cluster_info['name']):
                    return False

            if key == 'vc':
                if not filter_helper.match_string(value, cluster_info['vcenter']['name']):
                    return False

        return True

    def get_ocp_clusters_vcenter(self, cluster_filter=None):
        all_clusters = self.get_ocp_clusters_vcenter_info()
        if all_clusters is None:
            return None

        clusters = []

        for cluster_info in all_clusters:
            if not self.match_ocp_cluster_vcenter(cluster_info, cluster_filter):
                continue

            cluster_info['vms'] = self.get_ocp_cluster_vm_info(cluster_info)

            if not self.match_ocp_cluster_vcenter(cluster_info, cluster_filter):
                continue

            clusters.append(
                cluster_info
            )

        clusters = sorted(
            clusters,
            key=lambda i: i['name']
        )

        return clusters

    def get_ocp_cluster_vcenter(self, cluster_name):
        clusters = self.get_ocp_clusters_vcenter(
            cluster_filter=['name:%s' % (cluster_name)]
        )

        if clusters is None:
            return None

        if len(clusters) == 1:
            return clusters[0]

        return None
