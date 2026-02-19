from lib import filter_helper


class K8sNemoGuardrailInfo():
    def __init__(self):
        self.nemo_guardrail = None

    def get_nemo_guardrail_info(self, managed_object):
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

    def get_nemo_guardrails_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_guardrail is not None:
                return self.nemo_guardrail

        managed_objects = self.get_nemo_guardrail_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nemo_guardrail = []
        for managed_object in managed_objects:
            nemo_guardrail_info = {}
            nemo_guardrail_info['info'] = self.get_nemo_guardrail_info(
                managed_object
            )
            nemo_guardrail_info['mo'] = managed_object
            self.nemo_guardrail.append(
                nemo_guardrail_info
            )

        return self.nemo_guardrail

    def match_nemo_guardrail(self, nemo_guardrail_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nemo_guardrail_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nemo_guardrail_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nemo_guardrail',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nemo_guardrails(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nemo_guardrails = self.get_nemo_guardrails_info(cache_enabled=cache_enabled)
        if all_nemo_guardrails is None:
            return None

        nemo_guardrails = []

        for nemo_guardrail_info in all_nemo_guardrails:
            if not self.match_nemo_guardrail(nemo_guardrail_info['info'], object_filter):
                continue

            if return_mo:
                nemo_guardrails.append(
                    nemo_guardrail_info['mo']
                )
                continue

            nemo_guardrails.append(
                nemo_guardrail_info['info']
            )

        return nemo_guardrails

    def is_nemo_guardrail(self, namespace, name, cache_enabled=True):
        if self.get_nemo_guardrail(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nemo_guardrail(self, cache_enabled=True):
        policies = self.get_nemo_guardrails(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nemo_guardrail(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nemo_guardrails = self.get_nemo_guardrails(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nemo_guardrails is None:
            return None

        if len(nemo_guardrails) == 1:
            return nemo_guardrails[0]

        return None
