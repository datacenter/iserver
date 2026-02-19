import json
import random

from lib.intersight import chassis_extra_attributes
from lib.intersight.chassis_filter import ChassisFilter
from lib.intersight.chassis_cache import ChassisCache


class ChassisInfo(ChassisCache, ChassisFilter):
    """Class for intersight chassis objects
    """
    def __init__(self):
        ChassisFilter.__init__(self)
        ChassisCache.__init__(self)

    def get_default_settings(self):
        settings = {}
        settings['power'] = False
        settings['fan'] = False
        settings['fan_control'] = False
        settings['module'] = False
        settings['port'] = False
        settings['node'] = False
        return settings

    def get_info(self, chassiz_mo, settings, match_rules, cache_ttl, prepare_cache=True, bar_handler=None):
        if prepare_cache:
            self.set_cache(chassiz_mo, settings, cache_ttl)

        chassiz_info = []

        for chassis_mo in chassiz_mo:
            chassis_info_handler = chassis_extra_attributes.ChassisExtraAttributes(self.iaccount, log_id=self.log_id)
            chassis_info = chassis_info_handler.add_chassis_attributes(
                chassis_mo,
                settings
            )

            chassiz_info.append(
                chassis_info
            )

            if bar_handler is not None:
                bar_handler.next()

        return chassiz_info

    def anonymize_chassis_info(self, chassis_info):
        chassis_info['Name'] = 'Chassis%s' % (random.randint(100, 999))
        chassis_info['Moid'] = 'Moid-value'
        chassis_info['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
        chassis_info['Serial'] = 'SN-%s' % (random.randint(10, 99))
        chassis_info['ChassisSerial'] = chassis_info['Serial']

        if 'ContractInfo' in chassis_info:
            chassis_info['ContractInfo']['PurchaseOrderNumber'] = 'PO%s' % (random.randint(1, 254))
            chassis_info['ContractInfo']['SalesOrderNumber'] = 'SO%s' % (random.randint(1, 254))
            chassis_info['ContractInfo']['ContractUpdatedTime'] = '2025-01-01T00:00:00.000Z'

        if 'Inventory' in chassis_info:
            for item in chassis_info['Inventory']:
                item['Name'] = chassis_info['Name']
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['ServerType'] = '---'
                item['ServerPid'] = '---'
                item['ServerSerial'] = '---'

        if 'NodeInfo' in chassis_info:
            for item in chassis_info['NodeInfo']:
                item['Moid'] = 'Moid-value'
                item['Name'] = '%s-%s' % (
                    chassis_info['Name'],
                    item['SlotId']
                )
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'IfmInfo' in chassis_info:
            for item in chassis_info['IfmInfo']:
                item['Moid'] = 'Moid-value'
                item['ManagementIp'] = '--'
                item['ManagementSubnet'] = '--'
                item['ManagementPrefix'] = '--'
                item['ManagementCidr'] = '--'
                item['ManagementGateway'] = '--'
                item['ManagementVlan'] = '--'
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Version'] = '1.0(1a)'

        if 'ExpanderModuleInfo' in chassis_info:
            for item in chassis_info['ExpanderModuleInfo']:
                item['Moid'] = 'Moid-value'
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))

        if 'FanModuleInfo' in chassis_info:
            for item in chassis_info['FanModuleInfo']:
                item['Moid'] = 'Moid-value'

        if 'FanInfo' in chassis_info:
            for item in chassis_info['FanInfo']:
                item['Moid'] = 'Moid-value'
                item['PartNumber'] = 'PN-%s' % (random.randint(10, 99))
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Sku'] = 'SKU-%s' % (random.randint(10, 99))

        if 'FanControlInfo' in chassis_info:
            chassis_info['FanControlInfo']['Moid'] = 'Moid-value'

        if 'HostPortInfo' in chassis_info:
            for item in chassis_info['HostPortInfo']:
                item['Moid'] = 'Moid-value'
                item['MacAddress'] = 'aa:bb:%s:%s:%s:%s' % (
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99),
                    random.randint(10, 99)
                )

        if 'PsuInfo' in chassis_info:
            for item in chassis_info['PsuInfo']:
                item['Moid'] = 'Moid-value'
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))


        if 'Domain' in chassis_info:
            chassis_info['Domain']['Name'] = 'Domain-%s' % (random.randint(10, 99))
            for item in chassis_info['Domain']['Switch']:
                item['Moid'] = 'Moid-value'
                item['Serial'] = 'SN-%s' % (random.randint(10, 99))
                item['Name'] = 'Switch %s' % (item['SwitchId'])
                item['Version'] = '1.0(1a)'

                base = '10.%s.%s' % (
                    random.randint(1, 254),
                    random.randint(1, 254)
                )
                item['OutOfBandIpAddress'] = '%s.%s' % (
                    base,
                    random.randint(1, 253)
                )
                item['OutOfBandIpGateway'] = '%s.254' % (
                    base
                )

                item['OutOfBandIpMask'] = '255.255.255.0'

        return chassis_info
