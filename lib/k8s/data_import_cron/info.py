from lib import filter_helper


class K8sDataImportCronInfo():
    def __init__(self):
        self.data_import_cron = None

    def get_data_import_cron_info(self, data_import_cron_mo):
        if data_import_cron_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            data_import_cron_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(data_import_cron_mo, 'spec')
        info['status'] = self.get(data_import_cron_mo, 'status')

        info['data_source'] = self.get(data_import_cron_mo, 'spec:managedDataSource')
        info['data_volume'] = []
        imports_mo = self.get(data_import_cron_mo, 'status:currentImports', on_error=[], on_none=[])
        for import_mo in imports_mo:
            info['data_volume'].append(self.get(import_mo, 'DataVolumeName'))
            
        info['schedule'] = self.get(data_import_cron_mo, 'spec:schedule')
        info['url'] = self.get(data_import_cron_mo, 'spec:template:spec:source:registry:url')
        info['storage'] = self.get(data_import_cron_mo, 'spec:template:spec:storage:resources:requests:storage')

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        conditions_mo = self.get(data_import_cron_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'UpToDate':
                        if self.get(condition_mo, 'status') == 'True':
                            info['ready'] = True
                            info['readyTick'] = '\u2713'
                            info['__Output']['readyTick'] = 'Green'

        return info

    def get_data_import_crons_info(self, cache_enabled=True):
        if cache_enabled:
            if self.data_import_cron is not None:
                return self.data_import_cron

        managed_objects = self.get_data_import_cron_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.data_import_cron = []
        for managed_object in managed_objects:
            data_import_cron_info = {}
            data_import_cron_info['info'] = self.get_data_import_cron_info(
                managed_object
            )
            data_import_cron_info['mo'] = managed_object
            self.data_import_cron.append(
                data_import_cron_info
            )

        return self.data_import_cron

    def match_data_import_cron(self, data_import_cron_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, data_import_cron_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, data_import_cron_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_data_import_cron',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_data_import_crons(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_data_import_crons = self.get_data_import_crons_info(cache_enabled=cache_enabled)
        if all_data_import_crons is None:
            return None

        data_import_crons = []

        for data_import_cron_info in all_data_import_crons:
            if not self.match_data_import_cron(data_import_cron_info['info'], object_filter):
                continue

            if return_mo:
                data_import_crons.append(
                    data_import_cron_info['mo']
                )
                continue

            data_import_crons.append(
                data_import_cron_info['info']
            )

        return data_import_crons

    def is_data_import_cron(self, namespace, name, cache_enabled=True):
        if self.get_data_import_cron(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_data_import_cron(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        data_import_crons = self.get_data_import_crons(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if data_import_crons is None:
            return None

        if len(data_import_crons) == 1:
            return data_import_crons[0]

        return None
