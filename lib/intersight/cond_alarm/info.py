class CondAlarmInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['AffectedType'] = managed_object['AffectedMo']['ObjectType']
        info['AffectedMoid'] = managed_object['AffectedMo']['Moid']
        info['AffectedName'] = managed_object['AffectedMoDisplayName']
        info['AncestorMoId'] = managed_object['AncestorMoId']
        info['AncestorMoType'] = managed_object['AncestorMoType']
        info['CreateTime'] = managed_object['CreateTime']
        info['Description'] = managed_object['Description']
        info['Acknowledge'] = managed_object['Acknowledge']
        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']
        info['Code'] = managed_object['Code']

        info['Severity'] = managed_object['Severity']
        if info['Severity'] == 'Critical':
            info['__Output']['Severity'] = 'Red'

        if info['Severity'] == 'Warning':
            info['__Output']['Severity'] = 'Yellow'

        if info['Severity'] == 'Info':
            info['__Output']['Severity'] = 'Blue'

        return info
