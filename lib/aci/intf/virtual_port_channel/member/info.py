class InterfaceVirtualPortChannelMemberInfo():
    def __init__(self):
        self.interface_vpc_members = {}

    def add_interface_virtual_port_channel_members_summary(self, info):
        info['localMemberUp'] = 0
        info['localMemberDown'] = 0
        info['peerMemberUp'] = 0
        info['peerMemberDown'] = 0

        for member in info['members']:
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
            len(info['members'])
        )

        info['peerMemberSummary'] = '%s/%s' % (
            info['peerMemberUp'],
            len(info['members'])
        )

        info['memberSt'] = 'up'
        if info['localMemberUp'] == len(info['members']):
            info['__Output']['localMemberSummary'] = 'Green'
        else:
            info['__Output']['localMemberSummary'] = 'Red'
            info['memberSt'] = 'down'

        if info['peerMemberUp'] == len(info['members']):
            info['__Output']['peerMemberSummary'] = 'Green'
        else:
            info['__Output']['peerMemberSummary'] = 'Red'
            info['memberSt'] = 'down'

        return info

    def get_interface_virtual_port_channel_member_info(self, managed_object):
        keys = [
            'cfgdAccessVlan',
            'cfgdTrunkVlans',
            'compatQual',
            'compatQualStr',
            'compatSt',
            'descr',
            'dn',
            'fabEncMismatchVlans',
            'fabEncMismatchVlansSet',
            'fabricPathDn',
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

        return info

    def get_interface_virtual_port_channel_members_info(self, pod_id, node_id, vpc_domain_id):
        key = '%s.%s.%s' % (pod_id, node_id, vpc_domain_id)
        if key in self.interface_vpc_members:
            return self.interface_vpc_members[key]

        interface_vpc_members_mo = self.get_interface_virtual_port_channel_members_mo(pod_id, node_id, vpc_domain_id)
        if interface_vpc_members_mo is None:
            return None

        self.interface_vpc_members[key] = []
        for interface_vpc_member_mo in interface_vpc_members_mo:
            self.interface_vpc_members[key].append(
                self.get_interface_virtual_port_channel_member_info(
                    interface_vpc_member_mo
                )
            )

        return self.interface_vpc_members[key]

    def get_interface_virtual_port_channel_members(self, pod_id, node_id, vpc_domain_id):
        return self.get_interface_virtual_port_channel_members_info(pod_id, node_id, vpc_domain_id)
