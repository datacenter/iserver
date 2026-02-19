class RedfishEndpointHpeTemplatePower():
    def __init__(self):
        pass

    def get_template_power_properties(self):
        uri = '/redfish/v1/Chassis/1/Power'
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['Data'] = {}
        properties['Data']['PowerControl'] = {}

        power_control_data = data['PowerControl'][0]
        properties['Data']['PowerControl']['PowerConsumedWatts'] = power_control_data['PowerConsumedWatts']
        for key in power_control_data['PowerMetrics']:
            properties['Data']['PowerControl'][key] = power_control_data['PowerMetrics'][key]

        properties['Data']['PowerSupply'] = []
        for power_supply in data['PowerSupplies']:
            power_supply_info = {}
            power_supply_info['Name'] = power_supply['Name']
            power_supply_info['Model'] = power_supply['Model']
            power_supply_info['SerialNumber'] = power_supply['SerialNumber']
            power_supply_info['SparePartNumber'] = power_supply['SparePartNumber']
            power_supply_info['Manufacturer'] = power_supply['Manufacturer']
            power_supply_info['FirmwareVersion'] = power_supply['FirmwareVersion']
            power_supply_info['State'] = power_supply['Status']['State']
            power_supply_info['Health'] = power_supply['Status']['Health']
            power_supply_info['PowerSupplyType'] = power_supply['PowerSupplyType']
            power_supply_info['LastPowerOutputWatts'] = power_supply['LastPowerOutputWatts']
            power_supply_info['LineInputVoltage'] = power_supply['LineInputVoltage']
            properties['Data']['PowerSupply'].append(power_supply_info)

        properties['Summary'] = {}
        properties['Summary']['Source'] = 'Redfish'
        properties['Summary']['PowerNow'] = properties['Data']['PowerControl']['PowerConsumedWatts']
        properties['Summary']['PowerMin'] = properties['Data']['PowerControl']['MinConsumedWatts']
        properties['Summary']['PowerAvg'] = properties['Data']['PowerControl']['AverageConsumedWatts']
        properties['Summary']['PowerMax'] = properties['Data']['PowerControl']['MaxConsumedWatts']

        return properties
