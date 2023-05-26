class InterfaceMacSecOutput():
    def __init__(self):
        pass

    def print_interfaces_macsec(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No macsec interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'operSt',
            'operStQual',
            'sessOperSt',
            'peerCount',
            'cipherSuiteOper',
            'confOffsetOper',
            'keyChain',
            'keySvrPrio',
            'replayWindow'

        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Session State',
            'Peers',
            'Cepher Suite',
            'Confid Offset',
            'Key Chain',
            'Ker Server Prio',
            'Replay Window'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_macsec(self, interface):
        order = [
            'id',
            'adminSt',
            'operSt',
            'operStQual',
            'sessOperSt',
            'peerCount',
            'cipherSuiteOper',
            'confOffsetOper',
            'keyChain',
            'keySvrPrio',
            'replayWindow'

        ]

        headers = [
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Session State',
            'Peers',
            'Cepher Suite',
            'Confid Offset',
            'Key Chain',
            'Ker Server Prio',
            'Replay Window'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface Macsec',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        order = [
            'castats.kRekeys',
            'castats.mkpduRx',
            'castats.mkpduRxDistSak',
            'castats.mkpduTx',
            'castats.mkpduTxDistSak',
            'castats.sakRespRx',
            'castats.saksGen',
            'castats.saksRekeyed',
            'castats.saksRx',
            'stats.rxSakANNotInUse',
            'stats.mkpduNoRxIfDn',
            'stats.mkpduNoTxIfDn',
            'stats.mkpduRxCANotFnd',
            'stats.mkpduRxErr',
            'stats.mkpduRxSucc',
            'stats.mkpduTxPktBldFail',
            'stats.mkpduTxSucc'
        ]

        headers = [
            'Key Rekeys',
            'MKPDUs Validated/Received',
            'MKPDUs Received/Distributed Secure Association Key',
            'MKPDUs Transmitted',
            'MKPDUs Transmitted/Distributed Secure Association Key',
            'Secure Association Key Responses Received',
            'Secure Association Keys Generated',
            'Secure Association Keys Rekeyed',
            'Secure Association Keys Received',
            'MKPDUs Rx Drop Secure Association Key Use',
            'MKPDUs No Rx on Interface Down',
            'MKPDUs No Tx on Interface Down',
            'MKPDUs Rx Connectivity Association not found',
            'MKPDUs Rx Error',
            'MKPDUs Rx Success',
            'MKPDUs Tx Packet Build Fail',
            'MKPDUs Tx Success'
        ]

        self.my_output.dictionary(
            interface,
            title='MKA Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        order = [
            'rx.OkPkts',
            'rx.decryptedOctets',
            'rx.decryptedPkts',
            'rx.delayedPkts',
            'rx.invalidatedOctets',
            'rx.invalidatedPkts',
            'rx.invalidPkts',
            'rx.latePkts',
            'rx.notUsingSAPkts',
            'rx.notValidPkts',
            'rx.uncheckedPkts',
            'rx.unusedSAPkts',
            'tx.encryptedOctets',
            'tx.encryptedPkts',
            'tx.protectedOctets',
            'tx.protectedPkts'
        ]

        headers = [
            'OK Packets',
            'Rx Decrypted Octets',
            'Rx Decrypted Packets',
            'Delayed Packets',
            'Invalidated Octets',
            'Invalidated Packets',
            'Invalid Packets',
            'Late Packets',
            'Not Using SA Packets',
            'Not Valid Packets',
            'Unchecked Packets',
            'Unused SA Packets',
            'Tx Encrypted Octets',
            'Tx Encrypted Packets',
            'Tx Protected Octets',
            'Tx Protected Packets'
        ]

        self.my_output.dictionary(
            interface,
            title='SecY Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
