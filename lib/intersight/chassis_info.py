import json

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
        settings['summary'] = {}
        settings['summary']['enabled'] = True
        settings['power'] = {}
        settings['power']['enabled'] = False
        settings['fan'] = {}
        settings['fan']['enabled'] = False
        settings['module'] = {}
        settings['module']['enabled'] = False
        settings['port'] = {}
        settings['port']['enabled'] = False
        settings['node'] = {}
        settings['node']['enabled'] = False

        return settings

    def get_info(self, chassiz_mo, settings, match_rules, cache_ttl, parallel=False):
        self.set_cache(chassiz_mo, settings, cache_ttl, parallel=parallel)
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

        return chassiz_info
