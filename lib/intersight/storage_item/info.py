class StorageItemInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'Dn',
            'Moid',
            'Name',
            'Size',
            'Used'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            if key not in managed_object:
                info[key] = None
                continue

            info[key] = managed_object[key]

        if info['Size'] == 'nothing':
            info['Size'] = None
            
        info['UsedT'] = None
        if info['Used'] is not None and isinstance(info['Used'], str):
            if info['Used'] not in ['empty']:
                info['UsedT'] = '%s%%' % (info['Used'])

        return info
