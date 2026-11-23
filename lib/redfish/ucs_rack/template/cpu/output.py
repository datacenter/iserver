class RedfishEndpointUcsRackTemplateCpuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_cpu_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['CPU Id', 'Id'],
                ['Socket', 'Socket'],
                ['Health', 'Health'],
                ['State', 'State'],
                ['Model', 'Model'],
                ['Cores', 'TotalCores'],
                ['Threads', 'TotalThreads'],
                ['Arch', 'ProcessorArchitecture'],
                ['Instruction', 'InstructionSet'],
                ['Manufacturer', 'Manufacturer'],
                ['Speed [MHz]', 'MaxSpeedMHz'],
                ['Step', 'Step']
            ]
        )
