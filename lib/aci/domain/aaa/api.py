class DomainAaaApi():
    def __init__(self):
        self.mo_domain_aaa = None

    def initialize_domain_aaa(self):
        if self.mo_domain_aaa is not None:
            return True

        managed_objects = self.get_class(
            'aaaDomain',
            node_class=True
        )

        if managed_objects is None:
            return False

        self.mo_domain_aaa = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaDomain']['attributes']
            self.mo_domain_aaa.append(
                attributes
            )

        self.log.apic_mo(
            'aaaDomain',
            self.mo_domain_aaa
        )

        return True
