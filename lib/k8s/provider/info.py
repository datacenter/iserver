from lib import filter_helper


class K8sProviderInfo():
    def __init__(self):
        self.provider = None

    def get_provider_info(self, managed_object):
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

        info['secret_namespace'] = self.get(managed_object, 'spec:secret:namespace')
        info['secret_name'] = self.get(managed_object, 'spec:secret:name')
        info['provider_type'] = self.get(managed_object, 'spec:type')
        info['endpoint'] = self.get(managed_object, 'spec:url')
        info['phase'] = self.get(managed_object, 'status:phase')

        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        return info
    
    def add_provider_info(self, info, storage_maps=None, network_maps=None, plans=None):
        info['used'] = False

        if storage_maps is not None:
            info['storage_map_names'] = []
            info['storage_map_count'] = 0
            info['storage_map_ready'] = 0

            for storage_map in storage_maps:
                if info['name'] in storage_map['provider']:
                    info['used'] = True
                    info['storage_map_names'].append(storage_map['name'])
                    info['storage_map_count'] += 1
                    if storage_map['ready']:
                        info['storage_map_ready'] += 1

            info['storage_map_summary'] = '%s/%s' % (
                info['storage_map_ready'],
                info['storage_map_count']
            )

            if info['storage_map_count'] > 0:
                if info['storage_map_count'] == info['storage_map_ready']:
                    info['__Output']['storage_map_summary'] = 'Green'
                else:
                    info['__Output']['storage_map_summary'] = 'Red'

        if network_maps is not None:
            info['network_map_names'] = []
            info['network_map_count'] = 0
            info['network_map_ready'] = 0

            for network_map in network_maps:
                if info['name'] in network_map['provider']:
                    info['used'] = True
                    info['network_map_names'].append(network_map['name'])
                    info['network_map_count'] += 1
                    if network_map['ready']:
                        info['network_map_ready'] += 1

            info['network_map_summary'] = '%s/%s' % (
                info['network_map_ready'],
                info['network_map_count']
            )

            if info['network_map_count'] > 0:
                if info['network_map_count'] == info['network_map_ready']:
                    info['__Output']['network_map_summary'] = 'Green'
                else:
                    info['__Output']['network_map_summary'] = 'Red'

        if plans is not None:
            info['plan_names'] = []
            info['plan_count'] = 0
            info['plan_ready'] = 0

            for plan in plans:
                if info['name'] == plan['provider_source'] or info['name'] == plan['provider_destination']:
                    info['used'] = True
                    info['plan_names'].append(plan['name'])
                    info['plan_count'] += 1
                    if plan['ready']:
                        info['plan_ready'] += 1

            info['plan_summary'] = '%s/%s' % (
                info['plan_ready'],
                info['plan_count']
            )

            if info['plan_count'] > 0:
                if info['plan_count'] == info['plan_ready']:
                    info['__Output']['plan_summary'] = 'Green'
                else:
                    info['__Output']['plan_summary'] = 'Red'

        return info
    
    def get_providers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.provider is not None:
                return self.provider

        managed_objects = self.get_provider_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.provider = []
        for managed_object in managed_objects:
            provider_info = {}
            provider_info['info'] = self.get_provider_info(
                managed_object
            )
            provider_info['mo'] = managed_object
            self.provider.append(
                provider_info
            )

        return self.provider

    def match_provider(self, provider_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, provider_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (provider_info['namespace'], provider_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_provider',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_providers(self, object_filter=None, storage_info=False, network_info=False, plan_info=False, skip_host=False, return_mo=False, cache_enabled=True):
        all_providers = self.get_providers_info(cache_enabled=cache_enabled)
        if all_providers is None:
            return None

        providers = []

        storage_maps = None
        if storage_info:
            storage_maps = self.get_storage_maps(cache_enabled=cache_enabled)

        network_maps = None
        if network_info:
            network_maps = self.get_network_maps(cache_enabled=cache_enabled)

        plans = None
        if plan_info:
            plans = self.get_plans(cache_enabled=False)

        for provider_info in all_providers:
            provider_info['info'] = self.add_provider_info(
                provider_info['info'],
                storage_maps=storage_maps,
                network_maps=network_maps,
                plans=plans
            )

            if skip_host and provider_info['info']['name'] == 'host':
                continue

            if not self.match_provider(provider_info['info'], object_filter):
                continue

            if return_mo:
                providers.append(
                    provider_info['mo']
                )
                continue

            providers.append(
                provider_info['info']
            )

        return providers

    def is_provider(self, namespace, name, cache_enabled=True):
        if self.get_provider(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_provider(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        providers = self.get_providers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if providers is None:
            return None

        if len(providers) == 1:
            return providers[0]

        return None
