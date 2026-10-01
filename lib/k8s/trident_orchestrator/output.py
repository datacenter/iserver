import json
from lib import filter_helper


class K8sTridentOrchestratorOutput():
    def __init__(self):
        pass

    def print_trident_orchestrators(self, info):
        for item in info:           
            item['specT'] = json.dumps(
                item['spec'],
                indent=2
            ).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Trident Orchestrator', 'name'],
                ['Spec', 'specT']
            ]
        )