import json

from lib import output_helper


class ChassisPower():
    def __init__(self, log_id=None):
        self.mo_equipment_chassis_stats = None
        self.mo_equipment_psu_stats = None
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get_chassis_power_data(self):
        if self.mo_equipment_chassis_stats is None:
            managed_objects = self.query_classid(
                'equipmentChassisStats'
            )
            self.mo_equipment_chassis_stats = managed_objects

        if self.mo_equipment_psu_stats is None:
            managed_objects = self.query_classid(
                'EquipmentPsuStats'
            )
            self.mo_equipment_psu_stats = managed_objects

    def get_equipment_chassis_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]

        for suffix in ['', '_avg', '_min', '_max']:
            info['input_power%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'input_power%s' % (suffix))
                ),
                2
            )
            info['output_power%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'output_power%s' % (suffix))
                ),
                2
            )

        return info

    def get_equipment_chassis_stats(self, chassis_rn=None):
        self.get_chassis_power_data()
        chassis_stats = []

        for managed_object in self.mo_equipment_chassis_stats:
            chassis_info = self.get_equipment_chassis_stats_info(
                managed_object
            )
            chassis_stats.append(
                chassis_info
            )
            if chassis_rn is not None:
                if chassis_info['chassis_rn'] == chassis_rn:
                    return chassis_info

        return chassis_stats

    def get_equipment_psu_power_info(self, managed_object):
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

        for prefix in ['output_power', 'output_current']:
            for suffix in ['', '_avg', '_min', '_max']:
                info['%s%s' % (prefix, suffix)] = round(
                    float(
                        getattr(managed_object, '%s%s' % (prefix, suffix))
                    ),
                    2
                )

        return info

    def get_equipment_psu_power(self, chassis_rn=None):
        self.get_chassis_power_data()
        if self.mo_equipment_psu_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_equipment_psu_stats:
            thermal_info = self.get_equipment_psu_power_info(
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

    def get_chassis_power_stats(self, chassis_rn=None):
        self.get_chassis_power_data()

        power_stats = {}
        power_stats['Data'] = {}
        power_stats['Data']['Chassis'] = {}
        power_stats['Data']['PSU'] = []

        power_stats_chassis = self.get_equipment_chassis_stats(
            chassis_rn=chassis_rn
        )
        if power_stats_chassis is not None:
            power_stats['Data']['Chassis'] = power_stats_chassis

        power_stats_psu = self.get_equipment_psu_power(
            chassis_rn=chassis_rn
        )
        if power_stats_psu is not None:
            power_stats['Data']['PSU'] = power_stats_psu

        return power_stats

    def print_chassis_power(self, power):
        order = [
            'type',
            'current',
            'min',
            'avg',
            'max'
        ]

        headers = [
            'Type',
            'Now',
            'Min',
            'Avg',
            'Max'
        ]

        data = []

        item = {}
        item['type'] = 'Input Power'
        item['current'] = power['Data']['Chassis']['input_power']
        item['min'] = power['Data']['Chassis']['input_power_min']
        item['avg'] = power['Data']['Chassis']['input_power_avg']
        item['max'] = power['Data']['Chassis']['input_power_max']
        data.append(item)

        item = {}
        item['type'] = 'Output Power'
        item['current'] = power['Data']['Chassis']['output_power']
        item['min'] = power['Data']['Chassis']['output_power_min']
        item['avg'] = power['Data']['Chassis']['output_power_avg']
        item['max'] = power['Data']['Chassis']['output_power_max']
        data.append(item)

        self.my_output.my_table(
            data,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassiz_power(self, chassiz):
        order = [
            'rn',
            'power_stats.Data.Chassis.input_power',
            'power_stats.Data.Chassis.input_power_min',
            'power_stats.Data.Chassis.input_power_avg',
            'power_stats.Data.Chassis.input_power_max',
            'power_stats.Data.Chassis.output_power',
            'power_stats.Data.Chassis.output_power_min',
            'power_stats.Data.Chassis.output_power_avg',
            'power_stats.Data.Chassis.output_power_max'
        ]

        headers = [
            'Chassis',
            'Input Power Now',
            'Min',
            'Avg',
            'Max',
            'Output Power Now',
            'Min',
            'Avg',
            'Max'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassis_psu(self, power):
        order = [
            'name',
            'output_power',
            'output_power_min',
            'output_power_avg',
            'output_power_max',
            'output_current',
            'output_current_min',
            'output_current_avg',
            'output_current_max'

        ]

        headers = [
            'PSU',
            'Output Power (W)',
            'Min',
            'Avg',
            'Max',
            'Output Current (A)',
            'Min',
            'Avg',
            'Max'
        ]

        self.my_output.my_table(
            power['Data']['PSU'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_chassiz_psu(self, chassiz):
        order = [
            'chassis_rn',
            'name',
            'output_power',
            'output_power_min',
            'output_power_avg',
            'output_power_max',
            'output_current',
            'output_current_min',
            'output_current_avg',
            'output_current_max'

        ]

        headers = [
            'Chassis',
            'PSU',
            'Output Power (W)',
            'Min',
            'Avg',
            'Max',
            'Output Current (A)',
            'Min',
            'Avg',
            'Max'
        ]

        data = []
        for chassis in chassiz:
            data = data + chassis['power_stats']['Data']['PSU']

        self.my_output.my_table(
            data,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
