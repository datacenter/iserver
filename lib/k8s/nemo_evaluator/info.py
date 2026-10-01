from lib import filter_helper


class K8sNemoEvaluatorInfo():
    def __init__(self):
        self.nemo_evaluator = None

    def get_nemo_evaluator_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nemo_evaluators(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nemo_evaluator', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nemo_evaluator(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nemo_evaluator', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nemo_evaluator(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nemo_evaluator(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nemo_evaluator(self, cache_enabled=True):
        infos = self.get_nemo_evaluators(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True