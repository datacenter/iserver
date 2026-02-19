class K8sBareMetalHostOutput():
    def __init__(self):
        pass

    def print_bare_metal_hosts(self, info, title=False):
        if title:
            self.my_output.default(
                'Bare Metal Host [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'info.status',
            'status.hardware.hostname',
            'status.hardware.systemVendor.productName',
            'status.hardware.systemVendor.serialNumber',
            'spec.bmc.address',
            'spec.bmc.credentialsName',
            'spec.bmc.disableCertificateVerification'
        ]

        headers = [
            'Bare Metal Host',
            'Status',
            'Hostname',
            'Hardware',
            'Serial',
            'BMC',
            'Secret',
            'Disable Cert'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
