from lib.ocp.task.chrony.output import OcpTaskChronyOutput
from lib.ocp.task.container_policy.output import OcpTaskContainerPolicyOutput

class OcpTaskOutput(
        OcpTaskChronyOutput,
        OcpTaskContainerPolicyOutput
        ):
    def __init__(self):
        OcpTaskChronyOutput.__init__(self)
        OcpTaskContainerPolicyOutput.__init__(self)

    def print_ocp_ssh_authorized_keys(self, info):
        order = [
            'node',
            'username',
            'key',
            'mc'
        ]

        headers = [
            'Node',
            'Username',
            'Key',
            'Machine Config'
        ]

        for item in info:
            (key_type, key_pub, hostname) = item['key'].split(' ')
            if len(key_pub) > 30:
                item['key'] = '%s %s... %s' % (
                    key_type,
                    key_pub[:30],
                    hostname
                )

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
