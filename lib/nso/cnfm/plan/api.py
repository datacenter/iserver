import time


class NsoCnfmPlanApi():
    def __init__(self):
        self.cnfm_plan_mo = None

    def get_cnfm_plan_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_plan_mo is not None:
                return self.cnfm_plan_mo

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/cisco-cnf-descriptor:cnf/cisco-cnfo:cnf-plan'
            )
            self.log.nso(
                'get',
                'cnf-plan',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'cnf-plan',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success:
            self.log.error(
                'nso.get_cnfm_plan_mo',
                'Failed to get plan'
            )
            return None

        self.cnfm_plan_mo = content['cisco-cnfo:cnf-plan']

        self.log.nso_mo(
            'cnf-plan',
            self.cnfm_plan_mo
        )

        return self.cnfm_plan_mo
