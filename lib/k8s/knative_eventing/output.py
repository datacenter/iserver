class K8sKnativeEventingOutput():
    def __init__(self):
        pass

    def print_knative_eventings(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Knative Eventing', 'namespace_nameT']
            ]
        )