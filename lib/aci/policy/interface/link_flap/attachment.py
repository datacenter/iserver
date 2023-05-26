class PolicyInterfaceLinkFlapAttachment():
    def __init__(self):
        self.mo_policy_interface_link_flap_attachment = None

    def initialize_policy_interface_link_flap_attachment(self):
        if self.mo_policy_interface_link_flap_attachment is not None:
            return True

        self.mo_policy_interface_link_flap_attachment = self.get_policy_interface_attachment_attributes('l1RsLinkFlapPolCons')
        if self.mo_policy_interface_link_flap_attachment is None:
            return False

        return True

    def get_policy_interface_link_flap_attachments(self, managed_object):
        return self.get_policy_interface_attachment(
            managed_object,
            self.mo_policy_interface_link_flap_attachment
        )
