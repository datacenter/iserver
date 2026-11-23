class PolicyGroupAccessInterfaceVpcDelete():
    def __init__(self):
        pass

    def get_delete_policy_group_access_interface_vpc_body(self, policy_name):
        body = {}
        body['infraAccBndlGrp'] = {}
        body['infraAccBndlGrp']['attributes'] = {}
        body['infraAccBndlGrp']['attributes']['dn'] = 'uni/infra/funcprof/accbundle-%s' % (policy_name)
        body['infraAccBndlGrp']['attributes']['status'] = 'deleted'
        body['infraAccBndlGrp']['children'] = []

        return body

    def delete_policy_group_access_interface_vpc(self, policy_name):
        body = self.get_delete_policy_group_access_interface_vpc_body(
            policy_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'mo/uni/infra/funcprof/accbundle-%s.json' % (policy_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_policy_group_access_interface_vpc_mo()
            self.init_policy_group_access_interface_vpc()

        return success, error
