from lib import filter_helper


class K8sPlanInfo():
    def __init__(self):
        self.plan = None

    def get_plan_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['migration_type'] = self.get(managed_object, 'spec:type')
        info['provider_source'] = self.get(managed_object, 'spec:provider:source:name')
        info['provider_destination'] = self.get(managed_object, 'spec:provider:destination:name')

        info['network_map_namespace'] = self.get(managed_object, 'spec:map:network:namespace')
        info['network_map_name'] = self.get(managed_object, 'spec:map:network:name')
        info['network_mapT'] = [
            info['network_map_namespace'],
            info['network_map_name']
        ]

        info['storage_map_namespace'] = self.get(managed_object, 'spec:map:storage:namespace')
        info['storage_map_name'] = self.get(managed_object, 'spec:map:storage:name')
        info['storage_mapT'] = [
            info['storage_map_namespace'],
            info['storage_map_name']
        ]

        info['vm_name'] = []
        info['vm_migration_state'] = []
        vms_mo = self.get(managed_object, 'spec:vms', on_error=[], on_none=[])
        for vm_mo in vms_mo:
            vm_name = self.get(vm_mo, 'name')
            if vm_name is not None:
                info['vm_name'].append(vm_name)
                state = {}
                state['vm'] = vm_name
                state['state'] = 'Pending'
                info['vm_migration_state'].append(state)
        
        migration_vms_mo = self.get(managed_object, 'status:migration:vms', on_error=[], on_none=[])
        for migration_vm_mo in migration_vms_mo:
            migration_vm_name = self.get(migration_vm_mo, 'name')
            if migration_vm_name is None:
                continue

            for state in info['vm_migration_state']:
                if state['vm'] == migration_vm_name:
                    state['state'] = migration_vm_mo['phase']

                    if state['state'] == 'CopyDisksVirtV2V':
                        pipeline_mos = self.get(migration_vm_mo, 'pipeline', on_error=[], on_none=[])
                        for pipeline_mo in pipeline_mos:
                            pipeline_phase = self.get(pipeline_mo, 'phase')
                            if pipeline_phase == 'Running':
                                state['state'] = 'CopyDisksVirtV2V [%s/%s]%s' % (
                                    pipeline_mo['progress']['completed'],
                                    pipeline_mo['progress']['total'],
                                    pipeline_mo['annotations']['unit']
                                )

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        info['stateT'] = []
        info['state'] = None

        info['success'] = False
        info['successTick'] = '\u2717'
        info['__Output']['successTick'] = 'Red'

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['start_ready'] = False
        info['running'] = False

        if 'Ready' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
            info['start_ready'] = True
            
        if 'Ready' in info['conditions'] and 'Executing' not in info['conditions'] and 'Succeeded' not in info['conditions']:
            info['stateT'].append('Ready')

        if 'Executing' in info['conditions']:
            info['running'] = True
            info['stateT'].append('Running')
            info['start_ready'] = False

        if 'Succeeded' in info['conditions']:
            info['success'] = True 
            info['successTick'] = '\u2713'
            info['__Output']['successTick'] = 'Green'
            info['state'] = 'Completed'
            info['stateT'].append('Completed')
            info['start_ready'] = False

        if 'Archived' in info['conditions']:
            info['state'] = 'Archived'
            info['stateT'].append('Archived')
            info['start_ready'] = False

        info['vms_found'] = True
        if 'VMNotFound' in info['conditions']:
            info['vms_found'] = False
            info['state'] = 'InvalidVm'
            info['stateT'].append('Invalid VM')
            info['stateT'].append('Cannot start')
            info['start_ready'] = False

        return info

    def add_plan_info(self, info, nmap_info=False, smap_info=False):
        if nmap_info:
            nmap = self.get_network_map(
                info['network_map_namespace'],
                info['network_map_name'],
                cache_enabled=True
            )
            if nmap is not None:
                for item in nmap['map']:
                    info['network_mapT'].append(
                        '%s => %s' % (
                            item['source'],
                            item['destination']
                        )
                    )

        if smap_info:
            smap = self.get_storage_map(
                info['storage_map_namespace'],
                info['storage_map_name'],
                cache_enabled=True
            )
            if smap is not None:
                for item in smap['map']:
                    info['storage_mapT'].append(
                        '%s => %s' % (
                            item['source'],
                            item['destination']
                        )
                    )

        return info
    

    def get_plans_info(self, cache_enabled=True):
        if cache_enabled:
            if self.plan is not None:
                return self.plan

        managed_objects = self.get_plan_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.plan = []
        for managed_object in managed_objects:
            plan_info = {}
            plan_info['info'] = self.get_plan_info(
                managed_object
            )
            plan_info['mo'] = managed_object
            self.plan.append(
                plan_info
            )

        return self.plan

    def match_plan(self, plan_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, plan_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (plan_info['namespace'], plan_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_plan',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_plans(self, object_filter=None, smap_info=False, nmap_info=False, return_mo=False, cache_enabled=True):
        all_plans = self.get_plans_info(cache_enabled=cache_enabled)
        if all_plans is None:
            return None

        plans = []

        if nmap_info and not cache_enabled:
            self.get_network_maps(cache_enabled=False)

        if smap_info:
            self.get_storage_maps(cache_enabled=False)

        for plan_info in all_plans:
            if not self.match_plan(plan_info['info'], object_filter):
                continue

            if return_mo:
                plans.append(
                    plan_info['mo']
                )
                continue

            plan_info['info'] = self.add_plan_info(
                plan_info['info'], 
                nmap_info=nmap_info, 
                smap_info=smap_info
            )

            plans.append(
                plan_info['info']
            )

        return plans

    def is_plan(self, namespace, name, cache_enabled=True):
        if self.get_plan(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_plan(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        plans = self.get_plans(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if plans is None:
            return None

        if len(plans) == 1:
            return plans[0]

        return None
