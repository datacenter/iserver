from lib import filter_helper


class K8sSecurityContextConstraintInfo():
    def __init__(self):
        self.security_context_constraint = None

    def get_security_context_constraint_info(self, security_context_constraint_mo):
        if security_context_constraint_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            security_context_constraint_mo
        )
        info.update(metadata_info)

        keys = [
            'allowHostDirVolumePlugin',
            'allowHostIPC',
            'allowHostNetwork',
            'allowHostPID',
            'allowHostPorts',
            'allowPrivilegeEscalation',
            'allowPrivilegedContainer',
            'defaultAddCapabilities',
            'fsGroup',
            'groups',
            'priority',
            'readOnlyRootFilesystem',
            'requiredDropCapabilities',
            'runAsUser',
            'seLinuxContext',
            'supplementalGroups',
            'users',
            'volumes'
        ]
        for key in keys:
            info[key] = self.get(security_context_constraint_mo, key)

        keys = [
            'fsGroup',
            'runAsUser',
            'seLinuxContext',
            'supplementalGroups'
        ]
        for key in keys:
            info[key] = self.get(security_context_constraint_mo, '%s:type' % (key))

        info['allowedCapabilities'] = self.get(security_context_constraint_mo, 'allowedCapabilities', on_error=[], on_none=[])

        return info

    def get_security_context_constraints_info(self, cache_enabled=True):
        if cache_enabled:
            if self.security_context_constraint is not None:
                return self.security_context_constraint

        managed_objects = self.get_security_context_constraint_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.security_context_constraint = []
        for managed_object in managed_objects:
            security_context_constraint_info = {}
            security_context_constraint_info['info'] = self.get_security_context_constraint_info(
                managed_object
            )
            security_context_constraint_info['mo'] = managed_object
            self.security_context_constraint.append(
                security_context_constraint_info
            )

        return self.security_context_constraint

    def match_security_context_constraint(self, security_context_constraint_info, security_context_constraint_filter):
        if security_context_constraint_filter is None or len(security_context_constraint_filter) == 0:
            return True

        for ap_rule in security_context_constraint_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, '%s' % (security_context_constraint_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_security_context_constraint',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_security_context_constraints(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_security_context_constraints = self.get_security_context_constraints_info(cache_enabled=cache_enabled)
        if all_security_context_constraints is None:
            return None

        security_context_constraints = []

        for security_context_constraint_info in all_security_context_constraints:
            if not self.match_security_context_constraint(security_context_constraint_info['info'], object_filter):
                continue

            if return_mo:
                security_context_constraints.append(
                    security_context_constraint_info['mo']
                )
                continue

            security_context_constraints.append(
                security_context_constraint_info['info']
            )

        return security_context_constraints
