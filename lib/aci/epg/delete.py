class EpgDelete():
    def __init__(self):
        pass

    def get_delete_epg_body(
            self,
            epg_tenant,
            epg_ap,
            epg_name
        ):
        body = {}
        body['fvAEPg'] = {}
        body['fvAEPg']['attributes'] = {}
        body['fvAEPg']['attributes']['dn'] = 'uni/tn-%s/ap-%s/epg-%s' % (
            epg_tenant,
            epg_ap,
            epg_name
        )
        body['fvAEPg']['attributes']['status'] = 'deleted'
        body['fvAEPg']['children'] = []

        return body

    def delete_epg(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            wait=False
        ):
        body = self.get_delete_epg_body(
            epg_tenant,
            epg_ap,
            epg_name
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/ap-%s/epg-%s.json' % (
            epg_tenant,
            epg_ap,
            epg_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_epg_mo()
            self.init_epg()

            if wait:
                success = self.wait_no_epg(
                    epg_tenant,
                    epg_ap,
                    epg_name
                )
                if not success:
                    return False, 'Wait for no epg'

        return success, error
