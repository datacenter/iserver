import json


class LinuxContainerPolicyInfo():
    def __init__(self):
        self.container_policy_config = None

    def get_container_policy_config_info(self):
        if self.container_policy_config is not None:
            return self.container_policy_config

        container_policy_config_mo = self.get_container_policy_config_cmd()

        # {
        #     "default": [
        #         {
        #             "type": "reject"
        #         }
        #     ],
        #     "transports": {
        #         "atomic": {
        #             "quay.io": [
        #                 {
        #                     "type": "insecureAcceptAnything"
        #                 }
        #             ],
        #             "registry.redhat.io": [
        #                 {
        #                     "type": "insecureAcceptAnything"
        #                 }
        #             ]
        #         },
        #         "docker": {
        #             "quay.io": [
        #                 {
        #                     "type": "insecureAcceptAnything"
        #                 }
        #             ],
        #             "registry.redhat.io": [
        #                 {
        #                     "type": "insecureAcceptAnything"
        #                 }
        #             ]
        #         },
        #         "docker-daemon": {
        #             "": [
        #                 {
        #                     "type": "insecureAcceptAnything"
        #                 }
        #             ]
        #         }
        #     }
        # }


        self.container_policy_config = json.loads(
            container_policy_config_mo
        )

        return self.container_policy_config
