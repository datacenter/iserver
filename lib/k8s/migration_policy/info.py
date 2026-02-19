import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sMigrationPolicyInfo():
    def __init__(self):
        self.migration_policy = None

    def get_migration_policy_info(self, migration_policy_mo):
        if migration_policy_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            migration_policy_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(migration_policy_mo, 'spec')
        return info

    def get_migration_policies_info(self, cache_enabled=True):
        if cache_enabled:
            if self.migration_policy is not None:
                return self.migration_policy

        managed_objects = self.get_migration_policy_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.migration_policy = []
        for managed_object in managed_objects:
            migration_policy_info = {}
            migration_policy_info['info'] = self.get_migration_policy_info(
                managed_object
            )
            migration_policy_info['mo'] = managed_object
            self.migration_policy.append(
                migration_policy_info
            )

        return self.migration_policy

    def match_migration_policy(self, migration_policy_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, migration_policy_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_migration_policy',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_migration_policies(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_migration_policies = self.get_migration_policies_info(cache_enabled=cache_enabled)
        if all_migration_policies is None:
            return None

        migration_policies = []

        for migration_policy_info in all_migration_policies:
            if not self.match_migration_policy(migration_policy_info['info'], object_filter):
                continue

            if return_mo:
                migration_policies.append(
                    migration_policy_info['mo']
                )
                continue

            migration_policies.append(
                migration_policy_info['info']
            )

        return migration_policies

    def is_migration_policy(self, name, cache_enabled=True):
        if self.get_migration_policy(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_migration_policy(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        migration_policies = self.get_migration_policies(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if migration_policies is None:
            return None

        if len(migration_policies) == 1:
            return migration_policies[0]

        return None
