from lib import filter_helper


class OspImageInfo():
    def __init__(self):
        self.image = None

    def get_image_info(self, image_mo):
        if image_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = getattr(image_mo, 'name')
        info['disk_format'] = getattr(image_mo, 'disk_format')
        info['container_format'] = getattr(image_mo, 'container_format')
        info['visibility'] = getattr(image_mo, 'visibility')
        info['size'] = getattr(image_mo, 'size')
        info['sizeT'] = self.format_value_dotted(info['size'])
        info['virtual_size'] = getattr(image_mo, 'virtual_size')
        info['status'] = getattr(image_mo, 'status')
        if info['status'] == 'active':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'
        info['checksum'] = getattr(image_mo, 'checksum')
        info['protected'] = getattr(image_mo, 'protected')
        if info['protected']:
            info['protectedTick'] = '\u2713'
        else:
            info['protectedTick'] = '\u2717'
        info['min_ram'] = getattr(image_mo, 'min_ram')
        info['min_disk'] = getattr(image_mo, 'min_disk')
        info['owner'] = getattr(image_mo, 'owner')
        info['os_hidden'] = getattr(image_mo, 'os_hidden')
        info['os_hash_algo'] = getattr(image_mo, 'os_hash_algo')
        info['os_hash_value'] = getattr(image_mo, 'os_hash_value')
        info['id'] = getattr(image_mo, 'id')
        info['updated_at'] = getattr(image_mo, 'updated_at')
        info['created_at'] = getattr(image_mo, 'created_at')
        info['locations'] = getattr(image_mo, 'locations')
        info['file'] = getattr(image_mo, 'file')

        return info

    def get_images_info(self, cache_enabled=True):
        if cache_enabled:
            if self.image is not None:
                return self.image

        managed_objects = self.get_image_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.image = []
        for managed_object in managed_objects:
            image_info = self.get_image_info(
                managed_object
            )
            self.image.append(
                image_info
            )

        self.log.osp_mo(
            'images',
            self.image
        )

        return self.image

    def match_image(self, image_info, image_filter):
        if image_filter is None or len(image_filter) == 0:
            return True

        for ap_rule in image_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, image_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, image_info['name']):
                    return False

            if key == 'vm':
                key_found = True
                if 'vm' in image_info:
                    found = False
                    for vm_info in image_info['vm']:
                        if filter_helper.match_tenant_name(value, vm_info['tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_image',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_images(self, object_filter=None, vm_info=False, cache_enabled=True):
        all_images = self.get_images_info(cache_enabled=cache_enabled)
        if all_images is None:
            return None

        images = []

        for image_info in all_images:
            if not self.match_image(image_info, object_filter):
                continue

            if vm_info:
                image_info['vm'] = []
                image_vms = self.get_virtual_machines(
                    object_filter=[
                        'image_id:%s' % (image_info['id'])
                    ],
                    tenant_info=True
                )
                if image_vms is None:
                    self.log.error(
                        'get_images',
                        'Get vm with image failed: %s' % (image_info['id'])
                    )
                else:
                    for image_vm in image_vms:
                        image_vm_info = {}
                        image_vm_info['tenant'] = image_vm['tenant_name']
                        image_vm_info['name'] = image_vm['name']
                        image_vm_info['tenant_name'] = '%s/%s' % (
                            image_vm['tenant_name'],
                            image_vm['name']
                        )
                        image_info['vm'].append(
                            image_vm_info
                        )

                if not self.match_image(image_info, object_filter):
                    continue


            images.append(
                image_info
            )

        images = sorted(
            images,
            key=lambda i: i['name'].lower()
        )

        return images

    def get_image(self, image_id=None, image_name=None, cache_enabled=True):
        object_filter = []
        if image_id is not None:
            object_filter.append('id:%s' % (image_id))
        if image_name is not None:
            object_filter.append('name:%s' % (image_name))

        images = self.get_images(
            object_filter=object_filter,
            cache_enabled=cache_enabled
        )

        if images is None or len(images) != 1:
            return None

        return images[0]

    def is_image(self, image_id=None, image_name=None, cache_enabled=True):
        if self.get_image(image_id=image_id, image_name=image_name, cache_enabled=cache_enabled):
            return True
        return False
