class RedfishEndpointFabricInterconnectTemplateThermalServer():
    def __init__(self):
        pass

    def get_template_thermal_server_properties(self):
        uri = 'Chassis/SYSTEM_ID/Thermal'
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['State'] = data['Status']['State']
        properties['Health'] = data['Status']['Health']

        properties['Temperature'] = []
        for sensor in data['Temperatures']:
            sensor_info = {}
            sensor_info['State'] = sensor['Status']['State']
            sensor_info['Health'] = sensor['Status']['Health']
            sensor_info['Name'] = sensor['Name']
            sensor_info['PhysicalContext'] = sensor['PhysicalContext']
            sensor_info['ReadingCelsius'] = sensor['ReadingCelsius']
            sensor_info['UpperThresholdCritical'] = ''
            if 'UpperThresholdCritical' in sensor:
                sensor_info['UpperThresholdCritical'] = sensor['UpperThresholdCritical']
            sensor_info['UpperThresholdFatal'] = ''
            if 'UpperThresholdFatal' in sensor:
                sensor_info['UpperThresholdFatal'] = sensor['UpperThresholdFatal']
            properties['Temperature'].append(sensor_info)

        properties['Temperature'] = sorted(properties['Temperature'], key=lambda i: i['Name'])

        return properties
