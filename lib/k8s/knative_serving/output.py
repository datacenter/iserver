class K8sKnativeServingOutput():
    def __init__(self):
        pass

    def print_knative_servings(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Knative Serving', 'namespace_nameT'],
                ['Version', 'version'],
                ['Ready', 'readyTick'],
                ['Conditions', 'conditions'],
                ['Ingress', 'ingress'],
                ['Deployment', 'deploymentT']
            ]
        )