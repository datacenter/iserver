class ApplicationProfileApi():
    def __init__(self):
        self.application_profile_mo = None

    def get_application_profile_mo(self):
        if self.application_profile_mo is not None:
            return self.application_profile_mo

        cache = self.get_object_cache(
            'fvAp'
        )
        if cache is not None:
            self.application_profile_mo = cache
            self.log.apic_mo(
                'fvAp',
                self.application_profile_mo
            )
            return self.application_profile_mo

        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_class(
            'fvAp',
            query=query
        )
        if managed_objects is None:
            return None

        self.application_profile_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvAp']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'fvAp',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'fvAp',
                managed_object,
                'faultCounts'
            )
            self.application_profile_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvAp',
            self.application_profile_mo
        )

        self.set_object_cache(
            'fvAp',
            self.application_profile_mo
        )

        return self.application_profile_mo
