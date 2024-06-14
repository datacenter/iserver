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

        # "@odata.id": "/redfish/v1/Chassis/FCH25337EHM/Thermal#/Temperatures/0",
        # "MemberId": "0",
        # "Name": "TEMP_FRONT",
        # "PhysicalContext": "SystemBoard",
        # "ReadingCelsius": 16,
        # "Status": {
        #     "Health": "OK",
        #     "State": "Enabled"
        # },
        # "UpperThresholdCritical": 45,
        # "UpperThresholdFatal": 50
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

        # {
        #     "RelatedItem": [
        #         {
        #             "@odata.id": "/redfish/v1/Chassis/1"
        #         }
        #     ],
        #     "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN1",
        #     "ReadingUnits": "RPM",
        #     "Reading": 7070,
        #     "PhysicalContext": "Fan",
        #     "MemberId": "1",
        #     "Name": "MOD1_FAN1_SPEED",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     }
        # },
        # properties['Fan'] = []
        # for fan in data['Fans']:
        #     fan_info = {}
        #     fan_info['Name'] = fan['Name']
        #     fan_info['State'] = fan['Status']['State']
        #     fan_info['Health'] = ''
        #     if 'Health' in fan['Status']:
        #         fan_info['Health'] = fan['Status']['Health']
        #     fan_info['PhysicalContext'] = ''
        #     if 'PhysicalContext' in fan:
        #         fan_info['PhysicalContext'] = fan['PhysicalContext']
        #     fan_info['ReadingUnits'] = ''
        #     if 'ReadingUnits' in fan:
        #         fan_info['ReadingUnits'] = fan['ReadingUnits']
        #     fan_info['Reading'] = ''
        #     if 'Reading' in fan:
        #         fan_info['Reading'] = fan['Reading']
        #     fan_info['Value'] = '%s %s' % (fan_info['Reading'], fan_info['ReadingUnits'])
        #     properties['Fan'].append(fan_info)

        # properties['Fan'] = sorted(properties['Fan'], key=lambda i: i['Name'])

        return properties
