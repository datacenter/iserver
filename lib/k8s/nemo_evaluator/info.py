from lib import filter_helper


class K8sNemoEvaluatorInfo():
    def __init__(self):
        self.nemo_evaluator = None

    def get_nemo_evaluator_info(self, managed_object):
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
        return info

    def get_nemo_evaluators_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_evaluator is not None:
                return self.nemo_evaluator

        managed_objects = self.get_nemo_evaluator_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nemo_evaluator = []
        for managed_object in managed_objects:
            nemo_evaluator_info = {}
            nemo_evaluator_info['info'] = self.get_nemo_evaluator_info(
                managed_object
            )
            nemo_evaluator_info['mo'] = managed_object
            self.nemo_evaluator.append(
                nemo_evaluator_info
            )

        return self.nemo_evaluator

    def match_nemo_evaluator(self, nemo_evaluator_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nemo_evaluator_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nemo_evaluator_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nemo_evaluator',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nemo_evaluators(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nemo_evaluators = self.get_nemo_evaluators_info(cache_enabled=cache_enabled)
        if all_nemo_evaluators is None:
            return None

        nemo_evaluators = []

        for nemo_evaluator_info in all_nemo_evaluators:
            if not self.match_nemo_evaluator(nemo_evaluator_info['info'], object_filter):
                continue

            if return_mo:
                nemo_evaluators.append(
                    nemo_evaluator_info['mo']
                )
                continue

            nemo_evaluators.append(
                nemo_evaluator_info['info']
            )

        return nemo_evaluators

    def is_nemo_evaluator(self, namespace, name, cache_enabled=True):
        if self.get_nemo_evaluator(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nemo_evaluator(self, cache_enabled=True):
        policies = self.get_nemo_evaluators(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nemo_evaluator(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nemo_evaluators = self.get_nemo_evaluators(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nemo_evaluators is None:
            return None

        if len(nemo_evaluators) == 1:
            return nemo_evaluators[0]

        return None
