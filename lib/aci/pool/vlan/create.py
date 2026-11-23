class PoolVlanCreate():
    def __init__(self):
        pass

    def get_create_pool_vlan_body(
            self,
            pool_name,
            mode,
            blocks
        ):
        body = {}
        body['fvnsVlanInstP'] = {}
        body['fvnsVlanInstP']['attributes'] = {}
        body['fvnsVlanInstP']['attributes']['dn'] = 'uni/infra/vlanns-[%s]-%s' % (pool_name, mode)
        body['fvnsVlanInstP']['attributes']['name'] = pool_name
        body['fvnsVlanInstP']['attributes']['allocMode'] = mode
        body['fvnsVlanInstP']['attributes']['rn'] = 'vlanns-[%s]-%s' % (pool_name, mode)
        body['fvnsVlanInstP']['attributes']['status'] = 'created'
        body['fvnsVlanInstP']['children'] = []

        for block in blocks:
            (from_vlan, to_vlan) = block.split('-')

            block_mo = {}
            block_mo['fvnsEncapBlk'] = {}
            block_mo['fvnsEncapBlk']['attributes'] = {}
            block_mo['fvnsEncapBlk']['attributes']['dn'] = 'uni/infra/vlanns-[%s]-%s/from-[vlan-%s]-to-[vlan-%s]' % (
                pool_name,
                mode,
                from_vlan,
                to_vlan
            )
            block_mo['fvnsEncapBlk']['attributes']['from'] = 'vlan-%s' % (from_vlan)
            block_mo['fvnsEncapBlk']['attributes']['to'] = 'vlan-%s' % (to_vlan)
            block_mo['fvnsEncapBlk']['attributes']['allocMode'] = mode
            block_mo['fvnsEncapBlk']['attributes']['rn'] = 'from-[vlan-%s]-to-[vlan-%s]' % (
                from_vlan,
                to_vlan
            )
            block_mo['fvnsEncapBlk']['attributes']['status'] = 'created'
            block_mo['fvnsEncapBlk']['children'] = []

            body['fvnsVlanInstP']['children'].append(
                block_mo
            )

        return body

    def create_pool_vlan(
            self,
            pool_name,
            blocks,
            mode='static',
            wait=False
        ):
        body = self.get_create_pool_vlan_body(
            pool_name,
            mode,
            blocks
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

            if wait:
                if not self.wait_pool_vlan(pool_name):
                    return False, 'Wait time reached'

        return success, error
