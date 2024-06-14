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
