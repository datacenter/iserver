from lib import filter_helper


class EpgIfConnInfo():
    def __init__(self):
        self.epg_ifconn = None
        self.epg_ifconn_dns = [
            'uni/epp/br',
            'uni/epp/cld',
            'uni/epp/fv',
            'uni/epp/inb',
            'uni/epp/instp',
            'uni/epp/node',
            'uni/epp/oob',
            'uni/epp/rtd',
            'uni/epp/sec',
            'uni/epp/tnlp',
            'uni/epp/vns',
            'resPolCont/rtdOutCont/rtdOutDef'
        ]

        self.epg_ifconn_fv_types = [
            'phynodeatt',
            'stnodeatt',
            'vnodeatt',
            'dyatt',
            'extstpathatt',
            'stpathatt',
            'attEntitypathatt'
        ]

        self.epg_ifconn_unsupported_dn = []

    def get_epg_ifconn_summary(self, ifconns):
        info = {}

        for supported_dns in self.epg_ifconn_dns:
            dns_name = supported_dns.rsplit('/', maxsplit=1)[-1]
            info[dns_name] = {}
            for supported_type in self.epg_ifconn_fv_types:
                info[dns_name][supported_type] = 0

        for ifconn in ifconns:
            for supported_dns in self.epg_ifconn_dns:
                dns_name = supported_dns.rsplit('/', maxsplit=1)[-1]
                if ifconn['typeDn'] == supported_dns:
                    if ifconn['type'] in self.epg_ifconn_fv_types:
                        info[dns_name][ifconn['type']] = info[dns_name][ifconn['type']] + 1

        return info

    def get_epg_ifconn_epg_pkey_info(self, pkey):
        if len(pkey.split('/')) != 3 and len(pkey.split('/')) != 4:
            return None

        if len(pkey.split('/')) == 3:
            (key1, key2, key3) = pkey.split('/')
            key4 = None

        if len(pkey.split('/')) == 4:
            (key1, key2, key3, key4) = pkey.split('/')

        if key1 != 'uni':
            return None

        if not key2.startswith('tn-'):
            return None

        # uni/tn-infra/out-RL-L3Out/instP-ipnInstP
        if key3.startswith('out-'):
            if key4 is None:
                info = {}
                info['epgType'] = 'l3rtdout'
                info['epgTenant'] = key2[3:]
                info['epgL3out'] = key3[4:]
                info['epgFullName'] = '%s/%s' % (
                    info['epgTenant'],
                    info['epgL3out']
                )
                return info

            if not key4.startswith('instP-'):
                self.log.error(
                    'get_epg_ifconn_epg_pkey_info',
                    'Expected epgPKey uni/out/instP: %s' % (pkey)
                )
                return None

            info = {}
            info['epgType'] = 'l3out'
            info['epgTenant'] = key2[3:]
            info['epgL3out'] = key3[4:]
            info['epgName'] = key4[6:]
            info['epgFullName'] = '%s/%s/%s' % (
                info['epgTenant'],
                info['epgL3out'],
                info['epgName']
            )

            return info

        # uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg
        if key3.startswith('l2out-'):
            if not key4.startswith('instP-'):
                self.log.error(
                    'get_epg_ifconn_epg_pkey_info',
                    'Expected epgPKey uni/l2out/instP: %s' % (pkey)
                )
                return None

            info = {}
            info['epgType'] = 'l2out'
            info['epgTenant'] = key2[3:]
            info['epgL2out'] = key3[6:]
            info['epgName'] = key4[6:]
            info['epgFullName'] = '%s/%s/%s' % (
                info['epgTenant'],
                info['epgL2out'],
                info['epgName']
            )

            return info

        # uni/tn-mgmt/mgmtp-default/inb-default
        # uni/tn-mgmt/mgmtp-default/oob-default
        if key3.startswith('mgmtp-'):
            if not key4.startswith('inb-') and not key4.startswith('oob-'):
                self.log.error(
                    'get_epg_ifconn_epg_pkey_info',
                    'Expected epgPKey uni/mgmtp/inb|oob: %s' % (pkey)
                )
                return None

            info = {}

            if key4.startswith('inb-'):
                info['epgType'] = 'inb'

            if key4.startswith('oob-'):
                info['epgType'] = 'oob'

            info['epgTenant'] = key2[3:]
            info['epgMgmt'] = key3[6:]
            info['epgName'] = key4[4:]
            info['epgFullName'] = '%s/%s/%s' % (
                info['epgTenant'],
                info['epgMgmt'],
                info['epgName']
            )

            return info

        # uni/tn-common/ap-privIP_TEST/epg-privIP_TEST
        if key3.startswith('ap-'):
            if not key4.startswith('epg-'):
                self.log.error(
                    'get_epg_ifconn_epg_pkey_info',
                    'Expected epgPKey uni/ap/epg: %s' % (pkey)
                )
                return None

            info = {}
            info['epgType'] = 'application'
            info['epgTenant'] = key2[3:]
            info['epgAp'] = key3[3:]
            info['epgName'] = key4[4:]
            info['epgFullName'] = '%s/%s/%s' % (
                info['epgTenant'],
                info['epgAp'],
                info['epgName']
            )

            return info

        self.log.error(
            'get_epg_ifconn_epg_pkey_info',
            'Unsupported pkey: %s' % (pkey)
        )
        return None

    def get_epg_ifconn_targetdn_info(self, target_dn):
        info = {}
        info['pathType'] = ''
        info['podId'] = ''
        info['pathNode'] = ''
        info['pathNodeName'] = []
        info['pathNodeT'] = ''
        info['pathName'] = ''

        if target_dn.split('/')[2].startswith('protpaths-'):
            # "topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_1_PolGrp]"
            info['pathType'] = 'Policy Group'
            info['podId'] = target_dn.split('/')[1][4:]
            info['pathNode'] = target_dn.split('/')[2][10:]
            info['pathNodeT'] = 'node-%s' % (info['pathNode'])
            for node_id in info['pathNode'].split('-'):
                info['pathNodeName'].append(
                    'pod-%s/%s' % (
                        info['podId'],
                        self.get_node_name(
                            node_id
                        )
                    )
                )
            info['pathName'] = target_dn.split('[')[1].split(']')[0]

        if target_dn.split('/')[2].startswith('paths-'):
            # "topology/pod-1/paths-2207/pathep-[eth1/3/1]"
            info['pathType'] = 'Intf'
            info['podId'] = target_dn.split('/')[1][4:]
            info['pathNode'] = target_dn.split('/')[2][6:]
            info['pathNodeT'] = 'node-%s' % (info['pathNode'])
            for node_id in info['pathNode'].split('-'):
                info['pathNodeName'].append(
                    'pod-%s/%s' % (
                        info['podId'],
                        self.get_node_name(
                            node_id
                        )
                    )
                )
            info['pathName'] = target_dn.split('[')[1].split(']')[0]

        if target_dn.split('/')[2].startswith('node-') and target_dn.split('/')[3] == 'sys':
            info['pathType'] = 'LsNode'
            info['podId'] = target_dn.split('/')[1][4:]
            info['pathNode'] = target_dn.split('/')[2][6:]
            info['pathNodeT'] = 'node-%s' % (info['pathNode'])
            for node_id in info['pathNode'].split('-'):
                info['pathNodeName'].append(
                    'pod-%s/%s' % (
                        info['podId'],
                        self.get_node_name(
                            node_id
                        )
                    )
                )
            info['pathName'] = target_dn.split('/sys/lsnode-')[1]

        return info

    def get_epg_ifconn_type_info(self, info):
        # Step 1: epgPKey

        info['epgPKey'] = info['dn'].split('%s-[' % (info['typeDn']))[1].split(']')[0]
        epg_info = self.get_epg_ifconn_epg_pkey_info(info['epgPKey'])
        if epg_info is None:
            self.log.error(
                'get_epg_ifconn_type_info',
                'Unsupported epgPKey: %s' % (info['epgPKey'])
            )
            return None
        info.update(epg_info)

        # Step 2: node-{id}

        new_dn = info['dn'].replace('%s-[%s]/' % (info['typeDn'], info['epgPKey']), '')
        if not new_dn.startswith('node-'):
            self.log.error(
                'get_epg_ifconn_type_info',
                'Missing node-id: %s' % (info['dn'])
            )
            return None

        info['nodeId'] = new_dn.split('/')[0].split('-')[1]
        info['nodeName'] = self.get_node_name(
            info['nodeId']
        )
        if info['nodeName'] is None:
            info['nodeName'] = 'Node id: %s' % (info['nodeId'])

        # Step 3: type

        new_dn = '/'.join(new_dn.split('/')[1:])
        info['pathName'] = ''

        if new_dn.startswith('phynodeatt'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/phynodeatt/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'phynodeatt'
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('stnodeatt'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/stnodeatt/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'stnodeatt'
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('dynodeatt'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/dynodeatt/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'dynodeatt'
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('vnodeatt'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/vnodeatt/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'vnodeatt'
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('conndef'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'conndef'
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('dyatt-'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/dyatt-[{targetDn}]/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'dyatt'
            info['memberType'] = 'dynamic'
            info['targetDn'] = new_dn.split(']/conndef/conn', maxsplit=1)[0].split('dyatt-[')[1]
            info.update(
                self.get_epg_ifconn_targetdn_info(
                    info['targetDn']
                )
            )
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('extstpathatt-'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/extstpathatt-[{pathName}]-extchid-{extChId}/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'extstpathatt'
            info['member'] = 'static'
            info['pathName'] = new_dn.split(']-extchid-', maxsplit=1)[0].split('extstpathatt-[')[1]
            info['extChId'] = new_dn.split('-extchid-')[1].split('/')[0]
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('stpathatt-'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/stpathatt-[{pathName}]/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'stpathatt'
            info['memberType'] = 'static'
            info['pathName'] = new_dn.split(']/conndef/conn-[', maxsplit=1)[0].split('stpathatt-[')[1]
            if info['pathName'].startswith('eth') and len(info['pathName'][3:].split('/')) > 1:
                info['pathType'] = 'Intf'
            else:
                info['pathType'] = 'Policy Group'

            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        if new_dn.startswith('attEntitypathatt-'):
            # "uni/epp/fv-[{epgPKey}]/node-{id}/attEntitypathatt-[{pathName}]/conndef/conn-[{encap}]-[{addr}]",
            info['type'] = 'attEntitypathatt'
            info['pathName'] = new_dn.split(']/conndef/conn-[', maxsplit=1)[0].split('attEntitypathatt-[')[1]
            info['encap'] = new_dn.split('conndef/conn-[')[1].split(']')[0]
            return info

        self.log.error(
            'get_epg_ifconn_type_info',
            'Unsupported dn type: %s' % (info['dn'])
        )

        return None

    def get_epg_ifconn_info(self, managed_object):
        # "addr": "<ip>",
        # "auto": "no",
        # "autostate": "disabled",
        # "bcastP": "<ip>",
        # "childAction": "",
        # "classPref": "encap",
        # "descr": "",
        # "dn": "uni/epp/fv-[uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4]/node-2207/dyatt-[topology/pod-1/protpaths-2207-2208/pathep-[k8s_esx72_PolGrp]]/conndef/conn-[vlan-1368]-[<ip>]",
        # "encap": "vlan-1368",
        # "extEncap": "unknown",
        # "gw": "<ip>",
        # "ifInstT": "l3-port",
        # "ipv6Dad": "enabled",
        # "isMultiPodDirect": "no",
        # "lcOwn": "local",
        # "llAddr": "<ip>",
        # "mac": "00:00:00:00:00:00",
        # "mcastAddr": "<ip>",
        # "modTs": "2022-12-16T16:55:06.272+02:00",
        # "mode": "regular",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "mtu": "inherit",
        # "name": "",
        # "nameAlias": "",
        # "resImedcy": "immediate",
        # "status": "",
        # "validState": "not-validated"
        keys = [
            'addr',
            'auto',
            'autostate',
            'classPref',
            'dn',
            'encap',
            'extEncap',
            'gw',
            'ifInstT',
            'mac',
            'mode',
            'mtu',
            'resImedcy'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        is_supported_dn = False
        for supported_dn in self.epg_ifconn_dns:
            if info['dn'].startswith('%s-' % (supported_dn)):
                info['type'] = supported_dn.rsplit('/', maxsplit=1)[-1]
                info['typeDn'] = '%s' % (supported_dn)
                is_supported_dn = True
                break

        if not is_supported_dn:
            self.log.error(
                'get_epg_ifconn_info',
                'Unsupported dn: %s' % (info['dn'])
            )
            return None

        is_supported_dn = True
        unsupported_dns = [
            '/LDevInst-['
        ]
        for unsupported_dn in unsupported_dns:
            if unsupported_dn in info['dn']:
                # Avoid log debug of every unsupported dn
                if unsupported_dn not in self.epg_ifconn_unsupported_dn:
                    self.epg_ifconn_unsupported_dn.append(
                        unsupported_dn
                    )
                    self.log.debug(
                        'get_epg_ifconn_info',
                        'Unsupported dn: %s' % (info['dn'])
                    )

                return None

        info = self.get_epg_ifconn_type_info(
            info
        )

        return info

    def get_epgs_ifconn_info(self):
        if self.epg_ifconn is not None:
            return self.epg_ifconn

        epgs_ifconn_mo = self.get_epg_ifconn_mo()
        if epgs_ifconn_mo is None:
            return None

        self.epg_ifconn = []
        for epg_ifconn_mo in epgs_ifconn_mo:
            epg_ifconn_info = self.get_epg_ifconn_info(
                epg_ifconn_mo
            )
            if epg_ifconn_info is not None:
                self.epg_ifconn.append(
                    epg_ifconn_info
                )

        self.epg_ifconn = sorted(
            self.epg_ifconn,
            key=lambda i: (
                i['nodeName'],
                i['pathName']
            )
        )

        self.log.apic_mo(
            'fvIfConn.info',
            self.epg_ifconn
        )

        return self.epg_ifconn

    def match_epg_ifconn(self, epg_ifconn_info, epg_ifconn_filter):
        if epg_ifconn_filter is None or len(epg_ifconn_filter) == 0:
            return True

        for aepg_rule in epg_ifconn_filter:
            (key, value) = aepg_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_ap_name(value, epg_ifconn_info['epgFullName']):
                    return False

            if not key_found:
                self.log.error(
                    'match_epg_ifconn',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_epg_ifconn(self, epg_ifconn_filter=None):
        all_epg_ifconn = self.get_epgs_ifconn_info()
        if all_epg_ifconn is None:
            return None

        epg_ifconn = []

        for epg_ifconn_info in all_epg_ifconn:
            if not self.match_epg_ifconn(epg_ifconn_info, epg_ifconn_filter):
                continue

            epg_ifconn.append(epg_ifconn_info)

        return epg_ifconn
