import time
from datetime import timedelta
import os
import json

from progress.bar import Bar

from lib.aci import settings


class Cache():
    def __init__(self, apic_name, no_cache=False):
        if apic_name is None:
            self.cache_enabled = False
            self.cache_write_enabled = False
            return

        settings_handler = settings.ApicSettings()

        self.cache_directory = os.path.join(
            settings_handler.get_apic_cache_base_directory(),
            apic_name
        )
        self.apic_online_mode = settings_handler.is_apic_online(
            apic_name
        )

        if not self.apic_online_mode:
            self.cache_enabled = True
            self.cache_write_enabled = False
            self.cache_settings = settings_handler.get_apic_offline_cache_settings()
            if self.cache_enabled:
                self.import_logs_to_cache()
            return

        self.cache_settings = settings_handler.get_apic_cache_settings(
            apic_name
        )
        self.cache_enabled = self.cache_settings['enabled']
        self.cache_write_enabled = True
        if no_cache:
            self.cache_enabled = False

        if self.cache_enabled:
            self.import_logs_to_cache()

    def import_logs_to_cache(self):
        logs_directory = os.path.join(
            self.cache_directory,
            'log'
        )

        if not os.path.isdir(logs_directory):
            return

        for name in os.listdir(logs_directory):
            object_name = name[8:].split('.')[0]
            object_selector = None
            if len(name[8:].split('.')) > 1:
                object_selector = '.'.join(name[8:].split('.')[1:])

            filename = os.path.join(
                logs_directory,
                name
            )

            if not name.startswith('apic.mo.'):
                print('Remove non apic.mo. file: %s' % (filename))
                os.remove(filename)
                continue

            try:
                with open(filename, 'r', encoding='utf-8') as file_handler:
                    content = json.loads(file_handler.read())

            except BaseException:
                print('Remove file on failed json load: %s' % (filename))
                os.remove(filename)
                continue

            print('Import cache: %s from file %s' % (object_name, filename))
            success = self.set_object_cache(
                object_name,
                content,
                object_selector=object_selector,
                enforce=True
            )

            if not success:
                print('Import failed')

            os.remove(filename)

    def is_cache_enabled(self):
        return self.cache_enabled

    def is_object_cache_enabled(self, object_name):
        if not self.is_cache_enabled():
            return False

        if object_name not in self.cache_settings['object']:
            return True

        return self.cache_settings['object'][object_name]['enabled']

    def get_object_cache_filename(self, object_name):
        filename = os.path.join(
            self.cache_directory,
            object_name
        )
        return filename

    def get_object_cache_ttl(self, object_name):
        if object_name in self.cache_settings['object']:
            return self.cache_settings['object'][object_name]['ttl']

        return self.cache_settings['ttl']

    def get_object_cache(self, object_name, object_selector=None):
        if not self.is_cache_enabled():
            return None

        filename = self.get_object_cache_filename(object_name)
        if filename is None:
            return None

        if object_selector is not None:
            filename = '%s.%s' % (filename, object_selector)

        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                content = json.loads(file_handler.read())

        except BaseException:
            return None

        ttl = self.get_object_cache_ttl(object_name)
        age = int(time.time()) - content['timestamp']
        if ttl > 0:
            if age > ttl:
                return None

        self.log.cache_hit(
            'aci',
            self.apic_name,
            object_name,
            filename,
            ttl,
            age
        )

        return content['cache']

    def set_object_cache(self, object_name, cache, object_selector=None, enforce=False):
        if not self.cache_write_enabled:
            if not enforce:
                return False

        filename = self.get_object_cache_filename(object_name)
        if filename is None:
            return False

        if not os.path.isdir(self.cache_directory):
            os.makedirs(self.cache_directory, exist_ok=True)

        content = {}
        content['object'] = object_name
        content['selector'] = object_selector
        content['timestamp'] = int(time.time())
        content['cache'] = cache

        if object_selector is not None:
            object_selector = object_selector.replace('/', '_')
            filename = '%s.%s' % (filename, object_selector)

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(content, indent=4))

        except BaseException:
            self.log.error(
                'apic.set_object_cache',
                'Set cache failed: %s %s %s %s' % (
                    self.apic_name,
                    object_name,
                    object_selector,
                    filename
                )
            )
            return False

        return True

    def get_cache_stats(self):
        info = []

        if not os.path.isdir(self.cache_directory):
            return info

        for name in os.listdir(self.cache_directory):
            filename = os.path.join(
                self.cache_directory, name
            )

            try:
                with open(filename, 'r', encoding='utf-8') as file_handler:
                    content = json.loads(file_handler.read())

                cache_item = {}
                cache_item['__Output'] = {}
                cache_item['object'] = content['object']
                cache_item['selector'] = content['selector']
                if cache_item['selector'] is None:
                    cache_item['selector'] = ''

                cache_item['ttl'] = self.get_object_cache_ttl(
                    content['object']
                )
                if cache_item['ttl'] <= 0:
                    cache_item['ttlT'] = '--'
                else:
                    cache_item['ttlT'] = '{}'.format(str(timedelta(seconds=cache_item['ttl'])))

                cache_item['age'] = int(time.time()) - content['timestamp']
                cache_item['ageT'] = '{}'.format(str(timedelta(seconds=cache_item['age'])))

                cache_item['valid'] = True
                cache_item['validTick'] = '\u2713'
                cache_item['__Output']['validTick'] = 'Green'
                if cache_item['ttl'] > 0:
                    if cache_item['age'] > cache_item['ttl']:
                        cache_item['valid'] = False
                        cache_item['validTick'] = '\u2717'
                        cache_item['__Output']['validTick'] = 'Red'

                info.append(
                    cache_item
                )

            except BaseException:
                pass

        info = sorted(
            info,
            key=lambda i: (
                i['object'],
                i['selector']
            )
        )

        return info

    def clear_cache(self, bar_enabled=False):
        if not os.path.isdir(self.cache_directory):
            return True

        names = os.listdir(self.cache_directory)
        if bar_enabled:
            bar_handler = Bar('Cache Files', max=len(names))

        for name in names:
            filename = os.path.join(
                self.cache_directory, name
            )
            os.remove(filename)
            if bar_enabled:
                bar_handler.next()

        if bar_enabled:
            bar_handler.finish()

        return True
