class PolicyGeneralAaePgInfo():
    def __init__(self):
        self.policy_global_aae_pg = {}

    def get_policy_global_aae_pg_info(self, managed_object):
        return managed_object['pconsResourceCtx']

    def get_policy_global_aae_pg(self, domain_name):
        if domain_name in self.policy_global_aae_pg:
            return self.policy_global_aae_pg[domain_name]

        # one object or None value is expected
        domain_nodes_mo = self.get_policy_global_aae_pg_mo(domain_name)
        if domain_nodes_mo is None:
            return None

        self.policy_global_aae_pg[domain_name] = self.get_policy_global_aae_pg_info(
            domain_nodes_mo
        )

        self.log.apic_mo(
            'infraAttEntityP.pg.%s.info' % (domain_name),
            self.policy_global_aae_pg[domain_name]
        )

        return self.policy_global_aae_pg[domain_name]
