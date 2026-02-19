class K8sSplunkSearchHeadClusterOutput():
    def __init__(self):
        pass

    def print_splunk_search_head_clusters(self, info, title=False):
        if title:
            self.my_output.default(
                'Splunk Search Head Cluster [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name'
        ]

        headers = [
            'Splunk Search Head Cluster'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
