from lib import filter_helper


class NsoCnfmPlanInfo():
    def __init__(self):
        self.cnfm_plan = None

    def get_cnfm_plan_info(self, cnfm_plan_mo):
        if cnfm_plan_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(
            cnfm_plan_mo,
            'name'
        )

        info['component'] = []
        components_mo = self.get(
            cnfm_plan_mo,
            'plan:component',
            on_error=[],
            on_none=[]
        )
        for component_mo in components_mo:
            component_info = {}
            component_info['type'] = self.get(
                component_mo,
                'type'
            )
            component_info['name'] = self.get(
                component_mo,
                'name'
            )
            component_info['back_track'] = self.get(
                component_mo,
                'back-track'
            )

            component_info['state'] = []
            component_states_mo = self.get(
                component_mo,
                'state',
                on_error=[],
                on_none=[]
            )
            for component_state_mo in component_states_mo:
                component_state_info = {}
                component_state_info['__Output'] = {}
                component_state_info['name'] = self.get(
                    component_state_mo,
                    'name'
                )
                component_state_info['status'] = self.get(
                    component_state_mo,
                    'status'
                )
                if component_state_info['status'] == 'reached':
                    component_state_info['__Output']['status'] = 'Green'
                else:
                    component_state_info['__Output']['status'] = 'Red'

                component_state_info['when'] = self.get(
                    component_state_mo,
                    'when'
                )
                component_state_info['age'] = self.convert_timestamp_to_age(
                    component_state_info['when'],
                    on_error='--'
                )
                component_state_info['pre-conditions'] = self.get(
                    component_state_mo,
                    'pre',
                    on_error={},
                    on_none={}
                )
                component_state_info['post-actions'] = self.get(
                    component_state_mo,
                    'post',
                    on_error={},
                    on_none={}
                )
                component_info['state'].append(
                    component_state_info
                )

            info['component'].append(
                component_info
            )

        info['ready'] = []
        for component_info in info['component']:
            ready_info = {}
            ready_info['__Output'] = {}

            for key in ['name', 'type', 'back_track']:
                ready_info[key] = component_info[key]

            for component_state_info in component_info['state']:
                if component_state_info['name'] == 'tailf-ncs:ready':
                    ready_info['status'] = component_state_info['status']
                    ready_info['age'] = component_state_info['age']
                    ready_info['when'] = self.get(
                        component_state_info,
                        'when'
                    )
                    ready_info['__Output']['status'] = 'Red'
                    ready_info['ready'] = False
                    if ready_info['status'] == 'reached':
                        ready_info['__Output']['status'] = 'Green'
                        ready_info['ready'] = True

                    break

            info['ready'].append(
                ready_info
            )

        return info

    def get_cnfm_plans_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_plan is not None:
                return self.cnfm_plan

        managed_objects = self.get_cnfm_plan_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_plan = []
        for managed_object in managed_objects:
            cnfm_plan_info = self.get_cnfm_plan_info(
                managed_object
            )
            self.cnfm_plan.append(
                cnfm_plan_info
            )

        return self.cnfm_plan

    def match_cnfm_plan(self, cnfm_plan_info, cnfm_plan_filter):
        if cnfm_plan_filter is None or len(cnfm_plan_filter) == 0:
            return True

        for ap_rule in cnfm_plan_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_plan_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_plan',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_plans(self, object_filter=None, cache_enabled=True):
        all_cnfm_plans = self.get_cnfm_plans_info(cache_enabled=cache_enabled)
        if all_cnfm_plans is None:
            return None

        cnfm_plans = []

        for cnfm_plan_info in all_cnfm_plans:
            if not self.match_cnfm_plan(cnfm_plan_info, object_filter):
                continue

            cnfm_plans.append(
                cnfm_plan_info
            )

        return cnfm_plans

    def get_cnfm_plan(self, cnfm_instance_name, cache_enabled=True):
        plans = self.get_cnfm_plans(
            object_filter=[
                'name:%s' % (cnfm_instance_name)
            ],
            cache_enabled=cache_enabled
        )
        if plans is None or len(plans) != 1:
            return None

        return plans[0]
