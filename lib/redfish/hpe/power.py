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
        for key in power_control_data['PowerMetrics']:
            properties['Data']['PowerControl'][key] = power_control_data['PowerMetrics'][key]

        # {
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#PowerSupplies/0",
        #     "FirmwareVersion": "1.00",
        #     "LastPowerOutputWatts": 89,
        #     "LineInputVoltage": 206,
        #     "LineInputVoltageType": "ACHighLine",
        #     "Manufacturer": "DELTA",
        #     "MemberId": "0",
        #     "Model": "865438-B21",
        #     "Name": "HpeServerPowerSupply",
        #     "Oem": {
        #         "Hpe": {
        #             "@odata.context": "/redfish/v1/$metadata#HpeServerPowerSupply.HpeServerPowerSupply",
        #             "@odata.type": "#HpeServerPowerSupply.v2_0_0.HpeServerPowerSupply",
        #             "AveragePowerOutputWatts": 89,
        #             "BayNumber": 1,
        #             "HotplugCapable": true,
        #             "MaxPowerOutputWatts": 96,
        #             "Mismatched": false,
        #             "PowerSupplyStatus": {
        #                 "State": "Ok"
        #             },
        #             "iPDUCapable": false
        #         }
        #     },
        #     "PowerCapacityWatts": 800,
        #     "PowerSupplyType": "AC",
        #     "SerialNumber": "5WBYE0D4DEF1FM",
        #     "SparePartNumber": "866793-001",
        #     "Status": {
        #         "Health": "OK",
        #         "State": "Enabled"
        #     }
        # },
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

    def print_template_power_consumption_properties(self, properties):
        keys = [
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts'
        ]

        headers = [
            'Current',
            'Min',
            'Average',
            'Max'
        ]

        self.my_output.dictionary(
            properties['Data']['PowerControl'],
            title='Power Consumption (Watt)',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_power_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'LastPowerOutputWatts',
            'LineInputVoltage'
        ]

        headers = [
            'PSU Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (V)'
        ]

        self.my_output.my_table(
            properties['Data']['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_properties(self, properties):
        self.print_template_power_consumption_properties(properties)
        self.print_template_power_supply_properties(properties)
