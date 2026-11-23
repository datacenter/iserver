class EpgUpdate():
    def __init__(self):
        pass

    def get_add_epg_phys_domain_body(
            self,
            domain_name,
            resolution
        ):
        body = {}
        body['fvRsDomAtt'] = {}
        body['fvRsDomAtt']['attributes'] = {}
        body['fvRsDomAtt']['attributes']['resImedcy'] = resolution
        body['fvRsDomAtt']['attributes']['tDn'] = 'uni/phys-%s' % (domain_name)
        body['fvRsDomAtt']['attributes']['status'] = 'created'
        body['fvRsDomAtt']['children'] = []

        return body

    def add_epg_phys_domain(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name,
            resolution='immediate'
        ):
        body = self.get_add_epg_phys_domain_body(
            domain_name,
            resolution
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

        return success, error

    def get_delete_epg_phys_domain_body(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name
        ):
        body = {}
        body['fvRsDomAtt'] = {}
        body['fvRsDomAtt']['attributes'] = {}
        body['fvRsDomAtt']['attributes']['dn'] = 'uni/tn-%s/ap-%s/epg-%s/rsdomAtt-[uni/phys-%s]' % (
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name
        )
        body['fvRsDomAtt']['attributes']['status'] = 'deleted'
        body['fvRsDomAtt']['children'] = []

        return body

    def delete_epg_phys_domain(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name
        ):
        body = self.get_delete_epg_phys_domain_body(
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name
        )
        if body is None:
            return False, 'Body preparation failed'


        uri = 'node/mo/uni/tn-%s/ap-%s/epg-%s/rsdomAtt-[uni/phys-%s].json' % (
            epg_tenant,
            epg_ap,
            epg_name,
            domain_name
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_epg_mo()
            self.init_epg()

        return success, error

    def get_add_epg_static_port_body(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            tdn,
            encap,
            immediacy
        ):
        body = {}
        body['fvRsPathAtt'] = {}
        body['fvRsPathAtt']['attributes'] = {}
        body['fvRsPathAtt']['attributes']['dn'] = 'uni/tn-%s/ap-%s/epg-%s/rspathAtt-[%s]' % (
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        )
        body['fvRsPathAtt']['attributes']['encap'] = encap
        body['fvRsPathAtt']['attributes']['instrImedcy'] = immediacy
        body['fvRsPathAtt']['attributes']['tDn'] = tdn
        body['fvRsPathAtt']['attributes']['rn'] = 'rspathAtt-[%s]' % (tdn)
        body['fvRsPathAtt']['attributes']['status'] = 'created'
        body['fvRsPathAtt']['children'] = []

        return body

    def add_epg_static_port(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            tdn,
            encap,
            immediacy
        ):
        body = self.get_add_epg_static_port_body(
            epg_tenant,
            epg_ap,
            epg_name,
            tdn,
            encap,
            immediacy
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/ap-%s/epg-%s/rspathAtt-[%s].json' % (
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_epg_mo()
            self.init_epg()

        return success, error

    def get_delete_epg_static_port_body(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        ):
        body = {}
        body['fvRsPathAtt'] = {}
        body['fvRsPathAtt']['attributes'] = {}
        body['fvRsPathAtt']['attributes']['dn'] = 'uni/tn-%s/ap-%s/epg-%s/rspathAtt-[%s]' % (
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        )
        body['fvRsPathAtt']['attributes']['status'] = 'deleted'
        body['fvRsPathAtt']['children'] = []

        return body

    def delete_epg_static_port(
            self,
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        ):
        body = self.get_delete_epg_static_port_body(
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        )
        if body is None:
            return False, 'Body preparation failed'

        uri = 'node/mo/uni/tn-%s/ap-%s/epg-%s/rspathAtt-[%s].json' % (
            epg_tenant,
            epg_ap,
            epg_name,
            tdn
        )
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_epg_mo()
            self.init_epg()

        return success, error
