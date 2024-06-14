class PolicyGroupAccessInterfaceVpcEventApi():
    def __init__(self):
        self.policy_group_access_interface_vpc_event_mo = None

    def get_policy_group_access_interface_vpc_event_mo(self):
        if self.policy_group_access_interface_vpc_event_mo is not None:
            return self.policy_group_access_interface_vpc_event_mo

        cache = self.get_object_cache(
            'infraAccBndlGrp.eventLog'
        )
        if cache is not None:
            self.policy_group_access_interface_vpc_event_mo = cache
            self.log.apic_mo(
                'infraAccBndlGrp.eventLog',
                self.policy_group_access_interface_vpc_event_mo
            )
            return self.policy_group_access_interface_vpc_event_mo

        query = 'rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=%s' % (self.api_event_limit)
        managed_objects = self.get_class(
            'infraAccBndlGrp',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_policy_group_access_interface_vpc_event_mo',
                'API failed'
            )
            return None

        self.policy_group_access_interface_vpc_event_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.policy_group_access_interface_vpc_event_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAccBndlGrp.eventLog',
            self.policy_group_access_interface_vpc_event_mo
        )

        self.set_object_cache(
            'infraAccBndlGrp.eventLog',
            self.policy_group_access_interface_vpc_event_mo
        )

        return self.policy_group_access_interface_vpc_event_mo
