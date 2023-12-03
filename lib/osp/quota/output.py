class OspQuotaOutput():
    def __init__(self):
        pass

    def print_quotas(self, info, title=False):
        if title:
            self.my_output.default(
                'Quota [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenant_name',
            'instances',
            'cores',
            'ram',
            'fixed_ips',
            'floating_ips',
            'key_pairs',
            'metadata_items',
            'security_groups',
            'security_group_rules',
            'server_groups',
            'server_group_members',
            'injected_files',
            'injected_file_path_bytes',
            'injected_file_content_bytes'
        ]

        headers = [
            'Tenant',
            'Instance',
            'Core',
            'Memory',
            'Fixed IP',
            'Floating IP',
            'Key Pair',
            'Metadata',
            'SecGroups',
            'Rules',
            'ServerGroups',
            'Members',
            'Files',
            'PathBytes',
            'ContentBytes'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
