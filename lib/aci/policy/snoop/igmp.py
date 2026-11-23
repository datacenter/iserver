class PolicySnoopIgmp():
    def __init__(self):
        self.policy_snoop_igmp_mo = {}

    def get_policy_snoop_igmp_mo(self, tenant, name):
        key = '%s.%s' % (
            tenant,
            name
        )
        if key in self.policy_snoop_igmp_mo:
            return self.policy_snoop_igmp_mo[key]

        cache = self.get_object_cache(
            'igmpSnoopPol',
            object_selector=key
        )
        if cache is not None:
            self.policy_snoop_igmp_mo[key] = cache
            self.log.apic_mo(
                'igmpSnoopPol.%s' % (key),
                self.policy_snoop_igmp_mo[key]
            )
            return self.policy_snoop_igmp_mo[key]

        distinguished_name = 'uni/tn-%s/snPol-%s' % (
            tenant,
            name
        )

        managed_objects = self.get_managed_object(
            distinguished_name
        )
        if managed_objects is None:
            return None

        if managed_objects['totalCount'] != '1':
            return None

        self.policy_snoop_igmp_mo[key] = managed_objects['imdata'][0]['igmpSnoopPol']['attributes']

        self.log.apic_mo(
            'igmpSnoopPol',
            self.policy_snoop_igmp_mo[key]
        )

        self.set_object_cache(
            'igmpSnoopPol',
            self.policy_snoop_igmp_mo[key],
            object_selector=key
        )

        return self.policy_snoop_igmp_mo[key]

    def get_policy_snoop_igmp_info(self, managed_object):
        keys = [
            'adminSt',
            'dn',
            'lastMbrIntvl',
            'name',
            'queryIntvl',
            'rspIntvl',
            'startQueryCnt',
            'startQueryIntvl'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['tenant'] = managed_object['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_policy_snoop_igmp(self, tenant, name):
        managed_object = self.get_policy_snoop_igmp_mo(tenant, name)
        if managed_object is None:
            return None

        return self.get_policy_snoop_igmp_info(managed_object)
