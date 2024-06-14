import time
import json

from lib import filter_helper


class AssistedInstallClusterInfo():
    def __init__(self):
        self.assisted_install_cluster = None
        self.assisted_install_cluster_install_config = {}

    def get_assisted_install_cluster_install_config(self, cluster_id, cache_enabled=True):
        if cache_enabled and cluster_id in self.assisted_install_cluster_install_config:
            return self.assisted_install_cluster_install_config[cluster_id]

        config_mo = self.get_assisted_install_cluster_install_config_mo(cluster_id, cache_enabled=cache_enabled)
        if config_mo is None:
            return None

        self.assisted_install_cluster_install_config[cluster_id] = json.loads(config_mo)
        return self.assisted_install_cluster_install_config[cluster_id]

    def get_assisted_install_cluster_host_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key not in ['inventory', 'ntp_sources', 'validations_info', 'domain_name_resolutions']:
                info[key] = managed_object[key]

        try:
            info['inventory'] = json.loads(managed_object['inventory'])
        except BaseException:
            info['inventory'] = None

        info['hostname'] = None
        if 'requested_hostname' in info:
            info['hostname'] = info['requested_hostname']

        if info['inventory'] is not None:
            if info['hostname'] is None:
                info['hostname'] = info['inventory']['hostname']

            for disk_info in info['inventory']['disks']:
                disk_info['target'] = False
                disk_info['target_tick'] = ''
                if disk_info['path'] == info['installation_disk_path']:
                    disk_info['target_tick'] = '\u2713'

        info['is_valid'] = {}
        info['is_valid']['hardware'] = True
        info['is_valid']['hardware_tick'] = '\u2713'
        info['__Output']['is_valid.hardware_tick'] = 'Green'
        info['is_valid']['network'] = True
        info['is_valid']['network_tick'] = '\u2713'
        info['__Output']['is_valid.network_tick'] = 'Green'
        info['is_valid']['operators'] = True
        info['is_valid']['operators_tick'] = '\u2713'
        info['__Output']['is_valid.operators_tick'] = 'Green'

        try:
            validations_info = json.loads(managed_object['validations_info'])
            info['validations_info'] = []
            for key in ['hardware', 'network', 'operators']:
                for item in validations_info[key]:
                    item['__Output'] = {}
                    item['type'] = key
                    if item['status'] == 'success':
                        item['__Output']['status'] = 'Green'
                    if item['status'] == 'failure':
                        item['__Output']['status'] = 'Red'
                        info['is_valid'][key] = False
                        info['__Output']['is_valid.%s_tick' % (key)] = 'Red'

                    info['validations_info'].append(
                        item
                    )

            info['valid'] = info['is_valid']['hardware'] and info['is_valid']['network'] and info['is_valid']['operators']

        except BaseException:
            info['validations_info'] = None
            info['is_valid']['hardware'] = False
            info['is_valid']['network'] = False
            info['is_valid']['operators'] = False
            info['is_valid']['hardware_tick'] = '\u2717'
            info['is_valid']['network_tick'] = '\u2717'
            info['is_valid']['operators_tick'] = '\u2717'
            info['__Output']['is_valid.hardware_tick'] = 'Red'
            info['__Output']['is_valid.network_tick'] = 'Red'
            info['__Output']['is_valid.operators_tick'] = 'Red'
            info['valid'] = False

        try:
            info['domain_name_resolutions'] = json.loads(managed_object['domain_name_resolutions'])
        except BaseException:
            info['domain_name_resolutions'] = None

        try:
            info['ntp_sources'] = json.loads(managed_object['ntp_sources'])
        except BaseException:
            info['ntp_sources'] = None

        info['ntp_ready'] = False
        info['ntp_ready_tick'] = '\u2717'
        info['__Output']['ntp_ready_tick'] = 'Red'
        if info['ntp_sources'] is not None:
            for ntp_source in info['ntp_sources']:
                ntp_source['__Output'] = {}
                ntp_source['reachable_tick'] = '\u2717'
                ntp_source['__Output']['reachable_tick'] = 'Red'
                if ntp_source['source_state'] == 'reachable':
                    info['ntp_ready'] = True
                    info['ntp_ready_tick'] = '\u2713'
                    info['__Output']['ntp_ready_tick'] = 'Green'
                    ntp_source['reachable_tick'] = '\u2713'
                    ntp_source['__Output']['reachable_tick'] = 'Green'

        if info['status'] is not None and info['status'] == 'Cluster is installed':
            info['__Output']['status'] = 'Green'

        return info

    def get_assisted_install_cluster_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key not in ['hosts']:
                info[key] = managed_object[key]

        info['hosts'] = []
        for host_mo in managed_object['hosts']:
            info['hosts'].append(
                self.get_assisted_install_cluster_host_info(
                    host_mo
                )
            )

        info['cidr'] = []
        for cluster_network_mo in managed_object['cluster_networks']:
            cidr = {}
            cidr['type'] = 'Cluster'
            cidr['cidr'] = cluster_network_mo['cidr']
            cidr['prefix'] = cluster_network_mo['host_prefix']
            info['cidr'].append(cidr)

        for service_network_mo in managed_object['service_networks']:
            cidr = {}
            cidr['type'] = 'Service'
            cidr['cidr'] = service_network_mo['cidr']
            cidr['prefix'] = None
            info['cidr'].append(cidr)

        return info

    def get_assisted_install_clusters_info(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_cluster is not None:
            return self.assisted_install_cluster

        managed_objects = self.get_assisted_install_cluster_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.assisted_install_cluster = []
        for managed_object in managed_objects:
            self.assisted_install_cluster.append(
                self.get_assisted_install_cluster_info(
                    managed_object
                )
            )

        self.log.openshift_mo(
            'assisted_install_cluster.info',
            self.assisted_install_cluster
        )

        return self.assisted_install_cluster

    def match_assisted_install_cluster(self, assisted_install_cluster_info, assisted_install_cluster_filter):
        if assisted_install_cluster_filter is None or len(assisted_install_cluster_filter) == 0:
            return True

        for ap_rule in assisted_install_cluster_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, assisted_install_cluster_info['name']):
                    return False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, assisted_install_cluster_info['id']):
                    return False

            if key == 'ids':
                key_found = True
                if assisted_install_cluster_info['id'] not in value.split(','):
                    return False

            if not key_found:
                self.log.error(
                    'match_assisted_install_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_assisted_install_clusters(
            self,
            assisted_install_cluster_filter=None,
            config_info=False,
            credentials_info=False,
            infra_info=False,
            manifest_info=False,
            kubeconfig_info=False,
            cache_enabled=True
        ):
        all_clusters = self.get_assisted_install_clusters_info(cache_enabled=cache_enabled)
        if all_clusters is None:
            return None

        clusters = []

        for cluster_info in all_clusters:
            if not self.match_assisted_install_cluster(cluster_info, assisted_install_cluster_filter):
                continue

            if config_info:
                cluster_info['config'] = self.get_assisted_install_cluster_install_config(
                    cluster_info['id'],
                    cache_enabled=cache_enabled
                )

            if infra_info:
                object_filter = []
                object_filter.append('cluster_id:%s' % (cluster_info['id']))
                cluster_infra_info = self.get_assisted_install_infras(
                    assisted_install_infra_filter=object_filter,
                    cache_enabled=cache_enabled
                )
                cluster_info['static_network_config'] = None
                if cluster_infra_info is not None and len(cluster_infra_info) == 1:
                    cluster_info['static_network_config'] = cluster_infra_info[0]['static_network_config']
                    cluster_info['infra_id'] = cluster_infra_info[0]['id']
                    cluster_info['iso_url'] = cluster_infra_info[0]['download_url']
                    cluster_info['iso_type'] = cluster_infra_info[0]['type']

            if credentials_info:
                cluster_info['credentials'] = None
                if cluster_info['status'] == 'installed':
                    cluster_info['credentials'] = self.get_assisted_install_cluster_credentials_mo(
                        cluster_info['id'],
                        cache_enabled=cache_enabled
                    )

            if manifest_info:
                cluster_info['manifest'] = self.get_assisted_install_manifest_mo(
                    cluster_info['id']
                )

            if kubeconfig_info:
                cluster_info['kubeconfig'] = self.get_assisted_install_cluster_kubeconfig_mo(
                    cluster_info['id'],
                    cache_enabled=cache_enabled
                )

            clusters.append(cluster_info)

        clusters = sorted(
            clusters,
            key=lambda i: i['name'].lower()
        )

        self.log.openshift_mo(
            'assisted_install_cluster.full',
            clusters
        )

        return clusters

    def get_assisted_install_cluster(
            self,
            cluster_name=None,
            cluster_id=None,
            config_info=False,
            credentials_info=False,
            infra_info=False,
            manifest_info=False,
            kubeconfig_info=False,
            cache_enabled=True
        ):
        if cluster_name is None and cluster_id is None:
            self.log.error(
                'get_assisted_install_cluster',
                'Select cluster by name or id'
            )
            return None

        if cluster_name is not None and cluster_id is not None:
            self.log.error(
                'get_assisted_install_cluster',
                'Select cluster by name or id'
            )
            return None

        object_filter = []
        if cluster_id is not None:
            object_filter.append('id:%s' % (cluster_id))
        if cluster_name is not None:
            object_filter.append('name:%s' % (cluster_name))

        clusters = self.get_assisted_install_clusters(
            assisted_install_cluster_filter=object_filter,
            config_info=config_info,
            credentials_info=credentials_info,
            infra_info=infra_info,
            manifest_info=manifest_info,
            kubeconfig_info=kubeconfig_info,
            cache_enabled=cache_enabled
        )
        if clusters is None or len(clusters) == 0:
            return None

        if len(clusters) > 1:
            self.log.error(
                'get_assisted_install_cluster',
                'Multiple cluster found [%s] [%s]' % (cluster_id, cluster_name)
            )
            return None

        return clusters[0]

    def get_assisted_install_cluster_status(self, cluster_id):
        cluster_info = self.get_assisted_install_cluster(
            cluster_id=cluster_id,
            cache_enabled=False
        )
        if cluster_info is not None:
            return cluster_info['status']

        return None

    def get_assisted_install_cluster_host_status(self, cluster_id):
        cluster_info = self.get_assisted_install_cluster(
            cluster_id=cluster_id,
            cache_enabled=False
        )

        hosts = {}
        if cluster_info is not None:
            if 'hosts' in cluster_info and cluster_info['hosts'] is not None:
                for host_info in cluster_info['hosts']:
                    try:
                        host_ip = host_info['inventory']['bmc_address']
                        hosts[host_ip] = host_info['status']
                    except BaseException:
                        pass

        return hosts

    def get_assisted_install_cluster_progress(self, cluster_id):
        cluster_info = self.get_assisted_install_cluster(
            cluster_id=cluster_id,
            cache_enabled=False
        )
        if cluster_info is not None:
            if cluster_info['status'] == 'installed':
                return 100

            if 'progress' in cluster_info and cluster_info['progress'] is not None:
                if 'total_percentage' not in cluster_info['progress']:
                    self.log.error(
                        'get_assisted_install_cluster_progress',
                        'Unexpected cluster info: %s' % (json.dumps(cluster_info, indent=4))
                    )
                    return None

                return cluster_info['progress']['total_percentage']

        return None

    def wait_assisted_install_cluster_status(self, cluster_id, status, timeout=7200):
        start_time = int(time.time())

        while True:
            cluster_info = self.get_assisted_install_cluster(
                cluster_id=cluster_id,
                cache_enabled=False
            )
            if cluster_info is not None:
                if cluster_info['status'] == status:
                    return True

            time.sleep(5)

            if int(time.time()) - start_time > timeout:
                self.log.error(
                    'wait_assisted_install_cluster_status',
                    'Timeout %s reached' % (timeout)
                )
                return False

    def wait_assisted_install_cluster_hosts_discovered(self, cluster_id, bmc_addresses, timeout=3600):
        start_time = int(time.time())

        while True:
            cluster_info = self.get_assisted_install_cluster(
                cluster_id=cluster_id,
                cache_enabled=False
            )
            if cluster_info is not None:
                if 'hosts' in cluster_info and cluster_info['hosts'] is not None:
                    discovered_bmc_addresses = []
                    for host_info in cluster_info['hosts']:
                        if 'inventory' in host_info and host_info['inventory'] is not None:
                            if host_info['inventory']['bmc_address'] in bmc_addresses:
                                discovered_bmc_addresses.append(
                                    host_info['inventory']['bmc_address']
                                )

                    if len(discovered_bmc_addresses) == len(bmc_addresses):
                        return True

            time.sleep(5)

            if int(time.time()) - start_time > timeout:
                self.log.error(
                    'wait_assisted_install_cluster_hosts_discovered',
                    'Timeout %s reached' % (timeout)
                )
                return False

    def update_assisted_install_cluster_hosts_hostname(self, cluster_id, hostname, attempts=3):
        attempt = 0
        updated_hosts = {}
        while True:
            cluster_info = self.get_assisted_install_cluster(
                cluster_id=cluster_id,
                cache_enabled=False
            )
            if cluster_info is not None:
                if 'hosts' in cluster_info and cluster_info['hosts'] is not None:
                    for host_info in cluster_info['hosts']:
                        if 'inventory' in host_info and host_info['inventory'] is not None:
                            host_bmc = host_info['inventory']['bmc_address']
                            if host_bmc not in updated_hosts:
                                response = self.update_assisted_install_infra_hostname(
                                    host_info['infra_env_id'],
                                    host_info['id'],
                                    hostname[host_bmc]
                                )
                                if response is not None:
                                    updated_hosts[host_bmc] = True

            if len(hostname) == len(updated_hosts):
                return True

            time.sleep(5)

            attempt = attempt + 1
            if attempt > attempts:
                self.log.error(
                    'update_assisted_install_cluster_hosts_hostname',
                    'Max attempts reached'
                )
                return False
