import copy
import time

from lib import filter_helper


class TabooInfo():
    def __init__(self):
        self.taboos = None

    def get_taboo(self, tenant, name):
        taboo_filter = []
        taboo_filter.append(
            'tenant:%s' % (tenant)
        )
        taboo_filter.append(
            'name:%s' % (name)
        )

        taboos = self.get_taboos(
            taboo_filter=taboo_filter
        )

        if len(taboos) == 1:
            return taboos[0]

        return None

    def get_taboo_filters_info(self, managed_object):
        info = []
        for item in managed_object['vzTSubj']:
            taboo_subject_name = item['name']
            taboo_subject_tenant = managed_object['dn'].split('/')[1][3:]
            taboo_subject_info = self.get_taboo_subject(
                taboo_subject_tenant,
                taboo_subject_name
            )
            if taboo_subject_info is None:
                continue

            for taboo_filter_name in taboo_subject_info['vzFilterName']:
                filter_info = self.get_filter(
                    taboo_subject_tenant,
                    taboo_filter_name
                )
                if filter_info is None:
                    self.log.error(
                        'get_taboo_info',
                        'Filter not found: %s/%s' % (
                            taboo_subject_tenant,
                            taboo_filter_name
                        )
                    )
                    continue

                filter_info['subjectName'] = taboo_subject_name
                filter_info['subjectTenant'] = taboo_subject_tenant
                filter_info['subjectNameTenant'] = '%s/%s' % (
                    taboo_subject_tenant,
                    taboo_subject_name
                )
                info.append(
                    filter_info
                )

        return info

    def get_taboo_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'reevaluateAll',
            'scope',
            'status',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        info['vzFilter'] = self.get_taboo_filters_info(
            managed_object
        )

        info['protectedEpg'] = []
        for item in managed_object['vzRtProtBy']:
            contract_epg_info = self.get_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['protectedEpg'].append(
                    contract_epg_info
                )

        return info

    def get_taboos_info(self):
        if self.taboos is None:
            self.taboos = []

            taboos = self.get_taboos_mo()
            if taboos is not None:
                for managed_object in taboos:
                    self.taboos.append(
                        self.get_taboo_info(
                            managed_object
                        )
                    )

        return self.taboos

    def match_taboo(self, taboo_info, taboo_filter):
        if taboo_filter is None or len(taboo_filter) == 0:
            return True

        for taboo_rule in taboo_filter:
            (key, value) = taboo_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, taboo_info['name']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, taboo_info['tenant']):
                    return False

            if key == 'filter':
                found = False
                for filter_info in taboo_info['vzFilter']:
                    if filter_helper.match_string(value, filter_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

        return True

    def get_taboos(self, taboo_filter=None):
        start_time = int(time.time() * 1000)

        all_taboos = self.get_taboos_info()
        if all_taboos is None:
            return None

        taboos = []

        for taboo_info in all_taboos:
            if not self.match_taboo(taboo_info, taboo_filter):
                continue

            taboos.append(taboo_info)

        taboos = sorted(
            taboos,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'vzTaboo.info',
            taboos
        )

        self.log.trace(
            'get_taboos',
            start_time
        )

        return taboos
