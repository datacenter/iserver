class ApplicationProfileApi():
    def __init__(self):
        self.mo_application_profile = None

    def initialize_application_profile(self):
        if self.mo_application_profile is not None:
            return True

        managed_objects = self.get_class(
            'fvAp'
        )
        if managed_objects is None:
            return False

        self.mo_application_profile = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvAp']['attributes']
            self.mo_application_profile.append(
                attributes
            )

        self.log.apic_mo(
            'fvAp',
            self.mo_application_profile
        )

        return True
