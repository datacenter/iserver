from lib import filter_helper


class K8sServiceMeshMemberRollInfo():
    def __init__(self):
        self.service_mesh_member_roll = None

    def get_service_mesh_member_roll_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['status'] = self.get(managed_object, 'status')
        return info
    
    def get_service_mesh_member_rolls_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service_mesh_member_roll is not None:
                return self.service_mesh_member_roll

        managed_objects = self.get_service_mesh_member_roll_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service_mesh_member_roll = []
        for managed_object in managed_objects:
            service_mesh_member_roll_info = {}
            service_mesh_member_roll_info['info'] = self.get_service_mesh_member_roll_info(
                managed_object
            )
            service_mesh_member_roll_info['mo'] = managed_object
            self.service_mesh_member_roll.append(
                service_mesh_member_roll_info
            )

        return self.service_mesh_member_roll

    def match_service_mesh_member_roll(self, service_mesh_member_roll_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_member_roll_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_member_roll_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_service_mesh_member_roll',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_mesh_member_rolls(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_service_mesh_member_rolls = self.get_service_mesh_member_rolls_info(cache_enabled=cache_enabled)
        if all_service_mesh_member_rolls is None:
            return None

        service_mesh_member_rolls = []

        for service_mesh_member_roll_info in all_service_mesh_member_rolls:
            if not self.match_service_mesh_member_roll(service_mesh_member_roll_info['info'], object_filter):
                continue

            if return_mo:
                service_mesh_member_rolls.append(
                    service_mesh_member_roll_info['mo']
                )
                continue

            service_mesh_member_rolls.append(
                service_mesh_member_roll_info['info']
            )

        return service_mesh_member_rolls

    def is_service_mesh_member_roll(self, namespace, name, cache_enabled=True):
        if self.get_service_mesh_member_roll(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_service_mesh_member_roll(self, cache_enabled=True):
        policies = self.get_service_mesh_member_rolls(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_service_mesh_member_roll(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        service_mesh_member_rolls = self.get_service_mesh_member_rolls(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if service_mesh_member_rolls is None:
            return None

        if len(service_mesh_member_rolls) == 1:
            return service_mesh_member_rolls[0]

        return None
