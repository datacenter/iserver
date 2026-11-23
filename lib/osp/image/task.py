import os
import time
import traceback


class OspImageTask():
    def __init__(self):
        pass

    def wait_for_image_status(self, image_id, status_array, reverse=False, timeout=300):
        start_time = int(time.time())
        while True:
            try:
                image_mo = self.get_image_id_mo(image_id, cache_enabled=False)
                if image_mo is not None:
                    current_status = image_mo.status
                    if image_mo.status.lower() == 'error':
                        return False

                    if not reverse:
                        if current_status in status_array:
                            return True

                    if reverse:
                        if current_status not in status_array:
                            return True

            except BaseException:
                self.log.error(
                    'wait_for_image_status',
                    traceback.format_exc()
                )

            time.sleep(5)
            if (int(time.time()) - start_time) > timeout:
                self.log.error(
                    'wait_for_image_status',
                    'Timeout reached for image: %s' % (image_id)
                )
                return False

    def wait_for_image_active(self, image_id, timeout=300):
        return self.wait_for_image_status(image_id, ['active'], timeout=timeout)

    def create_image_from_virtual_machine(self, virtual_machine_id, image_name, wait=False):
        # https://github.com/openstack/python-novaclient/blob/master/novaclient/v2/servers.py
        api_handler = self.get_api_nova()
        if api_handler is None:
            self.log.error(
                'create_image_from_virtual_machine',
                'No api handler'
            )
            return None

        if self.get_image(image_name=image_name) is not None:
            self.log.error(
                'create_image_from_virtual_machine',
                'Image already exists: %s' % (image_name)
            )
            return None

        try:
            image_id = api_handler.servers.create_image(
                virtual_machine_id,
                image_name
            )
        except BaseException:
            self.log.error(
                'create_image_from_virtual_machine',
                'Failed for virtual machine %s and image name %s' % (
                    virtual_machine_id,
                    image_name
                )
            )
            self.log.error(
                'create_image_from_virtual_machine',
                traceback.format_exc()
            )
            return None

        if image_id is None:
            self.log.error(
                'create_image_from_virtual_machine',
                'Image id none for for virtual machine %s and image name %s' % (
                    virtual_machine_id,
                    image_name
                )
            )
            return None

        return image_id

    def download_image(self, image_id, filename):
        api_handler = self.get_api_glance()
        if api_handler is None:
            self.log.error(
                'download_image',
                'No api handler'
            )
            return False

        if os.path.isfile(filename):
            self.log.error(
                'Filename already exists: %s' % (filename)
            )

        try:
            data_handler = api_handler.images.data(image_id)

        except BaseException:
            self.log.error(
                'download_image',
                'Glance API Exception for image: %s' % (image_id)
            )
            self.log.error(
                'download_image',
                traceback.format_exc()
            )
            return False

        try:
            with open(filename, 'wb') as file_handler:
                for chunk in data_handler:
                    file_handler.write(chunk)

        except Exception:
            self.log.error(
                'download_image',
                'Glance Image download failed: %s => %s' % (
                    image_id,
                    filename
                )
            )
            self.log.error(
                'download_image',
                traceback.format_exc()
            )
            return False

        return True

    def delete_image(self, image_id):
        api_handler = self.get_api_glance()
        if api_handler is None:
            self.log.error(
                'download_image',
                'No api handler'
            )
            return None

        try:
            api_handler.images.delete(image_id)

        except BaseException:
            self.log.error(
                'delete_image',
                'Glance API Exception: %s' % (image_id)
            )
            self.log.error(
                'delete_image',
                traceback.format_exc()
            )
            return False

        return True
