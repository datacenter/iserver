import json


class K8sNetworkAttachmentDefinitionOutput():
    def __init__(self):
        pass

    def print_nads(self, info):
        for item in info:
            item['configT'] = json.dumps(
                item['config'],
                indent=2
            ).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Network Attachment Definition', 'namespace_nameT'],
                ['Type', 'config.type'],
                ['SR-IOV Resource', 'resource_name'],
                ['Config', 'configT'],
                ['Age', 'age']
            ]
        )
