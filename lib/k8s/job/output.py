class K8sJobOutput():
    def __init__(self):
        pass

    def print_jobs_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Job', 'namespace_nameT'],
                ['Completed', 'completedTick']
            ]
        )