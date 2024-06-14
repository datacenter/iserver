import json


class ImcCliSensor():
    def __init__(self):
        self.sensor_current_mo = None
        self.sensor_fan_mo = None
        self.sensor_psu_mo = None
        self.sensor_temperature_mo = None
        self.sensor_voltage_mo = None

    def get_sensor_current_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.sensor_current_mo is not None:
                return self.sensor_current_mo

            self.sensor_current_mo = self.get_icm_cli_cache_entry(
                'sensor_current'
            )
            if self.sensor_current_mo is not None:
                return self.sensor_current_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show current detail
        # Name PSU1_IOUT:
        #     Sensor Status: Normal
        #     Reading: 8.00
        #     Units: AMP
        #     Critical Min: N/A
        #     Critical Max: 87.00
        #     Non-Recoverable Min: N/A
        #     Non-Recoverable Max: 96.00

        if keep_scope:
            self.sensor_current_mo = self.show_list(
                'show current detail',
                'Name',
                'Name',
                method='last word',
                top=False
            )
        else:
            self.sensor_current_mo = self.show_list(
                'show current detail',
                'Name',
                'Name',
                method='last word',
                scope='sensor'
            )

        if self.sensor_current_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sensor_current',
            self.sensor_current_mo
        )

        self.log.debug(
            'get_sensor_current_mo',
            json.dumps(self.sensor_current_mo, indent=4)
        )
        return self.sensor_current_mo

    def get_sensor_current_info(self, sensor_current_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sensor_current_mo:
            info[key] = sensor_current_mo[key]

        return info

    def get_sensor_fan_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.sensor_fan_mo is not None:
                return self.sensor_fan_mo

            self.sensor_fan_mo = self.get_icm_cli_cache_entry(
                'sensor_fan'
            )
            if self.sensor_fan_mo is not None:
                return self.sensor_fan_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show fan detail
        # Name PSU1_IOUT:
        #     Sensor Status: Normal
        #     Reading: 8.00
        #     Units: AMP
        #     Critical Min: N/A
        #     Critical Max: 87.00
        #     Non-Recoverable Min: N/A
        #     Non-Recoverable Max: 96.00

        if keep_scope:
            self.sensor_fan_mo = self.show_list(
                'show fan detail',
                'Name',
                'Name',
                method='last word',
                top=False
            )
        else:
            self.sensor_fan_mo = self.show_list(
                'show fan detail',
                'Name',
                'Name',
                method='last word',
                scope='sensor'
            )

        if self.sensor_fan_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sensor_fan',
            self.sensor_fan_mo
        )

        self.log.debug(
            'get_sensor_fan_mo',
            json.dumps(self.sensor_fan_mo, indent=4)
        )
        return self.sensor_fan_mo

    def get_sensor_fan_info(self, sensor_fan_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sensor_fan_mo:
            info[key] = sensor_fan_mo[key]

        return info

    def get_sensor_psu_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.sensor_psu_mo is not None:
                return self.sensor_psu_mo

            self.sensor_psu_mo = self.get_icm_cli_cache_entry(
                'sensor_psu'
            )
            if self.sensor_psu_mo is not None:
                return self.sensor_psu_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show psu detail
        # Name PSU1_POUT:
        #     Sensor Status: Normal
        #     Reading: 96
        #     Units: Watts
        #     Critical Min: N/A
        #     Critical Max: 1048
        #     Non-Recoverable Min: N/A
        #     Non-Recoverable Max: 1152

        if keep_scope:
            self.sensor_psu_mo = self.show_list(
                'show psu detail',
                'Name',
                'Name',
                method='last word',
                top=False
            )
        else:
            self.sensor_psu_mo = self.show_list(
                'show psu detail',
                'Name',
                'Name',
                method='last word',
                scope='sensor'
            )

        if self.sensor_psu_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sensor_psu',
            self.sensor_psu_mo
        )

        self.log.debug(
            'get_sensor_psu_mo',
            json.dumps(self.sensor_psu_mo, indent=4)
        )
        return self.sensor_psu_mo

    def get_sensor_psu_info(self, sensor_psu_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sensor_psu_mo:
            info[key] = sensor_psu_mo[key]

        return info

    def get_sensor_temperature_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.sensor_temperature_mo is not None:
                return self.sensor_temperature_mo

            self.sensor_temperature_mo = self.get_icm_cli_cache_entry(
                'sensor_temperature'
            )
            if self.sensor_temperature_mo is not None:
                return self.sensor_temperature_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show temperature detail
        # Name MLOM_TEMP:
        #     Sensor Status: Normal
        #     Reading: 60.0
        #     Units: C
        #     Critical Min: N/A
        #     Critical Max: 90.0
        #     Non-Recoverable Min: N/A
        #     Non-Recoverable Max: 95.0

        if keep_scope:
            self.sensor_temperature_mo = self.show_list(
                'show temperature detail',
                'Name',
                'Name',
                method='last word',
                top=False
            )
        else:
            self.sensor_temperature_mo = self.show_list(
                'show temperature detail',
                'Name',
                'Name',
                method='last word',
                scope='sensor'
            )

        if self.sensor_temperature_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sensor_temperature',
            self.sensor_temperature_mo
        )

        self.log.debug(
            'get_sensor_temperature_mo',
            json.dumps(self.sensor_temperature_mo, indent=4)
        )
        return self.sensor_temperature_mo

    def get_sensor_temperature_info(self, sensor_temperature_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sensor_temperature_mo:
            info[key] = sensor_temperature_mo[key]

        return info

    def get_sensor_voltage_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.sensor_voltage_mo is not None:
                return self.sensor_voltage_mo

            self.sensor_voltage_mo = self.get_icm_cli_cache_entry(
                'sensor_voltage'
            )
            if self.sensor_voltage_mo is not None:
                return self.sensor_voltage_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show voltage detail
        # Name PSU1_VOUT:
        #     Sensor Status: Normal
        #     Reading: 12.100
        #     Units: V
        #     Critical Min: N/A
        #     Critical Max: 14.000
        #     Non-Recoverable Min: N/A
        #     Non-Recoverable Max: 15.000

        if keep_scope:
            self.sensor_voltage_mo = self.show_list(
                'show voltage detail',
                'Name',
                'Name',
                method='last word',
                top=False
            )
        else:
            self.sensor_voltage_mo = self.show_list(
                'show voltage detail',
                'Name',
                'Name',
                method='last word',
                scope='sensor'
            )

        if self.sensor_voltage_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sensor_voltage',
            self.sensor_voltage_mo
        )

        self.log.debug(
            'get_sensor_voltage_mo',
            json.dumps(self.sensor_voltage_mo, indent=4)
        )
        return self.sensor_voltage_mo

    def get_sensor_voltage_info(self, sensor_voltage_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sensor_voltage_mo:
            info[key] = sensor_voltage_mo[key]

        return info

    def get_sensor(
            self,
            current_info=False,
            fan_info=False,
            psu_info=False,
            temperature_info=False,
            voltage_info=False,
            cache_enabled=True
        ):
        sensor = {}

        self.set_scope('sensor')

        if current_info:
            sensors_current_mo = self.get_sensor_current_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if sensors_current_mo is not None:
                sensor['current'] = []
                for sensor_current_mo in sensors_current_mo:
                    sensor['current'].append(
                        self.get_sensor_current_info(
                            sensor_current_mo
                        )
                    )

        if fan_info:
            sensors_fan_mo = self.get_sensor_fan_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if sensors_fan_mo is not None:
                sensor['fan'] = []
                for sensor_fan_mo in sensors_fan_mo:
                    sensor['fan'].append(
                        self.get_sensor_fan_info(
                            sensor_fan_mo
                        )
                    )

        if psu_info:
            sensors_psu_mo = self.get_sensor_psu_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if sensors_psu_mo is not None:
                sensor['psu'] = []
                for sensor_psu_mo in sensors_psu_mo:
                    sensor['psu'].append(
                        self.get_sensor_psu_info(
                            sensor_psu_mo
                        )
                    )

        if temperature_info:
            sensors_temperature_mo = self.get_sensor_temperature_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if sensors_temperature_mo is not None:
                sensor['temperature'] = []
                for sensor_temperature_mo in sensors_temperature_mo:
                    sensor['temperature'].append(
                        self.get_sensor_temperature_info(
                            sensor_temperature_mo
                        )
                    )

        if voltage_info:
            sensors_voltage_mo = self.get_sensor_voltage_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if sensors_voltage_mo is not None:
                sensor['voltage'] = []
                for sensor_voltage_mo in sensors_voltage_mo:
                    sensor['voltage'].append(
                        self.get_sensor_voltage_info(
                            sensor_voltage_mo
                        )
                    )

        self.log.debug(
            'get_sensor_info',
            json.dumps(sensor, indent=4)
        )

        return sensor
