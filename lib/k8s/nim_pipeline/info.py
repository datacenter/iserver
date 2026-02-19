from lib import filter_helper


class K8sNimPipelineInfo():
    def __init__(self):
        self.nim_pipeline = None

    def get_nim_pipeline_info(self, managed_object):
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
        return info

    def get_nim_pipelines_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_pipeline is not None:
                return self.nim_pipeline

        managed_objects = self.get_nim_pipeline_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nim_pipeline = []
        for managed_object in managed_objects:
            nim_pipeline_info = {}
            nim_pipeline_info['info'] = self.get_nim_pipeline_info(
                managed_object
            )
            nim_pipeline_info['mo'] = managed_object
            self.nim_pipeline.append(
                nim_pipeline_info
            )

        return self.nim_pipeline

    def match_nim_pipeline(self, nim_pipeline_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nim_pipeline_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nim_pipeline_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nim_pipeline',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nim_pipelines(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nim_pipelines = self.get_nim_pipelines_info(cache_enabled=cache_enabled)
        if all_nim_pipelines is None:
            return None

        nim_pipelines = []

        for nim_pipeline_info in all_nim_pipelines:
            if not self.match_nim_pipeline(nim_pipeline_info['info'], object_filter):
                continue

            if return_mo:
                nim_pipelines.append(
                    nim_pipeline_info['mo']
                )
                continue

            nim_pipelines.append(
                nim_pipeline_info['info']
            )

        return nim_pipelines

    def is_nim_pipeline(self, namespace, name, cache_enabled=True):
        if self.get_nim_pipeline(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nim_pipeline(self, cache_enabled=True):
        policies = self.get_nim_pipelines(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nim_pipeline(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nim_pipelines = self.get_nim_pipelines(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nim_pipelines is None:
            return None

        if len(nim_pipelines) == 1:
            return nim_pipelines[0]

        return None
