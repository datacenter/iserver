class MdNexusConfigurationOutput():
    def __init__(self):
        pass

    def print_nexus_configuration(self, info, name, short_names=True):
        self.print_page_header('Configuration (%s)' % (name))
        self.print_nexus_devices_bar(name, 'configuration')
        self.print_nexus_table_bar(name, 'configuration')

        self.my_output.print_stream('```', 'output')
        self.my_output.print_stream(info['configuration'], 'output')
        self.my_output.print_stream('```', 'output')

        self.save_output('%s-configuration' % (name), subdir='nexus')
