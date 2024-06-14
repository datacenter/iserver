class InterfaceMacSecStatsInfo():
    def __init__(self):
        pass

    def get_interface_macsec_stats_info(self, managed_object):
        keys = [
            'dn',
            'invalidMkpduRx',
            'macsecRxSaInstallFail',
            'macsecTxSaInstallFail',
            'mkpduEtherMismatch',
            'mkpduNoRxIfDn',
            'mkpduNoTxIfDn',
            'mkpduRxBadPeerMN',
            'mkpduRxCANotFnd',
            'mkpduRxErr',
            'mkpduRxNRPListMN',
            'mkpduRxSucc',
            'mkpduTxFail',
            'mkpduTxPktBldFail',
            'mkpduTxSucc',
            'rxSakANNotInUse',
            'rxSakKNMismatch',
            'rxSakKeyMIMismatch',
            'rxSakKsRxTxNotSet',
            'rxSakRxNotSet',
            'sakDecryptFail',
            'sakEncryptFail',
            'sakGenFail',
            'sakHashKeyGenFail'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_macsec_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_macsec_stats_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_macsec_stats_info(managed_object)
