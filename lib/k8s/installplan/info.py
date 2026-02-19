import time
import yaml
from lib import filter_helper


class K8sInstallplanInfo():
    def __init__(self):
        self.installplan = None

    def get_installplan_info(self, installplan_mo):
        if installplan_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            installplan_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(installplan_mo, 'spec')
        info['status'] = self.get(installplan_mo, 'status')

        info['ready'] = False
        conditions_mo = self.get(installplan_mo, 'status:conditions')
        phase_mo = self.get(installplan_mo, 'status:phase')
        if conditions_mo is not None and phase_mo is not None:
            if phase_mo == 'Complete':
                for condition_mo in conditions_mo:
                    if condition_mo['type'] == 'Installed' and condition_mo['status'] in ['True', '"True"']:
                        info['ready'] = True

        info['approved'] = self.get(installplan_mo, 'spec:approved', on_error=False, on_none=False)
        if info['approved']:
            info['approvedTick'] = '\u2713'
            info['__Output']['approvedTick'] = 'Green'
        else:
            info['approvedTick'] = '\u2717'
            info['__Output']['approvedTick'] = 'Red'

        return info

    def get_installplans_info(self, cache_enabled=True):
        if cache_enabled:
            if self.installplan is not None:
                return self.installplan

        managed_objects = self.get_installplan_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.installplan = []
        for managed_object in managed_objects:
            installplan_info = {}
            installplan_info['info'] = self.get_installplan_info(
                managed_object
            )
            installplan_info['mo'] = managed_object
            self.installplan.append(
                installplan_info
            )

        return self.installplan

    def match_installplan(self, installplan_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, installplan_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (installplan_info['namespace'], installplan_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_installplan',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_installplans(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_installplans = self.get_installplans_info(cache_enabled=cache_enabled)
        if all_installplans is None:
            return None

        installplans = []

        for installplan_info in all_installplans:
            if not self.match_installplan(installplan_info['info'], object_filter):
                continue

            if return_mo:
                installplans.append(
                    installplan_info['mo']
                )
                continue

            installplans.append(
                installplan_info['info']
            )

        return installplans

    def is_installplan(self, namespace, name, cache_enabled=True):
        if self.get_installplan(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_installplan(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        installplans = self.get_installplans(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if installplans is None:
            return None

        if len(installplans) == 1:
            return installplans[0]

        return None

    def wait_installplan_install_plan_ready(self, namespace, name, max_time=600):
        start_time = int(time.time())
        while True:
            installplan = self.get_installplan(
                namespace,
                name,
                cache_enabled=False
            )
            if installplan is not None:
                if installplan['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_installplan_install_plan_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def approve_installplan(self, namespace, name, my_output=None):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'InstallPlan'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['approved'] = True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        return self.patch_installplan_mo(body)
    