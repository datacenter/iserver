class RedfishEndpointFabricInterconnectTemplateThermalChassis():
    def __init__(self):
        pass

    def get_template_thermal_chassis_properties(self):
        uri = '%s/Thermal' % (self.get_chassis_uri())
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}

        properties['Temperature'] = []
        for sensor in data['Temperatures']:
            sensor_info = {}
            sensor_info['State'] = sensor['Status']['State']
            sensor_info['Name'] = sensor['Name']
            if sensor_info['State'] == 'Enabled':
                sensor_info['ReadingCelsius'] = sensor['ReadingCelsius']
            else:
                sensor_info['ReadingCelsius'] = ''
            properties['Temperature'].append(sensor_info)

        properties['Temperature'] = sorted(properties['Temperature'], key=lambda i: i['Name'])

        properties['Fan'] = []
        for fan in data['Fans']:
            fan_info = {}
            fan_info['Name'] = fan['Name']
            fan_info['State'] = fan['Status']['State']
            if fan_info['State'] == 'Enabled':
                fan_info['PartNumber'] = fan['PartNumber']
                fan_info['SerialNumber'] = fan['SerialNumber']
                fan_info['Model'] = fan['Model']
                fan_info['Manufacturer'] = fan['Manufacturer']
            else:
                fan_info['PartNumber'] = ''
                fan_info['SerialNumber'] = ''
                fan_info['Model'] = ''
                fan_info['Manufacturer'] = ''

            properties['Fan'].append(fan_info)

        properties['Fan'] = sorted(properties['Fan'], key=lambda i: i['Name'])

        return properties
