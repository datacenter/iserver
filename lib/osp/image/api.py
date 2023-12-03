import time
import traceback


class OspImageApi():
    def __init__(self):
        self.image_mo = None

    def get_image_id_mo(self, image_id, cache_enabled=True):
        if cache_enabled:
            if self.image_mo is not None:
                for item in self.image_mo:
                    if item.id == image_id:
                        return item

        api_handler = self.get_api_glance(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_image_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            image_mo = api_handler.images.get(image_id)
            self.log.osp(
                'get',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_image_id_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return image_mo

    def get_image_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.image_mo is not None:
                return self.image_mo

        api_handler = self.get_api_glance(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_image_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.image_mo = api_handler.images.list()

            self.log.osp(
                'get',
                'images',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_image_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'images',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.image_mo
