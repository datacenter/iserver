from lib.aci.policy.interface.auth.main import PolicyInterfaceAuth
from lib.aci.policy.interface.cdp.main import PolicyInterfaceCdp
from lib.aci.policy.interface.copp.main import PolicyInterfaceCopp
from lib.aci.policy.interface.dpp.main import PolicyInterfaceDpp
from lib.aci.policy.interface.fc.main import PolicyInterfaceFc
from lib.aci.policy.interface.l2.main import PolicyInterfaceL2
from lib.aci.policy.interface.link_flap.main import PolicyInterfaceLinkFlap
from lib.aci.policy.interface.link_level.main import PolicyInterfaceLinkLevel
from lib.aci.policy.interface.link_level_fc.main import PolicyInterfaceLinkLevelFc
from lib.aci.policy.interface.lldp.main import PolicyInterfaceLldp
from lib.aci.policy.interface.mcp.main import PolicyInterfaceMcp
from lib.aci.policy.interface.pfc.main import PolicyInterfacePfc
from lib.aci.policy.interface.port_channel.main import PolicyInterfacePortChannel
from lib.aci.policy.interface.port_channel_member.main import PolicyInterfacePortChannelMember
from lib.aci.policy.interface.port_security.main import PolicyInterfacePortSecurity
from lib.aci.policy.interface.slow_drain.main import PolicyInterfaceSlowDrain
from lib.aci.policy.interface.storm_control.main import PolicyInterfaceStormControl
from lib.aci.policy.interface.stp.main import PolicyInterfaceStp
from lib.aci.policy.interface.synce.main import PolicyInterfaceSynce
from lib.aci.policy.interface.transceiver.main import PolicyInterfaceTransceiver


class PolicyInterface(
    PolicyInterfaceAuth,
    PolicyInterfaceCdp,
    PolicyInterfaceCopp,
    PolicyInterfaceDpp,
    PolicyInterfaceFc,
    PolicyInterfaceL2,
    PolicyInterfaceLinkFlap,
    PolicyInterfaceLinkLevel,
    PolicyInterfaceLinkLevelFc,
    PolicyInterfaceLldp,
    PolicyInterfaceMcp,
    PolicyInterfacePfc,
    PolicyInterfacePortChannel,
    PolicyInterfacePortChannelMember,
    PolicyInterfacePortSecurity,
    PolicyInterfaceSlowDrain,
    PolicyInterfaceStormControl,
    PolicyInterfaceStp,
    PolicyInterfaceSynce,
    PolicyInterfaceTransceiver
    ):
    def __init__(self):
        PolicyInterfaceAuth.__init__(self)
        PolicyInterfaceCdp.__init__(self)
        PolicyInterfaceCopp.__init__(self)
        PolicyInterfaceDpp.__init__(self)
        PolicyInterfaceFc.__init__(self)
        PolicyInterfaceL2.__init__(self)
        PolicyInterfaceLinkFlap.__init__(self)
        PolicyInterfaceLinkLevel.__init__(self)
        PolicyInterfaceLinkLevelFc.__init__(self)
        PolicyInterfaceLldp.__init__(self)
        PolicyInterfaceMcp.__init__(self)
        PolicyInterfacePfc.__init__(self)
        PolicyInterfacePortChannel.__init__(self)
        PolicyInterfacePortChannelMember.__init__(self)
        PolicyInterfacePortSecurity.__init__(self)
        PolicyInterfaceSlowDrain.__init__(self)
        PolicyInterfaceStormControl.__init__(self)
        PolicyInterfaceStp.__init__(self)
        PolicyInterfaceSynce.__init__(self)
        PolicyInterfaceTransceiver.__init__(self)

    def get_policy_interface_reln(self, managed_object, interface_class_name):
        attributes = []
        if 'children' in managed_object[interface_class_name]:
            for child in managed_object[interface_class_name]['children']:
                for class_name in child:
                    entry = {}
                    entry['class'] = class_name
                    entry['rn'] = child[class_name]['attributes']['rn']
                    entry['tCl'] = child[class_name]['attributes']['tCl']
                    entry['tDn'] = child[class_name]['attributes']['tDn']
                    entry['policyType'] = self.get_policy_type_from_tcl(
                        child[class_name]['attributes']['tCl']
                    )
                    entry['policyName'] = self.get_policy_name_from_tdn(
                        child[class_name]['attributes']['tDn']
                    )
                    attributes.append(
                        entry
                    )

        attributes = sorted(
            attributes,
            key=lambda i: (
                i['policyType'],
                i['policyName']
            )
        )

        return attributes

    def get_policy_interface_reference_attributes(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "extMngdBy": "",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-05-19T18:26:53.317+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "rType": "mo",
        # "rn": "rsstormctrlIfPol",
        # "state": "formed",
        # "stateQual": "default-target",
        # "status": "",
        # "tCl": "stormctrlIfPol",
        # "tContextDn": "",
        # "tDn": "uni/infra/stormctrlifp-default",
        # "tRn": "stormctrlifp-default",
        # "tType": "name",
        # "tnStormctrlIfPolName": "",
        # "uid": "0",
        # "userdom": "all"
        keys = [
            'state',
            'tDn',
            'tRn'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if managed_object is not None and key in managed_object:
                info[key] = managed_object[key]

        info['name'] = '--'
        if managed_object is not None:
            if 'tType' in managed_object:
                if managed_object['tType'] == 'name':
                    info['name'] = '-'.join(info['tRn'].split('-')[1:])
                if managed_object['tType'] == 'mo':
                    info['name'] = '-'.join(info['tDn'].split('-')[1:])

        return info
