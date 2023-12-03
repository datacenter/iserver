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

        return info
