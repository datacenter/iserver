class ConfigurationInterfaceCreate():
    def __init__(self):
        pass

    def get_create_leaf_interface_configuration_vpc_body(self, policy_name, node_id, port_id):
        body = {}
        body['infraInfra'] = {}
        body['infraInfra']['attributes'] = {}
        body['infraInfra']['children'] = []

        child_mo = {}
        child_mo['infraPortConfig'] = {}
        child_mo['infraPortConfig']['attributes'] = {}
        child_mo['infraPortConfig']['children'] = []

        child_mo['infraPortConfig']['attributes']['assocGrp'] = 'uni/infra/funcprof/accbundle-%s' % (policy_name)
        child_mo['infraPortConfig']['attributes']['description'] = ''
        child_mo['infraPortConfig']['attributes']['brkoutMap'] = 'none'
        child_mo['infraPortConfig']['attributes']['connectedFex'] = 'unspecified'
        child_mo['infraPortConfig']['attributes']['pcMember'] = ''
        child_mo['infraPortConfig']['attributes']['node'] = node_id

        if len(port_id.split('/')) == 2:
            child_mo['infraPortConfig']['attributes']['card'] = port_id.split('/')[0]
            child_mo['infraPortConfig']['attributes']['port'] = port_id.split('/')[1]
            child_mo['infraPortConfig']['attributes']['subPort'] = '0'
        else:
            child_mo['infraPortConfig']['attributes']['card'] = port_id.split('/')[0]
            child_mo['infraPortConfig']['attributes']['port'] = port_id.split('/')[1]
            child_mo['infraPortConfig']['attributes']['subPort'] = port_id.split('/')[2]

        body['infraInfra']['children'].append(
            child_mo
        )

        return body

    def create_leaf_interface_configuration_vpc(self, policy_name, node_id, port_id):
        body = self.get_create_leaf_interface_configuration_vpc_body(
            policy_name,
            node_id,
            port_id
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra.json'
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_configuration_interface_mo()

        return success, error
