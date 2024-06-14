import copy

class OspVolumeOutput():
    def __init__(self):
        pass

    def print_volumes(self, info, title=False):
        if title:
            self.my_output.default(
                'Volume [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if len(item['attachment']) == 0:
                item['attachment'].append(
                    dict(
                        vm_tenant_name='--',
                        device='--',
                        host_name='--'
                    )
                )

        order = [
            'name',
            'tenant_name',
            'status',
            'snapshotTick',
            'bootableTick',
            'encryptedTick',
            'multiattachTick',
            'size',
            'volume_type',
            'attachment.vm_tenant_name',
            'attachment.device',
            'attachment.host_name',
            'created_age'
        ]

        headers = [
            'Name',
            'Tenant',
            'Status',
            'Snap',
            'Boot',
            'Encr',
            'Multi',
            'Size',
            'Type',
            'VM',
            'Device',
            'HV',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['attachment']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_volumes_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Volume - Indentifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['snapshot_id'] is None:
                item['snapshot_id'] = '--'

            if len(item['attachment']) == 0:
                item['attachment'].append(
                    dict(
                        attachment_id='--',
                        server_id='--'
                    )
                )

        order = [
            'name',
            'tenant_name',
            'id',
            'snapshot_id',
            'attachment.attachment_id',
            'attachment.server_id'
        ]

        headers = [
            'Name',
            'Tenant',
            'Id',
            'Snapshot',
            'Attachment',
            'VM'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['attachment']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
