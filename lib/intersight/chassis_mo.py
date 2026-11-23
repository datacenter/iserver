class ChassisMo():
    def __init__(self):
        pass

    def get_mo(self, match_rules=None, cache_ttl=None):
        chassiz_mo = None

        if cache_ttl is not None:
            chassiz_mo = self.cache_handler.get_intersight_cache_entry(
                'inventory.chassis.%s' % (self.iaccount),
                cache_ttl=cache_ttl
            )

        if chassiz_mo is None:
            chassiz_mo = self.chassis_handler.get_all()
            self.cache_handler.set_intersight_cache_entry(
                'inventory.chassis.%s' % (self.iaccount),
                chassiz_mo
            )

        selected_chassiz_mo = []
        for chassis_mo in chassiz_mo:
            if self.match_chassis_mo(chassis_mo, match_rules):
                selected_chassiz_mo.append(chassis_mo)

        return selected_chassiz_mo
