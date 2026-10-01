from lib import filter_helper


class K8sClusterwidePrivateNetworkState():
    def __init__(self):
        # self.pnet_webhook_name = 'kubevirt-privnet-integration-webhook'
        # self.pnet_webhook_service_name = 'kubevirt-privnet-integration'
        self.pnet_webhook_name = 'cilium-private-networks'
        self.pnet_webhook_service_name = 'cilium-private-networks-webhook'

    def is_clusterwide_private_network_webhook(self, cache_enabled=True):
        return self.is_mutating_webhook(self.pnet_webhook_name, cache_enabled=cache_enabled)
    
    def get_clusterwide_private_network_state(self, cache_enabled=True):
        state = {}
        state['__Output'] = {}
        state['enabled'] = False
        state['mode'] = None
        state['enabledTick'] = '\u2717'
        state['__Output']['enabledTick'] = 'Red'
        state['multus'] = dict(enabled=False)
        state = filter_helper.add_tick(
            state,
            'multus:enabled',
            True,
            'multusEnabledTick'
        )
        state['webhook'] = dict(enabled=False)
        state = filter_helper.add_tick(
            state,
            'webhook:enabled',
            True,
            'webhookEnabledTick'
        )
        
        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return state

        state['enabled'] = self.is_cilium_private_network_enabled(cache_enabled=True)
        if not state['enabled']:
            return state

        state['mode'] = self.get(cilium_config_mo, 'spec:enterprise:privateNetworks:mode')
        state['enabledTick'] = '\u2713'
        state['__Output']['enabledTick'] = 'Green'

        state['configuration'] = self.get_cilium_private_network_configuration(cache_enabled=True)

        state['multus'] = {}
        state['multus']['enabled'] = self.is_cilium_private_network_multus_enabled(cache_enabled=True)
        state = filter_helper.add_tick(
            state,
            'multus:enabled',
            True,
            'multusEnabledTick'
        )

        state['webhook'] = {}
        state['webhook']['enabled'] = self.is_cilium_private_network_webhook_enabled(cache_enabled=True)
        state = filter_helper.add_tick(
            state,
            'webhook:enabled',
            True,
            'webhookEnabledTick'
        )

        state['webhook']['name'] = self.pnet_webhook_name
        state['webhook']['configured'] = self.is_clusterwide_private_network_webhook(cache_enabled=cache_enabled)

        service = self.get_service(
            self.cilium_namespace, 
            self.pnet_webhook_service_name, 
            endpoint_info=True,
            cache_enabled=cache_enabled
        )

        state['webhook']['service_name'] = '%s/%s' % (self.cilium_namespace, self.pnet_webhook_service_name)
        state['webhook']['service_found'] = False
        state['webhook']['service_endpoints'] = []
        if service is not None:
            state['webhook']['service_found'] = True
            state['webhook']['service_endpoints'] = service['addressT']

        return state