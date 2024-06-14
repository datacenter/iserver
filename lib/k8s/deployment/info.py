from lib import filter_helper


class K8sDeploymentInfo():
    def __init__(self):
        self.deployment = None

    def get_deployment_info(self, deployment_mo):
        if deployment_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            deployment_mo
        )
        info.update(metadata_info)

        keys = [
            'observedGeneration',
            'replicas',
            'updatedReplicas',
            'readyReplicas',
            'availableReplicas',
            'conditions'
        ]
        for key in keys:
            info[key] = self.get(deployment_mo, 'status:%s' % (key))

        info['readyT'] = '%s/%s' % (
            info['replicas'],
            info['readyReplicas']
        )
        if info['replicas'] > 0 and info['replicas'] == info['readyReplicas']:
            info['__Output']['readyT'] = 'Green'
        else:
            info['__Output']['readyT'] = 'Red'

        return info

    def get_deployments_info(self, cache_enabled=True):
        if cache_enabled:
            if self.deployment is not None:
                return self.deployment

        managed_objects = self.get_deployment_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.deployment = []
        for managed_object in managed_objects:
            deployment_info = {}
            deployment_info['info'] = self.get_deployment_info(
                managed_object
            )
            deployment_info['mo'] = managed_object
            self.deployment.append(
                deployment_info
            )

        return self.deployment

    def match_deployment(self, deployment_info, deployment_filter):
        if deployment_filter is None or len(deployment_filter) == 0:
            return True

        for ap_rule in deployment_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, deployment_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (deployment_info['namespace'], deployment_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, deployment_info['owner']):
                    return False

            if not key_found:
                self.log.error(
                    'match_deployment',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_deployments(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_deployments = self.get_deployments_info(cache_enabled=cache_enabled)
        if all_deployments is None:
            return None

        deployments = []

        for deployment_info in all_deployments:
            if not self.match_deployment(deployment_info['info'], object_filter):
                continue

            if return_mo:
                deployments.append(
                    deployment_info['mo']
                )
                continue

            deployments.append(
                deployment_info['info']
            )

        return deployments
