from lib import output_helper

from lib.linux.bond.output import LinuxBondOutput
from lib.linux.boot.output import LinuxBootOutput
from lib.linux.chrony.output import LinuxChronyOutput
from lib.linux.container_policy.output import LinuxContainerPolicyOutput
from lib.linux.huge_pages.output import LinuxHugePagesOutput
from lib.linux.sysctl.output import LinuxSysctlOutput


class LinuxOutput(
    LinuxBondOutput,
    LinuxBootOutput,
    LinuxChronyOutput,
    LinuxContainerPolicyOutput,
    LinuxHugePagesOutput,
    LinuxSysctlOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        LinuxBondOutput.__init__(self)
        LinuxBootOutput.__init__(self)
        LinuxChronyOutput.__init__(self)
        LinuxContainerPolicyOutput.__init__(self)
        LinuxHugePagesOutput.__init__(self)
        LinuxSysctlOutput.__init__(self)

    def print_linux_servers(self, servers, show_password=True):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(
                log_id=self.log_id,
                verbose=False,
                debug=False
            )

        servers = sorted(servers, key=lambda i: i['name'])
        if not show_password:
            for server in servers:
                if server['password'] is not None:
                    server['password'] = '******'

        for server in servers:
            server['__Output'] = {}
            if server['cache']['enabled']:
                server['cache']['enabledTick'] = '\u2713'
                server['__Output']['cache.enabledTick'] = 'Green'
            else:
                server['cache']['enabledTick'] = '\u2717'
                server['__Output']['cache.enabledTick'] = 'Red'

            if server['password'] is None:
                server['password'] = '--'

            if server['key'] is None:
                server['key'] = '--'

        order = [
            'name',
            'address',
            'username',
            'password',
            'key',
            'cache.enabledTick',
            'cache.ttlT',
            'cache.directory'
        ]

        headers = [
            'Name',
            'IP',
            'Username',
            'Password',
            'Key',
            'Cache',
            'TTL',
            'Directory'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
