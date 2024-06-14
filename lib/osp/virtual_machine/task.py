import time
import traceback


class OspVirtualMachineTask():
    def __init__(self):
        pass

    def wait_for_virtual_machine_status(self, virtual_machine_id, status_array, reverse=False, timeout=300):
        start_time = int(time.time())
        while True:
            virtual_machine_mo = self.get_virtual_machine_id_mo(virtual_machine_id, cache_enabled=False)
            if virtual_machine_mo is not None:
                current_status = virtual_machine_mo.status
                if virtual_machine_mo.status.lower() == 'error':
                    return False

                if not reverse:
                    if current_status in status_array:
                        return True

                if reverse:
                    if current_status not in status_array:
                        return True

            time.sleep(5)
            if (int(time.time()) - start_time) > timeout:
                self.log.error(
                    'wait_for_virtual_machine_status',
                    'Timeout reached for virtual machine: %s' % (virtual_machine_id)
                )
                return False

    def wait_for_virtual_machine_power_state(self, virtual_machine_id, status_array, reverse=False, timeout=300):
        start_time = int(time.time())
        while True:
            virtual_machine_mo = self.get_virtual_machine_id_mo(virtual_machine_id, cache_enabled=False)
            if virtual_machine_mo is not None:
                current_status = getattr(virtual_machine_mo, 'OS-EXT-STS:power_state')
                if not reverse:
                    if current_status in status_array:
                        return True

                if reverse:
                    if current_status not in status_array:
                        return True

            time.sleep(5)
            if (int(time.time()) - start_time) > timeout:
                self.log.error(
                    'wait_for_virtual_machine_power_state',
                    'Timeout reached for virtual machine: %s' % (virtual_machine_id)
                )
                return False

    def start_virtual_machine(self, virtual_machine_id, wait=False):
        api_handler = self.get_api_nova()
        if api_handler is None:
            self.log.error(
                'start_virtual_machine',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.start(virtual_machine_id)

        except BaseException:
            self.log.error(
                'start_virtual_machine',
                'API failed'
            )
            self.log.error(
                'start_virtual_machine',
                traceback.format_exc()
            )
            return False

        if wait:
            return self.wait_for_virtual_machine_status(virtual_machine_id, ['ACTIVE'])

        return True

    def stop_virtual_machine(self, virtual_machine_id, wait=False):
        api_handler = self.get_api_nova()
        if api_handler is None:
            self.log.error(
                'stop_virtual_machine',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.stop(virtual_machine_id)

        except BaseException:
            self.log.error(
                'stop_virtual_machine',
                'API failed'
            )
            self.log.error(
                'stop_virtual_machine',
                traceback.format_exc()
            )
            return False

        if wait:
            if not self.wait_for_virtual_machine_status(virtual_machine_id, ['SHUTOFF']):
                return False

            if not self.wait_for_virtual_machine_power_state(virtual_machine_id, [4]):
                return False

        return True

    def delete_virtual_machine(self, virtual_machine_id, wait=False, timeout=300):
        api_handler = self.get_api_nova()
        if api_handler is None:
            self.log.error(
                'delete_virtual_machine',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.delete(virtual_machine_id)

        except BaseException:
            self.log.error(
                'delete_virtual_machine',
                'API failed'
            )
            self.log.error(
                'delete_virtual_machine',
                traceback.format_exc()
            )
            return False

        if wait:
            start_time = int(time.time())
            while True:
                if not self.is_virtal_machine(virtual_machine_id, cache_enabled=False):
                    return True

                time.sleep(5)
                if (int(time.time()) - start_time) > timeout:
                    self.log.error(
                        'delete_virtual_machine',
                        'Timeout reached for virtual machine: %s' % (virtual_machine_id)
                    )
                    return False

        return True
