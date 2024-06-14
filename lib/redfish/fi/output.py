import json


class RedfishEndpointFabricInterconnectOutput(
    ):
    def __init__(self):
        pass

    def print_template_identity_chassis_properties(self, properties):
        keys = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'HostName',
            'SerialNumber',
            'UUID',
            'BiosVersion',
            'Firmware',
            'PowerState',
            'RedfishVersion'
        ]

        headers = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'Hostname',
            'Serial Number',
            'UUID',
            'Bios Version',
            'Firmware',
            'Power State',
            'Redfish Version'
        ]

        self.my_output.dictionary(
            properties,
            title='UCS Rack Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_identity_server_properties(self, properties):
        keys = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'HostName',
            'SerialNumber',
            'UUID',
            'BiosVersion',
            'Firmware',
            'PowerState',
            'RedfishVersion'
        ]

        headers = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'Hostname',
            'Serial Number',
            'UUID',
            'Bios Version',
            'Firmware',
            'Power State',
            'Redfish Version'
        ]

        self.my_output.dictionary(
            properties,
            title='UCS FI-Attached Server Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_inventory_chassis(self, chassis):
        order = [
            'InventoryType',
            'Identifier',
            'Iom1',
            'Iom2',
            'Name',
            'Model',
            'Serial'
        ]

        headers = [
            'Inventory Type',
            'Chassis Id',
            'Inventory Id (IOM1)',
            'Inventory Id (IOM2)',
            'Chassis Name',
            'Chassis Model',
            'Chassis Serial',
        ]

        self.my_output.my_table(
            chassis,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_inventory_servers(self, servers):
        order = [
            'InventoryType',
            'Name',
            'ChassisIdentifier',
            'Model',
            'Serial'
        ]

        headers = [
            'Inventory Type',
            'Inventory Id',
            'Chassis Id',
            'Server Model',
            'Server Serial'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_inventory(self, inventory, output='default'):
        if output == 'json':
            self.my_output.default(
                json.dumps(
                    inventory,
                    indent=4
                )
            )
            return

        self.print_inventory_chassis(inventory['chassis'])
        self.print_inventory_servers(inventory['servers'])

    def print_template_power_chassis_control_properties(self, properties):
        keys = [
            'CurrentConsumedWatts'
        ]
        headers = [
            'CurrentConsumedWatts'
        ]

        self.my_output.dictionary(
            properties['Data']['PowerControl'],
            title='Power Control',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_power_chassis_blade_properties(self, properties):
        order = [
            'MemberId',
            'State',
            'Health',
            'AverageConsumedWatts',
            'CurrentConsumedWatts',
            'MaxConsumedWatts',
            'MinConsumedWatts',
            'MaxPowerWatts',
            'MinPowerWatts'
        ]

        headers = [
            'Blade Name',
            'State',
            'Health',
            'AverageConsumedWatts',
            'CurrentConsumedWatts',
            'MaxConsumedWatts',
            'MinConsumedWatts',
            'MaxPowerWatts',
            'MinPowerWatts'
        ]

        self.my_output.my_table(
            properties['Data']['Blade'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_chassis_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Manufacturer',
            'Model',
            'SerialNumber'
        ]

        headers = [
            'PSU Name',
            'State',
            'Manufacturer',
            'Model',
            'SerialNumber'
        ]

        self.my_output.my_table(
            properties['Data']['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_chassis_properties(self, properties):
        self.print_template_power_chassis_control_properties(properties)
        self.print_template_power_chassis_blade_properties(properties)
        self.print_template_power_chassis_supply_properties(properties)

    def print_template_power_server_consumption_properties(self, properties):
        keys = [
            'CurrentConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts',
            'MinConsumedWatts'
        ]

        headers = [
            'Current',
            'Average',
            'Max',
            'Min'
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

    def print_template_power_server_voltage_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Voltage Sensor',
            'State',
            'Health',
            'Volts',
            'Upper Threshold'
        ]

        self.my_output.my_table(
            properties['Data']['Voltage'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_server_properties(self, properties):
        self.print_template_power_server_consumption_properties(properties)
        self.print_template_power_server_voltage_properties(properties)

    def print_template_thermal_chassis_temperature_properties(self, properties):
        order = [
            'Name',
            'State',
            'ReadingCelsius'
        ]

        headers = [
            'Sensor Name',
            'State',
            'Value (Celcius)'
        ]

        self.my_output.my_table(
            properties['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_thermal_chassis_fan_properties(self, properties):
        order = [
            'Name',
            'State',
            'Model',
            'SerialNumber'
        ]

        headers = [
            'Fan Name',
            'State',
            'Model',
            'SerialNumber'
        ]

        self.my_output.my_table(
            properties['Fan'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_thermal_chassis_properties(self, properties):
        self.print_template_thermal_chassis_temperature_properties(properties)
        self.print_template_thermal_chassis_fan_properties(properties)

    def print_template_thermal_server_summary_properties(self, properties):
        keys = [
            'State',
            'Health'
        ]

        headers = [
            'State',
            'Health'
        ]

        self.my_output.dictionary(
            properties,
            title='Thermal Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_thermal_server_temperature_properties(self, properties):
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
            properties['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_thermal_server_properties(self, properties):
        self.print_template_thermal_server_summary_properties(properties)
        self.print_template_thermal_server_temperature_properties(properties)
