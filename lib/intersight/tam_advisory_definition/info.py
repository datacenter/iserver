class TamAdvisoryDefinitionInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'AdvisoryId',
            'CreateTime',
            'DatePublished',
            'DateUpdated',
            'Description',
            'ExternalUrl',
            'Moid',
            'Name',
            'Recommendation',
            'Workaround'
        ]

        info = {}
        for key in keys:
            info[key] = managed_object[key]

        info['Urls'] = []
        info['Urls'].append(
            managed_object['ExternalUrl']
        )

        info['__Output'] = {}
        info['__Output']['Severity'] = None
        info['Severity'] = managed_object['Severity']['Level']
        if info['Severity'] == 'high':
            info['__Output']['Severity'] = 'Red'

        return info
