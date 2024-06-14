class Chassis():
    def __init__(self, log_id=None):
        self.mo_chassis = None

    def get_chassis_info(self, chassis_object):
        chassis_info = {}
        chassis_info['mo_type'] = 'chassis'

        keys = [
            'dn',
            'rn',
            'id',
            'model',
            'oper_state',
            'part_number',
            'power',
            'serial',
            'service_state',
            'thermal',
            'vendor'
        ]
        for key in keys:
            chassis_info[key] = getattr(chassis_object, key)

        return chassis_info

    def get_chassis_property(self, chassis_id, key):
        chassis = self.get_chassis(chassis_id)
        if chassis is None:
            return None

        if key not in chassis:
            return None

        return chassis[key]

    def get_chassis(self, chassis_id, blade=False, power=False, thermal=False):
        chassiz = self.get_chassiz()
        if chassiz is None:
            return None

        for chassis in chassiz:
            if str(chassis['id']) == str(chassis_id):
                if power:
                    chassis['power_stats'] = self.get_chassis_power_stats(
                        chassis_rn=chassis['rn']
                    )

                if thermal:
                    chassis['thermal_stats'] = self.get_chassis_thermal_stats(
                        chassis_rn=chassis['rn']
                    )

                if blade:
                    chassis['blade'] = self.get_blades(
                        chassis_rn=chassis['rn'],
                        power=power,
                        thermal=thermal
                    )

                return chassis

        return None

    def is_chassis_id(self, chassis_id):
        if self.get_chassis_id(chassis_id=chassis_id) is None:
            return False
        return True

    def get_chassis_id(self, chassis_rn=None, chassis_serial=None, chassis_id=None):
        chassiz = self.get_chassiz()
        if chassiz is None:
            return None

        for chassis in chassiz:
            if chassis_rn is not None:
                if chassis['rn'] == chassis_rn:
                    return chassis['id']

            if chassis_serial is not None:
                if chassis['serial'] == chassis_serial:
                    return chassis['id']

            if chassis_id is not None:
                if chassis['id'] == chassis_id:
                    return chassis['id']

        return None

    def get_chassiz(self, blade=False, power=False, thermal=False):
        if self.mo_chassis is None:
            managed_objects = self.query_classid(
                'EquipmentChassis'
            )
            if managed_objects is None:
                return None

            self.mo_chassis = managed_objects

        chassiz = []

        for managed_object in self.mo_chassis:
            managed_object_info = self.get_chassis_info(
                managed_object
            )
            if managed_object_info is not None:
                if blade:
                    managed_object_info['blade'] = self.get_blades(
                        chassis_rn=managed_object_info['rn'],
                        power=power,
                        thermal=thermal
                    )

                if power:
                    managed_object_info['power_stats'] = self.get_chassis_power_stats(
                        chassis_rn=managed_object_info['rn']
                    )

                if thermal:
                    managed_object_info['thermal_stats'] = self.get_chassis_thermal_stats(
                        chassis_rn=managed_object_info['rn']
                    )

                chassiz.append(managed_object_info)

        chassiz = sorted(chassiz, key=lambda i: i['dn'])
        return chassiz

    def print_chassis(self, chassis, power=False, blade=False, thermal=False):
        order = [
            'id',
            'rn',
            'model',
            'serial',
            'oper_state',
            'power',
            'thermal'
        ]

        headers = [
            'Chassis Id',
            'Name',
            'Model',
            'Serial',
            'Operability',
            'Power State',
            'Thermal State'
        ]

        self.my_output.dictionary(
            chassis,
            title='Chassis',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if power:
            self.print_chassis_power(
                chassis['power_stats']
            )

            self.print_chassis_psu(
                chassis['power_stats']
            )

        if thermal:
            self.print_chassis_thermal(
                chassis['thermal_stats']
            )

        if blade:
            self.print_blades(
                chassis['blade'],
                include_chassis_id=False
            )
            if power:
                self.print_blades_power(
                    chassis['blade']
                )
            if thermal:
                self.print_blades_thermal(
                    chassis['blade']
                )

    def print_chassiz(self, chassiz, power=False, thermal=False, blade=False):
        order = [
            'id',
            'rn',
            'model',
            'serial',
            'oper_state',
            'power',
            'thermal'
        ]

        headers = [
            'Chassis Id',
            'Name',
            'Model',
            'Serial',
            'Operability',
            'Power State',
            'Thermal State'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

        if blade:
            blades = []
            for chassis in chassiz:
                blades = blades + chassis['blade']

            self.print_blades(
                blades,
                include_chassis_id=True
            )

        if power:
            self.print_chassiz_power(
                chassiz
            )

            self.print_chassiz_psu(
                chassiz
            )

            if blade:
                self.print_blades_power(
                    blades,
                    include_chassis_id=True
                )

        if thermal:
            self.print_chassiz_thermal(
                chassiz
            )

            if blade:
                self.print_blades_thermal(
                    blades,
                    include_chassis_id=True
                )
