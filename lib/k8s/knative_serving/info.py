from lib import filter_helper


class K8sKnativeServingInfo():
    def __init__(self):
        self.knative_serving = None

    def get_knative_serving_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )
        if 'Ready' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'
        
        info['ingress'] = []
        ingresses_mo = self.get(managed_object, 'spec:ingress', on_error=[], on_none=[])
        for ingress_mo in ingresses_mo:
            if self.get(managed_object, 'spec:ingress:%s:enabled' % (ingress_mo)):
                info['ingress'].append(
                    ingress_mo
                )
        
        info['version'] = self.get(managed_object, 'status:version')
        return info

    def add_knative_serving_info(self, knative_serving_info, deployments):
        knative_serving_info['info']['deployment'] = []
        knative_serving_info['info']['deploymentT'] = []
        for deployment in deployments:
            if deployment['namespace'] != knative_serving_info['info']['namespace']:
                continue

            if 'app.kubernetes.io/name' not in deployment['label']:
                continue

            if deployment['label']['app.kubernetes.io/name'] == knative_serving_info['info']['name']:
                knative_serving_info['info']['deployment'].append(
                    deployment['name']
                )

                knative_serving_info['info']['deploymentT'].append(
                    '%s %s' % (
                        deployment['readyTick'],
                        deployment['name']
                    )
                )

        return knative_serving_info
    
    def get_knative_servings_info(self, cache_enabled=True):
        if cache_enabled:
            if self.knative_serving is not None:
                return self.knative_serving

        managed_objects = self.get_knative_serving_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.knative_serving = []
        for managed_object in managed_objects:
            knative_serving_info = {}
            knative_serving_info['info'] = self.get_knative_serving_info(
                managed_object
            )
            knative_serving_info['mo'] = managed_object
            self.knative_serving.append(
                knative_serving_info
            )

        return self.knative_serving

    def match_knative_serving(self, knative_serving_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, knative_serving_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, knative_serving_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_knative_serving',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_knative_servings(self, object_filter=None, deployment_info=False, return_mo=False, cache_enabled=True):
        all_knative_servings = self.get_knative_servings_info(cache_enabled=cache_enabled)
        if all_knative_servings is None:
            return None

        knative_servings = []

        deployments = None
        if deployment_info:
            deployments = self.get_deployments(cache_enabled=cache_enabled)

        for knative_serving_info in all_knative_servings:
            if deployment_info:
                knative_serving_info = self.add_knative_serving_info(knative_serving_info, deployments)

            if not self.match_knative_serving(knative_serving_info['info'], object_filter):
                continue

            if return_mo:
                knative_servings.append(
                    knative_serving_info['mo']
                )
                continue

            knative_servings.append(
                knative_serving_info['info']
            )

        return knative_servings

    def is_knative_serving(self, namespace, name, cache_enabled=True):
        if self.get_knative_serving(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_knative_serving(self, cache_enabled=True):
        policies = self.get_knative_servings(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_knative_serving(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        knative_servings = self.get_knative_servings(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if knative_servings is None:
            return None

        if len(knative_servings) == 1:
            return knative_servings[0]

        return None
