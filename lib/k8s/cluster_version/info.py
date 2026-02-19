import json
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sClusterVersionInfo():
    def __init__(self):
        self.cluster_version = None

    def get_cluster_version_info(self, cluster_version_mo):
        if cluster_version_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_version_mo
        )
        info.update(metadata_info)


        return info

    def get_cluster_versions_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_version is not None:
                return self.cluster_version

        managed_objects = self.get_cluster_version_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_version = []
        for managed_object in managed_objects:
            cluster_version_info = {}
            cluster_version_info['info'] = self.get_cluster_version_info(
                managed_object
            )
            cluster_version_info['mo'] = managed_object
            self.cluster_version.append(
                cluster_version_info
            )

        return self.cluster_version

    def match_cluster_version(self, cluster_version_info, cluster_version_filter):
        if cluster_version_filter is None or len(cluster_version_filter) == 0:
            return True

        for ap_rule in cluster_version_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_version_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_version',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_version_deployment(self, cluster_version_info, deployments):
        if cluster_version_info['related'] is None:
            return None

        namespaces = []
        for related in cluster_version_info['related']:
            if related['resource'] == 'namespaces':
                namespaces.append(
                    related['name']
                )

        names = []
        names.append(cluster_version_info['name'])
        names.append('openshift-%s' % (cluster_version_info['name']))
        names.append('%s-operator' % (cluster_version_info['name']))
        names.append('openshift-%s-operator' % (cluster_version_info['name']))
        names.append('cluster-%s-operator' % (cluster_version_info['name']))

        if cluster_version_info['name'] == 'openshift-samples':
            names.append('cluster-samples-operator')

        app_label_map = {}
        app_label_map['operator-lifecycle-manager'] = 'olm-operator'
        app_label_map['operator-lifecycle-manager-catalog'] = 'catalog-operator'
        app_label_map['operator-lifecycle-manager-packageserver'] = 'package-server-manager'

        for deployment in deployments:
            if deployment['owner_kind'] != 'ClusterVersion':
                continue

            if cluster_version_info['name'] in app_label_map:
                for label in deployment['label']:
                    if label == 'app':
                        if deployment['label'][label] == app_label_map[cluster_version_info['name']]:
                            return deployment

            if deployment['namespace'] not in namespaces:
                continue

            if deployment['name'] not in names:
                continue

            return deployment

        return None

    def get_cluster_version_related_deployments(self, cluster_version_info, deployments):
        related = []

        for deployment in deployments:
            for label in deployment['label']:
                if label == 'app.kubernetes.io/managed-by':
                    if deployment['label'][label] == cluster_version_info['co_deployment']['name']:
                        related.append(
                            deployment
                        )
                        continue

        return related

    def get_cluster_versions(self, object_filter=None, return_mo=False, deployment_info=False, cache_enabled=True):
        all_cluster_versions = self.get_cluster_versions_info(cache_enabled=cache_enabled)
        if all_cluster_versions is None:
            return None

        cluster_versions = []

        if deployment_info:
            deployments = self.get_deployments()

        for cluster_version_info in all_cluster_versions:
            if not self.match_cluster_version(cluster_version_info['info'], object_filter):
                continue

            if return_mo:
                cluster_versions.append(
                    cluster_version_info['mo']
                )
                continue

            if deployment_info:
                cluster_version_info['info']['co_deployment'] = None
                cluster_version_info['info']['related_deployment'] = None

                cluster_version_deployment = self.get_cluster_version_deployment(
                    cluster_version_info['info'],
                    deployments
                )
                if cluster_version_deployment is not None:
                    cluster_version_info['info']['co_deployment'] = {}
                    cluster_version_info['info']['co_deployment']['namespace'] = cluster_version_deployment['namespace']
                    cluster_version_info['info']['co_deployment']['name'] = cluster_version_deployment['name']
                    cluster_version_related_deployments = self.get_cluster_version_related_deployments(
                        cluster_version_info['info'],
                        deployments
                    )
                    if cluster_version_related_deployments is not None:
                        cluster_version_info['info']['related_deployment'] = []
                        for related_deployment in cluster_version_related_deployments:
                            item = {}
                            item['namespace'] = related_deployment['namespace']
                            item['name'] = related_deployment['name']
                            cluster_version_info['info']['related_deployment'].append(
                                item
                            )

            cluster_versions.append(
                cluster_version_info['info']
            )

        return cluster_versions

    def get_cluster_version(self, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:version'
        )
        networks = self.get_cluster_versions(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if networks is None:
            return None

        if len(networks) == 1:
            return networks[0]

        return None

    def get_disable_network_operator_management_body(self):
        body = {}
        body['api'] = 'config.openshift.io/v1'
        body['kind'] = 'ClusterVersion'
        body['metadata'] = dict(name='version')
        body['spec'] = {}
        value_mo = {}
        value_mo['kind'] = 'Deployment'
        value_mo['group'] = 'apps'
        value_mo['name'] = 'network-operator'
        value_mo['namespace'] = 'openshift-network-operator'
        value_mo['unmanaged'] = True
        body['spec']['overrides'] = [value_mo]
        return body

    def disable_network_operator_management(
            self, 
            confirmation=False, 
            my_output=None
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Disable network operator management', before_newline=True, underline=True)
            
        cluster_version_mo = self.get_cluster_version(return_mo=True)
        if cluster_version_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster version via rest api')
            return False
            
        body = self.get_disable_network_operator_management_body()
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        success = self.patch_cluster_version_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        return True    

    def get_enable_network_operator_management_body(self):
        body = {}
        body['api'] = 'config.openshift.io/v1'
        body['kind'] = 'ClusterVersion'
        body['metadata'] = dict(name='version')
        body['spec'] = {}
        body['spec']['overrides'] = None
        return body

    def enable_network_operator_management(
            self, 
            confirmation=False, 
            my_output=None
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Enable network operator management', before_newline=True, underline=True)
            
        cluster_version_mo = self.get_cluster_version(return_mo=True)
        if cluster_version_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster version via rest api')
            return False
            
        body = self.get_enable_network_operator_management_body()
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        success = self.patch_cluster_version_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        return True    
