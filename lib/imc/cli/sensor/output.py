class ImcCliSensorOutput():
    def __init__(self):
        pass

    def print_imc_sensor_current(self, info):
        self.print_list_dict(
            info,
            'Sensor Current',
            allow_order_subkeys=False
        )

    def print_imc_sensor_fan(self, info):
        self.print_list_dict(
            info,
            'Sensor Fan',
            allow_order_subkeys=False
        )

    def print_imc_sensor_psu(self, info):
        self.print_list_dict(
            info,
            'Sensor PSU',
            allow_order_subkeys=False
        )

    def print_imc_sensor_temperature(self, info):
        self.print_list_dict(
            info,
            'Sensor Temperature',
            allow_order_subkeys=False
        )

    def print_imc_sensor_voltage(self, info):
        self.print_list_dict(
            info,
            'Sensor Voltage',
            allow_order_subkeys=False
        )

    def print_imc_sensor(self, info):
        for item in info:
            if 'current' in item:
                self.print_imc_sensor_current(
                    item['current']
                )

            if 'fan' in item:
                self.print_imc_sensor_fan(
                    item['fan']
                )

            if 'psu' in item:
                self.print_imc_sensor_psu(
                    item['psu']
                )

            if 'temperature' in item:
                self.print_imc_sensor_temperature(
                    item['temperature']
                )

            if 'voltage' in item:
                self.print_imc_sensor_voltage(
                    item['voltage']
                )
