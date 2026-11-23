class InterfaceMacSecCaStatsInfo():
    def __init__(self):
        pass

    def get_interface_macsec_castats_info(self, managed_object):
        keys = [
            'dn',
            'ickDervFail',
            'invalidPeerCpbl',
            'kRekeys',
            'kekDervFail',
            'mkpduRx',
            'mkpduRxDistSak',
            'mkpduTx',
            'mkpduTxDistSak',
            'sakRespRx',
            'saksGen',
            'saksRekeyed',
            'saksRx'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_macsec_castats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_macsec_castats_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_macsec_castats_info(managed_object)
