from lib import filter_helper


class PsirtAdvisoryOutput():
    def __init__(self):
        pass

    def print_advisory(self, info, title=False):
        if title:
            self.my_output.default(
                'Advisory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['advisoryTitleT'] = filter_helper.get_string_chunks(
                item['advisoryTitle'],
                length=40
            )
            item['products'] = []
            for product_name in item['productVersion']:
                item['products'].append(
                    product_name
                )

        order = [
            'sir',
            'finalTick',
            'advisoryTitleT',
            'bugIDs',
            'cves',
            'cwe',
            'products',
            'add_age',
            'update_age'
        ]

        headers = [
            'Sev',
            'Final',
            'Title',
            'Bug',
            'CVE',
            'CWE',
            'Product',
            'Add',
            'Update'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['advisoryTitleT', 'bugIDs', 'cves', 'cwe', 'products']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_advisory_url(self, info, title=False):
        if title:
            self.my_output.default(
                'Advisory - URL [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['advisoryTitleT'] = filter_helper.get_string_chunks(
                item['advisoryTitle'],
                length=40
            )
            item['url'] = []
            item['url'].append(
                'cvrf: %s' % (item['cvrfUrl'])
            )
            item['url'].append(
                'csaf: %s' % (item['csafUrl'])
            )
            item['url'].append(
                'pub:  %s' % (item['publicationUrl'])
            )

        order = [
            'sir',
            'finalTick',
            'advisoryTitleT',
            'url'
        ]

        headers = [
            'Sev',
            'Final',
            'Title',
            'URL'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['advisoryTitleT', 'url']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_advisory_summary(self, info, title=False):
        if title:
            self.my_output.default(
                'Advisory - Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['advisoryTitleT'] = filter_helper.get_string_chunks(
                item['advisoryTitle'],
                length=40
            )

            item['summaryT'] = filter_helper.get_string_chunks(
                item['summary'].replace('\r\n', '').replace('<p>', '').replace('</p>', ''),
                length=100
            )

        order = [
            'sir',
            'finalTick',
            'advisoryTitleT',
            'summaryT'
        ]

        headers = [
            'Sev',
            'Final',
            'Title',
            'Summary'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['advisoryTitleT', 'summaryT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_advisory_version(self, info, title=False):
        if title:
            self.my_output.default(
                'Advisory - Product Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['advisoryTitleT'] = filter_helper.get_string_chunks(
                item['advisoryTitle'],
                length=40
            )
            item['productNameVersion'] = []
            for product_name in item['productVersion']:
                if len(item['productVersion'][product_name]) == 0:
                    item['productNameVersion'].append(
                        product_name
                    )
                else:
                    for product_version in item['productVersion'][product_name]:
                        item['productNameVersion'].append(
                            '%s %s' % (
                                product_name,
                                product_version
                            )
                        )

        order = [
            'sir',
            'finalTick',
            'advisoryTitleT',
            'bugIDs',
            'cves',
            'cwe',
            'productNameVersion',
            'add_age',
            'update_age'
        ]

        headers = [
            'Sev',
            'Final',
            'Title',
            'Bug',
            'CVE',
            'CWE',
            'Product',
            'Add',
            'Update'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['advisoryTitleT', 'bugIDs', 'cves', 'cwe', 'productNameVersion']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_advisory_product(self, info, title=False, product_filter=None):
        severities = ['Critical', 'High', 'Medium', 'NA', 'Low', 'Informational']
        products = {}
        for item in info:
            for product_name in item['productVersion']:
                if product_filter is not None and not filter_helper.match_string(product_filter, product_name):
                    continue

                if product_name not in products:
                    product_info = {}
                    product_info['ver'] = []
                    product_info['bug'] = []
                    product_info['cve'] = []
                    product_info['cwe'] = []
                    for sev in severities:
                        product_info[sev] = 0
                    products[product_name] = product_info

                for ver in item['productVersion'][product_name]:
                    if ver not in products[product_name]['ver']:
                        products[product_name]['ver'].append(ver)

                for bug in item['bugIDs']:
                    if bug not in products[product_name]['bug']:
                        products[product_name]['bug'].append(bug)

                for cve in item['cves']:
                    if cve not in products[product_name]['cve']:
                        products[product_name]['cve'].append(cve)

                for cwe in item['cwe']:
                    if cwe not in products[product_name]['cwe']:
                        products[product_name]['cwe'].append(cwe)

                if item['sir'] in severities:
                    products[product_name][item['sir']] = products[product_name][item['sir']] + 1

        items = []
        for product_name in products:
            item = products[product_name]
            item['name'] = product_name
            items.append(
                item
            )

        items = sorted(
            items,
            key=lambda i: i['name'].lower()
        )

        if title:
            self.my_output.default(
                'Advisory - Product Pivot View [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'ver',
            'Critical',
            'High',
            'Medium',
            'Low',
            'Informational',
            'bug',
            'cve',
            'cwe'
        ]

        headers = [
            'Product',
            'Version',
            'Crit',
            'High',
            'Med',
            'Low',
            'Info',
            'Bug',
            'CVE',
            'CWE'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                items,
                order,
                ['ver', 'bug', 'cve', 'cwe']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
