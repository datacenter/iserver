class K8sMigrationOutput():
    def __init__(self):
        pass

    def print_migrations(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Migration', 'namespace_nameT'],
                ['Plan', 'plan'],
                ['Conditions', 'conditions'],
                ['State', 'event']
            ]
        )