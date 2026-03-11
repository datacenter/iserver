class K8sDeploymentOutput():
    def __init__(self):
        pass

    def print_deployments_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Deployment', 'namespace_nameT'],
                ['Ready', 'readyT'],
                ['Up-To-Date', 'updatedReplicas'],
                ['Available', 'availableReplicas'],
                ['Age', 'age']
            ]
        )

    def print_deployments_metadata(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Deployment', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Label', 'labelT'],
                ['Annotation', 'annotationT']
            ]
        )

    def print_deployment(self, item):
        self.my_output.dictionary_ng(
            'Deployment',
            item, 
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['Ready', 'readyT'],
                ['Up-To-Date', 'updatedReplicas'],
                ['Available', 'availableReplicas'],
                ['Age', 'age']
            ]
        )