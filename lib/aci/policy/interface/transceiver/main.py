from lib import log_helper
from lib.aci.policy.interface.transceiver.attachment import PolicyInterfaceTransceiverAttachment


class PolicyInterfaceTransceiver(PolicyInterfaceTransceiverAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceTransceiverAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_transceiver = None

    def initialize_policy_interface_transceiver(self):
        if not self.initialize_policy_interface_transceiver_attachment():
            return False

        if self.mo_policy_interface_transceiver is not None:
            return True

        managed_objects = self.get_class(
            'xcvrOpticsIfPol'
        )
        if managed_objects is None:
            return None

        self.log.apic_mo(
            'xcvrOpticsIfPol',
            managed_objects['imdata']
        )

        self.mo_policy_interface_transceiver = []

        for managed_object in managed_objects['imdata']:
            if 'xcvrZRIfPol' in managed_object:
                attributes = managed_object['xcvrZRIfPol']['attributes']
                attributes['type'] = 'xcvrZRIfPol'
                self.mo_policy_interface_transceiver.append(
                    attributes
                )

            if 'xcvrZRPIfPol' in managed_object:
                attributes = managed_object['xcvrZRPIfPol']['attributes']
                attributes['type'] = 'xcvrZRPIfPol'
                self.mo_policy_interface_transceiver.append(
                    attributes
                )

        self.log.apic_mo(
            'xcvrOpticsIfPol.attributes',
            self.mo_policy_interface_transceiver
        )

        return True

    def get_policy_interface_transceiver_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "cdMax": "2400",
        # "cdMin": "-2400",
        # "childAction": "",
        # "dacRate": "1x1",
        # "descr": "",
        # "dn": "uni/infra/zr-default",
        # "dwdmCarrier": "100MHzFrequency",
        # "extMngdBy": "",
        # "fecMode": "cFEC",
        # "frequency100MHz": "1931000",
        # "frequency50GHz": "19310",
        # "ituChannel50GHz": "61",
        # "lcOwn": "local",
        # "modTs": "2022-09-14T19:08:11.182+01:00",
        # "modulation": "16QAM",
        # "muxponder": "1x400",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "transmitPower": "-190",
        # "uid": "0",
        # "userdom": "all",
        # "wavelength50GHz": "1552524"
        keys = [
            'adminSt',
            'annotation',
            'cdMax',
            'cdMin',
            'dacRate',
            'dn',
            'dwdmCarrier',
            'fecMode',
            'frequency100MHz',
            'frequency50GHz',
            'ituChannel50GHz',
            'modulation',
            'muxponder',
            'name',
            'type',
            'transmitPower',
            'wavelength50GHz'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['type'] == 'xcvrZRIfPol':
            info['typeT'] = 'ZR'

        if info['type'] == 'xcvrZRPIfPol':
            info['typeT'] = 'ZRP'

        return info

    def get_policy_interface_transceiver(self, transceiver_policy_name=None):
        if self.mo_policy_interface_transceiver is None:
            if not self.initialize_policy_interface_transceiver():
                self.log.error(
                    'get_policy_interface_transceiver',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_transceiver:
            policy_info = self.get_policy_interface_transceiver_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if transceiver_policy_name is not None:
            for transceiver_policy in policy:
                if transceiver_policy['name'] == transceiver_policy_name:
                    self.log.apic_mo(
                        'xcvrOpticsIfPol.info',
                        transceiver_policy
                    )
                    return transceiver_policy
            return None

        self.log.apic_mo(
            'xcvrOpticsIfPol.info',
            policy
        )

        return policy
