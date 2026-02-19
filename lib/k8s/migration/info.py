from lib import filter_helper


class K8sMigrationInfo():
    def __init__(self):
        self.migration = None

    def get_migration_info(self, managed_object):
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

        info['plan'] = self.get(managed_object, 'spec:plan:name')
        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        info['state'] = None
        info['finished'] = False

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'
        if 'Ready' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
            info['state'] = 'Ready'
            
        info['running'] = False
        info['runningTick'] = '\u2717'
        info['__Output']['runningTick'] = 'Red'
        if 'Running' in info['conditions']:
            info['running'] = True
            info['runningTick'] = '\u2713'
            info['__Output']['runningTick'] = 'Green'
            info['state'] = 'Running'

        info['succeeded'] = False
        info['succeededTick'] = '\u2717'
        info['__Output']['succeededTick'] = 'Red'
        if 'Succeeded' in info['conditions']:
            info['succeeded'] = True
            info['succeededTick'] = '\u2713'
            info['__Output']['succeededTick'] = 'Green'
            info['state'] = 'Succeeded'
            info['finished'] = True

        info['failed'] = False
        info['failedTick'] = ''
        if 'Failed' in info['conditions']:
            info['failed'] = True
            info['failedTick'] = '\u2713'
            info['__Output']['succeededTick'] = 'Red'
            info['state'] = 'Failed'
            info['finished'] = True

        info['vm_ids'] = {}
        info['vm'] = []
        info['event'] = []
        vms_mo = self.get(managed_object, 'status:vms', on_error=[], on_none=[])
        for vm_mo in vms_mo:
            vm_id = self.get(vm_mo, 'id')
            if vm_id is not None:
                info['vm_ids'][vm_id] = self.get(vm_mo, 'name')
            
            vm_info = {}
            vm_info['name'] = self.get(vm_mo, 'name')
            vm_info['phase'] = self.get(vm_mo, 'phase')
            vm_info['succeeded'] = False
            vm_info['failed'] = False
            vm_info['finished'] = False
            vm_info['progress'] = None

            if vm_info['phase'] == 'Completed':
                vm_info['finished'] = True

            vm_conditions = self.get_conditions(
                self.get(vm_mo, 'conditions')
            )
            if 'Succeeded' in vm_conditions:
                vm_info['succeeded'] = True
            
            if 'Failed' in vm_conditions:
                vm_info['failed'] = True

            if not vm_info['finished']:
                pipeline_mos = self.get(vm_mo, 'pipeline', on_error=[], on_none=[])
                if vm_info['phase'] == 'AllocateDisks':
                    for pipeline_mo in pipeline_mos:
                        pipeline_name = self.get(pipeline_mo, 'name')
                        if pipeline_name == 'DiskAllocation':
                            vm_info['progress'] = '%s/%s %s' % (
                                self.get(pipeline_mo, 'progress:completed'),
                                self.get(pipeline_mo, 'progress:total'),
                                self.get(pipeline_mo, 'annotations:unit')
                            )

                pipeline_mos = self.get(vm_mo, 'pipeline', on_error=[], on_none=[])
                if vm_info['phase'] == 'CopyDisksVirtV2V':
                    for pipeline_mo in pipeline_mos:
                        pipeline_name = self.get(pipeline_mo, 'name')
                        if pipeline_name == 'DiskTransferV2v':
                            vm_info['progress'] = '%s/%s %s' % (
                                self.get(pipeline_mo, 'progress:completed'),
                                self.get(pipeline_mo, 'progress:total'),
                                self.get(pipeline_mo, 'annotations:unit')
                            )

            info['vm'].append(vm_info)

            vm_description = 'VM [%s] Phase [%s]' % (vm_info['name'], vm_info['phase'])
            if vm_info['finished']:
                if vm_info['succeeded']:
                    vm_description = '%s Success' % (vm_description)
                if vm_info['failed']:
                    vm_description = '%s Failure' % (vm_description)

            if not vm_info['finished'] and vm_info['progress'] is not None:
                vm_description = '%s Progress [%s]' % (vm_description, vm_info['progress'])

            info['event'].append(vm_description)

        return info
    
    def add_migration_info(self, info, vms=None, vmis=None, pvcs=None, dvs=None, pods=None):
        info['vms'] = []
        migrated_vms = []
        vm_descriptions = {}

        if vms is not None:
            for vm in vms:
                if 'migration' not in vm['label']:
                    continue

                if vm['label']['migration'] != info['uid']:
                    continue

                info['vms'].append(vm)
                vm_description = '---'
                vm_id = None
                if 'vmID' in vm['label']:
                    vm_id = vm['label']['vmID']
                    vm_description = vm_id
                
                vm_name = None
                if vm_id in info['vm_ids']:
                    vm_name = info['vm_ids'][vm_id]
                    vm_description = vm_name

                migrated_vms.append('%s/%s' % (vm['namespace'], vm['name']))
                vm_descriptions['%s/%s' % (vm['namespace'], vm['name'])] = vm_description

                event = 'VM [%s] Virtual Machine [%s/%s] State [%s]' % (
                    vm_description,
                    vm['namespace'],
                    vm['name'],
                    vm['status']
                )
                info['event'].append(event)

        info['vmis'] = []
        if vmis is not None:
            for vmi in vmis:
                if '%s/%s' % (vmi['namespace'], vmi['name']) not in migrated_vms:
                    continue

                info['vmis'].append(vmi)
                vm_description = vm_descriptions['%s/%s' % (vmi['namespace'], vmi['name'])]
                
                event = 'VM [%s] Virtual Machine Instance [%s/%s] State [%s]' % (
                    vm_description,
                    vmi['namespace'],
                    vmi['name'],
                    vmi['phase']
                )
                info['event'].append(event)

        info['pvcs'] = []
        if pvcs is not None:
            for pvc in pvcs:
                if 'migration' not in pvc['label']:
                    continue

                if pvc['label']['migration'] != info['uid']:
                    continue

                info['pvcs'].append(pvc)
                vm_description = '---'
                vm_id = None
                if 'vmID' in pvc['label']:
                    vm_id = pvc['label']['vmID']
                    vm_description = vm_id
                
                vm_name = None
                if vm_id in info['vm_ids']:
                    vm_name = info['vm_ids'][vm_id]
                    vm_description = vm_name
                
                event = 'VM [%s] PVC [%s/%s] Capacity [%s] Phase [%s]' % (
                    vm_description,
                    pvc['namespace'],
                    pvc['name'],
                    self.get(pvc, 'capacity:storage'),
                    pvc['phase']
                )
                info['event'].append(event)

        info['dvs'] = []
        if dvs is not None:
            for dv in dvs:
                if 'migration' not in dv['label']:
                    continue

                if dv['label']['migration'] != info['uid']:
                    continue

                info['dvs'].append(dv)
                vm_description = '---'
                vm_id = None
                if 'vmID' in dv['label']:
                    vm_id = dv['label']['vmID']
                    vm_description = vm_id
                
                vm_name = None
                if vm_id in info['vm_ids']:
                    vm_name = info['vm_ids'][vm_id]
                    vm_description = vm_name
                
                event = 'VM [%s] DV [%s/%s] Progress [%s] Phase [%s]' % (
                    vm_description,
                    dv['namespace'],
                    dv['name'],
                    dv['progress'],
                    dv['phase']
                )
                info['event'].append(event)

        info['pods'] = []
        if pods is not None:
            for pod in pods:
                if 'migration' not in pod['label']:
                    continue

                if pod['label']['migration'] != info['uid']:
                    continue

                info['pods'].append(pod)
                vm_description = '---'
                vm_id = None
                if 'vmID' in pod['label']:
                    vm_id = pod['label']['vmID']
                    vm_description = vm_id
                
                vm_name = None
                if vm_id in info['vm_ids']:
                    vm_name = info['vm_ids'][vm_id]
                    vm_description = vm_name
                
                event = 'VM [%s] Pod [%s/%s] Phase [%s]' % (
                    vm_description,
                    pod['namespace'],
                    pod['name'],
                    pod['phase']
                )
                info['event'].append(event)

        return info
    
    def get_migrations_info(self, cache_enabled=True):
        if cache_enabled:
            if self.migration is not None:
                return self.migration

        managed_objects = self.get_migration_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.migration = []
        for managed_object in managed_objects:
            migration_info = {}
            migration_info['info'] = self.get_migration_info(
                managed_object
            )
            migration_info['mo'] = managed_object
            self.migration.append(
                migration_info
            )

        return self.migration

    def match_migration(self, migration_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, migration_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (migration_info['namespace'], migration_info['name'])):
                    return False

            if key == 'plan':
                key_found = True
                if not filter_helper.match_string(value, migration_info['plan']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_migration',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_migrations(self, object_filter=None, vm_info=False, vmi_info=False, pvc_info=False, dv_info=False, pod_info=False, return_mo=False, cache_enabled=True):
        all_migrations = self.get_migrations_info(cache_enabled=cache_enabled)
        if all_migrations is None:
            return None

        migrations = []

        vms = None
        if vm_info and len(all_migrations) > 0:
            vms = self.get_virtual_machines(cache_enabled=cache_enabled)

        vmis = None
        if vmi_info and len(all_migrations) > 0:
            vmis = self.get_virtual_machine_instances(cache_enabled=cache_enabled)

        pvcs = None
        if pvc_info and len(all_migrations) > 0:
            pvcs = self.get_pvcs(cache_enabled=cache_enabled)

        dvs = None
        if dv_info and len(all_migrations) > 0:
            dvs = self.get_data_volumes(cache_enabled=cache_enabled)

        pods = None
        if pod_info and len(all_migrations) > 0:
            pods = self.get_pods(cache_enabled=cache_enabled)

        for migration_info in all_migrations:
            migration_info['info'] = self.add_migration_info(
                migration_info['info'],
                vms=vms,
                vmis=vmis,
                pvcs=pvcs,
                dvs=dvs,
                pods=pods
            )

            if not self.match_migration(migration_info['info'], object_filter):
                continue

            if return_mo:
                migrations.append(
                    migration_info['mo']
                )
                continue

            migrations.append(
                migration_info['info']
            )

        return migrations

    def is_migration(self, namespace, name, cache_enabled=True):
        if self.get_migration(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_migration(self, namespace, name, vm_info=False, vmi_info=False, pvc_info=False, dv_info=False, pod_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        migrations = self.get_migrations(
            object_filter=object_filter,
            vm_info=vm_info,
            vmi_info=vmi_info,
            pvc_info=pvc_info,
            dv_info=dv_info,
            pod_info=pod_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if migrations is None:
            return None

        if len(migrations) == 1:
            return migrations[0]

        return None
