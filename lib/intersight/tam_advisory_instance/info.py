class TamAdvisoryInstanceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['AdvisoryMoid'] = managed_object['Advisory']['Moid']
        info['AffectedObjectType'] = managed_object['AffectedObjectType']
        info['AffectedObjectMoid'] = managed_object['AffectedObjectMoid']
        info['CreateTime'] = managed_object['CreateTime']
        info['Moid'] = managed_object['Moid']

        return info
