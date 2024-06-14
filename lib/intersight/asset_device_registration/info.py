class AssetDeviceRegistrationInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['Moid'] = managed_object['Moid']
        info['ClaimedByUserName'] = managed_object['ClaimedByUserName']
        info['ClaimedTime'] = managed_object['ClaimedTime']
        info['PlatformType'] = managed_object['PlatformType']
        info['ConnectorVersion'] = managed_object['ConnectorVersion']
        info['ConnectionStatus'] = managed_object['ConnectionStatus']
        info['DeviceExternalIpAddress'] = managed_object['DeviceExternalIpAddress']
        info['ConnectionStatusLastChangeTime'] = managed_object['ConnectionStatusLastChangeTime']
        if info['ConnectionStatus'] == 'Connected':
            info['__Output']['ConnectionStatus'] = 'Green'
            info['Connected'] = True
        else:
            info['__Output']['ConnectionStatus'] = 'Red'
            info['Connected'] = False

        return info
