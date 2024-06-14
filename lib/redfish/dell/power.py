class RedfishEndpointDellTemplatePower():
    def __init__(self):
        pass

    def get_template_power_properties(self):
        uri = '/redfish/v1/Chassis/System.Embedded.1/Power'
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['Data'] = {}
        properties['Data']['PowerControl'] = {}

        # {
        #     "PhysicalContext": "PowerSupply",
        #     "PowerMetrics": {
        #         "MinConsumedWatts": 186,
        #         "AverageConsumedWatts": 349,
        #         "MaxConsumedWatts": 495
        #     },
        #     "MemberId": "1",
        #     "PowerLimit": {
        #         "LimitException": "NoAction"
        #     },
        #     "PowerConsumedWatts": 360,
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/1"
        # }
        power_control_data = data['PowerControl'][0]
        properties['Data']['PowerControl']['PowerConsumedWatts'] = power_control_data['PowerConsumedWatts']
        properties['Data']['PowerControl']['LimitException'] = power_control_data['PowerLimit']['LimitException']
        for key in power_control_data['PowerMetrics']:
            properties['Data']['PowerControl'][key] = power_control_data['PowerMetrics'][key]

        # {
        #     "PhysicalContext": "PowerSupply",
        #     "SensorNumber": 48,
        #     "MemberId": "1",
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/PSU1_VOUT",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     },
        #     "UpperThresholdCritical": 14,
        #     "Name": "PSU1_VOUT",
        #     "ReadingVolts": 12.2
        # },
        properties['Data']['Voltage'] = []
        for voltage in data['Voltages']:
            voltage_info = {}
            voltage_info['Name'] = voltage['Name']
            voltage_info['ReadingVolts'] = voltage['ReadingVolts']
            voltage_info['UpperThresholdCritical'] = voltage['UpperThresholdCritical']
            voltage_info['PhysicalContext'] = voltage['PhysicalContext']
            voltage_info['State'] = voltage['Status']['State']
            voltage_info['Health'] = voltage['Status']['Health']
            properties['Data']['Voltage'].append(voltage_info)

        # {
        #     "SerialNumber": "LIT241244RQ",
        #     "InputRanges": [
        #         {
        #             "InputType": "AC",
        #             "OutputWattage": 1050,
        #             "MaximumFrequencyHz": 63,
        #             "MaximumVoltage": 264,
        #             "MinimumVoltage": 90,
        #             "MinimumFrequencyHz": 47
        #         }
        #     ],
        #     "FirmwareVersion": "10062019",
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
        #     "PowerOutputWatts": 171,
        #     "LineInputVoltage": 229,
        #     "Name": "PSU1",
        #     "PowerInputWatts": 186,
        #     "Manufacturer": "Cisco Systems Inc",
        #     "LastPowerOutputWatts": 171,
        #     "MemberId": "1",
        #     "PartNumber": "341-0638-03",
        #     "PowerSupplyType": "AC",
        #     "Model": "PS-2112-9S-LF",
        #     "SparePartNumber": "341-0638-03",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     }
        # },
        properties['Data']['PowerSupply'] = []
        for power_supply in data['PowerSupplies']:
            power_supply_info = {}
            power_supply_info['Name'] = power_supply['Name']
            power_supply_info['Model'] = power_supply['Model']
            power_supply_info['SerialNumber'] = power_supply['SerialNumber']
            power_supply_info['PartNumber'] = power_supply['PartNumber']
            power_supply_info['SparePartNumber'] = power_supply['SparePartNumber']
            power_supply_info['Manufacturer'] = power_supply['Manufacturer']
            power_supply_info['FirmwareVersion'] = power_supply['FirmwareVersion']
            power_supply_info['State'] = power_supply['Status']['State']
            power_supply_info['Health'] = power_supply['Status']['Health']
            power_supply_info['PowerSupplyType'] = power_supply['PowerSupplyType']
            power_supply_info['PowerOutputWatts'] = power_supply['PowerOutputWatts']
            power_supply_info['LastPowerOutputWatts'] = power_supply['LastPowerOutputWatts']
            power_supply_info['PowerInputWatts'] = power_supply['PowerInputWatts']
            for input_range in power_supply['InputRanges']:
                for key in input_range:
                    if key != 'InputType':
                        power_supply_info[key] = input_range[key]

            properties['Data']['PowerSupply'].append(power_supply_info)

        properties['Summary'] = {}
        properties['Summary']['Source'] = 'Redfish'
        properties['Summary']['PowerNow'] = properties['Data']['PowerControl']['PowerConsumedWatts']
        properties['Summary']['PowerMin'] = properties['Data']['PowerControl']['MinConsumedWatts']
        properties['Summary']['PowerAvg'] = properties['Data']['PowerControl']['AverageConsumedWatts']
        properties['Summary']['PowerMax'] = properties['Data']['PowerControl']['MaxConsumedWatts']

        return properties
