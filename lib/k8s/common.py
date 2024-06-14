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

        return info
