from lib import log_helper
from lib.aci.policy.interface.dpp.attachment import PolicyInterfaceDppAttachment


class PolicyInterfaceDpp(PolicyInterfaceDppAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceDppAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_dpp = None

    def initialize_policy_interface_dpp(self):
        if not self.initialize_policy_interface_dpp_attachment():
            return False

        if self.mo_policy_interface_dpp is not None:
            return True

        self.mo_policy_interface_dpp = self.get_policy_interface_attributes('qosDppPol', dn_filter='uni/infra/')
        if self.mo_policy_interface_dpp is None:
            return False

        return True

    def get_policy_interface_dpp_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "be": "unspecified",
        # "beUnit": "unspecified",
        # "burst": "unspecified",
        # "burstUnit": "unspecified",
        # "childAction": "",
        # "conformAction": "transmit",
        # "conformMarkCos": "unspecified",
        # "conformMarkDscp": "unspecified",
        # "descr": "",
        # "dn": "uni/infra/qosdpppol-default",
        # "exceedAction": "drop",
        # "exceedMarkCos": "unspecified",
        # "exceedMarkDscp": "unspecified",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "mode": "bit",
        # "monPolDn": "",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "pir": "0",
        # "pirUnit": "unspecified",
        # "rate": "0",
        # "rateUnit": "unspecified",
        # "sharingMode": "dedicated",
        # "status": "",
        # "type": "1R2C",
        # "uid": "0",
        # "userdom": "",
        # "violateAction": "drop",
        # "violateMarkCos": "unspecified",
        # "violateMarkDscp": "unspecified"
        keys = [
            'adminSt',
            'annotation',
            'be',
            'beUnit',
            'burst',
            'burstUnit',
            'conformAction',
            'conformMarkCos',
            'conformMarkDscp',
            'dn',
            'exceedAction',
            'exceedMarkCos',
            'exceedMarkDscp',
            'mode',
            'name',
            'pir',
            'pirUnit',
            'rate',
            'rateUnit',
            'sharingMode',
            'type',
            'violateAction',
            'violateMarkCos',
            'violateMarkDscp',
            'relnFrom'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['burst'] == 'unspecified':
            info['burstT'] = 'unspecified'
        else:
            info['burstT'] = '%s %s' % (
                info['burst'],
                info['burstUnit']
            )

        if info['be'] == 'unspecified':
            info['beT'] = 'unspecified'
        else:
            info['beT'] = '%s %s' % (
                info['be'],
                info['beUnit']
            )

        if info['rate'] == 'unspecified':
            info['rateT'] = 'unspecified'
        else:
            if info['rateUnit'] == 'unspecified':
                info['rateT'] = '%s pps' % (
                    info['rate']
                )
            else:
                info['rateT'] = '%s %s' % (
                    info['rate'],
                    info['rateUnit']
                )

        if info['pir'] == 'unspecified':
            info['pirT'] = 'unspecified'
        else:
            if info['pirUnit'] == 'unspecified':
                info['pirT'] = '%s pps' % (
                    info['pir']
                )
            else:
                info['pirT'] = '%s %s' % (
                    info['pir'],
                    info['pirUnit']
                )

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsQosEgressDppIfPolCons'] = self.get_policy_interface_dpp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsQosEgressDppIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsQosEgressDppIfPolCons']
        )

        return info

    def get_policy_interface_dpp(self, dpp_policy_name=None):
        if self.mo_policy_interface_dpp is None:
            if not self.initialize_policy_interface_dpp():
                self.log.error(
                    'get_policy_interface_dpp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_dpp:
            policy_info = self.get_policy_interface_dpp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if dpp_policy_name is not None:
            for dpp_policy in policy:
                if dpp_policy['name'] == dpp_policy_name:
                    self.log.apic_mo(
                        'qosDppPol.info',
                        dpp_policy
                    )
                    return dpp_policy
            return None

        self.log.apic_mo(
            'qosDppPol.info',
            policy
        )

        return policy

    def get_policy_interface_dpp_node(self, node_id, node_ports, dpp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_dpp(),
            'l1RsQosEgressDppIfPolCons',
            policy_name=dpp_policy_name
        )
