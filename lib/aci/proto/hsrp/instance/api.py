class ProtocolHsrpInstanceApi():
    def __init__(self):
        self.hsrp_instance_mo = {}

    def get_protocol_hsrp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_instance_mo:
            return self.hsrp_instance_mo[key]

        # url: https://apic11o-eu-spdc.cisco.com/api/node/mo/topology/pod-1/node-201.json?query-target=subtree&target-subtree-class=arpEntity&query-target=subtree&target-subtree-class=arpEntity,bfdInst,bgpInst,cdpInst,coopInst,igmpsnoopEntity,igmpEntity,isisEntity,lacpEntity,lldpEntity,ndEntity,ospfEntity,ospfv3Entity,eigrpEntity,ipv4Entity,ipv6Entity,uribv4Entity,uribv6Entity,pimEntity,pimDom,pimDb,pim6Entity,pim6Dom,hsrpEntity,fhsEntity,twampEntity,slaEntity
        distinguished_name = 'topology/pod-%s/node-%s' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=hsrpEntity'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_hsrp_instance_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_protocol_hsrp_instance_mo',
                'Unexpected object count'
            )
            return None

        self.hsrp_instance_mo[key] = managed_objects['imdata'][0]['hsrpEntity']['attributes']

        self.log.apic_mo(
            'hsrp.instance.%s' % (key),
            self.hsrp_instance_mo[key]
        )

        return self.hsrp_instance_mo[key]
