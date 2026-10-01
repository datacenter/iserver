class K8sTridentOrchestratorDelete():
    def __init__(self):
        pass

    def delete_trident_orchestrator(self, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.instance_trident_resources,
            cache_enabled=False
        )

        success, deleted = self.delete_resource(
            'TridentOrchestrator', 
            'trident.netapp.io/v1',
            name, 
            object_name='trident_orchestrator',
            my_output=my_output
        )
        if not success:
            return False
        
        if not deleted:
            return True
        
        if not wait:
            return True
        
        success = self.wait_no_trident_orchestrator(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_no_subscription_resources('trident', resources, my_output=my_output)
        if not success:
            return False
                                    
        return True
    
    def delete_trident_orchestrators(self, my_output=None, wait=True):
        orchestrators = self.get_trident_orchestrators(
            cache_enabled=False
        )
        if orchestrators is None:
            if my_output is not None:
                my_output.error('Failed to get trident orchestrators')
            return False

        if len(orchestrators) == 0:
            if my_output is not None:
                my_output.default('Trident orchestrators %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for orchestrator in orchestrators:
            success = self.delete_trident_orchestrator(
                orchestrator['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone