class RedfishEndpointUcsRackTemplateThermalOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_thermal_summary_properties(self, properties):
        keys = [
            'SensorHealth',
            'HighestTemperature',
            'SmallestGap',
            'OverThreshold',
            'FanHealth'
        ]

        headers = [
            'Sensors Health',
            'Highest (C)',
            'Smallest Gap (C)',
            'Over Threshold',
            'Fans Health'
        ]

        self.my_output.dictionary(
            properties['Summary'],
            title='Thermal Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_ucsc_thermal_temperature_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'PhysicalContext',
            'ReadingCelsius',
            'UpperThresholdCritical'
        ]

        headers = [
            'Sensor Name',
            'State',
            'Health',
            'Location',
            'Value (Celcius)',
            'Upper Threshold (Celcius)'
        ]

        self.my_output.my_table(
            properties['Data']['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ucsc_thermal_fan_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'Value'
        ]

        headers = [
            'Fan Name',
            'State',
            'Health',
            'Value'
        ]

        self.my_output.my_table(
            properties['Data']['Fan'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ucsc_thermal_properties(self, properties):
        self.print_ucsc_thermal_summary_properties(properties)
        self.print_ucsc_thermal_temperature_properties(properties)
        self.print_ucsc_thermal_fan_properties(properties)
