from lib import log_helper
from lib.aci.policy.interface.storm_control.attachment import PolicyInterfaceStormControlAttachment


class PolicyInterfaceStormControl(PolicyInterfaceStormControlAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceStormControlAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_storm_control = None

    def initialize_policy_interface_storm_control(self):
        if not self.initialize_policy_interface_storm_control_attachment():
            return False

        if self.mo_policy_interface_storm_control is not None:
            return True

        self.mo_policy_interface_storm_control = self.get_policy_interface_attributes('stormctrlIfPol')
        if self.mo_policy_interface_storm_control is None:
            return False

        return True

    def get_policy_interface_storm_control_info(self, managed_object):
        # "annotation": "",
        # "bcBurstPps": "unspecified",
        # "bcBurstRate": "100.000000",
        # "bcRate": "100.000000",
        # "bcRatePps": "unspecified",
        # "burstPps": "unspecified",
        # "burstRate": "100.000000",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/stormctrlifp-default",
        # "extMngdBy": "",
        # "isUcMcBcStormPktCfgValid": "Invalid",
        # "lcOwn": "local",
        # "mcBurstPps": "unspecified",
        # "mcBurstRate": "100.000000",
        # "mcRate": "100.000000",
        # "mcRatePps": "unspecified",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "rate": "100.000000",
        # "ratePps": "unspecified",
        # "status": "",
        # "stormCtrlAction": "drop",
        # "stormCtrlSoakInstCount": "3",
        # "type": "all",
        # "uid": "0",
        # "userdom": "",
        # "uucBurstPps": "unspecified",
        # "uucBurstRate": "100.000000",
        # "uucRate": "100.000000",
        # "uucRatePps": "unspecified"
        keys = [
            'annotation',
            'dn',
            'name',
            'relnFrom'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['packetType'] = []

        if managed_object['isUcMcBcStormPktCfgValid'] == 'Valid':
            packet_type_info = {}
            packet_type_info['type'] = 'unicast'
            packet_type_info['burstPps'] = managed_object['uucBurstPps']
            packet_type_info['burstRate'] = managed_object['uucBurstRate']
            packet_type_info['rate'] = managed_object['uucRate']
            packet_type_info['ratePps'] = managed_object['uucRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

            packet_type_info = {}
            packet_type_info['type'] = 'broadcast'
            packet_type_info['burstPps'] = managed_object['bcBurstPps']
            packet_type_info['burstRate'] = managed_object['bcBurstRate']
            packet_type_info['rate'] = managed_object['bcRate']
            packet_type_info['ratePps'] = managed_object['bcRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

            packet_type_info = {}
            packet_type_info['type'] = 'multicast'
            packet_type_info['burstPps'] = managed_object['mcBurstPps']
            packet_type_info['burstRate'] = managed_object['mcBurstRate']
            packet_type_info['rate'] = managed_object['mcRate']
            packet_type_info['ratePps'] = managed_object['mcRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

        if managed_object['isUcMcBcStormPktCfgValid'] == 'Invalid':
            packet_type_info = {}
            packet_type_info['type'] = 'all'
            packet_type_info['burstPps'] = managed_object['burstPps']
            packet_type_info['burstRate'] = managed_object['burstRate']
            packet_type_info['rate'] = managed_object['rate']
            packet_type_info['ratePps'] = managed_object['ratePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsStormctrlIfPolCons'] = self.get_policy_interface_storm_control_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsStormctrlIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsStormctrlIfPolCons']
        )

        return info

    def get_policy_interface_storm_control(self, storm_control_policy_name=None):
        if self.mo_policy_interface_storm_control is None:
            if not self.initialize_policy_interface_storm_control():
                self.log.error(
                    'get_policy_interface_storm_control',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_storm_control:
            policy_info = self.get_policy_interface_storm_control_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if storm_control_policy_name is not None:
            for storm_control_policy in policy:
                if storm_control_policy['name'] == storm_control_policy_name:
                    self.log.apic_mo(
                        'stormctrlIfPol.info',
                        storm_control_policy
                    )
                    return storm_control_policy
            return None

        self.log.apic_mo(
            'stormctrlIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_storm_control_node(self, node_id, node_ports, storm_control_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_storm_control(),
            'l1RsStormctrlIfPolCons',
            policy_name=storm_control_policy_name
        )
