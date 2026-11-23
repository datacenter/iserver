class K8sTridentOrchestratorInfo():
    def __init__(self):
        self.trident_orchestrator = None

    def get_trident_orchestrator_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        info = self.add_tick(
            info, 
            'status:status', 
            'Installed', 
            'installedTick', 
            bool_attribute='installed'
        )
        return info

    def get_trident_orchestrators(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'trident_orchestrator', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_trident_orchestrator(self, name, cache_enabled=True, optimized=True):
        if self.get_trident_orchestrator(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_trident_orchestrator(self, cache_enabled=True):
        orchestrators = self.get_trident_orchestrators(cache_enabled=cache_enabled)
        if orchestrators is None or len(orchestrators) == 0:
            return False
        return True

    def get_trident_orchestrator(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'trident_orchestrator', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )