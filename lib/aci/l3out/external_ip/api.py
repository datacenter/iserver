class L3OutExternalIpApi():
    def __init__(self):
        self.l3out_external_ip_mo = None

    def init_l3out_external_ip_mo(self):
        self.l3out_external_ip_mo = None

    def get_l3out_external_ip_mo(self, cache_enabled=True):
        if self.l3out_external_ip_mo is not None:
            return self.l3out_external_ip_mo
        
        if cache_enabled:
            cache = self.get_object_cache(
                'l3extIp'
            )
            if cache is not None:
                self.l3out_external_ip_mo = cache
                self.log.apic_mo(
                    'l3extIp',
                    self.l3out_external_ip_mo
                )
                return self.l3out_external_ip_mo

        managed_objects = self.get_class(
            'l3extIp',
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_l3out_external_ip_mo',
                'API failed'
            )
            return None

        self.l3out_external_ip_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extIp']['attributes']
            self.l3out_external_ip_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extIp',
            self.l3out_external_ip_mo
        )

        self.set_object_cache(
            'l3extIp',
            self.l3out_external_ip_mo
        )

        return self.l3out_external_ip_mo
