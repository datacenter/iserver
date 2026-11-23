class K8sPrivateNetworkNodeAttachmentOutput():
    def __init__(self):
        pass

    def print_private_network_node_attachments_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network Node Attachment', 'name']
            ]
        )