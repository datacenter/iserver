class PoolVlanDelete():
    def __init__(self):
        pass

    def get_delete_pool_vlan_body(
            self,
            pool_name,
            mode
        ):
        body = {}
        body['fvnsVlanInstP'] = {}
        body['fvnsVlanInstP']['attributes'] = {}
        body['fvnsVlanInstP']['attributes']['dn'] = 'uni/infra/vlanns-[%s]-%s' % (pool_name, mode)
        body['fvnsVlanInstP']['attributes']['status'] = 'deleted'
        body['fvnsVlanInstP']['children'] = []

        return body

    def delete_pool_vlan(
            self,
            pool_name,
            mode
        ):
        body = self.get_delete_pool_vlan_body(
            pool_name,
            mode
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/infra/vlanns-[%s]-%s.json' % (pool_name, mode)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_pool_vlan_mo()

        return success, error
