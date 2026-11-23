class K8sTridentOrchestratorWait():
    def __init__(self):
        pass

    def wait_trident_orchestrator(self, name, match_properties={}, break_properties={}, my_output=None, prompt='TridentOrchestrator', max_time=60):
        return self.wait_managed_object(
            'trident_orchestrator',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )


    def wait_no_trident_orchestrator(self, name, max_time=60, my_output=None, prompt='TridentOrchestrator'):
        return self.wait_no_managed_object(
            'trident_orchestrator',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )