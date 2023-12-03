class OspHypervisorOutput():
    def __init__(self):
        pass

    def print_hypervisors(self, info, title=False):
        if title:
            self.my_output.default(
                'Hypervisor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'hypervisor_hostname',
            'host_ip',
            'status',
            'state',
            'running_vms',
            'cpu_summary',
            'memory_summary',
            'disk_summary'
        ]

        headers = [
            'Id',
            'Hypervisor',
            'IP',
            'Status',
            'State',
            'VMs',
            'CPU',
            'Memory',
            'Disk'
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

    def print_hypervisors_vm(self, info, title=False):
        if title:
            self.my_output.default(
                'Hypervisor - Virtual Machine [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'hypervisor_hostname',
            'vm_info.tenant',
            'vm_info.name',
            'vm_info.status',
            'vm_info.vcpus',
            'vm_info.ram',
            'vm_info.disk'
        ]

        headers = [
            'Id',
            'Hypervisor',
            'Tenant',
            'Name',
            'Status',
            'CPU',
            'Memory [MB]',
            'Disk [GB]'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vm_info']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
