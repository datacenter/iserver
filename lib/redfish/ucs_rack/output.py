from lib.redfish.ucs_rack.template.output import RedfishEndpointUcsRackTemplateOutput


class RedfishEndpointUcsRackOutput(
        RedfishEndpointUcsRackTemplateOutput
        ):
    def __init__(self):
        RedfishEndpointUcsRackTemplateOutput.__init__(self)

    def print_ucsc_properties(self, template_name, properties, title=False):
        if template_name == 'account':
            self.print_ucsc_account_properties(
                properties,
                title=title
            )

        if template_name == 'identity':
            self.print_ucsc_identity_properties(properties)

        if template_name == 'power':
            self.print_ucsc_power_properties(properties)

        if template_name == 'role':
            self.print_ucsc_role_properties(
                properties,
                title=title
            )

        if template_name == 'storage':
            self.print_ucsc_storage_properties(properties)

        if template_name == 'thermal':
            self.print_ucsc_thermal_properties(properties)

    def print_ucsc_account_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Account [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        for item in info:
            if len(item['privileges']) == 0:
                item['privileges'].append('--')
            if len(item['oem']) == 0:
                item['oem'].append('--')

        order = [
            'username',
            'id',
            'role_id',
            'name',
            'description',
            'enabledTick',
            'changeTick',
            'privileges',
            'oem'
        ]

        headers = [
            'Username',
            'Id',
            'Role Id',
            'Name',
            'Description',
            'Enabled',
            'Change Req',
            'Role Privileges',
            'Role Oem Privileges'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['privileges', 'oem']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ucsc_power_consumption_properties(self, properties):
        keys = [
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts',
            'LimitException'
        ]

        headers = [
            'Current',
            'Min',
            'Average',
            'Max',
            'Limit action'
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

    def print_ucsc_power_voltage_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Sensor Name',
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

    def print_ucsc_power_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'PowerOutputWatts',
            'PowerInputWatts',
            'MaximumVoltage',
            'MinimumVoltage',
            'MaximumFrequencyHz',
            'MinimumFrequencyHz'
        ]

        headers = [
            'PSU Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (Watt)',
            'Max (V)',
            'Min (V)',
            'Max (Hz)',
            'Min (Hz)'
        ]

        self.my_output.my_table(
            properties['Data']['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ucsc_power_properties(self, properties):
        self.print_ucsc_power_consumption_properties(properties)
        self.print_ucsc_power_voltage_properties(properties)
        self.print_ucsc_power_supply_properties(properties)

    def print_ucsc_identity_properties(self, properties):
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

    def print_ucsc_role_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Role [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        for item in info:
            if len(item['privileges']) == 0:
                item['privileges'].append('--')
            if len(item['oem']) == 0:
                item['oem'].append('--')
            if len(item['username']) == 0:
                item['username'].append('--')

        order = [
            'id',
            'role_id',
            'name',
            'description',
            'privileges',
            'oem',
            'username'
        ]

        headers = [
            'Id',
            'Role Id',
            'Name',
            'Description',
            'Privileges',
            'Oem Privileges',
            'Account'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['privileges', 'oem', 'username']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ucsc_storage_controller_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Storage Controller [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Pid',
            'Model',
            'Vendor',
            'SerialNumber',
            'FirmwareVersion',
            'State',
            'Health',
            'PciSlot',
            'SupportedRAIDTypes',
            'PhysicalDiskCount',
            'VirtualDriveCount'
        ]

        headers = [
            'Controller',
            'Pid',
            'Model',
            'Vendor',
            'Serial',
            'Firmware',
            'State',
            'Health',
            'PCI Slot',
            'Raid Support',
            'PD',
            'VD'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['SupportedRAIDTypes']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_ucsc_storage_drive_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Disk [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'StateTick',
            'StorageControllerId',
            'DiskId',
            'VirtualDriveId',
            'SizeUnit',
            'Type',
            'Protocol',
            'BootableTick',
            'LinkSpeed',
            'Pid',
            'Model',
            'Vendor',
            'Revision',
            'SerialNumber'
        ]

        headers = [
            'State',
            'Controller',
            'Disk Id',
            'VD',
            'Size',
            'Type',
            'Protocol',
            'Bootable',
            'Link Speed',
            'Pid',
            'Model',
            'Vendor',
            'Fw',
            'Serial'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_ucsc_storage_volume_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Drive [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'StateTick',
            'StorageControllerId',
            'VirtualDriveId',
            'SizeUnit',
            'PhysicalDiskCount',
            'Type',
            'Name',
            'BootableTick',
            'ActualWriteCachePolicy',
            'DriveState'
        ]

        headers = [
            'State',
            'Controller',
            'Drive Id',
            'Size',
            'Disks',
            'Type',
            'Name',
            'Bootable',
            'Write Cache',
            'Drive State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_ucsc_storage_properties(self, properties):
        self.print_ucsc_storage_controller_properties(
            properties['Controller'],
            title=True
        )

        self.print_ucsc_storage_drive_properties(
            properties['Drive'],
            title=True
        )

        self.print_ucsc_storage_volume_properties(
            properties['Volume'],
            title=True
        )

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
