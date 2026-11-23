class VpcStateInfo():
    def __init__(self):
        self.vpc_state = None

    def get_vpc_state_info(self, vpc_state_mo):
        if vpc_state_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        keys = [
            'vpc-domain-id',
            'vpc-peer-status',
            'vpc-peer-status-reason',
            'vpc-peer-keepalive-status',
            'vpc-peer-consistency',
            'vpc-per-vlan-peer-consistency',
            'vpc-peer-consistency-status',
            'vpc-type-2-consistency',
            'vpc-type-2-consistency-status',
            'vpc-role',
            'num-of-vpcs',
            'peer-gateway',
            'dual-active-excluded-vlans',
            'vpc-graceful-consistency-check-status',
            'vpc-auto-recovery-status',
            'vpc-delay-restore-status',
            'vpc-delay-restore-svi-status',
            'vpc-delay-restore-orphan-port-status',
            'operational-l3-peer',
            'virtual-peerlink'
        ]
        for key in keys:
            info[key] = None
            if key in vpc_state_mo:
                info[key] = vpc_state_mo[key]

        info['peer'] = []
        if 'TABLE_peerlink' in vpc_state_mo:
            if 'ROW_peerlink' in vpc_state_mo['TABLE_peerlink']:
                if isinstance(vpc_state_mo['TABLE_peerlink']['ROW_peerlink'], dict):
                    item = {}
                    item['id'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['peer-link-id']
                    item['ifindex'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['peerlink-ifindex']
                    item['state'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['peer-link-port-state']
                    item['vlan'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['peer-up-vlan-bitset'].split(',')
                    info['peer'].append(
                        item
                    )
                if isinstance(vpc_state_mo['TABLE_peerlink']['ROW_peerlink'], list):
                    for item_mo in vpc_state_mo['TABLE_peerlink']['ROW_peerlink']:
                        item = {}
                        item['id'] = item_mo['peer-link-id']
                        item['ifindex'] = item_mo['peerlink-ifindex']
                        item['state'] = item_mo['peer-link-port-state']
                        item['vlan'] = item_mo['peer-up-vlan-bitset'].split(',')
                        info['peer'].append(
                            item
                        )

        info['vpc'] = []
        if 'TABLE_vpc' in vpc_state_mo:
            if 'ROW_vpc' in vpc_state_mo['TABLE_vpc']:
                if isinstance(vpc_state_mo['TABLE_vpc']['ROW_vpc'], dict):
                    item = {}
                    item['id'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-id']
                    item['ifindex'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-ifindex']
                    item['state'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-port-state']
                    item['peerlink'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-thru-peerlink']
                    item['consistency'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-consistency']
                    item['consistent'] = False
                    if vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['vpc-consistency-status'] == 'SUCCESS':
                        item['consistent'] = True
                    item['vlan'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['up-vlan-bitset'].split(',')
                    item['es'] = vpc_state_mo['TABLE_peerlink']['ROW_peerlink']['es-attr']
                    info['vpc'].append(
                        item
                    )
                if isinstance(vpc_state_mo['TABLE_vpc']['ROW_vpc'], list):
                    for item_mo in vpc_state_mo['TABLE_vpc']['ROW_vpc']:
                        item = {}
                        item['id'] = item_mo['vpc-id']
                        item['ifindex'] = item_mo['vpc-ifindex']
                        item['state'] = item_mo['vpc-port-state']
                        item['peerlink'] = item_mo['vpc-thru-peerlink']
                        item['consistency'] = item_mo['vpc-consistency']
                        item['consistent'] = False
                        if item_mo['vpc-consistency-status'] == 'SUCCESS':
                            item['consistent'] = True
                        item['vlan'] = item_mo['up-vlan-bitset'].split(',')
                        item['es'] = item_mo['es-attr']
                        info['vpc'].append(
                            item
                        )

        return info

    def get_vpc_state(self, cache_enabled=True):
        if not self.is_feature_enabled('vpc'):
            return None

        vpc_state_mo = self.get_vpc_state_mo(cache_enabled=cache_enabled)
        if vpc_state_mo is None:
            self.log.error(
                'get_vpc_state',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_vpc_state_info(vpc_state_mo)
