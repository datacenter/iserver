import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

from lib.intersight.compute_cache import ComputeCache
from lib.intersight.compute_filter import ComputeFilter
from lib.intersight.computes_worfklow import ComputesWorkflow

from lib.intersight import compute_extra_attributes


class ComputeInfo(ComputeCache, ComputeFilter, ComputesWorkflow):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self):
        ComputeCache.__init__(self)
        ComputeFilter.__init__(self)
        ComputesWorkflow.__init__(self)

    def get_server_info(self, server_mo, settings, log_id=None):
        server_info_handler = compute_extra_attributes.ComputeExtraAttributes(
            self.iaccount,
            log_id=log_id
        )
        server_info = server_info_handler.get_server_info(
            server_mo,
            settings
        )
        return server_info

    def get_threaded(self, servers_mo, settings):
        start_time = int(time.time() * 1000)
        servers_info = []

        self.log_handler.debug(
            'computes_info.get_threaded',
            'Start %s threads' % (len(servers_mo))
        )

        with ProcessPoolExecutor() as executor:
            pool = [executor.submit(self.get_server_info, server_mo, settings, log_id=self.log_id) for server_mo in servers_mo]
            result = concurrent.futures.wait(
                pool,
                timeout=120,
                return_when=concurrent.futures.ALL_COMPLETED
            )
            executor.shutdown(
                wait=False,
                cancel_futures=True
            )

        self.log_handler.debug(
            'computes_info.get',
            'Completed: %s/%s/%s' % (
                len(result[0]),
                len(result[1]),
                len(servers_mo)
            )
        )

        for server_mo in servers_mo:
            server_info = self.log_handler.get_log(
                'server_info.%s' % (server_mo['Moid']),
                json_conversion=True
            )

            if server_info is None:
                self.log_handler.error(
                    'computes_info.get_server_info',
                    'No server info: %s' % (server_mo['Moid'])
                )
                continue

            servers_info.append(
                server_info
            )

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'computes_info.get_threaded',
            'Finished: %s ms' % (duration)
        )

        return servers_info

    def get_sequential(self, servers_mo, settings, bar_handler=None):
        start_time = int(time.time() * 1000)
        servers_info = []

        self.log_handler.debug(
            'compute_info.get_sequential',
            'Start'
        )

        for server_mo in servers_mo:
            server_start_time = int(time.time() * 1000)
            server_info = self.get_server_info(
                server_mo,
                settings,
                log_id=self.log_id
            )
            if server_info is None:
                self.log_handler.error(
                    'compute_info.get_sequential',
                    'No server info: %s' % (server_mo['Moid'])
                )
                continue

            servers_info.append(server_info)

            duration = int(time.time() * 1000) - server_start_time
            self.log_handler.debug(
                'computes_info.get_sequential',
                'Server %s: %s ms' % (
                    server_mo['Serial'],
                    duration
                )
            )

            if bar_handler is not None:
                bar_handler.next()

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'computes_info.get_sequential',
            'Finished: %s ms' % (duration)
        )

        return servers_info

    def get_info(self, servers_mo, settings, match_rules, cache_ttl, prepare_cache=True, parallel=False, bar_handler=None):
        if prepare_cache:
            self.set_cache(servers_mo, settings, cache_ttl)

        start_time = int(time.time() * 1000)

        if parallel:
            all_servers_info = self.get_threaded(
                servers_mo,
                settings
            )

        if not parallel:
            all_servers_info = self.get_sequential(
                servers_mo,
                settings,
                bar_handler=bar_handler
            )

        self.log_handler.debug(
            'compute_info.get_info',
            'Match rules: %s' % (match_rules)
        )

        servers_info = []
        for server_info in all_servers_info:
            matching_server_info = self.match_server(server_info, match_rules)
            if matching_server_info is not None:
                servers_info.append(
                    matching_server_info
                )

        servers_info = sorted(
            servers_info,
            key=lambda i: i['Name'].lower()
        )

        end_time = int(time.time() * 1000)
        duration = end_time - start_time

        self.log_handler.debug(
            'compute_info.get_info',
            'Selected %s/%s/%s servers in %s ms' % (len(servers_info), len(all_servers_info), len(servers_mo), duration)
        )

        return servers_info
