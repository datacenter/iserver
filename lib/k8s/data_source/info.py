from lib import filter_helper


class K8sDataSourceInfo():
    def __init__(self):
        self.data_source = None

    def get_data_source_info(self, data_source_mo):
        if data_source_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            data_source_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(data_source_mo, 'spec')
        info['status'] = self.get(data_source_mo, 'status')

        info['pvc_namespace'] = self.get(data_source_mo, 'spec:source:pvc:namespace')
        info['pvc_name'] = self.get(data_source_mo, 'spec:source:pvc:name')
        
        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['error'] = []
        conditions_mo = self.get(data_source_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'Ready':
                        if self.get(condition_mo, 'status') == 'True':
                            info['ready'] = True
                            info['readyTick'] = '\u2713'
                            info['__Output']['readyTick'] = 'Green'
                        else:
                            info['error'].append('%s [%s]' % (
                                self.get(condition_mo, 'message', on_error='---', on_none='---'), 
                                self.get(condition_mo, 'reason', on_error='---', on_none='---')
                            ))
                            
        return info

    def get_data_sources_info(self, cache_enabled=True):
        if cache_enabled:
            if self.data_source is not None:
                return self.data_source

        managed_objects = self.get_data_source_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.data_source = []
        for managed_object in managed_objects:
            data_source_info = {}
            data_source_info['info'] = self.get_data_source_info(
                managed_object
            )
            data_source_info['mo'] = managed_object
            self.data_source.append(
                data_source_info
            )

        return self.data_source

    def match_data_source(self, data_source_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, data_source_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, data_source_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_data_source',
                    'Unsupported key: %s' % (key)
                )

        return True

    def add_data_source_info(self, info, pvcs=None, crons=None, dvs=None):
        if pvcs is not None:
            info['__Output']['pvc_phase'] = 'Red'
            info['pvc_phase'] = 'Not found'
            for pvc in pvcs:
                if pvc['namespace'] != info['pvc_namespace']:
                    continue

                if pvc['name'] != info['pvc_name']:
                    continue

                info['pvc_phase'] = pvc['phase']
                info['__Output']['pvc_phase'] = pvc['__Output']['phase']

        if dvs is not None:
            info['__Output']['dv_phase'] = 'Red'
            info['dv_phase'] = 'Not found'
            for dv in dvs:
                if dv['namespace'] != info['pvc_namespace']:
                    continue

                if dv['name'] != info['pvc_name']:
                    continue

                info['dv_phase'] = dv['phase']
                info['__Output']['dv_phase'] = dv['__Output']['boundTick']

        if crons is not None:
            info['__Output']['schedule'] = 'Red'
            info['schedule'] = '---'

            for cron in crons:
                if cron['data_source'] != info['name']:
                    continue

                info['schedule'] = cron['schedule']
                info['__Output']['schedule'] = cron['__Output']['readyTick']

        return info

    def get_data_sources(self, object_filter=None, dv_info=False, cron_info=False, pvc_info=False, return_mo=False, cache_enabled=True):
        all_data_sources = self.get_data_sources_info(cache_enabled=cache_enabled)
        if all_data_sources is None:
            return None

        data_sources = []

        pvcs = None
        if pvc_info:
            pvcs = self.get_pvcs(cache_enabled=cache_enabled)

        crons = None
        if cron_info:
            crons = self.get_data_import_crons(cache_enabled=cache_enabled)

        dvs = None
        if dv_info:
            dvs = self.get_data_volumes(cache_enabled=cache_enabled)

        for data_source_info in all_data_sources:
            data_source_info['info'] = self.add_data_source_info(
                data_source_info['info'],
                dvs=dvs,
                pvcs=pvcs,
                crons=crons
            )
            if not self.match_data_source(data_source_info['info'], object_filter):
                continue

            if return_mo:
                data_sources.append(
                    data_source_info['mo']
                )
                continue

            data_sources.append(
                data_source_info['info']
            )

        return data_sources

    def is_data_source(self, namespace, name, cache_enabled=True):
        if self.get_data_source(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_data_source(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        data_sources = self.get_data_sources(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if data_sources is None:
            return None

        if len(data_sources) == 1:
            return data_sources[0]

        return None
