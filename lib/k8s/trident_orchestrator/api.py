class K8sTridentOrchestratorApi():
    def __init__(self):
        self.trident_orchestrator_mo = None

    def get_trident_orchestrator_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.trident_orchestrator_mo
        )
        if cache_hit:
            return response

        response, self.trident_orchestrator_mo = self.get_resources(
            'TridentOrchestrator', 
            'trident.netapp.io/v1', 
            self.trident_orchestrator_mo,
            name=name
        )

        return response

    def delete_trident_orchestrator_mo(self, name):
        success, _ = self.delete_resource('TridentOrchestrator', 'trident.netapp.io/v1', name)
        return success