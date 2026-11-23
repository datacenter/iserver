import json


class ConfigurationInterfaceOutput():
    def __init__(self):
        pass

    def print_configuration_interface(self, info, title=False):
        print(json.dumps(info, indent=4))