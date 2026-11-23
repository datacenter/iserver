from lib import filter_helper


class K8sImageStreamInfo():
    def __init__(self):
        self.image_stream = None

    def get_image_stream_info(self, image_stream_mo):
        if image_stream_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            image_stream_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(image_stream_mo, 'spec')
        info['status'] = self.get(image_stream_mo, 'status')
        info['tags'] = []

        tags_mo = filter_helper.get(image_stream_mo, 'status:tags', on_error=[], on_none=[])
        for tag_mo in tags_mo:
            info['tags'].append(tag_mo['tag'])

        info['tags'] = sorted(info['tags'])
        return info

    def get_image_streams_info(self, cache_enabled=True):
        if cache_enabled:
            if self.image_stream is not None:
                return self.image_stream

        managed_objects = self.get_image_stream_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.image_stream = []
        for managed_object in managed_objects:
            image_stream_info = {}
            image_stream_info['info'] = self.get_image_stream_info(
                managed_object
            )
            image_stream_info['mo'] = managed_object
            self.image_stream.append(
                image_stream_info
            )

        return self.image_stream

    def match_image_stream(self, image_stream_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, image_stream_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, image_stream_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_image_stream',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_image_streams(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_image_streams = self.get_image_streams_info(cache_enabled=cache_enabled)
        if all_image_streams is None:
            return None

        image_streams = []

        for image_stream_info in all_image_streams:
            if not self.match_image_stream(image_stream_info['info'], object_filter):
                continue

            if return_mo:
                image_streams.append(
                    image_stream_info['mo']
                )
                continue

            image_streams.append(
                image_stream_info['info']
            )

        return image_streams

    def is_image_stream(self, namespace, name, cache_enabled=True):
        if self.get_image_stream(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_image_stream(self, cache_enabled=True):
        policies = self.get_image_streams(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_image_stream(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        image_streams = self.get_image_streams(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if image_streams is None:
            return None

        if len(image_streams) == 1:
            return image_streams[0]

        return None
