class InterfaceMacSecTxApi():
    def __init__(self):
        self.interface_macsec_tx_mo = {}

    def get_interface_macsec_tx_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id
        )
        if key in self.interface_macsec_tx_mo:
            return self.interface_macsec_tx_mo[key]

        cache = self.get_object_cache(
            'dbgIfMacsectx',
            object_selector=key
        )
        if cache is not None:
            self.interface_macsec_tx_mo[key] = cache
            self.log.apic_mo(
                'dbgIfMacsectx.%s' % (key),
                self.interface_macsec_tx_mo[key]
            )
            return self.interface_macsec_tx_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/phys-[%s]/dbgIfMacsectx' % (
            pod_id,
            node_id,
            interface_id
        )

        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_macsec_tx_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_macsec_tx_mo',
                'Unexpected object count'
            )
            return None

        self.interface_macsec_tx_mo[key] = managed_objects['imdata'][0]['rmonIfMacsectx']['attributes']

        self.log.apic_mo(
            'dbgIfMacsectx.%s' % (key),
            self.interface_macsec_tx_mo[key]
        )

        self.set_object_cache(
            'dbgIfMacsectx',
            self.interface_macsec_tx_mo[key],
            object_selector=key
        )

        return self.interface_macsec_tx_mo[key]
