import time


class NsoCnfmResultApi():
    def __init__(self):
        self.cnfm_result_mo = None

    def get_cnfm_result_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_result_mo is not None:
                return self.cnfm_result_mo

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/cisco-cnf-descriptor:cnf/cisco-cnfo:cnf-result'
            )
            self.log.nso(
                'get',
                'cnf-result',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'cnf-result',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success:
            self.log.error(
                'nso.get_cnfm_result_mo',
                'Failed to get result'
            )
            return None

        self.cnfm_result_mo = content['cisco-cnfo:cnf-result']

        self.log.nso_mo(
            'cnf-result',
            self.cnfm_result_mo
        )

        return self.cnfm_result_mo
