class FiMo():
    def __init__(self):
        pass

    def get_mo(self, match_rules=None, cache_ttl=None):
        fi_mo = None

        if cache_ttl is not None:
            fi_mo = self.cache_handler.get_intersight_cache_entry(
                'inventory.fi.%s' % (self.iaccount),
                cache_ttl=cache_ttl
            )

        if fi_mo is None:
            fi_mo = self.fi_handler.get_all()
            self.cache_handler.set_intersight_cache_entry(
                'inventory.fi.%s' % (self.iaccount),
                fi_mo
            )

        selected_fi_mo = []
        for fi_mo in fi_mo:
            if self.match_fi_mo(fi_mo, match_rules):
                selected_fi_mo.append(fi_mo)

        return selected_fi_mo
