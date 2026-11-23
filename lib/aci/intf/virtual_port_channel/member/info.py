class InterfaceVirtualPortChannelMemberInfo():
    def __init__(self):
        self.interface_vpc_members = {}

    def get_interface_virtual_port_channel_member_info(self, managed_object):
        keys = [
            'accBndlGrpDn',
            'cfgdAccessVlan',
            'cfgdTrunkVlans',
            'cfgdVlans',
            'compatSt',
            'descr',
            'fabEncMismatchVlans',
            'fabEncMismatchVlansSet',
            'id',
            'localOperSt',
            'name',
            'pcMode',
            'peerCfgdVlans',
            'peerUpVlans',
            'remoteOperSt',
            'suspVlans',
            'upVlans',
            'usage'
        ]
        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['localOperSt'] == 'up':
            info['__Output']['localOperSt'] = 'Green'
        else:
            info['__Output']['localOperSt'] = 'Red'

        if info['remoteOperSt'] == 'up':
            info['__Output']['remoteOperSt'] = 'Green'
        else:
            info['__Output']['remoteOperSt'] = 'Red'

        info['__Output']['domainId'] = 'Blue'
        info['__Output']['id'] = 'Blue'

        for key in ['cfgdTrunkVlans', 'cfgdVlans', 'upVlans', 'suspVlans', 'peerCfgdVlans', 'peerUpVlans']:
            info['%sT' % (key)] = []
            if len(info[key]) > 0:
                info['%sT' % (key)] = info[key].split(',')
            if len(info['%sT' % (key)]) == 0:
                info['%sT' % (key)].append('--')

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def add_interface_virtual_port_channel_members_summary(self, info):
        info['localMemberUp'] = 0
        info['localMemberDown'] = 0
        info['peerMemberUp'] = 0
        info['peerMemberDown'] = 0

        for member in info['member']:
            if member['localOperSt'] == 'up':
                info['localMemberUp'] = info['localMemberUp'] + 1
            else:
                info['localMemberDown'] = info['localMemberDown'] + 1

            if member['remoteOperSt'] == 'up':
                info['peerMemberUp'] = info['peerMemberUp'] + 1
            else:
                info['peerMemberDown'] = info['peerMemberDown'] + 1

        info['localMemberSummary'] = '%s/%s' % (
            info['localMemberUp'],
            len(info['member'])
        )

        info['peerMemberSummary'] = '%s/%s' % (
            info['peerMemberUp'],
            len(info['member'])
        )

        info['memberSt'] = 'up'
        if info['localMemberUp'] == len(info['member']):
            info['__Output']['localMemberSummary'] = 'Green'
        else:
            info['__Output']['localMemberSummary'] = 'Red'
            info['memberSt'] = 'down'

        if info['peerMemberUp'] == len(info['member']):
            info['__Output']['peerMemberSummary'] = 'Green'
        else:
            info['__Output']['peerMemberSummary'] = 'Red'
            info['memberSt'] = 'down'

        return info
