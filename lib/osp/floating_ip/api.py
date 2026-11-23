import time
import json
import traceback


class OspFloatingIpApi():
    def __init__(self):
        self.floating_ip_mo = None

    def get_floating_ip_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.floating_ip_mo is not None:
                return self.floating_ip_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_floating_ip_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.floating_ip_mo = api_handler.list_floatingips()['floatingips']
            self.log.osp(
                'get',
                'floating_ips',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_floating_ip_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'floating_ips',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.floating_ip_mo

    def create_floating_ip_mo(self, tenant_id, port_id, floating_network_id, floating_subnet_id, floating_ip_address=None):
        try:
            api_handler = self.get_api_neutron(cache_enabled=False)
            if api_handler is None:
                self.log.error(
                    'create_floating_ip_mo',
                    'No api handler'
                )
                return None

            body = {}
            body['floatingip'] = {}
            body['floatingip']['tenant_id'] = tenant_id
            body['floatingip']['port_id'] = port_id
            body['floatingip']['floating_network_id'] = floating_network_id
            body['floatingip']['subnet_id'] = floating_subnet_id
            if floating_ip_address is not None:
                body['floatingip']['floating_ip_address'] = floating_ip_address

            self.log.debug(
                'create_floating_ip_mo',
                'Create floating IP: %s' % (json.dumps(body, indent=4))
            )
            ret = api_handler.create_floatingip(body=body)
            floating_ip_id = ret['floatingip']['id']

        except BaseException:
            self.log.error(
                'create_floating_ip_mo',
                'Neutron API exception'
            )
            self.log.error(
                'create_floating_ip_mo',
                traceback.format_exc()
            )
            return None

        return floating_ip_id

    def delete_floating_ip_mo(self, floating_ip_id):
        try:
            api_handler = self.get_api_neutron(cache_enabled=False)
            if api_handler is None:
                self.log.error(
                    'delete_floating_ip_mo',
                    'No api handler'
                )
                return False

            self.log.debug(
                'create_floating_ip_mo',
                'Delete floating IP: %s' % (floating_ip_id)
            )

            api_handler.delete_floatingip(floating_ip_id)

        except BaseException:
            self.log.error(
                'delete_floating_ip_mo',
                'Neutron API exception'
            )
            self.log.error(
                'delete_floating_ip_mo',
                traceback.format_exc()
            )
            return False

        return True
