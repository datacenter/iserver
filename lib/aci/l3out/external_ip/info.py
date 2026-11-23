from lib import ip_helper


class L3OutExternalIpInfo():
    def __init__(self):
        self.l3out_external_ip = None

    def init_l3out_external_ip(self):
        self.l3out_external_ip = None

    def get_l3out_external_ip_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['address'] = managed_object['addr'].split('/')[0]
        info['prefix'] = int(managed_object['addr'].split('/')[1])
        info['subnet'] = ip_helper.prefix_to_netmask(info['prefix'])
        info['cidr'] = managed_object['addr']
        info['dn'] = managed_object['dn']

        try:
            info['tenant'] = info['dn'].split('/')[1].split('tn-')[1]
        except BaseException:
            info['tenant'] = None

        try:
            info['l3out'] = info['dn'].split('/')[2].split('out-')[1]
        except BaseException:
            info['l3out'] = None

        try:
            info['logical_node_profile'] = info['dn'].split('/')[3].split('lnodep-')[1]
        except BaseException:
            info['logical_node_profile'] = None

        try:
            info['logical_interface_profile'] = info['dn'].split('/')[4].split('lifp-')[1]
        except BaseException:
            info['logical_interface_profile'] = None

        return info

    def get_l3out_external_ip_infos(self, cache_enabled=True):
        if self.l3out_external_ip is not None:
            return self.l3out_external_ip

        managed_objects = self.get_l3out_external_ip_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.l3out_external_ip = []
        for managed_object in managed_objects:
            self.l3out_external_ip.append(
                self.get_l3out_external_ip_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'l3extIp.info',
            self.l3out_external_ip
        )

        return self.l3out_external_ip
    
    def l3out_external_ips(self, cache_enabled=True):
        if not cache_enabled:
            self.init_l3out_external_ip()
            self.init_l3out_external_ip_mo()

        ips = self.get_l3out_external_ip_infos(cache_enabled=cache_enabled)
        return ips
