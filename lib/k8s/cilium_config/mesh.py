import time
import yaml
import copy
from lib import filter_helper
from menu.common import get_confirmation


class K8sCiliumConfigMesh():
    def __init__(self):
        pass

    def is_cilium_mesh_enabled(self, cache_enabled=True):
        if self.get_cilium_mesh_configuration(cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_cilium_mesh_id(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        return filter_helper.get(cilium_config_mo, 'spec:cluster:id')

    def get_cilium_mesh_name(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        return filter_helper.get(cilium_config_mo, 'spec:cluster:name')

    def get_cilium_mesh_cluster_ids(self, cache_enabled=True):
        status = self.get_cilium_mesh_status(cache_enabled=cache_enabled)
        if status is None:
            return None
        
        ids = []
        for item in status:
            ids.append(int(item['cluster_id']))

        return ids
    
    def is_cilium_mesh_id_available(self, cluster_id):
        local_id = self.get_cilium_mesh_id(cache_enabled=False)
        if local_id is None:
            return False
        
        if int(local_id) == int(cluster_id):
            return False
        
        peer_ids = self.get_cilium_mesh_cluster_ids(cache_enabled=False)
        if peer_ids is None:
            return False
        
        if int(cluster_id) in peer_ids:
            return False
        
        return True
    
    def get_cilium_mesh_configuration(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        return filter_helper.get(cilium_config_mo, 'spec:clustermesh')

    def get_cilium_mesh_configured_clusters(self, cache_enabled=True):
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return None
        
        cluster_mesh_mo = filter_helper.get(cilium_config_mo, 'spec:clustermesh')
        if cluster_mesh_mo is None:
            return None
        
        return filter_helper.get(cilium_config_mo, 'spec:clustermesh:config:clusters', on_error=[], on_none=[])
    
    def get_cilium_agent_mesh_status_mo(self, cache_enabled=True):
        agents = self.get_cilium_agents_status_mo(cache_enabled)

        status = []
        for agent in agents:
            clusters_mo = filter_helper.get(agent, 'cluster-mesh:clusters')
            if clusters_mo is None:
                continue

            for cluster_mo in clusters_mo:
                cluster_mo['metadata'] = agent['metadata']
                status.append(cluster_mo)

        return status

    def get_cilium_agent_mesh_status_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['cluster_id'] = filter_helper.get(managed_object, 'config:cluster-id')
        info['cluster_name'] = filter_helper.get(managed_object, 'name')
        if 'connected' in info and info['connected']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_cilium_agents_mesh_status_info(self, cache_enabled=True):
        managed_objects = self.get_cilium_agent_mesh_status_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            info.append(
                self.get_cilium_agent_mesh_status_info(
                    managed_object
                )
            )

        return info
    
    def match_cilium_agemt_mesh_status(self, status_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'cluster_id':
                key_found = True
                if not filter_helper.match_integer(value, status_info['cluster_id']):
                    return False

            if key == 'cluster_name':
                key_found = True
                if not filter_helper.match_string(value, status_info['cluster_name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cilium_mesh_status',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cilium_agents_mesh_status(self, object_filter=None, cache_enabled=False):
        all_agents = self.get_cilium_agents_mesh_status_info(cache_enabled=cache_enabled)
        if all_agents is None:
            return None

        status = []

        for agent in all_agents:
            if not self.match_cilium_agemt_mesh_status(agent, object_filter):
                continue

            status.append(
                agent
            )

        status = sorted(
            status,
            key=lambda i: (
                i['cluster_name'], 
                i['metadata']['pod']
            )
        )
        return status

    def get_cilium_mesh_status(self, object_filter=None, cache_enabled=False):
        agents = self.get_cilium_agents_mesh_status(object_filter=object_filter, cache_enabled=cache_enabled)
        if agents is None:
            return None
        
        configs = self.get_cilium_mesh_configured_clusters(cache_enabled=cache_enabled)

        cluster_names = []
        for agent in agents:
            if agent['cluster_name'] not in cluster_names:
                cluster_names.append(
                    agent['cluster_name']
                )

        cluster_names = sorted(cluster_names)

        status = []
        for cluster_name in cluster_names:
            cluster_status = {}
            cluster_status['__Output'] = {}

            cluster_status['cluster_name'] = cluster_name
            cluster_status['agent_count'] = 0
            cluster_status['agent_up'] = 0

            cluster_status['ips'] = []
            cluster_status['port'] = None
            if configs is not None:
                for config in configs:
                    if config['name'] == cluster_name:
                        cluster_status['ips'] = config['ips']
                        cluster_status['port'] = config['port']

            cluster_status['agent'] = []
            for agent in agents:
                if agent['cluster_name'] == cluster_status['cluster_name']:
                    cluster_status['cluster_id'] = agent['cluster_id']
                    cluster_status['agent'].append(agent)

                    cluster_status['agent_count'] += 1
                    if agent['ready']:
                        cluster_status['agent_up'] += 1

            cluster_status['agent_summary'] = '%s/%s' % (
                cluster_status['agent_up'],
                cluster_status['agent_count']
            )
            cluster_status['ready'] = False

            if cluster_status['agent_count'] > 0:
                if cluster_status['agent_count'] == cluster_status['agent_up']:
                    cluster_status['__Output']['agent_summary'] = 'Green'
                    cluster_status['ready'] = True
                else:
                    cluster_status['__Output']['agent_summary'] = 'Red'

            cluster_status['agent'] = sorted(
                cluster_status['agent'],
                key=lambda i: i['metadata']['node'].lower()
            )
            status.append(cluster_status)

        return status

    def wait_cilium_mesh_cluster_ready_state(self, cluster_name, max_time=60, my_output=None):
        if my_output is not None:
            my_output.default('Wait for cluster [%s] connected...' % (cluster_name), before_newline=True)

        start_time = int(time.time())
        while True:
            status = self.get_cilium_mesh_status(object_filter=['cluster_name:%s' % (cluster_name)], cache_enabled=False)
            if status is not None:
                for item in status:
                    if item['ready']:
                        return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            time.sleep(5)
    
    def enable_cilium_mesh(self, mesh_id, mesh_name, mesh_port, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False
        
        if my_output is not None:
            my_output.default('Cluster mesh configuration', before_newline=True, underline=True)

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)

        body = {}
        body['cluster'] = {}
        body['cluster']['id'] = mesh_id
        body['cluster']['name'] = mesh_name
        body['clustermesh'] = {}
        body['clustermesh']['useAPIServer'] = True
        body['clustermesh']['apiserver'] = {}
        body['clustermesh']['apiserver']['kvstoremesh'] = dict(enabled=False)
        body['clustermesh']['apiserver']['replicas'] = 1
        body['clustermesh']['apiserver']['service'] = {}
        body['clustermesh']['apiserver']['type'] = 'NodePort'
        body['clustermesh']['apiserver']['nodePort'] = mesh_port
        body['clustermesh']['apiserver']['tls'] = {}
        body['clustermesh']['apiserver']['tls']['authMode'] = 'cluster'
        body['clustermesh']['apiserver']['tls']['auto'] = {}
        body['clustermesh']['apiserver']['tls']['auto']['certManagerIssuerRef'] = {}
        body['clustermesh']['apiserver']['tls']['auto']['certManagerIssuerRef']['group'] = 'cert-manager.io'
        body['clustermesh']['apiserver']['tls']['auto']['certManagerIssuerRef']['kind'] = 'Issuer'
        body['clustermesh']['apiserver']['tls']['auto']['certManagerIssuerRef']['name'] = 'cilium'
        body['clustermesh']['apiserver']['tls']['auto']['certValidityDuration'] = 1
        body['clustermesh']['apiserver']['tls']['auto']['enabled'] = True
        body['clustermesh']['apiserver']['tls']['auto']['method'] = 'certmanager'
        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        cilium_config['spec']['cluster'] = body['cluster']
        cilium_config['spec']['clustermesh'] = body['clustermesh']

        success = self.update_cilium_config(cilium_config['spec'], my_output=my_output, wait=True, confirmation=confirmation)
        if not success:
            return False
                
        return True

    def disable_cilium_mesh(self, my_output=None, confirmation=False):
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])
        if 'cluster' in cilium_spec:
            if 'id' in cilium_spec['cluster']:
                del cilium_spec['cluster']['id']
                if my_output is not None:
                    my_output.default('- spec.cluster.id deleted')

            if 'name' in cilium_spec['cluster']:
                del cilium_spec['cluster']['name']
                if my_output is not None:
                    my_output.default('- spec.cluster.name deleted')

            if len(cilium_spec['cluster']) == 0:
                del cilium_spec['cluster']
                if my_output is not None:
                    my_output.default('- spec.cluster')

        if 'clustermesh' in cilium_spec:
            del cilium_spec['clustermesh']
            if my_output is not None:
                my_output.default('- spec.clustermesh deleted')

        return self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)

    def add_cilium_mesh_cluster(self, mesh_ip, mesh_port, mesh_name, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])

        clusters = self.get_cilium_mesh_configured_clusters(cache_enabled=True)
        if clusters is None:
            if my_output is not None:
                my_output.error('Failed to get cilium mesh clusters configuration')
            return False
        
        new_clusters = []
        for cluster in clusters:
            if mesh_name == cluster['name']:
                continue

            new_clusters.append(
                cluster
            )

        new_cluster = {}
        new_cluster['name'] = mesh_name
        new_cluster['ips'] = [mesh_ip]
        new_cluster['port'] = mesh_port
        new_clusters.append(
            new_cluster
        )

        if 'config' not in cilium_spec['clustermesh']:
            cilium_spec['clustermesh']['config'] = {}
            cilium_spec['clustermesh']['config']['enabled'] = True

        cilium_spec['clustermesh']['config']['clusters'] = copy.deepcopy(new_clusters)
        success = self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)
        if not success:
            return False
        
        if not wait:
            return True
        
        if not self.wait_cilium_mesh_cluster_ready_state(mesh_name, my_output=my_output):
            return False
        
        return True
    
    def delete_cilium_mesh_cluster(self, mesh_ip=None, mesh_name=None, my_output=None, confirmation=False):
        if my_output is None:
            confirmation = False

        if mesh_ip is None and mesh_name is None:
            if my_output is not None:
                my_output.error('Select cluster mesh by ip or name')
            return False
        
        cilium_config = self.get_cilium_config(return_mo=True, cache_enabled=False)
        cilium_spec = copy.deepcopy(cilium_config['spec'])

        clusters = self.get_cilium_mesh_configured_clusters(cache_enabled=True)
        if clusters is None:
            if my_output is not None:
                my_output.error('Failed to get cilium mesh clusters configuration')
            return False
        
        new_clusters = []
        found = False
        for cluster in clusters:
            match = False
            if mesh_ip is not None and mesh_ip in cluster['ips']:
                match = True
            if mesh_name is not None and mesh_name == cluster['name']:
                match = True
            
            if match:
                found = True
                if my_output is not None:
                    my_output.default('Cluster to be deleted')
                    my_output.default(yaml.dump(cluster), wrap='~~~', before_newline=True)
                continue

            new_clusters.append(
                cluster
            )
        
        if not found:
            if my_output is not None:
                if mesh_ip is not None:
                    my_output.default('Cluster [ip:%s] already not configured' % (mesh_ip))
                else:
                    my_output.default('Cluster [name:%s] already not configured' % (mesh_name))

                my_output.default(yaml.dump(cilium_spec['clustermesh']), wrap='~~~', before_newline=True)
            return True
        
        if len(new_clusters) == 0:
            if 'config' in cilium_spec['clustermesh']:
                del cilium_spec['clustermesh']['config']
        else:
            cilium_spec['clustermesh']['config']['clusters'] = copy.deepcopy(new_clusters)

        return self.update_cilium_config(cilium_spec, my_output=my_output, wait=True, confirmation=confirmation)
    