import copy
import time

from lib import filter_helper


class FilterInfo():
    def __init__(self):
        self.filters = None

    def get_filter(self, tenant, name):
        filter_filter = []
        filter_filter.append(
            'tenant:%s' % (tenant)
        )
        filter_filter.append(
            'name:%s' % (name)
        )

        filters = self.get_filters(
            filter_filter=filter_filter
        )

        if len(filters) == 1:
            return filters[0]

        return None

    def get_filter_entry_info(self, managed_object):
        keys = [
            'applyToFrag',
            'arpOpc',
            'dFromPort',
            'dToPort',
            'descr',
            'etherT',
            'icmpv4T',
            'icmpv6T',
            'matchDscp',
            'name',
            'prot',
            'sFromPort',
            'sToPort',
            'stateful',
            'status',
            'tcpRules'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['source'] = ''
        if info['sFromPort'] != 'unspecified' and info['sToPort'] != 'unspecified':
            info['source'] = '%s - %s' % (
                info['sFromPort'],
                info['sToPort']
            )

        info['destination'] = ''
        if info['dFromPort'] != 'unspecified' and info['dToPort'] != 'unspecified':
            info['destination'] = '%s - %s' % (
                info['dFromPort'],
                info['dToPort']
            )

        for key in ['etherT', 'arpOpc', 'prot']:
            if info[key] == 'unspecified':
                info[key] = ''

        return info

    def get_filter_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
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

        info['vzEntry'] = []
        for entry_mo in managed_object['vzEntry']:
            info['vzEntry'].append(
                self.get_filter_entry_info(
                    entry_mo
                )
            )

        return info

    def get_filters_info(self):
        if self.filters is None:
            self.filters = []

            filters = self.get_filters_mo()
            if filters is not None:
                for managed_object in filters:
                    self.filters.append(
                        self.get_filter_info(
                            managed_object
                        )
                    )

        return self.filters

    def match_filter(self, filter_info, filter_filter):
        if filter_filter is None or len(filter_filter) == 0:
            return True

        for filter_rule in filter_filter:
            (key, value) = filter_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, filter_info['name']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, filter_info['tenant']):
                    return False

        return True

    def get_filter_usage_info(self, filter_info):
        filter_filter = ['filter:%s' % (filter_info['nameTenant'])]

        filter_info['taboo'] = copy.deepcopy(
            self.get_taboos(
                taboo_filter=filter_filter
            )
        )

        filter_info['contract'] = copy.deepcopy(
            self.get_contracts(
                contract_filter=filter_filter
            )
        )

        return filter_info

    def get_filters(self, filter_filter=None, usage_info=False):
        start_time = int(time.time() * 1000)

        all_filters = self.get_filters_info()
        if all_filters is None:
            return None

        filters = []

        for filter_info in all_filters:
            if not self.match_filter(filter_info, filter_filter):
                continue

            if usage_info:
                filter_info = self.get_filter_usage_info(filter_info)

            filters.append(filter_info)

        filters = sorted(
            filters,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'vzFilter.info',
            filters
        )

        self.log.trace(
            'get_filters',
            start_time
        )

        return filters
