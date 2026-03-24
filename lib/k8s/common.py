import json
import time
import datetime

from lib import filter_helper


class K8sCommon():
    def __init__(self):
        pass

    def _get(self, value, key):
        if value is None:
            return '__ERROR'

        if ':' in key:
            subkey = key.split(':')[0]
            if subkey not in value:
                return '__ERROR'

            new_key = ':'.join(key.split(':')[1:])
            return self._get(value[subkey], new_key)

        if key in value:
            return value[key]

        return '__ERROR'

    def get(self, managed_object, key, on_error=None, on_none=None):
        if managed_object is None:
            return on_error

        if not isinstance(managed_object, dict):
            return on_error

        value = self._get(managed_object, key)
        if value == '__ERROR':
            return on_error

        if value is None:
            return on_none

        return value

    def convert_object(self, item):
        if item is None:
            return None

        if isinstance(item, str):
            return item

        if isinstance(item, int):
            return item

        if isinstance(item, dict):
            converted = {}
            for key in item:
                converted[key] = self.convert_object(
                    item[key]
                )
            return converted

        if isinstance(item, list):
            converted = []
            for key in item:
                converted.append(
                    self.convert_object(
                        key
                    )
                )
            return converted

        converted = str(
            item
        )

        return converted

    def convert_age(self, seconds):
        if seconds > 60 * 60 * 24:
            return '%sd' % (int(seconds / (60 * 60 * 24)))

        if seconds > 60 * 60:
            hours = 0
            while True:
                if seconds < 60 * 60:
                    break

                hours = hours + 1
                seconds = seconds - 60 * 60

            return '%sh%sm' % (
                hours,
                int(seconds / 60)
            )

        if seconds > 60:
            return '%sm' % (int(seconds / 60))

        return '%ss' % (seconds)

    def get_max_timestamp(self, current, timestamp):
        converted = self.convert_timestamp(timestamp)
        if converted is None:
            return current

        if current is None:
            return converted
        
        if converted > current:
            return converted
        
        return current
    
    def convert_timestamp(self, timestamp):
        if timestamp is None:
            return None

        new_timestamp = None
        if isinstance(timestamp, str):
            try:
                new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').timetuple()))
            except BaseException:
                pass

            if new_timestamp is None:
                try:
                    new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S%z').timetuple()))
                except BaseException:
                    pass

            if new_timestamp is None:
                try:
                    new_timestamp = int(time.mktime(datetime.datetime.strptime(timestamp.rstrip('Z'), '%Y-%m-%dT%H:%M:%S').timetuple()))
                except BaseException:
                    pass

            return new_timestamp

        try:
            new_timestamp = int(timestamp.timestamp())
        except BaseException:
            pass

        return new_timestamp

    def convert_timestamp_to_age(self, timestamp, on_error=None):
        timestamp = self.convert_timestamp(timestamp)
        if timestamp is None:
            return on_error

        return self.convert_age(int(time.time()) - timestamp)

    def get_base_info(self, managed_object, condition_map=None):
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

        if condition_map is not None:
            info = self.get_condition_info(managed_object, condition_map, info)
        
        return info

    def get_metadata_info(self, managed_object, exclude_labels=[], exclude_annotations=[]):
        info = {}

        if 'metadata' not in managed_object:
            return info

        info['name'] = self.get(managed_object, 'metadata:name')
        namespace = self.get(managed_object, 'metadata:namespace')
        if namespace is not None:
            info['namespace'] = namespace
            info['namespace_name'] = '%s/%s' % (
                info['namespace'],
                info['name']
            )
            info['namespace_nameT'] = [info['namespace'], info['name']]

        info['resource_version'] = self.get(managed_object, 'metadata:resourceVersion')
        labels = self.get_metadata_label_info(
            managed_object,
            'metadata:labels',
            exclude_labels=exclude_labels
        )
        info.update(labels)

        annotations = self.get_metadata_annotation_info(
            managed_object,
            'metadata:annotations',
            exclude_annotations=exclude_annotations
        )
        info.update(annotations)

        owner_property_name = 'owner_references'
        if owner_property_name not in managed_object['metadata']:
            owner_property_name = 'ownerReferences'

        owner_references = self.get_metadata_owner_info(
            managed_object,
            'metadata:%s' % (owner_property_name)
        )
        info.update(owner_references)

        timestamp_name = 'creation_timestamp'
        if timestamp_name not in managed_object['metadata']:
            timestamp_name = 'creationTimestamp'

        info['uid'] = self.get(
            managed_object,
            'metadata:uid'
        )
        
        info['age'] = self.convert_timestamp_to_age(
            self.get(
                managed_object,
                'metadata:%s' % (timestamp_name)
            ),
            on_error='--'
        )

        return info

    def get_metadata_label_info(self, managed_object, property_name, exclude_labels=[], chunk=60):
        info = {}
        info['label'] = self.get(managed_object, property_name, on_error={}, on_none={})
        info['labelT'] = []
        for key in info['label']:
            if key in exclude_labels:
                continue

            line = '%s = %s' % (
                key,
                info['label'][key]
            )

            if chunk is not None:
                lines = filter_helper.get_string_chunks(
                    line,
                    chunk
                )
                info['labelT'] = info['labelT'] + lines
            else:
                info['labelT'].append(
                    line
                )

        return info

    def get_metadata_annotation_info(self, managed_object, property_name, exclude_annotations=[], chunk=60):
        info = {}
        info['annotation'] = self.get(managed_object, property_name, on_error={}, on_none={})
        info['annotationT'] = []

        exclude_annotations.append(
            'kubectl.kubernetes.io/last-applied-configuration'
        )
        exclude_annotations.append(
            'operator.cdi.kubevirt.io/lastAppliedConfiguration'
        )

        for key in info['annotation']:
            if key in exclude_annotations:
                continue

            line = '%s = %s' % (
                key,
                info['annotation'][key]
            )

            if chunk is not None:
                if len(line.split('\n')) == 1:
                    lines = filter_helper.get_string_chunks(
                        line,
                        chunk
                    )

                    info['annotationT'] = info['annotationT'] + lines

                else:
                    for item in line.split('\n'):
                        lines = filter_helper.get_string_chunks(
                            item,
                            chunk,
                            separator=',',
                            extra_separator='-'
                        )

                        info['annotationT'] = info['annotationT'] + lines

            else:
                info['annotationT'].append(
                    line
                )

        return info

    def get_metadata_owner_info(self, managed_object, property_name):
        owner_kind = None
        owner_name = None

        owner_references = self.get(
            managed_object,
            property_name,
            on_error=[],
            on_none=[]
        )

        if len(owner_references) == 1:
            owner_kind = self.get(
                owner_references[0],
                'kind'
            )

            owner_name = self.get(
                owner_references[0],
                'name'
            )

        if owner_kind is None or owner_name is None:
            owner = None
        else:
            owner = '%s/%s' % (
                owner_kind,
                owner_name
            )

        info = {}
        info['owner_kind'] = owner_kind
        info['owner_name'] = owner_name
        info['owner'] = owner
        if owner_kind is None and owner_name is None:
            info['ownerT'] = [None]
        else:
            info['ownerT'] = [owner_kind, owner_name]

        return info

    def get_conditions(self, conditions_mo):
        conditions = []

        if conditions_mo is None:
            return conditions
        
        if not isinstance(conditions_mo, list):
            return conditions
        
        for condition_mo in conditions_mo:
            if condition_mo['status'].lower() == 'true':
                conditions.append(
                    condition_mo['type']
                )

        conditions = sorted(conditions)
        return conditions
    
    def get_condition_info(self, managed_object, condition_map, info):
        for key in condition_map:
            info[key] = False
            info['%s_status' % (key)] = None
            info['%s_reason' % (key)] = None
            info['%s_message' % (key)] = None
            info['%sTick' % (key)] = '\u2717'
            info['__Output']['%sTick' % (key)] = 'Red'

        conditions_mo = self.get(managed_object, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                for key in condition_map:
                    if condition_mo['type'] == condition_map[key]:
                        info['%s_status' % (key)] = self.get(condition_mo, 'status')
                        info['%s_reason' % (key)] = self.get(condition_mo, 'reason')
                        info['%s_message' % (key)] = self.get(condition_mo, 'message')
                        if condition_mo['status'] in ['True', '"True"']:
                            info[key] = True
                            info['%sTick' % (key)] = '\u2713'
                            info['__Output']['%sTick' % (key)] = 'Green'

        return info

    def get_managed_objects_info(self, object_name, namespace=None, cache_enabled=True):
        if cache_enabled:
            value = getattr(self, object_name)
            if value is not None:
                return value

        if namespace is None:
            managed_objects = getattr(self, 'get_%s_mo' % (object_name))(cache_enabled=cache_enabled)
        else:
            managed_objects = getattr(self, 'get_%s_mo' % (object_name))(namespace=namespace, cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        infos = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = getattr(self, 'get_%s_info' % (object_name))(managed_object)
            info['mo'] = managed_object
            infos.append(info)

        setattr(self, object_name, infos)
        return infos

    def get_infos(self, object_name, object_filter=None, return_mo=False, cache_enabled=True, add={}):
        namespace = None
        if object_filter is not None:
            for rule in object_filter:
                key = rule.split(':')[0]
                value = ':'.join(rule.split(':')[1:])
                if key == 'namespace' and '*' not in value:
                    namespace = value

        all_infos = self.get_managed_objects_info(object_name, namespace=namespace, cache_enabled=cache_enabled)
        if all_infos is None:
            return None

        if not return_mo:
            for key in add:
                if add[key]:
                    extended_add = 'add_%ss_%s' % (object_name, key)
                    if not hasattr(self, extended_add):
                        self.log.error('get_infos', 'Unsupported info add: %s' % (extended_add))
                        continue

                    all_infos = getattr(self, extended_add)(all_infos, cache_enabled=cache_enabled)

        infos = []

        for info in all_infos:
            extended_match = hasattr(self, 'match_%s' % (object_name))
            if not self.match_info(info['info'], object_filter, is_extended=extended_match):
                continue

            if hasattr(self, 'match_%s' % (object_name)):
                if not getattr(self, 'match_%s' % (object_name))(info['info'], object_filter):
                    continue

            if return_mo:
                infos.append(
                    info['mo']
                )
                continue

            infos.append(
                info['info']
            )

        return infos

    def get_info(self, object_name, name, namespace=None, return_mo=False, cache_enabled=True, **kwargs):
        object_filter = []
        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )
        object_filter.append(
            'name:%s' % (name)
        )
        infos = getattr(self, 'get_%ss' % (object_name))(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled,
            **kwargs
        )
        if infos is None:
            return None

        if len(infos) == 1:
            return infos[0]

        return None

    def get_common_match(self):
        return ['namespace', 'name']
    
    def match_info(self, info, object_filter, is_extended=False):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                if 'namespace' in info:
                    key_found = True
                    if not filter_helper.match_string(value, info['namespace']):
                        return False

            if key == 'name':
                if 'name' in info:
                    key_found = True
                    if not filter_helper.match_string(value, info['name']):
                        return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, info['owner']):
                    return False
                
            if not is_extended and not key_found:
                self.log.error(
                    'match_info',
                    'Unsupported key [%s]: %s' % (key, json.dumps(info))
                )

        return True

    def wait_managed_object(
            self, 
            object_name, 
            name, 
            namespace=None, 
            match_properties={}, 
            break_properties={}, 
            my_output=None,
            prompt=None, 
            max_time=60,
            log_error_on_timeout=True
        ):
        if my_output is not None and prompt is not None:
            if len(match_properties) > 0:
                my_output.default('%s with %s' % (prompt, json.dumps(match_properties)))
            else:
                my_output.default(prompt)

        start_time = int(time.time())
        while True:
            if namespace is None:
                info = getattr(self, 'get_%s' % (object_name))(
                    name,
                    cache_enabled=False
                )
            else:
                info = getattr(self, 'get_%s' % (object_name))(
                    namespace,
                    name,
                    cache_enabled=False
                )

            if info is not None:
                success = True
                for key in match_properties:
                    if self.get(info, key) != match_properties[key]:
                        success = False
                        break

                failure = False
                failure_on = None
                for key in break_properties:
                    if self.get(info, key) == break_properties[key]:
                        failure_on = '%s:%s' % (key, break_properties[key])
                        failure = True
                        break

                if failure:
                    if my_output is not None:
                        my_output.error('failed on %s' % (failure_on))
                    return False
                
                if success:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    if namespace is None:
                        self.log.error(
                            'k8s.wait_managed_object',
                            'Max time reached [%s]: %s' % (object_name, name)
                        )
                    else:
                        self.log.error(
                            'k8s.wait_managed_object',
                            'Max time reached [%s]: %s/%s' % (object_name, namespace, name)
                        )

                if my_output is not None:
                    my_output.error('timed out')

                return False

            time.sleep(5)

    def wait_no_managed_object(
            self, 
            object_name, 
            name, 
            namespace=None, 
            my_output=None, 
            prompt=None, 
            max_time=60,
            log_error_on_timeout=True
        ):
        if my_output is not None and prompt is not None:
            my_output.default(prompt)

        start_time = int(time.time())
        while True:
            if namespace is None:
                info = getattr(self, 'get_%s' % (object_name))(
                    name,
                    cache_enabled=False
                )
            else:
                info = getattr(self, 'get_%s' % (object_name))(
                    namespace,
                    name,
                    cache_enabled=False
                )

            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    if namespace is None:
                        self.log.error(
                            'k8s.wait_no_managed_object',
                            'Max time reached [%s]: %s' % (object_name, name)
                        )
                    else:
                        self.log.error(
                            'k8s.wait_no_managed_object',
                            'Max time reached [%s]: %s/%s' % (object_name, namespace, name)
                        )

                if my_output is not None:
                    my_output.error('timed out')

                return False

            time.sleep(5)

    def cleanup_managed_object(self, managed_object, exclude=[]):
        for key in ['creationTimestamp', 'managedFields', 'generation', 'resourceVersion', 'uid']:
            if key in exclude:
                continue
            if key in managed_object['metadata']:
                del managed_object['metadata'][key]

        if 'status' in managed_object:
            del managed_object['status']

        return managed_object