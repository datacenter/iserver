class OcpVmGetPod():
    def __init__(self):
        pass

    def get_ocp_vm_pod_info(self, namespace, name):
        info = self.get_ocp_vms_info(
            name=name,
            namespace=namespace
        )
        if info is None:
            return None

        # vm_info['pod'] = None
        # vm_info['podName'] = ''
        # if vm_info['vmi_id'] is not None:
        #     vm_info['pod'] = self.get_pod_with_label(
        #         'kubevirt.io/created-by',
        #         vm_info['vmi_id']
        #     )
        #     if vm_info['pod'] is not None:
        #         vm_info['podName'] = vm_info['pod']['metadata']['name']

        return info
