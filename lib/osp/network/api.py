import time
import json
import traceback


class OspNetworkApi():
    def __init__(self):
        self.network_mo = None

    def get_network_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.network_mo is not None:
                return self.network_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_network_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.network_mo = api_handler.list_networks()['networks']
            self.log.osp(
                'get',
                'networks',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_network_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'networks',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.network_mo

    def create_external_network_mo(self, network_name, physical_network='phys_ext'):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_tenant_network_mo',
                'No api handler'
            )
            return None

        body = {}
        body['network'] = {}
        body['network']['name'] = network_name
        body['network']['admin_state_up'] = True
        body['network']['provider:physical_network'] = physical_network
        body['network']['provider:network_type'] = 'flat'
        body['network']['router:external'] = True

        self.log.debug(
            'create_external_network_mo',
            json.dumps(body, indent=4)
        )

        try:
            network = api_handler.create_network(body=body)
            network_id = network['network']['id']

        except BaseException:
            self.log.error(
                'create_provider_network_mo',
                traceback.format_exc()
            )
            return None

        return network_id

    def create_provider_network_mo(self, tenant_id, network_name, physical_network, provider_network_type, provider_segmentation_id):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_tenant_network_mo',
                'No api handler'
            )
            return None

        body = {}
        body['network'] = {}
        body['network']['name'] = network_name
        body['network']['admin_state_up'] = True
        body['network']['provider:physical_network'] = physical_network
        body['network']['provider:network_type'] = provider_network_type
        body['network']['provider:segmentation_id'] = provider_segmentation_id
        if tenant_id is not None:
            body['network']['tenant_id'] = tenant_id

        self.log.debug(
            'create_provider_network_mo',
            json.dumps(body, indent=4)
        )

        try:
            network = api_handler.create_network(body=body)
            network_id = network['network']['id']

        except BaseException:
            self.log.error(
                'create_provider_network_mo',
                traceback.format_exc()
            )
            return None

        return network_id

    def create_tenant_network_mo(self, tenant_id, network_name):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_tenant_network_mo',
                'No api handler'
            )
            return None

        body = {}
        body['network'] = {}
        body['network']['name'] = network_name
        body['network']['admin_state_up'] = True
        if tenant_id is not None:
            body['network']['tenant_id'] = tenant_id

        self.log.debug(
            'create_tenant_network_mo',
            json.dumps(body, indent=4)
        )

        try:
            network = api_handler.create_network(body=body)
            network_id = network['network']['id']

        except BaseException:
            self.log.error(
                'create_tenant_network_mo',
                traceback.format_exc()
            )
            return None

        return network_id

    def delete_network_mo(self, network_id):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'delete_network_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.delete_network(network_id)

        except BaseException:
            self.log.error(
                'delete_network_mo',
                traceback.format_exc()
            )
            return False

        return True
