class K8sKnativeKafkaOutput():
    def __init__(self):
        pass

    def print_knative_kafkas(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Knative Kafka', 'namespace_nameT']
            ]
        )