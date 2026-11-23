import json
from lib import filter_helper


class Common():
    def __init__(self):
        pass

    def get_section(self, content, starting_line, ending_pattern):
        lines = []
        section = False

        input_lines = None

        if isinstance(content, str):
            input_lines = content.split('\n')

        if isinstance(content, list):
            input_lines = content

        if input_lines is None:
            self.log.error(
                'get_section',
                'Unexpected content: %s' % (content)
            )
            return None

        for line in input_lines:
            if line.startswith(ending_pattern):
                if section:
                    section = False
                    break

            if line == starting_line:
                section = True
                continue

            if section:
                lines.append(
                    line
                )

        return lines

    def get_lines(self, content, begin_pattern=None, strip=False, limit=-1):
        lines = []

        input_lines = None

        if isinstance(content, str):
            input_lines = content.split('\n')

        if isinstance(content, list):
            input_lines = content

        if input_lines is None:
            self.log.error(
                'get_section',
                'Unexpected content: %s' % (content)
            )
            return None

        for line in input_lines:
            if begin_pattern is None:
                lines.append(line)
            else:
                if line.startswith(begin_pattern):
                    if strip:
                        lines.append(line[len(begin_pattern):])
                    else:
                        lines.append(line)

            if limit > 0 and len(lines) >= limit:
                break

        return lines

    def get_line(self, content, begin_pattern, strip=False):
        lines = self.get_lines(
            content,
            begin_pattern=begin_pattern,
            strip=strip,
            limit=1
        )
        if len(lines) == 1:
            return lines[0]
        return None

    def match_info(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if value != filter_helper.get(info, key):
                return False

        return True
    
    def get_cmd(self, object_name, cache_enabled=True):
        if cache_enabled:
            if getattr(self, '%s_cmd' % (object_name)) is not None:
                return getattr(self, '%s_cmd' % (object_name))

            cache = self.get_cmd_cache(
                object_name
            )
            if cache is not None:
                setattr(self, '%s_cmd' % (object_name), cache)
                return getattr(self, '%s_cmd' % (object_name))

        command = getattr(self, '%s_cli' % (object_name))
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_cmd',
                'Commands output collection failed: %s' % (object_name)
            )
            return None

        setattr(self, '%s_cmd' % (object_name), outputs[command])
        self.set_cmd_cache(
            object_name,
            getattr(self, '%s_cmd' % (object_name))
        )

        return getattr(self, '%s_cmd' % (object_name))
    
    def get_json_infos(self, object_name, object_filter=[], cache_enabled=True):
        if cache_enabled and getattr(self, object_name) is not None:
            return getattr(self, object_name)

        try:
            managed_objects = json.loads(
                getattr(self, 'get_%s_cmd' % (object_name))(cache_enabled=cache_enabled)
            )
        except BaseException:
            return None
        
        infos = []
        for managed_object in managed_objects:
            info = getattr(self, 'get_%s_info' % (object_name))(
                managed_object
            )
            if not self.match_info(info, object_filter):
                continue

            infos.append(
                info
            )

        setattr(self, object_name, infos)
        return infos
    
    def get_json_info(self, object_name, object_filter, cache_enabled=True):
        infos = self.get_json_infos(object_name, object_filter, cache_enabled=cache_enabled)
        if infos is None or len(infos) != 1:
            return None
        return infos[0]