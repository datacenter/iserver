class PolicyInterfaceCoppProtocolInfo():
    def __init__(self):
        self.policy_interface_copp_protocol = None

    def get_policy_interface_copp_protocol_info(self, managed_object):
        info = {}
        for key in managed_object:
            info[key] = managed_object[key]
        return info

    def get_policy_interface_copp_protocols_info(self):
        if self.policy_interface_copp_protocol is not None:
            return self.policy_interface_copp_protocol

        managed_objects = self.get_policy_interface_copp_protocol_mo()
        if managed_objects is not None:
            self.policy_interface_copp_protocol = []
            for managed_object in managed_objects:
                self.policy_interface_copp_protocol.append(
                    self.get_policy_interface_copp_protocol_info(
                        managed_object
                    )
                )

        return self.policy_interface_copp_protocol

    def get_policy_interface_copp_protocols(self):
        all_protocols = self.get_policy_interface_copp_protocols_info()
        if all_protocols is None:
            return None

        return all_protocols
