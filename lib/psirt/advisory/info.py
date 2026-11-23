from lib import filter_helper


class PsirtAdvisoryInfo():
    def __init__(self):
        self.advisory = None

    def get_advisory_info(self, advisory_mo):
        if advisory_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        for key in advisory_mo:
            if key in ['bugIDs']:
                continue
            info[key] = advisory_mo[key]

        info['bugIDs'] = []
        for bug_mo in advisory_mo['bugIDs']:
            if bug_mo != 'NA':
                info['bugIDs'].append(
                    bug_mo
                )

        info['productVersion'] = {}
        products_with_version = [
            'Cisco Wireless LAN Controller (WLC)',
            'Cisco Firepower Threat Defense Software',
            'Cisco Adaptive Security Appliance (ASA) Software',
            'Cisco Firepower Extensible Operating System (FXOS)',
            'Cisco Firepower Management Center',
            'Cisco NX-OS Software',
            'Cisco NX-OS System Software in ACI Mode',
            'Cisco IOS XE Software',
            'Cisco IOS'
        ]

        for product_mo in advisory_mo['productNames']:
            if product_mo in info['productVersion']:
                # base product name already defined, there is no version here anyway in product_mo
                continue

            is_product_mo_with_version = False
            for product_with_version in products_with_version:
                if product_mo == product_with_version:
                    # it must have been already added to 'productName'
                    continue

                if product_mo.startswith(product_with_version):
                    if len(product_mo.split(' ')) == len(product_with_version.split(' ')) + 1:
                        # product_mo = Cisco IOS 12.2
                        # product_with_version = Cisco IOS
                        is_product_mo_with_version = True
                        if product_with_version not in info['productVersion']:
                            info['productVersion'][product_with_version] = []

                        if len(product_mo.split(' ')[-1]) > 0:
                            info['productVersion'][product_with_version].append(
                                product_mo.split(' ')[-1]
                            )

            if not is_product_mo_with_version:
                info['productVersion'][product_mo] = []

        if info['sir'] == 'Critical':
            info['__Output']['sir'] = 'Red'

        if info['sir'] == 'High':
            info['__Output']['sir'] = 'Magenta'

        if info['sir'] == 'Medium':
            info['__Output']['sir'] = 'Yellow'

        if info['sir'] == 'Low':
            info['__Output']['sir'] = 'Green'

        if info['sir'] == 'Informational':
            info['__Output']['sir'] = 'Blue'

        if info['sir'] not in ['Critical', 'High', 'Medium', 'NA', 'Low', 'Informational']:
            print(info['sir'])

        if info['status'] == 'Final':
            info['finalTick'] = '\u2713'
        else:
            info['finalTick'] = '\u2717'

        info['add_age'] = self.convert_timestamp_to_age(
            info['firstPublished'],
            on_error='--'
        )

        info['add_days'] = self.convert_timestamp_to_days(
            info['firstPublished']
        )

        info['update_age'] = self.convert_timestamp_to_age(
            info['lastUpdated'],
            on_error='--'
        )

        info['update_days'] = self.convert_timestamp_to_days(
            info['lastUpdated'],
            on_error=None
        )
        return info

    def get_advisories_info(self, cache_enabled=True):
        if cache_enabled:
            if self.advisory is not None:
                return self.advisory

        managed_objects = self.get_advisory_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.advisory = []
        for managed_object in managed_objects:
            advisory_info = self.get_advisory_info(
                managed_object
            )
            self.advisory.append(
                advisory_info
            )

        self.log.psirt_mo(
            'advisory',
            self.advisory
        )

        return self.advisory

    def match_advisory(self, advisory_info, advisory_filter):
        if advisory_filter is None or len(advisory_filter) == 0:
            return True

        for ap_rule in advisory_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'bug':
                key_found = True
                found = False
                for bug in advisory_info['bugIDs']:
                    if filter_helper.match_string(value, bug):
                        found = True
                        break

                if not found:
                    return False

            if key == 'cve':
                key_found = True
                found = False
                for cve in advisory_info['cves']:
                    if filter_helper.match_string(value, cve):
                        found = True
                        break

                if not found:
                    return False

            if key == 'cwe':
                key_found = True
                found = False
                for cwe in advisory_info['cwe']:
                    if filter_helper.match_string(value, cwe):
                        found = True
                        break

                if not found:
                    return False

            if key == 'product':
                key_found = True
                found = False
                for product_name in advisory_info['productVersion']:
                    if filter_helper.match_string(value, product_name):
                        found = True
                        break

                if not found:
                    return False

            if key == 'version':
                key_found = True
                found = False
                for product_name in advisory_info['productVersion']:
                    for product_version in advisory_info['productVersion'][product_name]:
                        if filter_helper.match_string(value, product_version):
                            found = True
                            break

                if not found:
                    return False

            if key == 'severity':
                key_found = True

                if value not in ['crit', 'high', 'med', 'low', 'info']:
                    self.log.error(
                        'match_advisory',
                        'Unsupported severity value: %s' % (value)
                    )

                if value == 'crit':
                    if advisory_info['sir'] not in ['Critical']:
                        return False

                if value == 'high':
                    if advisory_info['sir'] not in ['Critical', 'High']:
                        return False

                if value == 'med':
                    if advisory_info['sir'] not in ['Critical', 'High', 'Medium']:
                        return False

                if value == 'low':
                    if advisory_info['sir'] not in ['Critical', 'High', 'Medium', 'Low']:
                        return False

                if value == 'info':
                    if advisory_info['sir'] not in ['Critical', 'High', 'Medium', 'Low', 'Informational']:
                        return False

            if key == 'added':
                key_found = True
                if advisory_info['add_days'] is None:
                    return False

                if advisory_info['add_days'] > int(value):
                    return False

            if key == 'updated':
                key_found = True
                if advisory_info['update_days'] is None:
                    return False

                if advisory_info['update_days'] > int(value):
                    return False

            if not key_found:
                self.log.error(
                    'match_advisory',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_advisory_product_versions(self, product_versions, advisory_filter):
        selected_product_versions = {}

        product_filter = None
        version_filter = None
        for ap_rule in advisory_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'product':
                product_filter = value

            if key == 'version':
                version_filter = value

        for product_name in product_versions:
            if product_filter is not None:
                if not filter_helper.match_string(product_filter, product_name):
                    continue

            selected_product_versions[product_name] = []
            for product_version in product_versions[product_name]:
                if version_filter is not None:
                    if not filter_helper.match_string(version_filter, product_version):
                        continue

                selected_product_versions[product_name].append(
                    product_version
                )

        return selected_product_versions

    def get_advisories(self, object_filter=None, cache_enabled=True):
        all_advisories = self.get_advisories_info(cache_enabled=cache_enabled)
        if all_advisories is None:
            return None

        advisories = []

        for advisory_info in all_advisories:
            if not self.match_advisory(advisory_info, object_filter):
                continue

            advisory_info['productVersion'] = self.get_advisory_product_versions(
                advisory_info['productVersion'],
                object_filter
            )

            advisories.append(
                advisory_info
            )

        return advisories
