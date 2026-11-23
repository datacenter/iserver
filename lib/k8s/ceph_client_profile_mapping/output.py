class K8sCephClientProfileMappingOutput():
    def __init__(self):
        pass

    def print_ceph_client_profile_mappings(self, info, title=False):
        if title:
            self.my_output.default(
                'CephClientProfileMapping [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name'
        ]

        headers = [
            'Ceph Client Profile Mapping'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
