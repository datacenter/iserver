import os
import time

from lib import settings_helper
from lib import file_helper


class Cache():
    def __init__(self):
        self.cache_ttl = 0
        self.cache_filenames = None

    def set_ttl(self, ttl):
        self.cache_ttl = ttl

    def get_post_cache(self, name):
        content = file_helper.get_file_json(
            os.path.join(
                self.get_directory(dir_type='post'),
                '%s.json' % (name)
            )
        )
        if content is None:
            self.log.error('get_post_cache', name)

        return content

    def set_post_cache(self, name, content):
        if content is None or len(content) == 0:
            self.my_output.debug('Empty content: %s' % (name))

        success = file_helper.set_file_json(
            os.path.join(
                self.get_directory(dir_type='post'),
                '%s.json' % (name)
            ),
            content
        )
        return success

    def load_timestamp(self):
        value = file_helper.get_file(
            os.path.join(
                self.get_directory(dir_type='post'),
                'timestamp'
            )
        )
        self.timestamp = int(value)

    def save_timestamp(self):
        success = file_helper.set_file(
            os.path.join(
                self.get_directory(dir_type='post'),
                'timestamp'
            ),
            str(self.timestamp)
        )
        return success

    def load_out_of_sync(self):
        self.out_of_sync = file_helper.get_file_json(
            os.path.join(
                self.get_directory(dir_type='post'),
                'out_of_sync'
            )
        )

    def save_out_of_sync(self):
        success = file_helper.set_file_json(
            os.path.join(
                self.get_directory(dir_type='post'),
                'out_of_sync'
            ),
            self.out_of_sync
        )
        return success

    def get_pre_cache_content(self, name):
        content = file_helper.get_file_json(
            os.path.join(
                self.get_directory(dir_type='pre'),
                '%s.json' % (name)
            )
        )
        if content is None:
            return None

        return content['content']

    def get_pre_cache(self, prefix, suffix):
        if self.cache_filenames is None:
            self.cache_filenames = []
            for filename in os.listdir(self.get_directory()):
                self.cache_filenames.append(
                    filename.split('.')[0]
                )

        pre_cache = {}
        for filename in self.cache_filenames:
            if len(filename.split('%s-' % (prefix))) == 1:
                continue

            if filename[:(len(prefix))] != prefix:
                continue

            key = filename[(len(prefix) + 1):]

            if len(suffix) > 0:
                if len(filename.split('-%s' % (suffix))) == 1:
                    continue

                if key[-(len(suffix)):] != suffix:
                    continue

                key = key[:-(len(suffix))][:-1]

            pre_cache[key] = self.get_cache(filename, out_of_sync=True)
            if pre_cache[key] is None:
                self.my_output.error('Failed to read file: %s' % (filename))
                return None

        if len(pre_cache) == 0:
            self.my_output.error('Failed to find filename for: prefix [%s] suffix [%s]' % (prefix, suffix))
            return None

        return pre_cache

    def get_pre_cache_2level(self, prefix, middle):
        if self.cache_filenames is None:
            self.cache_filenames = []
            for filename in os.listdir(self.get_directory()):
                self.cache_filenames.append(
                    filename.split('.')[0]
                )

        pre_cache = {}
        for filename in self.cache_filenames:
            if len(filename.split('-')) != 4:
                continue

            if filename.split('-')[0] != prefix:
                continue

            if filename.split('-')[2] != middle:
                continue

            if filename.split('-')[1] not in pre_cache:
                pre_cache[filename.split('-')[1]] = {}

            pre_cache[filename.split('-')[1]][filename.split('-')[3]] = self.get_cache(filename, out_of_sync=True)
            if pre_cache[filename.split('-')[1]][filename.split('-')[3]] is None:
                return None

        if len(pre_cache) == 0:
            self.my_output.error('Failed to find filename for: prefix [%s] middle [%s]' % (prefix, middle))
            return None

        return pre_cache

    def get_directory(self, dir_type='pre'):
        settings_handler = settings_helper.Settings(log_id=self.log_id)
        directory = os.path.join(
            os.path.join(
                os.path.join(
                    settings_handler.get_settings_dir(),
                    'xd'
                ),
                dir_type
            ),
            self.domain_name
        )
        if not os.path.isdir(directory):
            os.makedirs(directory, exist_ok=True)

        return directory

    def get_cache(self, name, out_of_sync=False):
        content = file_helper.get_file_json(
            os.path.join(
                self.get_directory(),
                '%s.json' % (name)
            )
        )
        if content is None:
            return None

        if out_of_sync:
            # For loading pre results into xd
            if content['timestamp'] <= self.timestamp:
                self.out_of_sync.append(
                    name
                )

            return content['content']

        # For prepare phase where ttl may be set
        if self.cache_ttl == 0:
            self.set_timestamp(content['timestamp'])
            return content['content']

        if int(time.time()) - content['timestamp'] > self.cache_ttl:
            return None

        self.set_timestamp(content['timestamp'])
        return content['content']

    def set_cache(self, name, body):
        content = {}
        content['timestamp'] = int(time.time())
        content['content'] = body
        success = file_helper.set_file_json(
            os.path.join(
                self.get_directory(),
                '%s.json' % (name)
            ),
            content
        )
        return success
