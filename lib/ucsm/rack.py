class Rack():
    def __init__(self):
        self.mo_rack = None

    def get_rack_info(self, rack_object):
        rack_info = {}
        rack_info['mo_type'] = 'rack'

        keys = [
            'admin_power',
            'admin_state',
            'asset_tag',
            'assigned_to_dn',
            'association',
            'availability',
            'available_memory',
            'conn_path',
            'conn_status',
            'discovery',
            'dn',
            'enclosure_id',
            'fan_speed_config_status',
            'fan_speed_policy_fault',
            'id',
            'low_voltage_memory',
            'managing_inst',
            'memory_speed',
            'model',
            'name',
            'num_of40_g_adaptors_with_old_fw',
            'num_of40_g_adaptors_with_unknown_fw',
            'num_of_adaptors',
            'num_of_cores',
            'num_of_cores_enabled',
            'num_of_cpus',
            'num_of_eth_host_ifs',
            'num_of_fc_host_ifs',
            'num_of_threads',
            'oper_power',
            'oper_pwr_trans_src',
            'oper_state',
            'operability',
            'original_uuid',
            'part_number',
            'physical_security',
            'presence',
            'revision',
            'rn',
            'serial',
            'server_id',
            'slot_id',
            'status',
            'storage_oper_qualifier',
            'total_memory',
            'uuid',
            'vendor',
            'veth_status',
            'vid'
        ]
        for key in keys:
            rack_info[key] = getattr(rack_object, key, None)

        return rack_info

    def get_rack(self, rack_serial=None, power=False, thermal=False):
        racks = self.get_racks(power=power, thermal=thermal)
        if racks is None:
            return None

        for rack in racks:
            if rack_serial is not None:
                if rack['serial'] == rack_serial:
                    return rack

        return None

    def get_racks(self, chassis_rn=None, power=False, thermal=False, net=False):
        if self.mo_rack is None:
            managed_objects = self.query_classid(
                'ComputeRackUnit'
            )
            if managed_objects is None:
                return None

            self.mo_rack = managed_objects

        racks = []

        for managed_object in self.mo_rack:
            managed_object_info = self.get_rack_info(
                managed_object
            )
            if managed_object_info is None:
                continue

            if net:
                managed_object_info['adaptor'] = self.get_compute_adaptors(
                    rack_id=managed_object_info['server_id']
                )

                managed_object_info['extEthIf'] = self.get_compute_ext_eth_ifs(
                    rack_id=managed_object_info['server_id']
                )

                managed_object_info['hostEthIf'] = self.get_compute_host_eth_ifs(
                    rack_id=managed_object_info['server_id']

                )
                managed_object_info['vif'] = self.get_compute_vifs(
                    rack_id=managed_object_info['server_id']
                )

            racks.append(managed_object_info)

        racks = sorted(racks, key=lambda i: i['dn'])

        return racks

    def print_rack(self, rack, power=False, thermal=False):
        order = [
            'rn',
            'model',
            'serial',
            'oper_state',
            'operability',
            'oper_power'
        ]

        headers = [
            'Rack',
            'Model',
            'Serial',
            'Overal Status',
            'Operability',
            'Power State'
        ]

        self.my_output.dictionary(
            rack,
            title='Rack',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_racks(self, racks, power=False, thermal=False):
        order = [
            'rn',
            'model',
            'serial',
            'oper_state',
            'operability',
            'oper_power'
        ]

        headers = [
            'Rack',
            'Model',
            'Serial',
            'Overal Status',
            'Operability',
            'Power State'
        ]

        self.my_output.my_table(
            racks,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
