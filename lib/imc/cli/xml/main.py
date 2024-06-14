import json


class ImcCliXml():
    def __init__(self):
        self.xml_mo = None

    def get_xml_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.xml_mo is not None:
                return self.xml_mo

            self.xml_mo = self.get_icm_cli_cache_entry(
                'xml'
            )
            if self.xml_mo is not None:
                return self.xml_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show xmlapi detail
        # XMLAPI Settings:
        #     Enabled: yes
        #     Active Sessions: 0
        #     Max Sessions: 4

        self.xml_mo = self.show_dict(
            'show xmlapi detail',
            start='XMLAPI Settings:'
        )

        if self.xml_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'xml',
            self.xml_mo
        )

        self.log.debug(
            'get_xml_mo',
            json.dumps(self.xml_mo, indent=4)
        )
        return self.xml_mo

    def get_xml_info(self, xml_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in xml_mo:
            info[key] = xml_mo[key]

        self.log.debug(
            'get_xml_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_xml(self, cache_enabled=True):
        xml_mo = self.get_xml_mo(cache_enabled=cache_enabled)
        if xml_mo is None:
            return None

        xml_info = self.get_xml_info(
            xml_mo
        )

        return xml_info
