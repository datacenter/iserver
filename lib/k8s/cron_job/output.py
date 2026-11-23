class K8sCronJobOutput():
    def __init__(self):
        pass

    def print_cron_jobs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cron Job', 'namespace_name'],
                ['Age', 'age']
            ]
        )