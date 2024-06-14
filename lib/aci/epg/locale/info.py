from lib import filter_helper


class EpgLocaleInfo():
    def __init__(self):
        self.epg_locale = None
        self.epg_locale_unsupported_dn = []

    def get_epg_locale_node(self, locales_info):
        info = []
        node_ids = []

        for locale_info in locales_info:
            if locale_info['id'] in node_ids:
                continue

            node_info = self.get_node(
                node_id=locale_info['id']
            )
            if node_info is not None:
                info.append(
                    node_info
                )

        return info

    def get_epg_locale_fv_info(self, info):
        # "dn": "uni/epp/fv-[uni/tn-common/ap-privIP_TEST/epg-privIP_TEST]/node-2202"
        info['type'] = 'epg'

        epg_dn = info['dn'].split('[')[1].split(']')[0]
        info['epgTenant'] = epg_dn.split('/')[1][3:]
        info['epgAp'] = epg_dn.split('/')[2][3:]
        info['epgName'] = epg_dn.split('/')[3][4:]
        info['epgNameApTenant'] = '%s/%s/%s' % (
            info['epgTenant'],
            info['epgAp'],
            info['epgName']
        )

        return info

    def get_epg_locale_br_info(self, info):
        # uni/epp/br-[uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg]/node-2208
        info['type'] = 'l2out'

        epg_dn = info['dn'].split('[')[1].split(']')[0]
        info['l2outTenant'] = epg_dn.split('/')[1][3:]
        info['l2outName'] = epg_dn.split('/')[2][6:]
        info['epgName'] = epg_dn.split('/')[3][6:]

        return info

    def get_epg_locale_rtd_info(self, info):
        # uni/epp/rtd-[uni/tn-Ericsson_PACO/out-RAN/instP-RAN]/node-2208
        info['type'] = 'l3out'

        epg_dn = info['dn'].split('[')[1].split(']')[0]
        info['l3outTenant'] = epg_dn.split('/')[1][3:]
        info['l3outName'] = epg_dn.split('/')[2][4:]
        info['epgName'] = epg_dn.split('/')[3][6:]

        return info

    def get_epg_locale_info(self, managed_object):
        # "boostrapTriggered": "no",
        # "childAction": "",
        # "deployAllPorts": "no",
        # "dn": "uni/epp/fv-[uni/tn-common/ap-privIP_TEST/epg-privIP_TEST]/node-2202",
        # "fabricExtCtrlPeering": "no",
        # "fabricExtIntersiteCtrlPeering": "no",
        # "fabricExtIntersitePeering": "no",
        # "firstUpdateDeployed": "yes",
        # "id": "2202",
        # "instrImedcy": "immediate",
        # "ipv4LbAddr": "<ip>",
        # "ipv6LbAddr": "<ip>",
        # "lcOwn": "local",
        # "modTs": "2023-06-12T11:29:17.382+02:00",
        # "modeMisconfiguration": "no",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "operSt": "allocated",
        # "rtrId": "<ip>",
        # "rtrIdLoopBack": "yes",
        # "status": "",
        # "summaryNeeded": "full"
        keys = [
            'deployAllPorts',
            'dn',
            'fabricExtCtrlPeering',
            'fabricExtIntersiteCtrlPeering',
            'fabricExtIntersitePeering',
            'firstUpdateDeployed',
            'id',
            'instrImedcy',
            'operSt'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['nodeName'] = self.get_node_name(
            info['id']
        )

        # state
        if info['operSt'] == 'allocated':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        # Dn format
        # "uni/epp/sec-[{epgPKey}]/node-{id}",
        # "uni/epp/cld-[{epgPKey}]/node-{id}",
        # "uni/epp/tnlp-[{epgPKey}]/node-{id}",
        # "uni/epp/instp-[{epgPKey}]/node-{id}",
        # "uni/epp/vns-[{epgPKey}]/node-{id}",
        # "uni/epp/inb-[{epgPKey}]/node-{id}",
        # "uni/epp/oob-[{epgPKey}]/node-{id}",
        # "uni/epp/node-{id}",
        # "uni/epp/fv-[{epgPKey}]/node-{id}",
        # "uni/epp/rtd-[{epgPKey}]/node-{id}",
        # "uni/epp/br-[{epgPKey}]/node-{id}",
        # "uni/epp/node-{id}",
        # "uni/epp/node-{id}"

        supported_dns = [
            'uni/epp/fv-',
            'uni/epp/br-',
            'uni/epp/rtd-',
            'uni/epp/inb-',
            'uni/epp/oob-'
        ]
        is_supported_dn = False
        for supported_dn in supported_dns:
            if info['dn'].startswith(supported_dn):
                is_supported_dn = True

        if not is_supported_dn:
            self.log.error(
                'get_epg_locale_info',
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
                if unsupported_dn not in self.epg_locale_unsupported_dn:
                    self.epg_locale_unsupported_dn.append(
                        unsupported_dn
                    )
                    self.log.debug(
                        'get_epg_locale_info',
                        'Unsupported dn: %s' % (info['dn'])
                    )

                return None

        if info['dn'].startswith('uni/epp/fv-'):
            info = self.get_epg_locale_fv_info(
                info
            )

        if info['dn'].startswith('uni/epp/br-'):
            info = self.get_epg_locale_br_info(
                info
            )

        if info['dn'].startswith('uni/epp/rtd-'):
            info = self.get_epg_locale_rtd_info(
                info
            )

        if info['dn'].startswith('uni/epp/inb-'):
            return None

        if info['dn'].startswith('uni/epp/oob-'):
            return None

        return info

    def get_epgs_locale_info(self):
        if self.epg_locale is not None:
            return self.epg_locale

        epgs_locale_mo = self.get_epg_locale_mo()
        if epgs_locale_mo is None:
            return None

        self.epg_locale = []
        for epg_locale_mo in epgs_locale_mo:
            epg_locale_info = self.get_epg_locale_info(
                epg_locale_mo
            )

            if epg_locale_info is not None:
                self.epg_locale.append(
                    epg_locale_info
                )

        self.log.apic_mo(
            'fvLocale.info',
            self.epg_locale
        )

        return self.epg_locale

    def match_epg_locale(self, epg_locale_info, epg_locale_filter):
        if epg_locale_info['type'] != 'epg':
            return False

        if epg_locale_filter is None or len(epg_locale_filter) == 0:
            return True

        for aepg_rule in epg_locale_filter:
            (key, value) = aepg_rule.split(':')
            key_found = False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, epg_locale_info['epgTenant']):
                    return False

            if key == 'profile':
                key_found = True
                if not filter_helper.match_string(value, epg_locale_info['epgAp']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_ap_name(value, epg_locale_info['epgNameApTenant']):
                    return False

            if key == 'node_name':
                key_found = True
                if not filter_helper.match_string(value, epg_locale_info['nodeName']):
                    return False

            if key == 'node_id':
                key_found = True
                if not filter_helper.match_string(value, epg_locale_info['id']):
                    return False

            if not key_found:
                self.log.error(
                    'match_epg_locale',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_epg_locale(self, epg_locale_filter=None):
        all_epg_locale = self.get_epgs_locale_info()
        if all_epg_locale is None:
            return None

        epg_locale = []

        for epg_locale_info in all_epg_locale:
            if not self.match_epg_locale(epg_locale_info, epg_locale_filter):
                continue

            epg_locale.append(epg_locale_info)

        return epg_locale
