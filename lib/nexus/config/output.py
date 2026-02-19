class ConfigOutput():
    def __init__(self):
        pass

    def print_configs(self, info, title=False):
        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            self.my_output.default('Device: %s' % (item['nexus_name']), underline=True)
            self.my_output.default(item['configuration'])