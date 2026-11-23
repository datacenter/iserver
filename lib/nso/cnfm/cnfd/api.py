import time


class NsoCnfmCnfdApi():
    def __init__(self):
        self.cnfm_cnfd_mo = None

    def get_cnfm_cnfd_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_cnfd_mo is not None:
                return self.cnfm_cnfd_mo

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/cisco-cnf-descriptor:cnf/cnfd'
            )
            self.log.nso(
                'get',
                'cnfd',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'cnfd',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success:
            self.log.error(
                'nso.get_cnfm_cnfd_mo',
                'Failed to get cnfd'
            )
            return None

        self.cnfm_cnfd_mo = content['cisco-cnf-descriptor:cnfd']

        self.log.nso_mo(
            'cnfd',
            self.cnfm_cnfd_mo
        )

        return self.cnfm_cnfd_mo
