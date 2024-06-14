class InterfacePolicyProfileApi():
    def __init__(self):
        self.interface_policy_profile_mo = {}

    def get_interface_policy_profile_mo(self, profile_name):
        key = profile_name
        if key in self.interface_policy_profile_mo:
            return self.interface_policy_profile_mo[key]

        cache = self.get_object_cache(
            'accportprof',
            object_selector=key
        )
        if cache is not None:
            self.interface_policy_profile_mo[key] = cache
            self.log.apic_mo(
                'accportprof.%s' % (key),
                self.interface_policy_profile_mo[key]
            )
            return self.interface_policy_profile_mo[key]

        # https://<apic>/api/node/mo/uni/infra/accportprof-SPN_IntProf.json?query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk&_dc=1684139157872
        distinguished_name = 'uni/infra/accportprof-%s' % (
            profile_name
        )

        children = [
            'infraHPortS',
            'infraRsAccBaseGrp',
            'infraPortBlk',
            'infraSubPortBlk'
        ]
        query = 'query-target=subtree&target-subtree-class=%s' % (','.join(children))

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_policy_profile_mo',
                'API failed'
            )
            return None

        self.interface_policy_profile_mo[key] = {}
        self.interface_policy_profile_mo[key]['profile'] = profile_name
        self.interface_policy_profile_mo[key]['infraHPortS'] = []
        self.interface_policy_profile_mo[key]['infraRsAccBaseGrp'] = []
        self.interface_policy_profile_mo[key]['infraPortBlk'] = []
        self.interface_policy_profile_mo[key]['infraSubPortBlk'] = []

        for managed_object in managed_objects['imdata']:
            if 'infraHPortS' in managed_object:
                self.interface_policy_profile_mo[key]['infraHPortS'].append(
                    managed_object['infraHPortS']['attributes']
                )

            if 'infraRsAccBaseGrp' in managed_object:
                self.interface_policy_profile_mo[key]['infraRsAccBaseGrp'].append(
                    managed_object['infraRsAccBaseGrp']['attributes']
                )

            if 'infraPortBlk' in managed_object:
                self.interface_policy_profile_mo[key]['infraPortBlk'].append(
                    managed_object['infraPortBlk']['attributes']
                )

            if 'infraSubPortBlk' in managed_object:
                self.interface_policy_profile_mo[key]['infraSubPortBlk'].append(
                    managed_object['infraSubPortBlk']['attributes']
                )

        self.log.apic_mo(
            'accportprof.%s' % (key),
            self.interface_policy_profile_mo[key]
        )

        self.set_object_cache(
            'accportprof',
            self.interface_policy_profile_mo[key],
            object_selector=key
        )

        return self.interface_policy_profile_mo[key]
