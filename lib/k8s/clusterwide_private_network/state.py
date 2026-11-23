import yaml
from lib import filter_helper


class K8sClusterwidePrivateNetworkState():
    def __init__(self):
        self.pnet_webhook_name = 'isovalent'
        self.pnet_webhook_service_name = 'cilium-private-networks-webhook'

    def is_clusterwide_private_network_webhook(self, cache_enabled=True):
        return self.is_mutating_webhook(self.pnet_webhook_name, cache_enabled=cache_enabled)

    def get_clusterwide_private_network_state_dict(self):
        state = {}
        state['enabled'] = False
        state['multus'] = dict(enabled=False)
        state['webhook'] = {}
        state['webhook']['enabled'] =False
        state['webhook']['name'] = self.pnet_webhook_name
        state['webhook']['service_name'] = '%s/%s' % (self.cilium_namespace, self.pnet_webhook_service_name)
        state['webhook']['service_found'] = False
        state['webhook']['service_endpoints'] = []
        state['tls'] = dict(enabled=False)
        state['localaccess'] = dict(enabled=False)
        state['evpn'] = dict(enabled=False)
        return state

    def set_clusterwide_private_network_state_output_flags(self, state):
        state['__Output'] = {}
        state = filter_helper.add_tick(
            state,
            'enabled',
            True,
            'enabledTick'
        )
        state = filter_helper.add_tick(
            state,
            'multus:enabled',
            True,
            'multusEnabledTick'
        )
        state = filter_helper.add_tick(
            state,
            'webhook:enabled',
            True,
            'webhookEnabledTick'
        )
        state = filter_helper.add_tick(
            state,
            'tls:enabled',
            True,
            'tlsEnabledTick'
        )
        state = filter_helper.add_tick(
            state,
            'localaccess:enabled',
            True,
            'localaccessEnabledTick'
        )
        state = filter_helper.add_tick(
            state,
            'evpn:enabled',
            True,
            'evpnEnabledTick'
        )
        return state

    # iserver-orig replaced with cd-backend
    # def get_clusterwide_private_network_state(self, cache_enabled=True):
    #     state = {}
    #     state['__Output'] = {}
    #     state['enabled'] = False
    #     state['mode'] = None
    #     state['enabledTick'] = '\u2717'
    #     state['__Output']['enabledTick'] = 'Red'
    #     state['multus'] = dict(enabled=False)
    #     state = filter_helper.add_tick(
    #         state,
    #         'multus:enabled',
    #         True,
    #         'multusEnabledTick'
    #     )
    #     state['webhook'] = dict(enabled=False)
    #     state = filter_helper.add_tick(
    #         state,
    #         'webhook:enabled',
    #         True,
    #         'webhookEnabledTick'
    #     )
        
    #     cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
    #     if cilium_config_mo is None:
    #         return state

    #     state['enabled'] = self.is_cilium_private_network_enabled(cache_enabled=True)
    #     if not state['enabled']:
    #         return state

    #     state['mode'] = self.get(cilium_config_mo, 'spec:enterprise:privateNetworks:mode')
    #     state['enabledTick'] = '\u2713'
    #     state['__Output']['enabledTick'] = 'Green'

    #     state['configuration'] = self.get_cilium_private_network_configuration(cache_enabled=True)

    #     state['multus'] = {}
    #     state['multus']['enabled'] = self.is_cilium_private_network_multus_enabled(cache_enabled=True)
    #     state = filter_helper.add_tick(
    #         state,
    #         'multus:enabled',
    #         True,
    #         'multusEnabledTick'
    #     )

    #     state['webhook'] = {}
    #     state['webhook']['enabled'] = self.is_cilium_private_network_webhook_enabled(cache_enabled=True)
    #     state = filter_helper.add_tick(
    #         state,
    #         'webhook:enabled',
    #         True,
    #         'webhookEnabledTick'
    #     )

    #     state['webhook']['name'] = self.pnet_webhook_name
    #     state['webhook']['configured'] = self.is_clusterwide_private_network_webhook(cache_enabled=cache_enabled)

    #     service = self.get_service(
    #         self.cilium_namespace, 
    #         self.pnet_webhook_service_name, 
    #         endpoint_info=True,
    #         cache_enabled=cache_enabled
    #     )

    #     state['webhook']['service_name'] = '%s/%s' % (self.cilium_namespace, self.pnet_webhook_service_name)
    #     state['webhook']['service_found'] = False
    #     state['webhook']['service_endpoints'] = []
    #     if service is not None:
    #         state['webhook']['service_found'] = True
    #         state['webhook']['service_endpoints'] = service['addressT']

    #     return state

    def get_clusterwide_private_network_state(self, cache_enabled=True):
        state = self.get_clusterwide_private_network_state_dict()

        cilium_config_mo = self.get_cilium_config(cache_enabled=cache_enabled, return_mo=True)
        if cilium_config_mo is None:
            return state

        state['configuration'] = self.get_cilium_private_network_configuration(cache_enabled=True)
        state['yconfiguration'] = yaml.safe_dump(state['configuration'])
        state['enabled'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:enabled', on_error=False, on_none=False)
        state['multus']['enabled'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:networkAttachmentDefinitions:enabled', on_error=False, on_none=False)
        state['tls']['enabled'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:api:tls:enabled', on_error=False, on_none=False)
        state['evpn']['enabled'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:bgpControlPlane:enabled', on_error=False, on_none=False)
        state['evpn']['enabled'] = state['evpn']['enabled'] and filter_helper.get(cilium_config_mo, 'spec:enterprise:bgpControlPlane:routeImport:enabled', on_error=False, on_none=False)
        state['evpn']['enabled'] = state['evpn']['enabled'] and filter_helper.get(cilium_config_mo, 'spec:enterprise:evpn:enabled', on_error=False, on_none=False)

        mode = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:mode', on_error=None, on_none=None)
        if mode == 'local-access':
            state['localaccess']['enabled'] = True

        state['webhook']['enabled'] = filter_helper.get(cilium_config_mo, 'spec:enterprise:privateNetworks:webhook:enabled', on_error=False, on_none=False)
        if state['webhook']['enabled']:
            state['webhook']['configured'] = self.is_mutating_webhook(self.pnet_webhook_name, cache_enabled=cache_enabled)

            service = self.get_service(
                self.cilium_namespace, 
                self.pnet_webhook_service_name, 
                endpoint_info=True,
                cache_enabled=cache_enabled
            )

            if service is not None:
                state['webhook']['service_found'] = True
                state['webhook']['service_endpoints'] = service['addressT']

        return self.set_clusterwide_private_network_state_output_flags(state)

    def get_clusterwide_private_network_crds(self, cache_enabled=True):
        crd = {}
        crd['kind'] = {}
        crd['total'] = {}
        crd['valid'] = {}

        crd['kind']['ClusterwidePrivateNetwork'] = self.get_clusterwide_private_networks(cache_enabled=cache_enabled)
        crd['total']['ClusterwidePrivateNetwork'] = '---'
        crd['valid']['ClusterwidePrivateNetwork'] = False
        if crd['kind']['ClusterwidePrivateNetwork'] is not None:
            crd['total']['ClusterwidePrivateNetwork'] = len(crd['kind']['ClusterwidePrivateNetwork'])
            crd['valid']['ClusterwidePrivateNetwork'] = True

        crd['kind']['PrivateNetworkEndpointSlice'] = self.get_private_network_endpoint_slices(cache_enabled=cache_enabled)
        crd['total']['PrivateNetworkEndpointSlice'] = '---'
        crd['valid']['PrivateNetworkEndpointSlice'] = False
        if crd['kind']['PrivateNetworkEndpointSlice'] is not None:
            crd['total']['PrivateNetworkEndpointSlice'] = len(crd['kind']['PrivateNetworkEndpointSlice'])
            crd['valid']['PrivateNetworkEndpointSlice'] = True

        crd['kind']['PrivateNetworkExternalEndpoint'] = self.get_private_network_external_endpoints(cache_enabled=cache_enabled)
        crd['total']['PrivateNetworkExternalEndpoint'] = '---'
        crd['valid']['PrivateNetworkExternalEndpoint'] = False
        if crd['kind']['PrivateNetworkExternalEndpoint'] is not None:
            crd['total']['PrivateNetworkExternalEndpoint'] = len(crd['kind']['PrivateNetworkExternalEndpoint'])
            crd['valid']['PrivateNetworkExternalEndpoint'] = True

        crd['kind']['PrivateNetworkNodeAttachment'] = self.get_private_network_node_attachments(cache_enabled=cache_enabled)
        crd['total']['PrivateNetworkNodeAttachment'] = '---'
        crd['valid']['PrivateNetworkNodeAttachment'] = False
        if crd['kind']['PrivateNetworkNodeAttachment'] is not None:
            crd['total']['PrivateNetworkNodeAttachment'] = len(crd['kind']['PrivateNetworkNodeAttachment'])
            crd['valid']['PrivateNetworkExternalEndpoint'] = True
            for item in response['crd']['kind']['PrivateNetworkNodeAttachment']:
                if not item['ebpf']['valid']:
                    response['crd']['valid']['PrivateNetworkNodeAttachment'] = False
        
        return crd