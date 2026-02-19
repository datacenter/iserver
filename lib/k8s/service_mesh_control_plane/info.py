from lib import filter_helper


class K8sServiceMeshControlPlaneInfo():
    def __init__(self):
        self.service_mesh_control_plane = None

    def get_service_mesh_control_plane_info(self, managed_object):
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
        
        info['components'] = []
        info['componentsT'] = []
        components_mo = self.get(managed_object, 'status:readiness:components:ready', on_error=[], on_none=[])
        for component_mo in components_mo:
            info['componentsT'].append('\u2713 %s' % (component_mo))
            info['components'].append(component_mo)

        components_mo = self.get(managed_object, 'status:readiness:components:unready', on_error=[], on_none=[])
        for component_mo in components_mo:
            info['componentsT'].append('\u2717 %s' % (component_mo))

        components_mo = self.get(managed_object, 'status:readiness:components:pending', on_error=[], on_none=[])
        for component_mo in components_mo:
            info['componentsT'].append('? %s' % (component_mo))

        info['version'] = self.get(managed_object, 'status:operatorVersion')

        info['disabledT'] = []

        info['istio-ingress-gateway'] = self.get(
            managed_object, 'status:appliedValues:istio:gateways:istio-ingressgateway'
        )
        if info['istio-ingress-gateway'] is None or not info['istio-ingress-gateway']['enabled']:
            info['disabledT'].append(
                'istio-ingress'
            )
        else:
            if 'istio-ingress' not in info['components']:
                info['components'].append('istio-ingress')
                info['componentsT'].append('\u2713 istio-ingress')

        info['istio-egress-gateway'] = self.get(
            managed_object, 'status:appliedValues:istio:gateways:istio-egressgateway'
        )
        if info['istio-egress-gateway'] is None or not info['istio-egress-gateway']['enabled']:
            info['disabledT'].append(
                'istio-egress'
            )
        else:
            if 'istio-egress' not in info['components']:
                info['components'].append('istio-egress')
                info['componentsT'].append('\u2713 istio-egress')

        info['api-gateway'] = self.get(
            managed_object, 'status:appliedValues:istio:gatewayAPI'
        )
        if info['api-gateway'] is None or not info['api-gateway']['enabled']:
            info['disabledT'].append(
                'api-gateway'
            )
        else:
            if 'api-gateway' not in info['components']:
                info['components'].append('api-gateway')
                info['componentsT'].append('\u2713 api-gateway')

        info['grafana'] = self.get(
            managed_object, 'status:appliedValues:istio:grafana'
        )
        if info['grafana'] is None or not info['grafana']['enabled']:
            info['disabledT'].append(
                'grafana'
            )
        else:
            if 'grafana' not in info['components']:
                info['components'].append('grafana')
                info['componentsT'].append('\u2713 grafana')

        info['istio-cni'] = self.get(
            managed_object, 'status:appliedValues:istio:istio_cni'
        )
        if info['istio-cni'] is None or not info['istio-cni']['enabled']:
            info['disabledT'].append(
                'istio-cni'
            )
        else:
            if 'istio-cni' not in info['components']:
                info['components'].append('istio-cni')
                info['componentsT'].append('\u2713 istio-cni')

        info['kiali'] = self.get(
            managed_object, 'status:appliedValues:istio:kiali'
        )
        if info['kiali'] is None or not info['kiali']['enabled']:
            info['disabledT'].append(
                'kiali'
            )
        else:
            if 'kiali' not in info['components']:
                info['components'].append('kiali')
                info['componentsT'].append('\u2713 kiali')

        info['prometheus'] = self.get(
            managed_object, 'status:appliedValues:istio:prometheus'
        )
        if info['prometheus'] is None or not info['prometheus']['enabled']:
            info['disabledT'].append(
                'prometheus'
            )
        else:
            if 'prometheus' not in info['components']:
                info['components'].append('prometheus')
                info['componentsT'].append('\u2713 prometheus')

        info['telemetry'] = self.get(
            managed_object, 'status:appliedValues:istio:telemetry'
        )
        if info['telemetry'] is None or not info['telemetry']['enabled']:
            info['disabledT'].append(
                'telemetry'
            )
        else:
            if 'telemetry' not in info['components']:
                info['components'].append('telemetry')
                info['componentsT'].append('\u2713 telemetry')

        info['tracing'] = self.get(
            managed_object, 'status:appliedValues:istio:tracing'
        )
        if info['tracing'] is None or not info['tracing']['enabled']:
            info['disabledT'].append(
                'tracing'
            )
        else:
            if 'tracing' not in info['components']:
                info['components'].append('tracing')
                info['componentsT'].append('\u2713 tracing')

        return info

    def add_service_mesh_control_plane_info(self, service_mesh_control_plane_info, deployments, services, members, member_rolls):
        service_mesh_control_plane_info['info']['deployment'] = []
        service_mesh_control_plane_info['info']['deploymentT'] = []

        if service_mesh_control_plane_info['info']['istio-ingress-gateway'] is not None:
            service_mesh_control_plane_info['info']['istio-ingress-gateway']['deployment'] = None
            service_mesh_control_plane_info['info']['istio-ingress-gateway']['service'] = None

        if service_mesh_control_plane_info['info']['istio-egress-gateway'] is not None:
            service_mesh_control_plane_info['info']['istio-egress-gateway']['deployment'] = None
            service_mesh_control_plane_info['info']['istio-egress-gateway']['service'] = None

        if deployments is not None:
            for deployment in deployments:
                if deployment['namespace'] != service_mesh_control_plane_info['info']['namespace']:
                    continue

                if service_mesh_control_plane_info['info']['istio-ingress-gateway'] is not None:
                    if deployment['name'] == service_mesh_control_plane_info['info']['istio-ingress-gateway']['name']:
                        service_mesh_control_plane_info['info']['istio-ingress-gateway']['deployment'] = deployment

                if service_mesh_control_plane_info['info']['istio-egress-gateway'] is not None:
                    if deployment['name'] == service_mesh_control_plane_info['info']['istio-egress-gateway']['name']:
                        service_mesh_control_plane_info['info']['istio-egress-gateway']['deployment'] = deployment

                if 'app.kubernetes.io/name' in deployment['label'] and deployment['label']['app.kubernetes.io/name'] == service_mesh_control_plane_info['info']['name']:
                    service_mesh_control_plane_info['info']['deployment'].append(
                        deployment['name']
                    )

                    service_mesh_control_plane_info['info']['deploymentT'].append(
                        '%s %s' % (
                            deployment['readyTick'],
                            deployment['name']
                        )
                    )

        if services is not None:
            for service in services:
                if service_mesh_control_plane_info['info']['istio-ingress-gateway'] is not None:
                    if service['name'] == service_mesh_control_plane_info['info']['istio-ingress-gateway']['name']:
                        service_mesh_control_plane_info['info']['istio-ingress-gateway']['service'] = service

                if service_mesh_control_plane_info['info']['istio-egress-gateway'] is not None:
                    if service['name'] == service_mesh_control_plane_info['info']['istio-egress-gateway']['name']:
                        service_mesh_control_plane_info['info']['istio-egress-gateway']['service'] = service

        service_mesh_control_plane_info['info']['members'] = []
        service_mesh_control_plane_info['info']['membersT'] = []
        members_count = 0
        member_ready = 0

        if members is not None:
            for member in members:
                if member['cp_namespace'] != service_mesh_control_plane_info['info']['namespace']:
                    continue

                if member['cp_name'] != service_mesh_control_plane_info['info']['name']:
                    continue

                service_mesh_control_plane_info['info']['members'].append(
                    member['namespace_name']
                )
                members_count += 1

                if member['ready']:
                    member_ready += 1
                    service_mesh_control_plane_info['info']['membersT'].append(
                        '\u2713 %s' % (member['namespace_name'])
                    )
                else:
                    service_mesh_control_plane_info['info']['membersT'].append(
                        '\u2717 %s' % (member['namespace_name'])
                    )
                    
        service_mesh_control_plane_info['info']['members_summary'] = '%s/%s' % (
            member_ready,
            members_count
        )

        if member_rolls is not None:
            for member in member_rolls:
                if member['cp_namespace'] != service_mesh_control_plane_info['info']['namespace']:
                    continue

                if member['cp_name'] != service_mesh_control_plane_info['info']['name']:
                    continue

                members_mo = self.get(member, 'status:pendingMembers', on_error=[], on_none=[])
                for member_mo in members_mo:
                    if member_mo not in service_mesh_control_plane_info['info']['members']:
                        service_mesh_control_plane_info['info']['members'].append(member_mo)
                        service_mesh_control_plane_info['info']['membersT'].append('? %s' % (member_mo))

                members_mo = self.get(member, 'status:terminatingMembers', on_error=[], on_none=[])
                for member_mo in members_mo:
                    if member_mo not in service_mesh_control_plane_info['info']['members']:
                        service_mesh_control_plane_info['info']['members'].append(member_mo)
                        service_mesh_control_plane_info['info']['membersT'].append('\u2717 %s' % (member_mo))

        return service_mesh_control_plane_info
    
    def get_service_mesh_control_planes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service_mesh_control_plane is not None:
                return self.service_mesh_control_plane

        managed_objects = self.get_service_mesh_control_plane_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service_mesh_control_plane = []
        for managed_object in managed_objects:
            service_mesh_control_plane_info = {}
            service_mesh_control_plane_info['info'] = self.get_service_mesh_control_plane_info(
                managed_object
            )
            service_mesh_control_plane_info['mo'] = managed_object
            self.service_mesh_control_plane.append(
                service_mesh_control_plane_info
            )

        return self.service_mesh_control_plane

    def match_service_mesh_control_plane(self, service_mesh_control_plane_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_control_plane_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, service_mesh_control_plane_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_service_mesh_control_plane',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_mesh_control_planes(self, object_filter=None, deployment_info=False, member_info=False, service_info=False, return_mo=False, cache_enabled=True):
        all_service_mesh_control_planes = self.get_service_mesh_control_planes_info(cache_enabled=cache_enabled)
        if all_service_mesh_control_planes is None:
            return None

        service_mesh_control_planes = []

        deployments = None
        if deployment_info:
            deployments = self.get_deployments(cache_enabled=cache_enabled)

        services = None
        if service_info:
            services = self.get_services(
                endpoint_info=True,
                cache_enabled=cache_enabled
            )

        members = None
        member_rolls = None
        if member_info:
            members = self.get_service_mesh_members(cache_enabled=cache_enabled)
            member_rolls = self.get_service_mesh_members(cache_enabled=cache_enabled)

        for service_mesh_control_plane_info in all_service_mesh_control_planes:
            if deployment_info:
                service_mesh_control_plane_info = self.add_service_mesh_control_plane_info(
                    service_mesh_control_plane_info, 
                    deployments,
                    services,
                    members,
                    member_rolls
                )

            if not self.match_service_mesh_control_plane(service_mesh_control_plane_info['info'], object_filter):
                continue

            if return_mo:
                service_mesh_control_planes.append(
                    service_mesh_control_plane_info['mo']
                )
                continue

            service_mesh_control_planes.append(
                service_mesh_control_plane_info['info']
            )

        return service_mesh_control_planes

    def is_service_mesh_control_plane(self, namespace, name, cache_enabled=True):
        if self.get_service_mesh_control_plane(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_service_mesh_control_plane(self, cache_enabled=True):
        policies = self.get_service_mesh_control_planes(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_service_mesh_control_plane(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        service_mesh_control_planes = self.get_service_mesh_control_planes(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if service_mesh_control_planes is None:
            return None

        if len(service_mesh_control_planes) == 1:
            return service_mesh_control_planes[0]

        return None
