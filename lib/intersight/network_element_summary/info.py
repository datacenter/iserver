class NetworkElementSummaryInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']

        if managed_object['AlarmSummary']['Warning'] == 0 and managed_object['AlarmSummary']['Critical'] == 0:
            if managed_object['AlarmSummary']['Info'] == 0:
                info['Health'] = 'Healthy'
                info['HealthSummary'] = 'Healthy'
                info['__Output']['HealthSummary'] = 'Green'
            else:
                info['Health'] = 'Warnings'
                info['HealthSummary'] = 'Healthy (%s)' % (managed_object['AlarmSummary']['Info'])
                info['__Output']['HealthSummary'] = 'Blue'

        if managed_object['AlarmSummary']['Warning'] > 0 and managed_object['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Warnings'
            info['HealthSummary'] = 'Warnings (%s)' % (managed_object['AlarmSummary']['Warning'])
            info['__Output']['HealthSummary'] = 'Yellow'

        if managed_object['AlarmSummary']['Critical'] > 0:
            info['Health'] = 'Critical'
            info['HealthSummary'] = 'Critical (%s)' % (managed_object['AlarmSummary']['Critical'])
            info['__Output']['HealthSummary'] = 'Red'

        info['ConnectionStatus'] = managed_object['ConnectionStatus']
        info['Dn'] = managed_object['Dn']
        info['Model'] = managed_object['Model']
        info['NumEtherPorts'] = managed_object['NumEtherPorts']
        info['NumEtherPortsConfigured'] = managed_object['NumEtherPortsConfigured']
        info['NumEtherPortsLinkUp'] = managed_object['NumEtherPortsLinkUp']
        info['NumEtherPortsSummary'] = '%s/%s/%s' % (
            info['NumEtherPortsLinkUp'],
            info['NumEtherPortsConfigured'],
            info['NumEtherPorts']
        )
        info['OutOfBandIpAddress'] = managed_object['OutOfBandIpAddress']
        info['OutOfBandIpGateway'] = managed_object['OutOfBandIpGateway']
        info['OutOfBandIpMask'] = managed_object['OutOfBandIpMask']
        info['Serial'] = managed_object['Serial']
        info['SwitchId'] = managed_object['SwitchId']
        info['Version'] = managed_object['Version']

        return info
