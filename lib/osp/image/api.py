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

    def create_image_mo(self, image_name, source_filename, container_format='bare', disk_format='qcow2'):
        api_handler = self.get_api_glance(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'create_image_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            image_ref = api_handler.images.create(
                name=image_name,
                container_format=container_format,
                disk_format=disk_format
            )

            new_image_id = image_ref.id
            api_handler.images.upload(
                new_image_id,
                open(source_filename, 'rb')
            )

            self.log.osp(
                'create',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.create_image_mo', traceback.format_exc())
            self.log.osp(
                'create',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return new_image_id

    def delete_image_mo(self, image_id):
        api_handler = self.get_api_glance(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'delete_image_mo',
                'No api handler'
            )
            return False

        try:
            start_time = int(time.time() * 1000)

            api_handler.images.delete(image_id)

            self.log.osp(
                'delete',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.delete_image_mo', traceback.format_exc())
            self.log.osp(
                'delete',
                'image',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        return True

    def download_image(self, image_id, destination_filename):
        api_handler = self.get_api_glance(cache_enabled=False)
        if api_handler is None:
            self.log.error(
                'download_image',
                'No api handler'
            )
            return False

        try:
            image_data = api_handler.images.data(image_id)

        except BaseException:
            self.log.error(
                'download_image',
                'API Exception'
            )
            self.log.error(
                'download_image',
                traceback.format_exc()
            )
            return False

        try:
            with open(destination_filename, "wb") as file_handler:
                for chunk in image_data:
                    file_handler.write(chunk)

        except BaseException:
            self.log.error(
                'download_image',
                'Image download failed'
            )
            self.log.error(
                'download_image',
                traceback.format_exc()
            )
            return False

        return True
