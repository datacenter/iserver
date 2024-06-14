class GraphicsControllerInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        keys = [
            'ControllerId',
            'Dn',
            'Model',
            'Moid',
            'PciAddr',
            'PciSlot',
            'Presence',
            'Serial',
            'Vendor'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['Pid'] = info['Model']
        info['SlotId'] = info['PciSlot']

        info['ChassisMoid'] = None
        info['BladeMoid'] = None
        info['PciNodeId'] = None
        info['GraphicsCardId'] = None

        for ancestor_mo in managed_object['Ancestors']:
            if ancestor_mo['ObjectType'] == 'graphics.Card':
                info['GraphicsCardId'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'pci.Node':
                info['PciNodeId'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'compute.Blade':
                info['BladeMoid'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'equipment.Chassis':
                info['ChassisMoid'] = ancestor_mo['Moid']

        return info
