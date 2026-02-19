from lib import output_helper

from lib.linux.bond.output import LinuxBondOutput
from lib.linux.boot.output import LinuxBootOutput
from lib.linux.chrony.output import LinuxChronyOutput
from lib.linux.container_policy.output import LinuxContainerPolicyOutput
from lib.linux.crictl.output import LinuxCrictlOutput
from lib.linux.huge_pages.output import LinuxHugePagesOutput
from lib.linux.lsblk.output import LinuxLsblkOutput
from lib.linux.lv.output import LinuxLvOutput
from lib.linux.pv.output import LinuxPvOutput
from lib.linux.sysctl.output import LinuxSysctlOutput
from lib.linux.vg.output import LinuxVgOutput


class LinuxOutput(
        LinuxBondOutput,
        LinuxBootOutput,
        LinuxChronyOutput,
        LinuxContainerPolicyOutput,
        LinuxCrictlOutput,
        LinuxHugePagesOutput,
        LinuxLsblkOutput,
        LinuxLvOutput,
        LinuxPvOutput,
        LinuxSysctlOutput,
        LinuxVgOutput
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
        LinuxCrictlOutput.__init__(self)
        LinuxHugePagesOutput.__init__(self)
        LinuxLsblkOutput.__init__(self)
        LinuxLvOutput.__init__(self)
        LinuxPvOutput.__init__(self)
        LinuxSysctlOutput.__init__(self)
        LinuxVgOutput.__init__(self)

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

    def add_id(self, items):
        index = 1
        for item in items:
            item['__id__'] = index
            index += 1
        return items
    
    def my_table(self, items, info):
        if items is None:
            items = []

        headers = ['ID']
        order = ['__id__']
        for key in info:
            headers.append(key[0])
            order.append(key[1])

        items = self.add_id(items)

        expand = []
        if len(items) > 0:
            for key in order:
                if isinstance(items[0][key.split('.')[0]], list):
                    expand.append(key.split('.')[0])

        for item in items:
            for key in expand:
                if len(item[key]) == 0:
                    item[key].append('---')
                    
        if len(expand) == 0:
            self.my_output.my_table(
                items,
                order=order,
                headers=headers,
                row_separator=False,
                allow_order_subkeys=True,
                cast_none=True,
                underline=True,
                table=True
            )
        else:
            self.my_output.my_table(
                self.my_output.expand_lists(
                    items,
                    order,
                    expand
                ),
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                cast_none=True,
                underline=True,
                table=True
            )

    def print_interfaces(self, info):
        self.my_table(
            info,
            [
                ['Index', 'index'],
                ['Name', 'name'],
                ['Flags', 'flags'],
                ['MTU', 'mtu'],
                ['State', 'state'],
                ['MAC', 'mac']
            ]
        )
        