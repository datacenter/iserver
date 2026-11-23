import time


class NsoCnfmCnfiApi():
    def __init__(self):
        self.cnfm_cnfi_mo = None

    def get_cnfm_cnfi_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_cnfi_mo is not None:
                return self.cnfm_cnfi_mo

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/cisco-cnf-descriptor:cnf/cisco-cnfo:cnf-instance'
            )
            self.log.nso(
                'get',
                'cnf-instance',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'cnf-instance',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success:
            self.log.error(
                'nso.get_cnfm_cnfi_mo',
                'Failed to get cnfi'
            )
            return None

        self.cnfm_cnfi_mo = content['cisco-cnfo:cnf-instance']

        self.log.nso_mo(
            'cnf-instance',
            self.cnfm_cnfi_mo
        )

        return self.cnfm_cnfi_mo
