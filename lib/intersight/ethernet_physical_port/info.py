class EthernetPhysicalPortInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['Name'] = '%s/%s' % (
            managed_object['SlotId'],
            managed_object['PortId']
        )
        info['AdminState'] = managed_object['AdminState']
        info['AggregatePortId'] = managed_object['AggregatePortId']
        info['MacAddress'] = managed_object['MacAddress']
        info['Mode'] = managed_object['Mode']
        info['OperSpeed'] = managed_object['OperSpeed']
        info['OperState'] = managed_object['OperState']
        info['PortId'] = managed_object['PortId']
        info['PortChannelId'] = managed_object['PortChannelId']
        info['Role'] = managed_object['Role']
        info['SlotId'] = managed_object['SlotId']
        info['SwitchId'] = managed_object['SwitchId']
        info['TransceiverType'] = managed_object['TransceiverType']

        if 'AcknowledgedPeerInterface' in managed_object:
            if managed_object['AcknowledgedPeerInterface'] is None:
                info['Peer'] = None
            else:
                info['Peer'] = {}

                keys = [
                    'AdminState',
                    'Dn',
                    'EpDn',
                    'ExtEthInterfaceId',
                    'MacAddress',
                    'Moid',
                    'OperState',
                    'PeerDn',
                    'PeerPortId',
                    'PeerSlotId',
                    'SlotId',
                    'PortId',
                    'SwitchId'
                ]
                for key in keys:
                    if key not in managed_object['AcknowledgedPeerInterface']:
                        info['Peer'][key] = None
                        continue

                    info['Peer'][key] = managed_object['AcknowledgedPeerInterface'][key]

                info['Peer']['ServerMoid'] = None
                info['Peer']['ChassisMoid'] = None
                info['Peer']['ServerName'] = None

                info['Peer']['ServerPort'] = None
                info['Peer']['Adapter'] = None
                info['Peer']['IO'] = None

                if managed_object['AcknowledgedPeerInterface'] is not None and 'Ancestors' in managed_object['AcknowledgedPeerInterface']:
                    for ancestor_mo in managed_object['AcknowledgedPeerInterface']['Ancestors']:
                        if ancestor_mo['ObjectType'] == 'compute.RackUnit':
                            info['Peer']['ServerMoid'] = ancestor_mo['Moid']
                            info['Peer']['ServerName'] = ancestor_mo['Name']

                        if ancestor_mo['ObjectType'] == 'equipment.Chassis':
                            info['Peer']['ChassisMoid'] = ancestor_mo['Moid']
                            info['Peer']['ServerName'] = ancestor_mo['Name']

                        if ancestor_mo['ObjectType'] == 'equipment.IoCard':
                            keys = [
                                'ConnectionPath',
                                'ConnectionStatus',
                                'Description',
                                'DeviceMoId',
                                'Dn',
                                'Model',
                                'ModuleId',
                                'Moid',
                                'OperState',
                                'PartNumber',
                                'Pid',
                                'Presence',
                                'Serial',
                                'Side',
                                'Sku',
                                'Version'
                            ]
                            info['Peer']['IO'] = {}
                            for key in keys:
                                if key not in ancestor_mo:
                                    info['Peer']['IO'][key] = None
                                    continue

                                info['Peer']['IO'][key] = ancestor_mo[key]

                            info['Peer']['IO']['HostPorts'] = []
                            for host_port_mo in ancestor_mo['HostPorts']:
                                info['Peer']['IO']['HostPorts'].append(
                                    host_port_mo['Moid']
                                )

                            info['Peer']['ServerPort'] = 'IO Card %s/%s' % (
                                info['Peer']['SlotId'],
                                info['Peer']['PortId']
                            )

                        if ancestor_mo['ObjectType'] == 'adapter.Unit':
                            keys = [
                                'AdapterId',
                                'Dn',
                                'Moid',
                                'PartNumber',
                                'PciSlot',
                                'Power',
                                'Presence',
                                'Serial'
                            ]
                            info['Peer']['Adapter'] = {}
                            for key in keys:
                                if key not in ancestor_mo:
                                    info['Peer']['Adapter'][key] = None
                                    continue

                                info['Peer']['Adapter'][key] = ancestor_mo[key]

                            info['Peer']['Adapter']['RegisteredDevice'] = ','.join(ancestor_mo['RegisteredDevice']['DeviceHostname'])
                            info['Peer']['Adapter']['RegisteredMoid'] = ancestor_mo['RegisteredDevice']['Moid']
                            info['Peer']['ServerPort'] = 'Adapter %s' % (info['Peer']['Adapter']['AdapterId'])

        return info
