import json
from lib import output_helper


class ChassisThermal():
    def __init__(self, log_id=None):
        self.mo_equipment_fan_stats = None
        self.mo_equipment_fan_module_stats = None
        self.mo_equipment_psu_stats = None
        self.mo_equipment_io_card_stats = None
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get_chassis_thermal_data(self):
        if self.mo_equipment_fan_stats is None:
            managed_objects = self.query_classid(
                'EquipmentFanStats'
            )
            self.mo_equipment_fan_stats = managed_objects

        if self.mo_equipment_fan_module_stats is None:
            managed_objects = self.query_classid(
                'EquipmentFanModuleStats'
            )
            self.mo_equipment_fan_module_stats = managed_objects

        if self.mo_equipment_psu_stats is None:
            managed_objects = self.query_classid(
                'EquipmentPsuStats'
            )
            self.mo_equipment_psu_stats = managed_objects

        if self.mo_equipment_io_card_stats is None:
            managed_objects = self.query_classid(
                'EquipmentIOCardStats'
            )
            self.mo_equipment_io_card_stats = managed_objects

    def get_equipment_fan_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['fan_module_rn'] = info['dn'].split('/')[2]
        info['fan_module_id'] = info['fan_module_rn'].split('-')[-1]
        info['fan_rn'] = info['dn'].split('/')[3]
        info['fan_id'] = info['fan_rn'].split('-')[-1]
        info['name'] = 'Fan Module %s - Fan %s' % (
            info['fan_module_id'],
            info['fan_id']
        )

        for suffix in ['', '_avg', '_min', '_max']:
            info['speed%s' % (suffix)] = getattr(managed_object, 'speed%s' % (suffix))

        return info

    def get_equipment_fan_stats(self, chassis_rn=None):
        self.get_chassis_thermal_data()
        if self.mo_equipment_fan_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_equipment_fan_stats:
            thermal_info = self.get_equipment_fan_stats_info(
                managed_object
            )
            if chassis_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

        return thermal_stats

    def get_equipment_fan_module_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['fan_module_rn'] = info['dn'].split('/')[2]
        info['fan_module_id'] = info['fan_module_rn'].split('-')[-1]
        info['name'] = 'Fan Module %s' % (
            info['fan_module_id']
        )

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'ambient_temp%s' % (suffix))
                ),
                2
            )

        return info

    def get_equipment_fan_module_stats(self, chassis_rn=None):
        self.get_chassis_thermal_data()
        if self.mo_equipment_fan_module_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_equipment_fan_module_stats:
            thermal_info = self.get_equipment_fan_module_stats_info(
                managed_object
            )
            if chassis_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

        return thermal_stats

    def get_equipment_psu_temp_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['psu_rn'] = info['dn'].split('/')[2]
        info['psu_id'] = info['psu_rn'].split('-')[-1]
        info['name'] = 'PSU %s' % (
            info['psu_id']
        )

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'ambient_temp%s' % (suffix))
                ),
                2
            )

        return info

    def get_equipment_psu_temp(self, chassis_rn=None):
        self.get_chassis_thermal_data()
        if self.mo_equipment_psu_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_equipment_psu_stats:
            thermal_info = self.get_equipment_psu_temp_info(
                managed_object
            )
            if chassis_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

        return thermal_stats

    def get_equipment_io_ambient_temp_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['slot_rn'] = info['dn'].split('/')[2]
        info['slot_id'] = info['slot_rn'].split('-')[-1]
        info['name'] = 'IO Module %s - Ambient' % (
            info['slot_id']
        )

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'ambient_temp%s' % (suffix))
                ),
                2
            )

        return info

    def get_equipment_io_asic_temp_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['slot_rn'] = info['dn'].split('/')[2]
        info['slot_id'] = info['slot_rn'].split('-')[-1]
        info['name'] = 'IO Module %s - ASIC' % (
            info['slot_id']
        )

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'temp%s' % (suffix))
                ),
                2
            )

        return info

    def get_equipment_io_thermal_stats(self, chassis_rn=None):
        self.get_chassis_thermal_data()
        if self.mo_equipment_io_card_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_equipment_io_card_stats:
            thermal_info = self.get_equipment_io_ambient_temp_info(
                managed_object
            )
            if chassis_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

        for managed_object in self.mo_equipment_io_card_stats:
            thermal_info = self.get_equipment_io_asic_temp_info(
                managed_object
            )
            if chassis_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

        return thermal_stats

    def get_chassis_thermal_stats(self, chassis_rn=None):
        self.get_chassis_thermal_data()

        thermal_stats = {}
        thermal_stats['Data'] = {}
        thermal_stats['Data']['Fan'] = []
        thermal_stats['Data']['Temperature'] = []

        thermal_stats_fan = self.get_equipment_fan_stats(
            chassis_rn=chassis_rn
        )
        if thermal_stats_fan is not None:
            thermal_stats['Data']['Fan'] = thermal_stats_fan

        thermal_stats_fan_module = self.get_equipment_fan_module_stats(
            chassis_rn=chassis_rn
        )
        if thermal_stats_fan_module is not None:
            thermal_stats['Data']['Temperature'] = thermal_stats['Data']['Temperature'] + thermal_stats_fan_module

        thermal_stats_psu = self.get_equipment_psu_temp(
            chassis_rn=chassis_rn
        )
        if thermal_stats_psu is not None:
            thermal_stats['Data']['Temperature'] = thermal_stats['Data']['Temperature'] + thermal_stats_psu

        thermal_stats_io = self.get_equipment_io_thermal_stats(
            chassis_rn=chassis_rn
        )
        if thermal_stats_io is not None:
            thermal_stats['Data']['Temperature'] = thermal_stats['Data']['Temperature'] + thermal_stats_io

        thermal_stats['Summary'] = {}
        thermal_stats['Summary']['Source'] = 'UCSM'
        thermal_stats['Summary']['HighestTemperature'] = None

        for item in thermal_stats['Data']['Temperature']:
            if 'temperature' in item:
                if thermal_stats['Summary']['HighestTemperature'] is None:
                    thermal_stats['Summary']['HighestTemperature'] = item['temperature']
                    continue

                thermal_stats['Summary']['HighestTemperature'] = max(
                    thermal_stats['Summary']['HighestTemperature'],
                    item['temperature']
                )

        return thermal_stats

    def print_chassis_fans(self, thermal):
        order = [
            'name',
            'speed',
            'speed_min',
            'speed_avg',
            'speed_max'

        ]

        headers = [
            'Fan',
            'Speed (RPM)',
            'Min',
            'Avg',
            'Max'
        ]

        self.my_output.my_table(
            thermal['Data']['Fan'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassis_sensors(self, thermal):
        order = [
            'name',
            'temperature',
            'temperature_min',
            'temperature_avg',
            'temperature_max'

        ]

        headers = [
            'Sensor',
            'Temperature (C)',
            'Min',
            'Avg',
            'Max'
        ]

        self.my_output.my_table(
            thermal['Data']['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassis_thermal(self, data):
        self.print_chassis_fans(data)
        self.print_chassis_sensors(data)

    def print_chassiz_fans(self, chassiz):
        order = [
            'chassis_rn',
            'name',
            'speed',
            'speed_min',
            'speed_avg',
            'speed_max'

        ]

        headers = [
            'Chassis',
            'Fan',
            'Speed (RPM)',
            'Min',
            'Avg',
            'Max'
        ]

        data = []
        for chassis in chassiz:
            data = data + chassis['thermal_stats']['Data']['Fan']

        self.my_output.my_table(
            data,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassiz_sensors(self, chassiz):
        order = [
            'chassis_rn',
            'name',
            'temperature',
            'temperature_min',
            'temperature_avg',
            'temperature_max'

        ]

        headers = [
            'Chassis',
            'Sensor',
            'Temperature (C)',
            'Min',
            'Avg',
            'Max'
        ]

        data = []
        for chassis in chassiz:
            data = data + chassis['thermal_stats']['Data']['Temperature']

        self.my_output.my_table(
            data,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassiz_thermal(self, chassiz):
        self.print_chassiz_fans(chassiz)
        self.print_chassiz_sensors(chassiz)
