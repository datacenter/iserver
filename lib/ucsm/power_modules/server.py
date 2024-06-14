from lib import output_helper


class ServerPower():
    def __init__(self, log_id=None):
        self.mo_compute_stats = None
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get_compute_power_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['chassis_rn'] = info['dn'].split('/')[1]
        info['blade_rn'] = info['dn'].split('/')[2]

        for suffix in ['', '_avg', '_min', '_max']:
            info['consumed_power%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'consumed_power%s' % (suffix))
                ),
                2
            )
            info['input_current%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'input_current%s' % (suffix))
                ),
                2
            )
            info['input_voltage%s' % (suffix)] = round(
                float(
                    getattr(managed_object, 'input_voltage%s' % (suffix))
                ),
                2
            )

        return info

    def get_compute_power_stats(self, chassis_rn=None, blade_rn=None):
        if self.mo_compute_stats is None:
            managed_objects = self.query_classid(
                'ComputeMbPowerStats'
            )
            if managed_objects is None:
                return None

            self.mo_compute_stats = managed_objects

        power_stats = {}
        power_stats['Data'] = []

        for managed_object in self.mo_compute_stats:
            power_info = self.get_compute_power_stats_info(
                managed_object
            )
            if chassis_rn is None and blade_rn is None:
                power_stats['Data'].append(
                    power_info
                )
                continue

            if chassis_rn is not None and blade_rn is None:
                if power_info['chassis_rn'] == chassis_rn:
                    power_stats['Data'] = power_info
                    continue

            if power_info['chassis_rn'] == chassis_rn and power_info['blade_rn'] == blade_rn:
                power_stats['Data'] = power_info

                power_stats['Summary'] = {}
                power_stats['Summary']['Source'] = 'UCSM'
                power_stats['Summary']['PowerNow'] = power_info['consumed_power']
                power_stats['Summary']['PowerMin'] = power_info['consumed_power_min']
                power_stats['Summary']['PowerAvg'] = power_info['consumed_power_avg']
                power_stats['Summary']['PowerMax'] = power_info['consumed_power_max']
                continue

        return power_stats

    def print_blades_power(self, blades, include_chassis_id=True):
        order = [
            'chassis_rn',
            'rn',
            'power.Data.consumed_power',
            'power.Data.consumed_power_min',
            'power.Data.consumed_power_avg',
            'power.Data.consumed_power_max',
            'power.Data.input_current',
            'power.Data.input_current_min',
            'power.Data.input_current_avg',
            'power.Data.input_current_max',
            'power.Data.input_voltage',
            'power.Data.input_voltage_min',
            'power.Data.input_voltage_avg',
            'power.Data.input_voltage_max'
        ]

        headers = [
            'Chassis',
            'Name',
            'Power',
            'Min',
            'Avg',
            'Max',
            'Current',
            'Min',
            'Avg',
            'Max',
            'Voltage',
            'Min',
            'Avg',
            'Max'
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

    def print_blade_power(self, power):
        headers = [
            'Power Statistics',
            'Value',
            'Min',
            'Avg',
            'Max'
        ]

        order = [
            'Type',
            'Value',
            'Min',
            'Avg',
            'Max'
        ]

        info = []

        entry = {}
        entry['Type'] = 'Consumed Power (W)'
        entry['Value'] = power['Data']['consumed_power']
        entry['Min'] = power['Data']['consumed_power_min']
        entry['Avg'] = power['Data']['consumed_power_avg']
        entry['Max'] = power['Data']['consumed_power_max']
        info.append(entry)

        entry = {}
        entry['Type'] = 'Input Current (A)'
        entry['Value'] = power['Data']['input_current']
        entry['Min'] = power['Data']['input_current_min']
        entry['Avg'] = power['Data']['input_current_avg']
        entry['Max'] = power['Data']['input_current_max']
        info.append(entry)

        entry = {}
        entry['Type'] = 'Input Voltage (V)'
        entry['Value'] = power['Data']['input_voltage']
        entry['Min'] = power['Data']['input_voltage_min']
        entry['Avg'] = power['Data']['input_voltage_avg']
        entry['Max'] = power['Data']['input_voltage_max']
        info.append(entry)

        self.my_output.my_table(
            info,
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )
