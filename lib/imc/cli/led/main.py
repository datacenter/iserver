import json


class ImcCliLed():
    def __init__(self):
        self.led_mo = None

    def get_led_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.led_mo is not None:
                return self.led_mo

            self.led_mo = self.get_icm_cli_cache_entry(
                'led'
            )
            if self.led_mo is not None:
                return self.led_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /sensor # show led detail
        # LEDs:
        #     LED Name: LED_PSU_STATUS
        #     LED State: ON
        #     LED Color: GREEN
        #     :
        # LEDs:
        #     LED Name: LED_TEMP_STATUS
        #     LED State: ON
        #     LED Color: GREEN

        self.led_mo = self.show_list(
            'show led detail',
            'LEDs',
            'LED Name',
            method='last word',
            scope='sensor'
        )

        if self.led_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'led',
            self.led_mo
        )

        self.log.debug(
            'get_led_mo',
            json.dumps(self.led_mo, indent=4)
        )
        return self.led_mo

    def get_led_info(self, led_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in led_mo:
            if len(key) > 0:
                info[key] = led_mo[key]

        return info

    def get_led(self, cache_enabled=True):
        leds_mo = self.get_led_mo(cache_enabled=cache_enabled)
        if leds_mo is None:
            return None

        leds_info = []

        for led_mo in leds_mo:
            leds_info.append(
                self.get_led_info(
                    led_mo
                )
            )

        self.log.debug(
            'get_led_info',
            json.dumps(leds_info, indent=4)
        )

        return leds_info
