class OcpVmGetImage():
    def __init__(self):
        pass

    def is_ocp_dv_vm_image(self, label_special, cache=True):
        dvs_mo = self.get_ocp_dv_vm_image(
            label_special,
            cache=cache
        )
        if dvs_mo is None or len(dvs_mo) == 0:
            return False
        return True

    def get_ocp_dv_vm_image(self, image_filename, cache=True):
        data_volumes = self.k8s_handler.get_data_volumes(return_mo=True, cache_enabled=cache)
        if data_volumes is None:
            return []

        image_mo = []
        for dv_mo in data_volumes:
            if 'labels' not in dv_mo['metadata']:
                continue

            if 'type' not in dv_mo['metadata']['labels']:
                continue

            if dv_mo['metadata']['labels']['type'] != 'image':
                continue

            if 'filename' not in dv_mo['metadata']['labels']:
                continue

            if dv_mo['metadata']['labels']['filename'] != image_filename:
                continue

            image_mo.append(
                dv_mo
            )

        return image_mo
