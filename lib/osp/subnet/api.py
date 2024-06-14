import time
import json
import traceback

from lib import ip_helper


class OspSubnetApi():
    def __init__(self):
        self.subnet_mo = None

    def get_subnet_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.subnet_mo is not None:
                return self.subnet_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_subnet_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.subnet_mo = api_handler.list_subnets()['subnets']
            self.log.osp(
                'get',
                'subnets',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_subnet_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'subnets',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.subnet_mo

    def create_subnet_mo(self, network_id, cidr, tenant_id=None, subnet_name=None, gateway=None, dns=None, dhcp=True, start_ip=None, end_ip=None):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_subnet_ipv4_mo',
                'No api handler'
            )
            return None

        if not ip_helper.is_valid_ipv4_cidr(cidr):
            self.log.error(
                'create_subnet_mo',
                'IPv4 subnet supported only'
            )
            return None

        subnet_mo = {}
        subnet_mo['cidr'] = cidr
        subnet_mo['ip_version'] = 4
        subnet_mo['network_id'] = network_id
        subnet_mo['enable_dhcp'] = dhcp

        if subnet_name is not None:
            subnet_mo['name'] = subnet_name

        if gateway is not None:
            subnet_mo['gateway_ip'] = gateway

        if dns is not None:
            if isinstance(dns, list):
                subnet_mo['dns_nameservers'] = dns
            if isinstance(dns, str):
                subnet_mo['dns_nameservers'] = [dns]

        if tenant_id is not None:
            subnet_mo['tenant_id'] = tenant_id

        if dhcp:
            if start_ip is not None and end_ip is not None:
                allocation_pool = {}
                allocation_pool['start'] = start_ip
                allocation_pool['end'] = end_ip
                subnet_mo['allocation_pools'] = [allocation_pool]

        body = {}
        body['subnets'] = [subnet_mo]

        self.log.debug(
            'create_subnet_mo',
            json.dumps(body, indent=4)
        )

        try:
            # https://wiki.openstack.org/wiki/Neutron/APIv2-specification
            new_subnets = api_handler.create_subnet(body=body)
            new_subnet = new_subnets['subnets'][0]
        except BaseException:
            self.log.error(
                'create_subnet_mo',
                traceback.format_exc()
            )
            return None

        return new_subnet

    def delete_subnet_mo(self, subnet_id):
        api_handler = self.get_api_neutron(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'delete_subnet_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.delete_subnet(subnet_id)
        except BaseException:
            self.log.error(
                'delete_subnet_mo',
                traceback.format_exc()
            )
            return False

        return True
