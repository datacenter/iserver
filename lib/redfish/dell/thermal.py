class RedfishEndpointDellTemplateThermal():
    def __init__(self):
        pass

    def get_template_thermal_properties(self):
        uri = '/redfish/v1/Chassis/System.Embedded.1/Thermal'
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['Data'] = {}
        properties['Summary'] = {}
        properties['Summary']['FanHealth'] = True
        properties['Summary']['SensorHealth'] = True
        properties['Summary']['HighestTemperature'] = None
        properties['Summary']['SmallestGap'] = None
        properties['Summary']['OverThreshold'] = 0

        # {
        #     "RelatedItem": [
        #         {
        #             "@odata.id": "/redfish/v1/Chassis/1"
        #         }
        #     ],
        #     "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/MLOM_TEMP",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     },
        #     "SensorNumber": 60,
        #     "Name": "MLOM_TEMP",
        #     "PhysicalContext": "NetworkingDevice",
        #     "MemberId": "1",
        #     "UpperThresholdCritical": 90,
        #     "ReadingCelsius": 55
        # },
        properties['Data']['Temperature'] = []
        for sensor in data['Temperatures']:
            sensor_info = {}
            sensor_info['State'] = sensor['Status']['State']
            sensor_info['Health'] = ''
            if 'Health' in sensor['Status']:
                sensor_info['Health'] = sensor['Status']['Health']
                if sensor_info['State'] == 'Enabled':
                    if sensor_info['Health'].lower() != 'ok':
                        properties['Summary']['SensorHealth'] = False

            sensor_info['SensorNumber'] = sensor['SensorNumber']
            sensor_info['Name'] = sensor['Name']
            sensor_info['PhysicalContext'] = sensor['PhysicalContext']
            sensor_info['ReadingCelsius'] = sensor['ReadingCelsius']
            sensor_info['UpperThresholdCritical'] = sensor['UpperThresholdCritical']

            properties['Data']['Temperature'].append(sensor_info)

            try:
                value = int(sensor_info['ReadingCelsius'])
                if properties['Summary']['HighestTemperature'] is None:
                    properties['Summary']['HighestTemperature'] = value
                else:
                    properties['Summary']['HighestTemperature'] = max(
                        properties['Summary']['HighestTemperature'],
                        value
                    )
            except BaseException:
                pass

            try:
                value = int(sensor_info['UpperThresholdCritical']) - int(sensor_info['ReadingCelsius'])
                if value < 0:
                    properties['Summary']['OverThreshold'] = properties['Summary']['OverThreshold'] + 1
                else:
                    if properties['Summary']['SmallestGap'] is None:
                        properties['Summary']['SmallestGap'] = value
                    else:
                        properties['Summary']['SmallestGap'] = min(
                            properties['Summary']['SmallestGap'],
                            value
                        )
            except BaseException:
                pass

        properties['Data']['Temperature'] = sorted(properties['Data']['Temperature'], key=lambda i: i['Name'])

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
        properties['Data']['Fan'] = []
        for fan in data['Fans']:
            fan_info = {}
            fan_info['Name'] = fan['Name']
            fan_info['State'] = fan['Status']['State']
            fan_info['Health'] = ''
            if 'Health' in fan['Status']:
                fan_info['Health'] = fan['Status']['Health']
                if fan_info['State'] == 'Enabled':
                    if fan_info['Health'].lower() != 'ok':
                        properties['Summary']['FanHealth'] = False

            fan_info['PhysicalContext'] = ''
            if 'PhysicalContext' in fan:
                fan_info['PhysicalContext'] = fan['PhysicalContext']
            fan_info['ReadingUnits'] = ''
            if 'ReadingUnits' in fan:
                fan_info['ReadingUnits'] = fan['ReadingUnits']
            fan_info['Reading'] = ''
            if 'Reading' in fan:
                fan_info['Reading'] = fan['Reading']
            fan_info['Value'] = '%s %s' % (fan_info['Reading'], fan_info['ReadingUnits'])
            properties['Data']['Fan'].append(fan_info)

        properties['Data']['Fan'] = sorted(properties['Data']['Fan'], key=lambda i: i['Name'])

        return properties
