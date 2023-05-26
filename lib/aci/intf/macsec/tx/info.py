class InterfaceMacSecTxInfo():
    def __init__(self):
        pass

    def get_interface_macsec_tx_info(self, managed_object):
        keys = [
            'dn',
            'encryptedOctets',
            'encryptedPkts',
            'protectedOctets',
            'protectedPkts'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_macsec_tx(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_macsec_tx_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_macsec_tx_info(managed_object)
