class FabricPathApi():
    def __init__(self):
        self.fabric_path_mo = None

    def get_fabric_path_mo(self):
        if self.fabric_path_mo is not None:
            return self.fabric_path_mo

        managed_objects = self.get_class(
            'fabricPathEp'
        )
        if managed_objects is None:
            return None

        self.fabric_path_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fabricPathEp']['attributes']
            self.fabric_path_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fabricPathEp',
            self.fabric_path_mo
        )

        return self.fabric_path_mo
