class Blade():
    def __init__(self, log_id=None):
        self.mo_blade = None

    def get_blade_info(self, blade_object):
        blade_info = {}
        blade_info['mo_type'] = 'blade'

        keys = [
            'association',
            'chassis_id',
            'available_memory',
            'assigned_to_dn',
            'admin_state',
            'dn',
            'model',
            'num_of_adaptors',
            'num_of_cores',
            'num_of_cores_enabled',
            'num_of_cpus',
            'num_of_eth_host_ifs',
            'num_of_fc_host_ifs',
            'num_of_threads',
            'oper_power',
            'oper_state',
            'operability',
            'part_number',
            'rn',
            'serial',
            'server_id',
            'slot_id',
            'total_memory',
            'uuid',
            'vendor'
        ]
        for key in keys:
            blade_info[key] = getattr(blade_object, key)

        blade_info['id'] = blade_info['rn'].split('-')[1]
        blade_info['chassis_rn'] = blade_info['dn'].split('/')[1]

        return blade_info

    def get_blade(self, blade_serial=None, chassis_id=None, blade_id=None, power=False, thermal=False):
        blades = self.get_blades(power=power, thermal=thermal)
        if blades is None:
            return None

        for blade in blades:
            if blade_serial is not None:
                if blade['serial'] == blade_serial:
                    return blade

            if chassis_id is not None and blade_id is not None:
                if blade['chassis_id'] == chassis_id and blade['id'] == blade_id:
                    return blade

        return None

    def get_blades(self, chassis_rn=None, power=False, thermal=False):
        if self.mo_blade is None:
            managed_objects = self.query_classid(
                'ComputeBlade'
            )
            if managed_objects is None:
                return None

            self.mo_blade = managed_objects

        blades = []

        for managed_object in self.mo_blade:
            managed_object_info = self.get_blade_info(
                managed_object
            )
            if managed_object_info is None:
                continue

            if power:
                managed_object_info['power'] = self.get_compute_power_stats(
                    chassis_rn=managed_object_info['chassis_rn'],
                    blade_rn=managed_object_info['rn']
                )

            if thermal:
                managed_object_info['thermal'] = self.get_compute_thermal_stats(
                    chassis_rn=managed_object_info['chassis_rn'],
                    blade_rn=managed_object_info['rn']
                )

            if chassis_rn is None:
                blades.append(managed_object_info)
                continue

            if managed_object_info['chassis_rn'] == chassis_rn:
                blades.append(managed_object_info)

        blades = sorted(blades, key=lambda i: i['dn'])

        return blades

    def print_blade(self, blade, power=False, thermal=False):
        order = [
            'chassis_rn',
            'rn',
            'model',
            'serial',
            'oper_state',
            'operability',
            'oper_power',
            'association'
        ]

        headers = [
            'Chassis',
            'Blade',
            'Model',
            'Serial',
            'Overal Status',
            'Operability',
            'Power State',
            'Assoc State'
        ]

        self.my_output.dictionary(
            blade,
            title='Blade',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if power:
            self.print_blade_power(
                blade['power']
            )

        if thermal:
            self.print_blade_thermal(
                blade['thermal']
            )

    def print_blades(self, blades, power=False, thermal=False, include_chassis_id=True):
        order = [
            'chassis_rn',
            'rn',
            'model',
            'serial',
            'oper_state',
            'operability',
            'oper_power',
            'association'
        ]

        headers = [
            'Chassis',
            'Blade',
            'Model',
            'Serial',
            'Overal Status',
            'Operability',
            'Power State',
            'Assoc State'
        ]

        if not include_chassis_id:
            order.remove('chassis_rn')
            headers.remove('Chassis')

        self.my_output.my_table(
            blades,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

        if power:
            self.print_blades_power(
                blades,
                include_chassis_id=include_chassis_id
            )

        if power:
            self.print_blades_thermal(
                blades,
                include_chassis_id=include_chassis_id
            )
