class RedfishEndpointFabricInterconnectTemplatePowerChassis():
    def __init__(self):
        pass

    def is_chassis_power_on(self, inventory_type=None, inventory_id=None):
        power_properties = self.get_template_power_chassis_properties(
            inventory_type=inventory_type,
            inventory_id=inventory_id
        )
        if power_properties is None:
            return False

        chassis_power_on = False
        for power_supply in power_properties['Data']['PowerSupply']:
            chassis_power_on = chassis_power_on or power_supply['On']

        return chassis_power_on

    def get_template_power_chassis_properties(self, inventory_type=None, inventory_id=None):
        uri = '%s/Power' % (self.get_chassis_uri())
        data = self.get_properties(
            uri,
            inventory_type=inventory_type,
            inventory_id=inventory_id
        )
        if data is None:
            return None

        properties = {}
        properties['Data'] = {}
        properties['Data']['PowerControl'] = {}
        properties['Data']['PowerControl']['CurrentConsumedWatts'] = 0
        properties['Data']['Blade'] = []
        properties['Data']['PowerSupply'] = []

        for item in data['PowerControl']:
            if item['MemberId'] == 'Chassis':
                # "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Chassis",
                # "MemberId": "Chassis",
                # "Name": "Chassis Power Control",
                # "Oem": {
                #     "Cisco": {
                #         "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                #         "PowerExtendedEnabled": false,
                #         "PowerGridMaxWatts": 3044,
                #         "PowerN+1MaxWatts": 3044,
                #         "PowerN+2MaxWatts": 3044,
                #         "PowerNotRedundantMaxWatts": 6087,
                #         "PowerProfileMaxWatts": 8027,
                #         "PowerProfileMinWatts": 4060,
                #         "PowerRebalanceEnabled": true,
                #         "PowerSaveEnabled": false
                #     }
                # },
                # "PowerLimit": {
                #     "LimitInWatts": null
                # },
                # "Status": {
                #     "Health": "OK",
                #     "State": "Enabled"
                # }
                for key in item['Oem']['Cisco']:
                    if key != '@odata.type':
                        properties['Data']['PowerControl'][key] = item['Oem']['Cisco'][key]

            if item['MemberId'].startswith('Blade'):
                # {
                #     "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/Blade8",
                #     "MemberId": "Blade8",
                #     "Name": "Blade 8 Power Control",
                #     "Oem": {
                #         "Cisco": {
                #             "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
                #             "InitialPowerLimit": {
                #                 "LimitInWatts": 0
                #             },
                #             "PowerAllocationPriority": 3,
                #             "PowerCharacteristics": {
                #                 "MaxPowerWatts": 0,
                #                 "MinPowerWatts": 0,
                #                 "PowerProfileMaxWatts": 0,
                #                 "PowerProfileMinWatts": 0
                #             },
                #             "PowerMetrics": {
                #                 "AverageConsumedWatts": 0,
                #                 "CurrentConsumedWatts": 0,
                #                 "IntervalInMsec": 1000,
                #                 "MaxConsumedWatts": 0,
                #                 "MinConsumedWatts": 0
                #             }
                #         }
                #     },
                #     "PowerLimit": {
                #         "LimitInWatts": 0
                #     },
                #     "Status": {
                #         "Health": "OK",
                #         "State": "Absent"
                #     }
                # },
                blade_info = {}
                blade_info['MemberId'] = item['MemberId']
                blade_info['State'] = item['Status']['State']
                blade_info['Health'] = item['Status']['Health']
                blade_info['PowerLimitInWatts'] = item['PowerLimit']['LimitInWatts']
                for key in item['Oem']['Cisco']['PowerMetrics']:
                    blade_info[key] = item['Oem']['Cisco']['PowerMetrics'][key]
                for key in item['Oem']['Cisco']['PowerCharacteristics']:
                    blade_info[key] = item['Oem']['Cisco']['PowerCharacteristics'][key]
                properties['Data']['Blade'].append(blade_info)

                properties['Data']['PowerControl']['CurrentConsumedWatts'] = properties['Data']['PowerControl']['CurrentConsumedWatts'] + item['Oem']['Cisco']['PowerMetrics']['CurrentConsumedWatts']

        for item in data['PowerSupplies']:
            power_supply_info = {}
            power_supply_info['MemberId'] = item['MemberId']
            power_supply_info['Name'] = item['Name']
            power_supply_info['State'] = item['Status']['State']
            if power_supply_info['State'] == 'Enabled':
                power_supply_info['On'] = True
                power_supply_info['Manufacturer'] = item['Manufacturer']
                power_supply_info['Model'] = item['Model']
                power_supply_info['SerialNumber'] = item['SerialNumber']
            else:
                power_supply_info['On'] = False
                power_supply_info['Manufacturer'] = ''
                power_supply_info['Model'] = ''
                power_supply_info['SerialNumber'] = ''

            properties['Data']['PowerSupply'].append(power_supply_info)

        properties['Summary'] = {}
        properties['Summary']['Source'] = 'Redfish'
        properties['Summary']['PowerNow'] = properties['Data']['PowerControl']['CurrentConsumedWatts']

        return properties
