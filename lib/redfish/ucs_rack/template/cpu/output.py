class RedfishEndpointUcsRackTemplateCpuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_cpu_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'CPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Socket',
            'Health',
            'State',
            'Model',
            'TotalCores',
            'TotalThreads',
            'ProcessorArchitecture',
            'InstructionSet',
            'Manufacturer',
            'MaxSpeedMHz',
            'Step'
        ]

        headers = [
            'Id',
            'Socket',
            'Health',
            'State',
            'Model',
            'Cores',
            'Threads',
            'Arch',
            'Instruction',
            'Manufacturer',
            'Speed [MHz]',
            'Step'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
