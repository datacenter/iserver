from lib import output_helper


class ServerThermal():
    def __init__(self, log_id=None):
        self.mo_compute_motherboard_stats = None
        self.mo_compute_cpu_stats = None
        self.mo_compute_memory_stats = None
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get_compute_thermal_data(self):
        if self.mo_compute_motherboard_stats is None:
            managed_objects = self.query_classid(
                'ComputeMbTempStats'
            )
            self.mo_compute_motherboard_stats = managed_objects

        if self.mo_compute_cpu_stats is None:
            managed_objects = self.query_classid(
                'ProcessorEnvStats'
            )
            self.mo_compute_cpu_stats = managed_objects

        if self.mo_compute_memory_stats is None:
            managed_objects = self.query_classid(
                'MemoryUnitEnvStats'
            )
            self.mo_compute_memory_stats = managed_objects

    def get_compute_thermal_motherboard_front_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['blade_rn'] = info['dn'].split('/')[2]
        info['name'] = 'Motherboard Front'
        info['type'] = 'motherboard'

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'fm_temp_sen_io%s' % (suffix))
                ),
                2
            )
            info['fm_temp_sen_rear%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'fm_temp_sen_rear%s' % (suffix))
                ),
                2
            )

        return info

    def get_compute_thermal_motherboard_rear_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['blade_rn'] = info['dn'].split('/')[2]
        info['name'] = 'Motherboard Rear'
        info['type'] = 'motherboard'

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'fm_temp_sen_rear%s' % (suffix))
                ),
                2
            )

        return info

    def get_compute_thermal_motherboard_stats(self, chassis_rn=None, blade_rn=None):
        self.get_compute_thermal_data()
        if self.mo_compute_motherboard_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_compute_motherboard_stats:
            thermal_info = self.get_compute_thermal_motherboard_front_stats_info(
                managed_object
            )
            if chassis_rn is None and blade_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None and blade_rn is None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

            if thermal_info['chassis_rn'] == chassis_rn and thermal_info['blade_rn'] == blade_rn:
                thermal_stats.append(
                    thermal_info
                )

        for managed_object in self.mo_compute_motherboard_stats:
            thermal_info = self.get_compute_thermal_motherboard_rear_stats_info(
                managed_object
            )
            if chassis_rn is None and blade_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None and blade_rn is None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

            if thermal_info['chassis_rn'] == chassis_rn and thermal_info['blade_rn'] == blade_rn:
                thermal_stats.append(
                    thermal_info
                )

        return thermal_stats

    def get_compute_thermal_cpu_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['blade_rn'] = info['dn'].split('/')[2]
        info['cpu_rn'] = info['dn'].split('/')[4]
        info['name'] = info['cpu_rn'].upper()
        info['type'] = 'cpu'

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'temperature%s' % (suffix))
                ),
                2
            )

        return info

    def get_compute_thermal_cpu_stats(self, chassis_rn=None, blade_rn=None):
        self.get_compute_thermal_data()
        if self.mo_compute_cpu_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_compute_cpu_stats:
            thermal_info = self.get_compute_thermal_cpu_stats_info(
                managed_object
            )
            if chassis_rn is None and blade_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None and blade_rn is None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

            if thermal_info['chassis_rn'] == chassis_rn and thermal_info['blade_rn'] == blade_rn:
                thermal_stats.append(thermal_info)

        return thermal_stats

    def get_compute_thermal_memory_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['blade_rn'] = info['dn'].split('/')[2]
        info['array_rn'] = info['dn'].split('/')[4]
        info['dimm_rn'] = info['dn'].split('/')[5]
        info['name'] = info['dimm_rn'].upper()
        info['type'] = 'memory'

        for suffix in ['', '_avg', '_min', '_max']:
            info['temperature%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'temperature%s' % (suffix))
                ),
                2
            )

        return info

    def get_compute_thermal_memory_stats(self, chassis_rn=None, blade_rn=None):
        self.get_compute_thermal_data()
        if self.mo_compute_memory_stats is None:
            return None

        thermal_stats = []

        for managed_object in self.mo_compute_memory_stats:
            thermal_info = self.get_compute_thermal_memory_stats_info(
                managed_object
            )
            if chassis_rn is None and blade_rn is None:
                thermal_stats.append(
                    thermal_info
                )
                continue

            if chassis_rn is not None and blade_rn is None:
                if thermal_info['chassis_rn'] == chassis_rn:
                    thermal_stats.append(
                        thermal_info
                    )
                    continue

            if thermal_info['chassis_rn'] == chassis_rn and thermal_info['blade_rn'] == blade_rn:
                thermal_stats.append(thermal_info)

        thermal_stats = sorted(thermal_stats, key=lambda i: i['name'])

        return thermal_stats

    def get_compute_thermal_stats(self, chassis_rn=None, blade_rn=None):
        self.get_compute_thermal_data()

        thermal_stats = {}
        thermal_stats['Data'] = []
        thermal_stats_motherboard = self.get_compute_thermal_motherboard_stats(
            chassis_rn=chassis_rn,
            blade_rn=blade_rn
        )
        if thermal_stats_motherboard is not None:
            thermal_stats['Data'] = thermal_stats['Data'] + thermal_stats_motherboard

        thermal_stats_cpu = self.get_compute_thermal_cpu_stats(
            chassis_rn=chassis_rn,
            blade_rn=blade_rn
        )
        if thermal_stats_cpu is not None:
            thermal_stats['Data'] = thermal_stats['Data'] + thermal_stats_cpu

        thermal_stats_memory = self.get_compute_thermal_memory_stats(
            chassis_rn=chassis_rn,
            blade_rn=blade_rn
        )
        if thermal_stats_memory is not None:
            thermal_stats['Data'] = thermal_stats['Data'] + thermal_stats_memory

        thermal_stats['Summary'] = {}
        thermal_stats['Summary']['Source'] = 'UCSM'
        thermal_stats['Summary']['FanHealth'] = 'N/A'
        thermal_stats['Summary']['SensorHealth'] = True
        thermal_stats['Summary']['HighestTemperature'] = None
        thermal_stats['Summary']['SmallestGap'] = 'N/A'
        thermal_stats['Summary']['OverThreshold'] = 'N/A'

        for item in thermal_stats['Data']:
            if 'temperature' in item:
                if thermal_stats['Summary']['HighestTemperature'] is None:
                    thermal_stats['Summary']['HighestTemperature'] = item['temperature']
                    continue

                thermal_stats['Summary']['HighestTemperature'] = max(
                    thermal_stats['Summary']['HighestTemperature'],
                    item['temperature']
                )

        return thermal_stats

    def print_blades_thermal(self, blades, include_chassis_id=True):
        order = [
            'chassis_rn',
            'rn',
            'thermal.Summary.SensorHealth',
            'thermal.Summary.HighestTemperature'
        ]

        headers = [
            'Chassis',
            'Name',
            'Sensor Health',
            'Highest Temperature'
        ]

        if not include_chassis_id:
            order.remove('chassis_rn')
            headers.remove('Chassis')

        self.my_output.my_table(
            blades,
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )

    def print_blade_thermal(self, thermal):
        headers = [
            'Thermal Statistics',
            'Value',
            'Min',
            'Avg',
            'Max'
        ]

        order = [
            'name',
            'temperature',
            'temperature_min',
            'temperature_avg',
            'temperature_max'
        ]

        self.my_output.my_table(
            thermal['Data'],
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )
