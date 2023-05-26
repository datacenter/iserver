class PolicyInterfaceMcpOutput():
    def __init__(self):
        pass

    def print_policy_interface_mcp(self, info, verbose=False):
        if info['mcpMode'] == 'off':
            order = [
                'name',
                'tf',
                'adminSt',
                'mcpModeT',
                'interfaces',
                'references'
            ]

            headers = [
                'Policy Name',
                'TF',
                'Admin State',
                'MCP Mode',
                'Interfaces',
                'Ref Policies'
            ]

        if info['mcpMode'] == 'on':
            order = [
                'name',
                'tf',
                'adminSt',
                'mcpModeT',
                'strictInitDelayTime',
                'strictTxFreq',
                'strictTxFreqMsec',
                'gracePeriod',
                'gracePeriodMsec',
                'interfaces',
                'references'
            ]

            headers = [
                'Policy Name',
                'TF',
                'Admin State',
                'MCP Mode',
                'Initial Delay Time [sec]',
                'Transmission Frequency [sec]',
                'Transmission Frequency [msec]',
                'Grace Period [sec]',
                'Grace Period [msec]',
                'Interfaces',
                'Ref Policies'
            ]

        self.print_policy_interface(
            info,
            'MCP Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_mcp(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'mcpModeT',
            'strictInitDelayTime',
            'strictTxFreq',
            'strictTxFreqMsec',
            'gracePeriod',
            'gracePeriodMsec'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'MCP Mode',
            'Delay Time [sec]',
            'TX Freq [sec]',
            'TX Freq [msec]',
            'Grace Period [sec]',
            'Grace Period [msec]'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_mcp_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt',
            'policy.mcpModeT'
        ]

        headers = [
            'MCP Policy Name',
            'MCP Admin State',
            'MCP Mode'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
