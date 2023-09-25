import time
import traceback


class K8sVolumeAttachmentApi():
    def __init__(self):
        self.volume_attachment_mo = None

    def get_volume_attachment_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_attachment_mo is not None:
                return self.volume_attachment_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='storage.k8s.io/v1',
                kind='VolumeAttachment'
            )
            self.volume_attachment_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'volume_attachment',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_volume_attachment_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'volume_attachment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'volume_attachment',
            self.volume_attachment_mo
        )

        return self.volume_attachment_mo
