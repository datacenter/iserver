class RedfishEndpointFabricInterconnectTemplatePowerServer():
    def __init__(self):
        pass

    def get_server_chassis_properties(self):
        if self.is_cache_enabled():
            return self.cache['extra']['Power']

        server_inventory = self.get_server_inventory(self.get_system_id())
        if server_inventory is None:
            return None

        chassis_power = self.get_template_power_chassis_properties(
            inventory_type='Chassis',
            inventory_id=server_inventory['Chassis']['Iom1']
        )

        return chassis_power

    def get_server_power_utilization(self):
        server_inventory = self.get_server_inventory(self.get_system_id())
        if server_inventory is None:
            return None

        chassis_power = self.get_server_chassis_properties()
        if chassis_power is None:
            return None

        info = {}
        for blade in chassis_power['Blade']:
            if blade['MemberId'] == server_inventory['BladeId']:
                keys = [
                    'MaxPowerWatts',
                    'MinPowerWatts',
                    'PowerProfileMaxWatts',
                    'PowerProfileMinWatts',
                    'PowerMetrics',
                    'AverageConsumedWatts',
                    'CurrentConsumedWatts',
                    'IntervalInMsec',
                    'MaxConsumedWatts',
                    'MinConsumedWatts'
                ]
                for key in keys:
                    if key in blade:
                        info[key] = blade[key]

        return info

    def get_template_power_server_properties(self):
        uri = 'Chassis/SYSTEM_ID/Power'
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['Data'] = {}
        properties['Data']['PowerControl'] = {}

        # "PowerControl": [
        #     {
        #         "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power#/PowerControl/0",
        #         "MemberId": "0",
        #         "Name": "POWER_USAGE",
        #         "PowerConsumedWatts": 253
        #     }
        # ],
        power_control_data = data['PowerControl'][0]
        properties['Data']['PowerControl']['PowerConsumedWatts'] = power_control_data['PowerConsumedWatts']

        server_power_utilization = self.get_server_power_utilization()
        if server_power_utilization is not None:
            for key in server_power_utilization:
                properties['Data']['PowerControl'][key] = server_power_utilization[key]

        # "Voltages": [
        #     {
        #         "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Power#/Voltages/0",
        #         "LowerThresholdFatal": 10.79699993133545,
        #         "MemberId": "0",
        #         "Name": "P12V",
        #         "PhysicalContext": "PowerSupply",
        #         "ReadingVolts": 12.095000267028809,
        #         "Status": {
        #             "Health": "OK",
        #             "State": "Enabled"
        #         },
        #         "UpperThresholdCritical": 12.6850004196167,
        #         "UpperThresholdFatal": 13.156999588012695
        #     }
        # ],
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
        # properties['PowerSupply'] = []
        # for power_supply in data['PowerSupplies']:
        #     power_supply_info = {}
        #     power_supply_info['Name'] = power_supply['Name']
        #     power_supply_info['Model'] = power_supply['Model']
        #     power_supply_info['SerialNumber'] = power_supply['SerialNumber']
        #     power_supply_info['PartNumber'] = power_supply['PartNumber']
        #     power_supply_info['SparePartNumber'] = power_supply['SparePartNumber']
        #     power_supply_info['Manufacturer'] = power_supply['Manufacturer']
        #     power_supply_info['FirmwareVersion'] = power_supply['FirmwareVersion']
        #     power_supply_info['State'] = power_supply['Status']['State']
        #     power_supply_info['Health'] = power_supply['Status']['Health']
        #     power_supply_info['PowerSupplyType'] = power_supply['PowerSupplyType']
        #     power_supply_info['PowerOutputWatts'] = power_supply['PowerOutputWatts']
        #     power_supply_info['LastPowerOutputWatts'] = power_supply['LastPowerOutputWatts']
        #     power_supply_info['PowerInputWatts'] = power_supply['PowerInputWatts']
        #     for input_range in power_supply['InputRanges']:
        #         for key in input_range:
        #             if key != 'InputType':
        #                 power_supply_info[key] = input_range[key]

        #     properties['PowerSupply'].append(power_supply_info)

        properties['Summary'] = {}
        properties['Summary']['Source'] = 'Redfish'
        properties['Summary']['PowerNow'] = properties['Data']['PowerControl']['PowerConsumedWatts']
        properties['Summary']['PowerMin'] = properties['Data']['PowerControl']['MinConsumedWatts']
        properties['Summary']['PowerAvg'] = properties['Data']['PowerControl']['AverageConsumedWatts']
        properties['Summary']['PowerMax'] = properties['Data']['PowerControl']['MaxConsumedWatts']

        return properties
