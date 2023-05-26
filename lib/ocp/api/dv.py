import time
import traceback


class OcpApiDv():
    def __init__(self):
        self.dvs = None

    def is_ocp_dv(self, dv_namespace, dv_name, cache=True):
        if self.get_ocp_dv(dv_namespace, dv_name, cache=cache) is None:
            return False
        return True

    def get_ocp_dv(self, dv_namespace, dv_name, cache=True):
        if not self.get_ocp_dvs(cache=cache):
            return None

        for data_volume in self.dvs:
            if data_volume['metadata']['name'] == dv_name and data_volume['metadata']['namespace'] == dv_namespace:
                return data_volume

        return None

    def get_ocp_dvs(self, cache=True):
        if not self.connect():
            return False

        if self.dvs is not None and cache:
            return True

        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
            self.dvs = obj_list.get().to_dict()['items']

            self.log.ocp(
                'get',
                'dv',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('ocp.get_ocp_dvs', traceback.format_exc())
            self.log.ocp(
                'get',
                'dv',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.ocp_mo(
            'dv',
            self.dvs
        )

        return True

    def create_ocp_dv(self, data_volume):
        try:
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
            success = True
            response = obj_list.create(
                body=data_volume,
                namespace=data_volume['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ocp_dv', traceback.format_exc())

        self.log.ocp(
            'create',
            'dv',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_ocp_dv(self, namespace, name):
        try:
            success = True
            start_time = int(time.time() * 1000)
            obj_list = self.api.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
            success = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ocp_dv_vm_day0', traceback.format_exc())

        self.log.ocp(
            'delete',
            'dv',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
