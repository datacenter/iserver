class OspAvailabilityZoneOutput():
    def __init__(self):
        pass

    def print_availability_zones(self, info, title=False):
        if title:
            self.my_output.default(
                'Availability Zone [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'availableTick',
            'host.name',
            'host.service_namesT'
        ]

        headers = [
            'AZ',
            'Avail',
            'Hypervisor',
            'Service Name [Active]'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['host']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_availability_zones_hv(self, info, title=False):
        if title:
            self.my_output.default(
                'Availability Zone - Hypervisor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'availableTick',
            'host.name',
            'host.running_vms',
            'host.cpu_summary',
            'host.memory_summary',
            'host.disk_summary'
        ]

        headers = [
            'AZ',
            'Avail',
            'Hypervisor',
            'VMs',
            'CPU',
            'Memory',
            'Disk'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['host']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
