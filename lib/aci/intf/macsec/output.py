class InterfaceMacSecOutput():
    def __init__(self):
        pass

    def print_interfaces_macsec_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface MacSec - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'health',
            'faults',
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
            'Health',
            'Faults',
            'Interface',
            'Admin',
            'Oper',
            'Reason',
            'Session',
            'Peers',
            'Cepher Suite',
            'Confid Offset',
            'Key Chain',
            'Ker Server Prio',
            'Replay Window'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_macsec_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface MacSec - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface MacSec - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interface_macsec_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface MacSec - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_macsec_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface MacSec - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface MacSec - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_macsec_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface MacSec - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface MacSec - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interface_macsec_verbose(self, interface):
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
