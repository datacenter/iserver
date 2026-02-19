class ConfigurationInterfaceApi():
    def __init__(self):
        self.configuration_interface_mo = None
        self.configuration_interface_types = ['infraPortSummary', 'fabricPortSummary', 'infraBundleSummary']

    def init_configuration_interface_mo(self):
        self.configuration_interface_mo = None

    def get_configuration_interface_mo(self, cache_enabled=True):
        if self.configuration_interface_mo is not None:
            return self.configuration_interface_mo

        if cache_enabled:
            cache = self.get_object_cache(
                'configurationInterface'
            )
            if cache is not None:
                self.configuration_interface_mo = cache
                self.log.apic_mo(
                    'configurationInterface',
                    self.configuration_interface_mo
                )
                return self.configuration_interface_mo

        query = 'target-subtree-class=%s&query-target=subtree' % (','.join(self.configuration_interface_types))
        managed_objects = self.get_class(
            'polUni',
            node_class=True,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_configuration_interface_mo',
                'API failed'
            )
            return None

        self.configuration_interface_mo = {}
        for key in self.configuration_interface_types:
            self.configuration_interface_mo[key] = []

        for managed_object in managed_objects['imdata']:
            found = False
            for key in self.configuration_interface_types:
                if key in managed_object:
                    self.configuration_interface_mo[key].append(
                        managed_object[key]['attributes']
                    )
                    found = True

            if not found:
                self.log.error(
                    'get_configuration_interface_mo',
                    'Unsupported mo: %s' % (managed_object)
                )

        self.set_object_cache(
            'configurationInterface',
            self.configuration_interface_mo
        )

        return self.configuration_interface_mo
