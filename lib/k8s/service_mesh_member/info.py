from lib import filter_helper


class K8sServiceMeshMemberInfo():
    def __init__(self):
        self.service_mesh_member = None

    def get_service_mesh_member_info(self, managed_object):
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
        
        info['cp_namespace'] = self.get(managed_object, 'spec:controlPlaneRef:namespace')
        info['cp_name'] = self.get(managed_object, 'spec:controlPlaneRef:name')
        info['cp_namespace_nameT'] = []
        if info['cp_namespace'] is not None:
            info['cp_namespace_nameT'].append(
                info['cp_namespace']
            )
        if info['cp_name'] is not None:
            info['cp_namespace_nameT'].append(
                info['cp_name']
            )

        return info

    def add_service_mesh_member_info(self, service_mesh_member_info, deployments):
        service_mesh_member_info['info']['deployment'] = []
        service_mesh_member_info['info']['deploymentT'] = []
        for deployment in deployments:
            if deployment['namespace'] != service_mesh_member_info['info']['namespace']:
                continue

            if 'app.kubernetes.io/name' not in deployment['label']:
                continue

            if deployment['label']['app.kubernetes.io/name'] == service_mesh_member_info['info']['name']:
                service_mesh_member_info['info']['deployment'].append(
                    deployment['name']
                )

                service_mesh_member_info['info']['deploymentT'].append(
                    '%s %s' % (
                        deployment['readyTick'],
                        deployment['name']
                    )
                )

        return service_mesh_member_info
    
    def get_service_mesh_members_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service_mesh_member is not None:
                return self.service_mesh_member

        managed_objects = self.get_service_mesh_member_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service_mesh_member = []
        for managed_object in managed_objects:
            service_mesh_member_info = {}
            service_mesh_member_info['info'] = self.get_service_mesh_member_info(
                managed_object
            )
            service_mesh_member_info['mo'] = managed_object
            self.service_mesh_member.append(
                service_mesh_member_info
            )

        return self.service_mesh_member

    def match_service_mesh_member(self, service_mesh_member_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_member_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_member_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_service_mesh_member',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_mesh_members(self, object_filter=None, deployment_info=False, return_mo=False, cache_enabled=True):
        all_service_mesh_members = self.get_service_mesh_members_info(cache_enabled=cache_enabled)
        if all_service_mesh_members is None:
            return None

        service_mesh_members = []

        deployments = None
        if deployment_info:
            deployments = self.get_deployments(cache_enabled=cache_enabled)

        for service_mesh_member_info in all_service_mesh_members:
            if deployment_info:
                service_mesh_member_info = self.add_service_mesh_member_info(service_mesh_member_info, deployments)

            if not self.match_service_mesh_member(service_mesh_member_info['info'], object_filter):
                continue

            if return_mo:
                service_mesh_members.append(
                    service_mesh_member_info['mo']
                )
                continue

            service_mesh_members.append(
                service_mesh_member_info['info']
            )

        return service_mesh_members

    def is_service_mesh_member(self, namespace, name, cache_enabled=True):
        if self.get_service_mesh_member(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_service_mesh_member(self, cache_enabled=True):
        policies = self.get_service_mesh_members(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_service_mesh_member(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        service_mesh_members = self.get_service_mesh_members(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if service_mesh_members is None:
            return None

        if len(service_mesh_members) == 1:
            return service_mesh_members[0]

        return None
