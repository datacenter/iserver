class TamSecurityAdvisoryInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'AdvisoryId',
            'BaseScore',
            'CreateTime',
            'CveIds',
            'DatePublished',
            'DateUpdated',
            'Description',
            'ExternalUrl',
            'Moid',
            'Name',
            'OtherRefUrls',
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
        if managed_object['OtherRefUrls'] is not None:
            for url in managed_object['OtherRefUrls']:
                info['Urls'].append(url)

        info['__Output'] = {}
        info['__Output']['Severity'] = None
        info['Severity'] = managed_object['Severity']['Level']
        if info['Severity'] == 'high':
            info['__Output']['Severity'] = 'Red'

        return info
