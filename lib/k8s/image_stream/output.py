class K8sImageStreamOutput():
    def __init__(self):
        pass

    def print_image_streams(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Image Stream', 'namespace_name'],
                ['Tags', 'tags']
            ]
        )