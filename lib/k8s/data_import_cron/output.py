class K8sDataImportCronOutput():
    def __init__(self):
        pass

    def print_data_import_crons(self, info, title=False):
        self.my_output.my_table_ng(
            info,
            [
                ['Data Import Cron', 'name'],
                ['Schedule', 'schedule'],
                ['Ready', 'readyTick'],
                ['Storage', 'storage'],
                ['Data Source', 'data_source'],
                ['Data Volume', 'data_volume']
            ]
        )
