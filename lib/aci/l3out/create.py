class L3OutCreate():
    def __init__(self):
        pass

    def create_l3out(
            self,
            tenant_name,
            l3out_name,
            body,
            wait=False
        ):

        uri = 'node/mo/uni/tn-%s.json' % (tenant_name)
        success, error = self.create_managed_object(
            uri,
            body
        )

        if success:
            self.init_l3out_mo()
            self.init_l3out()

            if wait:
                if not self.wait_l3out(l3out_name):
                    return False, 'Wait time reached'

        return success, error
