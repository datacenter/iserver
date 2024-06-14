import time
import traceback


class OspVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None

    def get_virtual_machine_id_mo(self, virtual_machine_id, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                for item in self.virtual_machine_mo:
                    if item.id == virtual_machine_id:
                        return item

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            virtual_machine_mo = api_handler.servers.get(virtual_machine_id)
            self.log.osp(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_id_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return virtual_machine_mo

    def get_virtual_machine_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                return self.virtual_machine_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.virtual_machine_mo = api_handler.servers.list(search_opts={'all_tenants': 1})
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.virtual_machine_mo

    def get_virtual_machine_console(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_console',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            virtual_machine_console = api_handler.servers.get_vnc_console(virtual_machine_id, "novnc")['console']['url']
            self.log.osp(
                'get',
                'get_vnc_console',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_console', traceback.format_exc())
            self.log.osp(
                'get',
                'get_vnc_console',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return virtual_machine_console

    def get_virtual_machine_logs(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_logs',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            virtual_machine_logs = api_handler.servers.get_console_output(virtual_machine_id)
            self.log.osp(
                'get',
                'get_console_output',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_console', traceback.format_exc())
            self.log.osp(
                'get',
                'get_console_output',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return virtual_machine_logs

    def create_virtual_machine_mo(self, vm_name, image_id, flavor_id, az=None, config_drive=None, nics=[], files=[], userdata=None):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_virtual_machine_mo',
                'No api handler'
            )
            return None

        try:
            # C:\Users\<user>\AppData\Local\Programs\Python\Python39\Lib\site-packages\novaclient\v2\servers.py
            server_obj = api_handler.servers.create(
                name=vm_name,
                image=image_id,
                flavor=flavor_id,
                nics=nics,
                config_drive=config_drive,
                files=files,
                availability_zone=az,
                userdata=userdata
            )

            self.log.debug(
                'create_virtual_machine_mo',
                str(server_obj)
            )

            new_virtual_machine_id = server_obj.id

        except BaseException:
            self.log.error(
                'create_virtual_machine_mo',
                traceback.format_exc()
            )
            return None

        return new_virtual_machine_id

    def start_virtual_machine_mo(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'start_virtual_machine_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.start(virtual_machine_id)
        except BaseException:
            self.log.error(
                'start_virtual_machine',
                traceback.format_exc()
            )
            return False

        return True

    def stop_virtual_machine_mo(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'stop_virtual_machine_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.stop(virtual_machine_id)
        except BaseException:
            self.log.error(
                'stop_virtual_machine_mo',
                traceback.format_exc()
            )
            return False

        return True

    def migrate_virtual_machine_mo(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'migrate_virtual_machine_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.migrate(virtual_machine_id)
        except BaseException:
            self.log.error(
                'migrate_virtual_machine_mo',
                traceback.format_exc()
            )
            return False

        return True

    def resize_virtual_machine_mo(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'resize_virtual_machine_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.confirm_resize(virtual_machine_id)
        except BaseException:
            self.log.error(
                'resize_virtual_machine_mo',
                traceback.format_exc()
            )
            return False

        return True

    def delete_virtual_machine_mo(self, virtual_machine_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'delete_virtual_machine_mo',
                'No api handler'
            )
            return False

        try:
            api_handler.servers.delete(virtual_machine_id)
        except BaseException:
            self.log.error(
                'delete_virtual_machine_mo',
                traceback.format_exc()
            )
            return False

        return True
