class InterfaceMacSecRxInfo():
    def __init__(self):
        pass

    def get_interface_macsec_rx_info(self, managed_object):
        keys = [
            'OkPkts',
            'decryptedOctets',
            'decryptedPkts',
            'delayedPkts',
            'dn',
            'invalidPkts',
            'invalidatedOctets',
            'invalidatedPkts',
            'latePkts',
            'notUsingSAPkts',
            'notValidPkts',
            'uncheckedPkts',
            'unusedSAPkts'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_macsec_rx(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_macsec_rx_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_macsec_rx_info(managed_object)
