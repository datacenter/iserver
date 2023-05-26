class PolicyInterfaceCoppProtocol():
    def __init__(self):
        self.mo_policy_interface_copp_protocol = None

    def initialize_policy_interface_copp_protocol(self):
        if self.mo_policy_interface_copp_protocol is not None:
            return True

        self.mo_policy_interface_copp_protocol = self.get_policy_interface_attachment_attributes('coppProtoClassP')
        if self.mo_policy_interface_copp_protocol is None:
            return False

        return True

    def get_policy_interface_copp_protocol(self):
        return self.mo_policy_interface_copp_protocol
