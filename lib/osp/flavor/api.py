import time
import traceback


class OspFlavorApi():
    def __init__(self):
        self.flavor_mo = None
        self.flavor_keys_mo = None

    def get_flavor_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.flavor_mo is not None:
                return self.flavor_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_flavor_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.flavor_mo = api_handler.flavors.list()
            self.log.osp(
                'get',
                'flavors',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_flavor_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'flavors',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.flavor_mo

    def get_flavor_keys_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.flavor_keys_mo is not None:
                return self.flavor_keys_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_flavor_keys_mo',
                'No api handler'
            )
            return None

        try:
            flavors_mo = self.get_flavor_mo(cache_enabled=cache_enabled)
            if flavors_mo is None:
                return None

            start_time = int(time.time() * 1000)

            self.flavor_keys_mo = {}
            for flavor_mo in flavors_mo:
                self.flavor_keys_mo[flavor_mo.id] = flavor_mo.get_keys()

            self.log.osp(
                'get',
                'flavors_keys',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_flavor_keys_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'flavors_keys',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.flavor_keys_mo

    def create_flavor_mo(self, name, ram, vcpus, disk, uuid='auto'):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_flavor',
                'No api handler'
            )
            return None

        try:
            ret = api_handler.flavors.create(
                name,
                ram,
                vcpus,
                disk,
                uuid
            )
            new_flavor_id = ret.id
        except BaseException:
            self.log.error(
                'create_flavor',
                'API failed'
            )
            self.log.error(
                'create_flavor',
                traceback.format_exc()
            )
            return None

        return new_flavor_id

    def delete_flavor_mo(self, flavor_id):
        api_handler = self.get_api_nova(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'delete_flavor',
                'No api handler'
            )
            return None

        try:
            api_handler.flavors.delete(
                flavor_id
            )

        except BaseException:
            self.log.error(
                'create_flavor',
                'API failed'
            )
            self.log.error(
                'create_flavor',
                traceback.format_exc()
            )
            return False

        return True
