import json


class OcpTaskContainerPolicyOutput():
    def __init__(self):
        pass

    def print_ocp_container_policy_config(self, info, title=False):
        if title:
            self.my_output.default(
                'Container Policy Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        equal = True
        if len(info) > 1:
            reference = '\n'.join(info[0]['config'])
            for item in info:
                if '\n'.join(item['config']) != reference:
                    equal = False

        if equal:
            self.my_output.default('Configuration the same on all nodes', before_newline=True, after_newline=True)
            self.my_output.default(
                json.dumps(
                    info[0]['config'],
                    indent=4
                )
            )

        if not equal:
            for item in info:
                self.my_output.default('Node %s [%s]' % (item['name'], item['ip']), after_newline=True)

                self.my_output.default(
                    json.dumps(
                        item['config'],
                        indent=4
                    )
                )

    def print_ocp_container_policy_mc(self, info, title=False):
        if title:
            self.my_output.default(
                'ContainerPolicy Machine Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            self.my_output.default('Machine config: %s' % (item['name']), before_newline=True)
            self.my_output.default('Node: %s' % (', '.join(item['node'])))
            for file_info in item['file']:
                self.my_output.default('Path: %s' % (file_info['path']))
                self.my_output.default(file_info['content'])

    def print_ocp_container_policy_info(self, info):
        if 'config' in info:
            self.print_ocp_container_policy_config(info['config'], title=True)

        if 'mc' in info:
            self.print_ocp_container_policy_mc(info['mc'], title=True)
