class ConfigurationInterfaceDelete():
    def __init__(self):
        pass

    def get_delete_leaf_interface_configuration_body(self, node_id, port_id):
        body = {}
        body['polUni'] = {}
        body['polUni']['attributes'] = {}
        body['polUni']['attributes']['status'] = 'created,modified'
        body['polUni']['children'] = []

        child_mo = {}
        child_mo['infraInfra'] = {}
        child_mo['infraInfra']['attributes'] = {}
        child_mo['infraInfra']['children'] = []

        infra_mo = {}
        infra_mo['infraPortConfig'] = {}
        infra_mo['infraPortConfig']['attributes'] = {}
        infra_mo['infraPortConfig']['attributes']['node'] = node_id
        infra_mo['infraPortConfig']['attributes']['role'] = 'leaf'
        infra_mo['infraPortConfig']['attributes']['action'] = 'unconfigure'
        infra_mo['infraPortConfig']['attributes']['status'] = ''

        if len(port_id.split('/')) == 2:
            infra_mo['infraPortConfig']['attributes']['card'] = port_id.split('/')[0]
            infra_mo['infraPortConfig']['attributes']['port'] = port_id.split('/')[1]
            infra_mo['infraPortConfig']['attributes']['subPort'] = ''

        if len(port_id.split('/')) == 3:
            infra_mo['infraPortConfig']['attributes']['card'] = port_id.split('/')[0]
            infra_mo['infraPortConfig']['attributes']['port'] = port_id.split('/')[1]
            infra_mo['infraPortConfig']['attributes']['subPort'] = port_id.split('/')[2]

        child_mo['infraInfra']['children'].append(
            infra_mo
        )
        body['polUni']['children'].append(
            child_mo
        )

        return body

    def delete_leaf_interface_configuration(self, node_id, port_id):
        body = self.get_delete_leaf_interface_configuration_body(node_id, port_id)
        if body is None:
            return False

        uri = 'node/mo/.json'
        success, error = self.create_managed_object(
            uri,
            body
        )

        return success, error
