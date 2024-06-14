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
