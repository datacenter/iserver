from lib import filter_helper


class RedfishEndpointFabricInterconnectTemplatePowerServer():
    def __init__(self):
        pass

    def get_server_chassis_properties(self):
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

        power_control_data = data['PowerControl'][0]
        properties['Data']['PowerControl']['PowerConsumedWatts'] = filter_helper.get(power_control_data, 'PowerConsumedWatts')

        server_power_utilization = self.get_server_power_utilization()
        if server_power_utilization is not None:
            for key in server_power_utilization:
                properties['Data']['PowerControl'][key] = server_power_utilization[key]

        properties['Data']['Voltage'] = []
        for voltage in data['Voltages']:
            voltage_info = {}
            voltage_info['Name'] = filter_helper.get(voltage, 'Name')
            voltage_info['ReadingVolts'] = filter_helper.get(voltage, 'ReadingVolts')
            voltage_info['UpperThresholdCritical'] = filter_helper.get(voltage, 'UpperThresholdCritical')
            voltage_info['PhysicalContext'] = filter_helper.get(voltage, 'PhysicalContext')
            voltage_info['State'] = filter_helper.get(voltage, 'Status:State')
            voltage_info['Health'] = filter_helper.get(voltage, 'Status:Health')
            properties['Data']['Voltage'].append(voltage_info)

        properties['Summary'] = {}
        properties['Summary']['Source'] = 'Redfish'
        properties['Summary']['PowerNow'] = filter_helper.get(properties, 'Data:PowerControl:PowerConsumedWatts')
        properties['Summary']['PowerMin'] = filter_helper.get(properties, 'Data:PowerControl:MinConsumedWatts')
        properties['Summary']['PowerAvg'] = filter_helper.get(properties, 'Data:PowerControl:AverageConsumedWatts')
        properties['Summary']['PowerMax'] = filter_helper.get(properties, 'Data:PowerControl:MaxConsumedWatts')

        return properties
