import json
import os
import re
import copy
import traceback

from inputimeout import inputimeout, TimeoutOccurred
import colorama


class OutputHelper():
    def __init__(self, silent=False, verbose=False, debug=False, log_id=None):
        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug
        self.output = ''
        self.stream = None
        self.set_stream()

        self.output_directory = '/tmp/iserver/'
        if log_id is not None:
            self.output_directory = os.path.join(self.output_directory, log_id)

        self.default_filename = os.path.join(self.output_directory, 'iserver.output.default')
        self.verbose_filename = os.path.join(self.output_directory, 'iserver.output.verbose')
        self.debug_filename = os.path.join(self.output_directory, 'iserver.output.debug')
        self.json_filename = os.path.join(self.output_directory, 'iserver.output.json')
        self.devel_filename = os.path.join(self.output_directory, 'devel.debug')
        self.duration_filename = os.path.join(self.output_directory, 'duration.debug')

        colorama.init()

    def initialize(self, max_dirs=1000):
        try:
            if not os.path.isdir(self.output_directory):
                os.makedirs(self.output_directory, exist_ok=True)

        except BaseException:
            print(traceback.format_exc())

    def is_output(self):
        for filename in [self.default_filename, self.verbose_filename, self.debug_filename]:
            if os.path.isfile(filename):
                return True
        return False

    def json_output(self, output):
        try:
            self.append(self.json_filename, json.dumps(output, indent=4))
        except BaseException:
            pass

    def clean(self):
        try:
            for filename in [self.default_filename, self.verbose_filename, self.debug_filename]:
                if os.path.isfile(filename):
                    os.remove(filename)
        except BaseException:
            pass

    def clear_output(self):
        self.output = ''

    def get_output(self):
        return self.output

    def my_print(self, output):
        if output is not None:
            if not self.flags['silent']:
                self.output = '%s\n%s' % (
                    self.output,
                    self.escape_ansi(
                        self.escape_ticks(
                            output,
                            alternative=True
                        )
                    )
                )

    def print_stream(self, output, stream):
        if stream == 'output':
            self.my_print(output)

        if stream == 'debug':
            self.debug(output)

        if stream == 'info':
            self.info(output)

        if stream == 'default':
            self.default(output)
            self.my_print(output)

    def set_stream(self):
        if self.flags['silent']:
            self.stream = None
            return

        if self.flags['verbose']:
            self.stream = 'info'
            return

        if self.flags['debug']:
            self.stream = 'debug'
            return

        self.stream = 'default'

    def set_flags(self, silent, verbose, debug):
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug
        self.set_stream()

    def escape_ansi(self, line):
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        return ansi_escape.sub('', line)

    def escape_ticks(self, line, alternative=False):
        if alternative:
            line = line.replace('\u2713', 'V')
            line = line.replace('\u2717', 'X')
        else:
            line = line.replace('\u2713', '+')
            line = line.replace('\u2717', '-')

        return line

    def append(self, filename, output):
        try:
            output = self.escape_ansi(output)
            with open(filename, 'a', encoding='utf-8') as file_handler:
                file_handler.write('%s\n' % (output))
        except BaseException:
            pass

    def traceback(self, output):
        ''' Always print '''
        output = '%s %s' % (
            self.add_color('[ERROR]', 'Red'),
            output
        )
        print(output)
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def error(self, output):
        ''' Always print '''
        output = '%s %s' % (
            self.add_color('[ERROR]', 'Red'),
            output
        )
        print(output)
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def files_only(self, output):
        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def default(self, output, underline=False, color=None, before_newline=False, after_newline=False):
        ''' Unless silent is set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if color is not None:
            output = self.add_color(
                output,
                color
            )

        if before_newline:
            output = '\n%s' % (output)

        if after_newline:
            output = '%s\n' % (output)

        if not self.flags['silent']:
            try:
                print(output)
            except BaseException:
                print(
                    self.escape_ticks(output)
                )

        self.append(self.default_filename, output)
        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def debug(self, output, underline=False, color=None, before_newline=False, after_newline=False):
        ''' When debug flag set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if color is not None:
            output = self.add_color(
                output,
                color
            )

        if before_newline:
            output = '\n%s' % (output)

        if after_newline:
            output = '%s\n' % (output)

        if not self.flags['silent']:
            if self.flags['debug']:
                print(output)

        self.append(self.debug_filename, output)

    def duration(self, output):
        self.append(self.duration_filename, output)

    def devel(self, output):
        self.append(self.devel_filename, output)

    def info(self, output, underline=False, color=None, before_newline=False, after_newline=False):
        ''' When verbose flag set '''
        if underline:
            output = '%s\n%s' % (output, "".join(('-',) * len(output)))

        if color is not None:
            output = self.add_color(
                output,
                color
            )

        if before_newline:
            output = '\n%s' % (output)

        if after_newline:
            output = '%s\n' % (output)

        if not self.flags['silent']:
            if self.flags['verbose']:
                print(output)

        self.append(self.verbose_filename, output)
        self.append(self.debug_filename, output)

    def get_subkey(self, value, key):
        if value is not None:
            if '.' in key:
                subkey = key.split('.')[0]
                if subkey not in value:
                    return ''

                new_key = '.'.join(key.split('.')[1:])
                return self.get_subkey(value[subkey], new_key)

            if key in value:
                return value[key]

        return ''

    def replace_subkey(self, value, key, new_value):
        if '.' in key:
            subkey = key.split('.')[0]
            if subkey not in value:
                return value

            if value[subkey] is not None:
                if isinstance(value[subkey], dict):
                    value[subkey][key.split('.')[1]] = new_value

            return value

        value[key] = new_value
        return value

    def merge_output(self, values):
        if isinstance(values, dict):
            if '__Output' not in values:
                values['__Output'] = {}

            for key in values:
                if isinstance(values[key], dict):
                    if '__Output' in values[key]:
                        for okey in values[key]['__Output']:
                            values['__Output']['%s.%s' % (key, okey)] = values[key]['__Output'][okey]

        if isinstance(values, list):
            for value in values:
                if '__Output' not in value:
                    value['__Output'] = {}

                for key in value:
                    if isinstance(value[key], dict):
                        if '__Output' in value[key]:
                            for okey in value[key]['__Output']:
                                value['__Output']['%s.%s' % (key, okey)] = value[key]['__Output'][okey]

        return values

    def add_color(self, value, color):
        if color == 'Red':
            return colorama.Fore.RED + value + colorama.Fore.RESET

        if color == 'Green':
            return colorama.Fore.GREEN + value + colorama.Fore.RESET

        if color == 'Yellow':
            return colorama.Fore.YELLOW + value + colorama.Fore.RESET

        if color == 'Blue':
            return colorama.Fore.BLUE + value + colorama.Fore.RESET

        return value

    def add_key_color(self, key, value, value_definition):
        if '__Output' not in value_definition:
            return value

        if key not in value_definition['__Output']:
            return value

        color = value_definition['__Output'][key]

        if color is None:
            return value

        if color == 'Red':
            return colorama.Fore.RED + str(value) + colorama.Fore.RESET

        if color == 'Green':
            return colorama.Fore.GREEN + str(value) + colorama.Fore.RESET

        if color == 'Yellow':
            return colorama.Fore.YELLOW + str(value) + colorama.Fore.RESET

        if color == 'Blue':
            return colorama.Fore.BLUE + str(value) + colorama.Fore.RESET

        if color.startswith(':'):
            letters = color.lstrip(':')
            colored_output = ''
            for index, letter in enumerate(value):
                if index >= len(letters):
                    colored_output = colored_output + letter
                    continue

                if letters[index] == 'R':
                    colored_output = colored_output + colorama.Fore.RED + letter + colorama.Fore.RESET
                    continue

                if letters[index] == 'G':
                    colored_output = colored_output + colorama.Fore.GREEN + letter + colorama.Fore.RESET
                    continue

                if letters[index] == 'Y':
                    colored_output = colored_output + colorama.Fore.YELLOW + letter + colorama.Fore.RESET
                    continue

                if letters[index] == 'B':
                    colored_output = colored_output + colorama.Fore.BLUE + letter + colorama.Fore.RESET
                    continue

                colored_output = colored_output + letter

            return colored_output

        return value

    def remove_empty_columns(self, headers, order, values, allow_order_subkeys=False):
        if headers is None or order is None:
            return headers, order

        remove_keys = []
        for key in order:
            show_key = False
            for value in values:
                if allow_order_subkeys and '.' in key:
                    if isinstance(self.get_subkey(value, key), str):
                        if len(self.get_subkey(value, key)) > 0:
                            show_key = True
                    else:
                        show_key = True

                else:
                    if key in value:
                        if isinstance(value[key], str):
                            if len(value[key]) > 0:
                                show_key = True
                        else:
                            show_key = True

            if not show_key:
                remove_keys.append(key)

        for key in remove_keys:
            index = order.index(key)
            headers.remove(
                headers[index]
            )
            order.remove(
                key
            )

        return headers, order

    def expand_list(self, values, order, key):
        new_values = []
        for value in values:
            if len(value[key]) == 0:
                value[key] = ''
                value['__Last'] = True
                new_values.append(value)
                continue

            if len(value[key]) == 1:
                value[key] = value[key][0]
                if '__Output' in value and '__Output' in value[key]:
                    for okey in value[key]['__Output']:
                        value['__Output']['%s.%s' % (key, okey)] = value[key]['__Output'][okey]
                value['__Last'] = True
                new_values.append(value)
                continue

            if len(value[key]) > 1:
                index = 1
                for item in value[key]:
                    if isinstance(item, dict):
                        if index == 1:
                            new_value = copy.deepcopy(value)
                            new_value[key] = item
                        else:
                            new_value = copy.deepcopy(value)
                            new_value[key] = {}
                            for displayed_field in order:
                                new_value = self.replace_subkey(
                                    new_value,
                                    displayed_field,
                                    ''
                                )

                            new_value = self.replace_subkey(
                                new_value,
                                key,
                                item
                            )

                        if '__Output' in new_value and '__Output' in item:
                            for okey in item['__Output']:
                                new_value['__Output']['%s.%s' % (key, okey)] = item['__Output'][okey]

                        new_value['__Last'] = False
                        if index == len(value[key]) - 1:
                            new_value['__Last'] = True

                        new_values.append(new_value)
                        index = index + 1

                    else:
                        if index == 1:
                            new_value = copy.deepcopy(value)
                            new_value[key] = item
                        else:
                            new_value = copy.deepcopy(value)
                            for displayed_field in order:
                                new_value = self.replace_subkey(
                                    new_value,
                                    displayed_field,
                                    ''
                                )

                            new_value = self.replace_subkey(
                                new_value,
                                key,
                                item
                            )

                        if '__Output' in new_value and '__Output' in item:
                            for okey in item['__Output']:
                                new_value['__Output']['%s.%s' % (key, okey)] = item['__Output'][okey]

                        new_value['__Last'] = False
                        if index == len(value[key]) - 1:
                            new_value['__Last'] = True

                        new_values.append(new_value)
                        index = index + 1

                continue

        return new_values

    def expand_lists(self, values_ref, order, keys):
        values = copy.deepcopy(values_ref)
        new_values = []
        for value in values:
            max_key_length = 0
            for key in keys:
                if key in value and value[key] is not None:
                    max_key_length = max(
                        max_key_length,
                        len(value[key])
                    )

            if max_key_length == 0:
                for key in keys:
                    value[key] = ''
                value['__Last'] = True
                new_values.append(value)

            if max_key_length == 1:
                for key in keys:
                    if key not in value or value[key] is None or len(value[key]) == 0:
                        value[key] = ''
                    else:
                        if '__Output' in value[key][0]:
                            if '__Output' not in value:
                                value['__Output'] = {}

                            for output_key in value[key][0]['__Output']:
                                value['__Output']['%s.%s' % (key, output_key)] = value[key][0]['__Output'][output_key]

                        value[key] = value[key][0]

                value['__Last'] = True
                new_values.append(value)

            if max_key_length > 1:
                for index in range(0, max_key_length):
                    if index == 0:
                        new_value = copy.deepcopy(value)
                        if '__Output' not in new_value:
                            new_value['__Output'] = {}
                        value['__Last'] = False

                        for key in keys:
                            if key not in value:
                                new_value[key] = ''
                                continue

                            if len(value[key]) == 0:
                                new_value[key] = {}
                            else:
                                new_value[key] = copy.deepcopy(value[key][0])
                                if '__Output' in value[key][0]:
                                    for output_key in value[key][0]['__Output']:
                                        new_value['__Output']['%s.%s' % (key, output_key)] = value[key][0]['__Output'][output_key]

                        new_values.append(new_value)

                    if index > 0:
                        new_value = copy.deepcopy(value)
                        if '__Output' not in new_value:
                            new_value['__Output'] = {}

                        for key in keys:
                            if key not in value:
                                new_value[key] = ''
                                continue

                            if len(value[key]) == 0:
                                new_value[key] = {}
                            else:
                                new_value[key] = copy.deepcopy(value[key][0])

                        for displayed_field in order:
                            new_value = self.replace_subkey(
                                new_value,
                                displayed_field,
                                ''
                            )

                        new_value['__Last'] = False
                        for key in keys:
                            if key not in value:
                                continue

                            if len(value[key]) > index:
                                new_value[key] = copy.deepcopy(value[key][index])
                                if '__Output' in value[key][index]:
                                    for output_key in value[key][index]['__Output']:
                                        new_value['__Output']['%s.%s' % (key, output_key)] = value[key][index]['__Output'][output_key]

                        if index == max_key_length - 1:
                            new_value['__Last'] = True

                        new_values.append(new_value)

        return new_values

    def add_last_tag(self, values):
        new_values = []
        is_last = False
        for value in values:
            if '__Last' in value:
                is_last = True
            new_values.append(value)

        if not is_last:
            for value in new_values:
                value['__Last'] = True

        return new_values

    def my_table(self, values, spacing=3, underline=False, order=None, allow_order_subkeys=False, headers=None, headers_upper=False, table=False, row_separator=False, remove_empty_columns=False, stream='default', merge=False):
        if merge:
            values = self.merge_output(
                values
            )

        if remove_empty_columns:
            headers, order = self.remove_empty_columns(headers, order, values, allow_order_subkeys=allow_order_subkeys)

        if table and row_separator:
            values = self.add_last_tag(values)

        if values is None:
            values = []

        if len(values) == 0:
            if not table:
                return

        # Params fixup
        if table:
            spacing = 1
            underline = False

        if order is None:
            item = values[0]
            display = item.keys()
        else:
            display = order

        # keys holds the column length

        keys = {}
        if headers is None:
            for key in display:
                keys[key] = len(key)
        else:
            for index, value in enumerate(display):
                keys[value] = len(headers[index])

        for value in values:
            for key in keys:
                try:
                    if allow_order_subkeys and '.' in key:
                        value[key] = str(
                            self.get_subkey(value, key)
                        )
                    else:
                        value[key] = str(value[key])
                except BaseException:
                    value[key] = ''

                keys[key] = max(keys[key], len(value[key]))

        if headers is not None:
            index = 0
            for key in keys:
                keys[key] = max(keys[key], len(headers[index]))
                index = index + 1

        for key in keys:
            keys[key] = keys[key] + spacing

        # print header

        if headers is None:
            header = ''
            for key in keys:
                header = '%s%s' % (header, key.capitalize().ljust(keys[key]))
        else:
            header = ''
            if table:
                header = '| '
                table_top = '+-'

            index = 0
            for key in keys:

                column_title = headers[index]
                if headers_upper:
                    column_title = column_title.upper()

                if table:
                    table_top = '%s%s+-' % (table_top, ''.ljust(keys[key], '-'))
                    header = '%s%s| ' % (header, column_title.ljust(keys[key]))
                else:
                    header = '%s%s' % (header, column_title.ljust(keys[key]))

                index = index + 1

            if table:
                header = header.rstrip(' ')
                table_top = table_top.rstrip('-')

        if table:
            header = '%s\n%s\n%s' % (
                table_top,
                header,
                table_top
            )

        self.print_stream('\n%s' % (header), stream)

        if underline:
            line = ''
            index = 0
            for key in keys:
                if table:
                    line = '%s%s%s | ' % (
                        line,
                        ''.ljust(keys[key] - spacing, '-'),
                        ''.ljust(spacing)
                    )

                else:
                    line = '%s%s%s' % (
                        line,
                        ''.ljust(keys[key] - spacing, '-'),
                        ''.ljust(spacing)
                    )
                index = index + 1

            self.print_stream(line, stream)

        for value in values:
            line = ''
            if table:
                line = '| '

            index = 0
            for key in keys:
                if table:
                    line = '%s%s| ' % (
                        line,
                        self.add_key_color(
                            key,
                            value[key].ljust(keys[key]),
                            value
                        )
                    )
                else:
                    line = '%s%s' % (line, value[key].ljust(keys[key]))

                index = index + 1

            self.print_stream(line, stream)
            if table and row_separator:
                if '__Last' in value and value['__Last']:
                    self.print_stream(table_top, stream)

        if table:
            if not row_separator:
                self.print_stream(table_top, stream)

    def get_dictionary_value(self, dictionary, key):
        my_dictionary = dictionary
        dictionary_value = None

        if ':' not in key:
            if '.' in key:
                dictionary_value = ''
                if isinstance(dictionary[key.split('.')[0]], dict):
                    dictionary_value = self.get_subkey(dictionary, key)

                if isinstance(dictionary[key.split('.')[0]], list):
                    values = []
                    for item in dictionary[key.split('.')[0]]:
                        values.append(
                            self.get_subkey(item, key.split('.')[1])
                        )
                    dictionary_value = ', '.join(values)
            else:
                dictionary_value = self.get_subkey(dictionary, key)

        if ':' in key:
            keys = key.split(':')
            for index, iter_key in enumerate(keys):
                if iter_key not in my_dictionary:
                    break

                if index < len(keys) - 1:
                    my_dictionary = my_dictionary[iter_key]
                    continue

                dictionary_value = my_dictionary[iter_key]

        return dictionary_value

    def dictionary(self, items, exclude=[], title=None, underline=True, prefix=None, keys=None, values=None, title_keys=None, justify=False, newline=[], stream='default', start='\n'):
        header = ''
        if title is not None:
            header = '%s%s' % (start, title)
            if underline:
                header = '%s\n%s' % (header, "".join(('-',) * len(title)))

        body = ''

        # Get longest key
        # note that keys may have : syntax
        if justify:
            longest = 0
            if title_keys is None:
                if keys is None:
                    for i in items:
                        if i not in exclude:
                            longest = max(longest, len(i))
                if keys is not None:
                    for key in keys:
                        longest = max(longest, len(key.split(':')[-1]))

            if title_keys is not None:
                for title_key in title_keys:
                    longest = max(longest, len(title_key))

            longest = longest + 1

        # Print all items
        if keys is None:
            for item in items:
                if item not in exclude:
                    ikey = item
                    if justify:
                        ikey = ikey.ljust(longest)

                    if isinstance(items[item], list):
                        if prefix is not None:
                            body = '%s%s%s:\n' % (body, prefix, ikey)
                        else:
                            body = '%s%s:\n' % (body, ikey)

                        for list_item in items[item]:
                            body = '%s\t%s\n' % (body, list_item)

                    else:

                        if prefix is not None:
                            body = '%s%s%s: %s\n' % (body, prefix, ikey, items[item])
                        else:
                            body = '%s%s: %s\n' % (body, ikey, items[item])

        # Print selected keys with optional title
        if keys is not None:
            index = 0
            for key in keys:
                if key is not None:
                    ikey = key.split(':')[-1]
                    ivalue = self.add_key_color(
                        key,
                        self.get_dictionary_value(items, key),
                        items
                    )
                if key is None:
                    ikey = None
                    ivalue = values[index]

                if ivalue is not None:
                    if title_keys is not None:
                        ikey = title_keys[index]

                    if justify:
                        ikey = ikey.ljust(longest)

                    if isinstance(ivalue, list):
                        if prefix is not None:
                            body = '%s%s%s:\n' % (body, prefix, ikey)
                        else:
                            body = '%s%s:\n' % (body, ikey)

                        for list_item in ivalue:
                            body = '%s\t%s\n' % (body, list_item)

                    if isinstance(ivalue, str):
                        if '\n' in ivalue:
                            ivalue = ivalue.replace('\n', '\n\t')
                            if prefix is not None:
                                body = '%s%s%s:\n\t%s\n' % (body, prefix, ikey, ivalue)
                            else:
                                body = '%s%s:\n\t%s\n' % (body, ikey, ivalue)
                        else:
                            if prefix is not None:
                                body = '%s%s%s: %s\n' % (body, prefix, ikey, ivalue)
                            else:
                                body = '%s%s: %s\n' % (body, ikey, ivalue)

                    if not isinstance(ivalue, str) and not isinstance(ivalue, list):
                        if prefix is not None:
                            body = '%s%s%s: %s\n' % (body, prefix, ikey, ivalue)
                        else:
                            body = '%s%s: %s\n' % (body, ikey, ivalue)

                if key in newline:
                    body = '%s\n' % (body)

                index = index + 1

        if stream is not None:
            if len(header) > 0:
                self.print_stream(header, stream)

            if len(body) > 0:
                self.print_stream(body, stream)

        output = '%s\n%s' % (header, body)
        return output

    def columns(self, data, spacing=2, stream='default', max_length=80):
        column_width = []
        column_height = []
        for col in data:
            column_height.append(len(col))
            col_width = 0
            for item in col:
                col_width = max(col_width, len(item))
            column_width.append(col_width)

        rows = []
        row_length = 0
        row = []
        for col_index in list(range(len(data))):
            if row_length > 0:
                if row_length + column_width[col_index] > max_length:
                    rows.append(row)
                    row = []
                    row_length = 0
                else:
                    row.append(
                        dict(
                            data=data[col_index],
                            width=column_width[col_index],
                            height=column_height[col_index]
                        )
                    )
                    row_length = row_length + column_width[col_index]
                    continue

            if row_length == 0:
                row.append(
                    dict(
                        data=data[col_index],
                        width=column_width[col_index],
                        height=column_height[col_index]
                    )
                )
                row_length = column_width[col_index]

        rows.append(row)

        # Fixup column width per row

        for row in rows:
            avg_column_width = int(max_length / len(row))
            for col in row:
                if col['width'] < avg_column_width:
                    col['width'] = avg_column_width - spacing - 1

        # Print out of rows

        for row in rows:
            row_lines = 0
            for col in row:
                row_lines = max(row_lines, col['height'])

            for line_index in list(range(row_lines)):
                line = ''
                for col in row:
                    try:
                        line = '%s%s%s' % (
                            line,
                            col['data'][line_index].ljust(col['width']),
                            ''.ljust(spacing)
                        )
                    except BaseException:
                        line = '%s%s%s' % (
                            line,
                            ''.ljust(col['width']),
                            ''.ljust(spacing)
                        )
                self.print_stream(line, stream)

            self.print_stream('', stream)

    def kubernetes_versions(self, versions, verbose, output):
        if output == 'json':
            self.my_print(json.dumps(versions, indent=4))
            return
        self.my_table(versions)

    def clusters_name(self, names, prefix=None):
        try:
            if names is None or len(names) == 0:
                self.my_print('[INFO] No cluster found')
                return

            for name in names:
                if prefix is None:
                    self.my_print(name)
                else:
                    self.my_print('%s%s' % (prefix, name))
        except BaseException:
            self.my_print('[ERROR] Exception')

    def my_logs(self, logs, stream='devel'):
        for log_entry in logs:
            if logs[log_entry] is not None:
                output = '\nLog: %s' % (log_entry)
                output = '%s\n%s\n' % (output, "".join(('-',) * len(output)))

                if stream == 'devel':
                    if log_entry != 'debug':
                        self.devel(output)
                        self.devel(logs[log_entry])

                if stream == 'default':
                    self.default(output)
                    self.default(logs[log_entry])

    def get_input(self, message, timeout=None):
        if timeout is None:
            return input(message)

        try:
            user_input = inputimeout(prompt=message, timeout=timeout)
        except TimeoutOccurred:
            user_input = None

        return user_input
