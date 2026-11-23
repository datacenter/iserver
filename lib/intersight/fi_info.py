from lib import filter_helper
from lib.intersight import fi_extra_attributes
from lib.intersight.fi_filter import FiFilter
from lib.intersight.fi_cache import FiCache


class FiInfo(FiCache, FiFilter):
    """Class for intersight fi objects
    """
    def __init__(self):
        FiFilter.__init__(self)
        FiCache.__init__(self)

    def get_info(self, fis_mo, settings, match_rules, cache_ttl, prepare_cache=True, bar_handler=None):
        if prepare_cache:
            self.set_cache(fis_mo, settings, cache_ttl)

        fis_info = []

        for fi_mo in fis_mo:
            fi_info_handler = fi_extra_attributes.FiExtraAttributes(self.iaccount, log_id=self.log_id)
            fi_info = fi_info_handler.add_fi_attributes(
                fi_mo,
                settings
            )

            matched = True
            for item in match_rules['name']:
                if not filter_helper.match_string(item, fi_info['Name']):
                    matched = False

            if not matched:
                if bar_handler is not None:
                    bar_handler.next()
                continue
        
            fis_info.append(
                fi_info
            )

            if bar_handler is not None:
                bar_handler.next()

        if 'summary' in settings and settings['summary']:
            # Name is from network element summary
            fis_info = sorted(
                fis_info,
                key=lambda i: i['Name'].lower()
            )

        return fis_info
