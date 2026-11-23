class PciNodeInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        keys = [
            'ChassisId',
            'Dn',
            'Model',
            'Moid',
            'Presence',
            'Serial',
            'SlotId',
            'Vendor'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['Pid'] = info['Model']

        info['GraphicsCardsMoids'] = []
        if 'GraphicsCards' in managed_object and managed_object['GraphicsCards'] is not None:
            for gcard_mo in managed_object['GraphicsCards']:
                info['GraphicsCardsMoids'].append(
                    gcard_mo['Moid']
                )

        info['NumGraphicsCards'] = len(
            info['GraphicsCardsMoids']
        )

        info['BladeMoid'] = None
        info['ChassisMoid'] = None

        for ancestor_mo in managed_object['Ancestors']:
            if ancestor_mo['ObjectType'] == 'compute.Blade':
                info['BladeMoid'] = ancestor_mo['Moid']

            if ancestor_mo['ObjectType'] == 'compute.equipment.Chassis':
                info['ChassisMoid'] = ancestor_mo['Moid']

        return info
