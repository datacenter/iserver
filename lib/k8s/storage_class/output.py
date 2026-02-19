class K8sStorageClassOutput():
    def __init__(self):
        pass

    def print_storage_classes(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Storage Class', 'name'],
                ['Default', 'defaultTick'],
                ['Provisioner', 'provisioner'],
                ['Reclaim Policy', 'reclaimPolicy'],
                ['Volume Binding Mode', 'volumeBindingMode'],
                ['Allow Volume Expansion', 'allowVolumeExpansion'],
                ['PVC', 'pvc_count'],
                ['PV', 'pv_count']
            ],
            cast_zero=True
        )

    def print_storage_classes_with_resources(self, info, title=False):
        self.print_storage_classes(info, title=title)

        if len(info) == 0:
            return

        pv = []
        pvc = []
        for item in info:
            if 'pv' in item and item['pv'] is not None:
                pv.extend(item['pv'])
            if 'pvc' in item and item['pvc'] is not None:
                pvc.extend(item['pvc'])

        if len(pv) > 0:
            self.print_pvs(pv)

        if len(pvc) > 0:
            self.print_pvcs(pvc)