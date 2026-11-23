class GraphicsCardInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        keys = [
            'CardId',
            'Description',
            'DeviceId',
            'Dn',
            'FirmwareVersion',
            'GpuId',
            'Model',
            'Moid',
            'NumGpus',
            'OperState',
            'PartNumber',
            'PciSlot',
            'Pid',
            'Presence',
            'Serial',
            'SubDeviceId',
            'SubVendorId',
            'Vendor',
            'VendorId'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['SlotId'] = info['PciSlot']

        info['ChassisMoid'] = None
        info['BladeMoid'] = None
        info['PciNodeId'] = None

        for ancestor_mo in managed_object['Ancestors']:
            if ancestor_mo['ObjectType'] == 'pci.Node':
                info['PciNodeId'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'compute.Blade':
                info['BladeMoid'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'equipment.Chassis':
                info['ChassisMoid'] = ancestor_mo['Moid']

        return info
