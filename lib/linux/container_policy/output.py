import json


class LinuxContainerPolicyOutput():
    def __init__(self):
        pass

    def print_linux_container_policy_config(self, info, title=False):
        if title:
            self.my_output.default(
                'Container Policy Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )