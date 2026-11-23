import json
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sClusterVersionInfo():
    def __init__(self):
        self.cluster_version = None

    def get_cluster_version_info(self, managed_object):
        return self.get_base_info(managed_object)

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
        all_cluster_versions = self.get_infos(
            'cluster_version', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if all_cluster_versions is None:
            return None

        cluster_versions = []

        if deployment_info:
            deployments = self.get_deployments()

        for cluster_version_info in all_cluster_versions:
            if not self.match_cluster_version(cluster_version_info, object_filter):
                continue

            if return_mo:
                cluster_versions.append(
                    cluster_version_info['mo']
                )
                continue

            if deployment_info:
                cluster_version_info['co_deployment'] = None
                cluster_version_info['related_deployment'] = None

                cluster_version_deployment = self.get_cluster_version_deployment(
                    cluster_version_info,
                    deployments
                )
                if cluster_version_deployment is not None:
                    cluster_version_info['co_deployment'] = {}
                    cluster_version_info['co_deployment']['namespace'] = cluster_version_deployment['namespace']
                    cluster_version_info['co_deployment']['name'] = cluster_version_deployment['name']
                    cluster_version_related_deployments = self.get_cluster_version_related_deployments(
                        cluster_version_info,
                        deployments
                    )
                    if cluster_version_related_deployments is not None:
                        cluster_version_info['related_deployment'] = []
                        for related_deployment in cluster_version_related_deployments:
                            item = {}
                            item['namespace'] = related_deployment['namespace']
                            item['name'] = related_deployment['name']
                            cluster_version_info['related_deployment'].append(
                                item
                            )

            cluster_versions.append(
                cluster_version_info
            )

        return cluster_versions

    def get_cluster_version(self, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cluster_version', 
            'version',
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )