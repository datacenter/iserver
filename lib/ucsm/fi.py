class Fi():
    def __init__(self):
        self.mo_fi = None

    def get_fi_info(self, fi_object):
        info = {}
        info['mo_type'] = 'fi'

        keys = [
            'admin_evac_state',
            'admin_inband_if_state',
            'diff_memory',
            'dn',
            'expected_memory',
            'id',
            'inband_if_gw',
            'inband_if_ip',
            'inband_if_mask',
            'inband_if_vnet',
            'inventory_status',
            'min_active_fan',
            'model',
            'oob_if_gw',
            'oob_if_ip',
            'oob_if_mac',
            'oob_if_mask',
            'oper_evac_state',
            'operability',
            'revision',
            'rn',
            'serial',
            'status',
            'thermal',
            'total_memory',
            'vendor'
        ]
        for key in keys:
            info[key] = getattr(fi_object, key, None)

        return info

    def get_fi(self, fi_id):
        fis = self.get_fis()
        if fis is None:
            return None

        for fi in fis:
            if fi['id'] == fi_id:
                return fi

        return None

    def get_fis(self, power=False, thermal=False, net=False):
        if self.mo_fi is None:
            managed_objects = self.query_classid(
                'NetworkElement'
            )
            if managed_objects is None:
                return None

            self.mo_fi = managed_objects

        fiz = []

        for managed_object in self.mo_fi:
            managed_object_info = self.get_fi_info(
                managed_object
            )
            if managed_object_info is not None:
                if net:
                    managed_object_info['ethPort'] = self.get_eth_ports(
                        fi_id=managed_object_info['id']
                    )
                    managed_object_info['switchCard'] = self.get_switch_cards(
                        fi_id=managed_object_info['id']
                    )
                    managed_object_info['switchPortGroup'] = self.get_switch_port_groups(
                        fi_id=managed_object_info['id']
                    )

                fiz.append(managed_object_info)

        fiz = sorted(fiz, key=lambda i: i['dn'])
        return fiz

    def print_fi(self, fi, power=False, thermal=False):
        order = [
            'rn'
        ]

        headers = [
            'Name'
        ]

        self.my_output.dictionary(
            fi,
            title='FI',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_fis(self, fis, power=False, thermal=False):
        order = [
            'id',
            'rn'
        ]

        headers = [
            'Id',
            'Name'
        ]

        self.my_output.my_table(
            fis,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
