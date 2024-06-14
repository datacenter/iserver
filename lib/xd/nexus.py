from lib.nexus import settings as nexus_settings
from lib.nexus import nxapi


def get_nexus_lldp_info(log_id=None, verbose=False, cache_enabled=False):
    nexus_lldp_info = []

    nexus_settings_handler = nexus_settings.NexusSettings(log_id=log_id)
    nexus_switches = nexus_settings_handler.get_nexus_switches()
    if nexus_switches is not None:
        for nexus_switch in nexus_switches:
            nexus_handler = nxapi.NxApi(
                nexus_switch['ip'],
                nexus_switch['username'],
                nexus_switch['password'],
                name=nexus_switch['name'],
                log_id=log_id,
                cache_enabled=cache_enabled
            )

            info = {}
            info['name'] = nexus_switch['name']
            info['neighbors'] = nexus_handler.get_lldp_neighbors()
            nexus_lldp_info.append(
                info
            )

    return nexus_lldp_info
