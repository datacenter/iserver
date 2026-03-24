import copy
import re
import time


def format_subtring_match(value):
    if not value.startswith('*'):
        value = '*%s' % (value)

    if not value.endswith('*'):
        value = '%s*' % (value)

    return value


def sanitize_string(value):
    value = value.strip()
    value = re.sub(' +', ' ', value)
    return value


def get_string_chunks(value, length, separator=' ', extra_separator='-', fixup_newline=False):
    lines = []

    if value is None:
        return lines

    words = []
    for word in value.split(separator):
        if len(word) < length:
            words.append(
                '%s%s' % (word, separator)
            )
            continue

        chunks = len(word.split(extra_separator))
        chunk_index = 1
        for word_chunk in word.split(extra_separator):
            if len(word_chunk) >= length:
                words.append(
                    '%s...-' % (word_chunk[(length - 4):])
                )
                continue

            if chunk_index < chunks:
                words.append(
                    '%s%s' % (word_chunk, extra_separator)
                )
            else:
                words.append(
                    '%s%s' % (word_chunk, separator)
                )

            chunk_index = chunk_index + 1

    line = ''
    for word in words:
        if len(word) > length:
            continue

        if len(line) + len(word) > length:
            lines.append(line)
            line = word
            continue

        line = '%s%s' % (line, word)

    if separator == ' ':
        lines.append(line.strip())
    else:
        lines.append(line[:-1])

    if fixup_newline:
        lines_no_newline = []
        for item in lines:
            lines_no_newline = lines_no_newline + item.split('\n')
        
        return lines_no_newline
    
    return lines


def get_values_from_range(value):
    values = []

    if value is not None and len(value) > 0:
        # 1,9-20,22-23,37-38
        for item in value.split(','):
            if len(item.split('-')) == 1:
                values.append(int(item))

            if len(item.split('-')) == 2:
                (start, end) = item.split('-')
                for idx in range(int(start), int(end) + 1):
                    values.append(idx)

    values = sorted(values)
    return values


def get_range_from_values(values):
    range_items = []

    values = sorted(values)
    start = None
    stop = None
    for value in values:
        value = int(value)

        if start is None:
            start = value
            stop = value
            continue

        if value == stop + 1:
            stop = value
            continue

        if start == stop:
            range_items.append(
                str(start)
            )
        else:
            range_items.append(
                '%s-%s' % (str(start), str(stop))
            )

        start = value
        stop = value

    if start is not None:
        if start == stop:
            range_items.append(
                str(start)
            )
        else:
            range_items.append(
                '%s-%s' % (str(start), str(stop))
            )

    return ','.join(range_items)


def get_tenant_name(value, delimiter='/'):
    if len(value.split(delimiter)) == 1:
        return (None, value)

    if len(value.split(delimiter)) == 2:
        return value.split(delimiter)

    return None, None


def match_tenant_name(key, value, strict=False, delimiter='/'):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if not isinstance(key, str):
        return False

    if not isinstance(value, str):
        return False

    if len(key) == 0:
        return True

    if len(value) == 0:
        return False

    if len(value.split(delimiter)) != 2:
        return False

    if len(key.split(delimiter)) > 2:
        return False

    (key_tenant, key_name) = get_tenant_name(key, delimiter=delimiter)
    (value_tenant, value_name) = get_tenant_name(value, delimiter=delimiter)

    if key_tenant is not None:
        if not match_string(key_tenant, value_tenant):
            return False
        if not match_string(key_name, value_name):
            return False

    if key_tenant is None:
        if not match_string(key_name, value_name):
            return False

    return True


def get_tenant_ap_name(value):
    if len(value.split('/')) == 1:
        return (None, None, value)

    if len(value.split('/')) == 2:
        return (None, value.split('/')[0], value.split('/')[1])

    if len(value.split('/')) == 3:
        return value.split('/')

    return None, None, None


def match_tenant_ap_name(key, value, strict=False):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if not isinstance(key, str):
        return False

    if not isinstance(value, str):
        return False

    if len(key) == 0:
        return True

    if len(value) == 0:
        return False

    if len(value.split('/')) != 3:
        return False

    if len(key.split('/')) > 3:
        return False

    (key_tenant, key_ap, key_name) = get_tenant_ap_name(key)
    (value_tenant, value_ap, value_name) = get_tenant_ap_name(value)

    if key_tenant is not None:
        if not match_string(key_tenant, value_tenant):
            return False
        if not match_string(key_ap, value_ap):
            return False
        if not match_string(key_name, value_name):
            return False

    if key_tenant is None and key_ap is not None:
        if not match_string(key_ap, value_ap):
            return False
        if not match_string(key_name, value_name):
            return False

    if key_tenant is None and key_ap is None:
        if not match_string(key_name, value_name):
            return False

    return True


def match_integer(key, value):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if isinstance(value, str):
        try:
            value = int(value)
        except BaseException:
            return False

    if key.startswith('gt'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value <= reference:
            return False

        return True

    if key.startswith('ge'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value < reference:
            return False

        return True

    if key.startswith('lt'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value >= reference:
            return False

        return True

    if key.startswith('le'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value < reference:
            return False

        return True

    if key.startswith('eq'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value != reference:
            return False

        return True

    if key.startswith('ne'):
        try:
            reference = int(key[2:])
        except BaseException:
            return False

        if value == reference:
            return False

        return True

    if len(key.split('-')) == 2:
        (start, end) = key.split('-')
        try:
            start = int(start)
        except BaseException:
            return False

        try:
            end = int(end)
        except BaseException:
            return False

        if start <= value <= end:
            return True

        return False

    try:
        reference = int(key)
    except BaseException:
        return False

    if reference != value:
        return False

    return True


def match_string(key, value, strict=False, sub=False):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if not isinstance(key, str):
        return False

    if not isinstance(value, str):
        return False

    if len(key) == 0:
        return True

    if len(value) == 0:
        return False

    if strict:
        if key == value:
            return True
        return False

    key = key.lower()
    if sub:
        if key[0] != '*':
            key ='*%s' % (key)
        if key[-1] != '*':
            key ='%s*' % (key)

    value = value.lower()

    if '*' not in key:
        if key == value:
            return True
        return False

    if key == '*':
        return True

    if key.startswith('*') and key.endswith('*'):
        if key[1:][:-1] in value:
            return True
        return False

    if key.startswith('*'):
        if value.endswith(key[1:]):
            return True
        return False

    if key.endswith('*'):
        if value.startswith(key[:-1]):
            return True
        return False

    return False


def match_mac(key, value, strict=False):
    key = '*%s*' % (
        key.replace(':', '').replace(':', '').lower()
    )
    value = value.replace(':', '').replace('.', '').lower()
    return match_string(key, value, strict=strict)


def match_wwn(key, value, strict=False):
    key = '*%s*' % (
        key.replace(':', '').replace(':', '').lower()
    )
    value = value.replace(':', '').replace('.', '').lower()
    return match_string(key, value, strict=strict)


def match_id(key, values):
    try:
        ikey = int(key)
    except BaseException:
        return False

    for value in values.split(','):
        if '-' in value:
            (start, end) = value.split('-')
            try:
                istart = int(start)
            except BaseException:
                return False

            try:
                iend = int(end)
            except BaseException:
                return False

            if istart <= ikey <= iend:
                return True

        if '-' not in value:
            try:
                ivalue = int(value)
            except BaseException:
                return False

            if ikey == ivalue:
                return True

    return False


def match_timestamp(key, value):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if not isinstance(key, str):
        return False

    if not isinstance(value, int):
        return False

    reference = None
    now = int(time.time())

    if key.endswith('m'):
        try:
            reference = now - int(key[:-1]) * 60
        except BaseException:
            return False

    if key.endswith('h'):
        try:
            reference = now - int(key[:-1]) * 60 * 60
        except BaseException:
            return False

    if key.endswith('d'):
        try:
            reference = now - int(key[:-1]) * 60 * 60 * 24
        except BaseException:
            return False

    if key.endswith('y'):
        try:
            reference = now - int(key[:-1]) * 60 * 60 * 24 * 365
        except BaseException:
            return False

    if reference is not None and reference < value:
        return True

    return False


def get_namespace_name(value, delimiter='/'):
    if len(value.split(delimiter)) == 1:
        return (None, value)

    if len(value.split(delimiter)) == 2:
        return value.split(delimiter)

    return None, None


def match_namespace_name(key, value, strict=False, delimiter='/'):
    if key is None and value is None:
        return True

    if key is None and value is not None:
        return False

    if key is not None and value is None:
        return False

    if not isinstance(key, str):
        return False

    if not isinstance(value, str):
        return False

    if len(key) == 0:
        return True

    if len(value) == 0:
        return False

    if len(value.split(delimiter)) != 2:
        return False

    if len(key.split(delimiter)) > 2:
        return False

    (key_namespace, key_name) = get_namespace_name(key, delimiter=delimiter)
    namespace_negative = False
    if key_namespace is not None:
        if len(key_namespace.split('!')) == 2:
            namespace_negative = True
            key_namespace = key_namespace.split('!')[1]

    name_negative = False
    if len(key_name.split('!')) == 2:
        name_negative = True
        key_name = key_name.split('!')[1]

    (value_namespace, value_name) = get_namespace_name(value, delimiter=delimiter)

    if key_namespace is not None:
        if not namespace_negative:
            if not match_string(key_namespace, value_namespace):
                return False
        if namespace_negative:
            if match_string(key_namespace, value_namespace):
                return False
            
        if not name_negative:
            if not match_string(key_name, value_name):
                return False
        if name_negative:
            if match_string(key_name, value_name):
                return False

    if key_namespace is None:
        if not name_negative:
            if not match_string(key_name, value_name):
                return False

        if name_negative:
            if match_string(key_name, value_name):
                return False

    return True


def split_list_of_dict(items, key):
    keys = {}
    for item in items:
        if item[key] not in keys:
            keys[item[key]] = []

    for item in items:
        keys[item[key]].append(
            item
        )

    return keys


def get_json_root_attributes(source, exceptions=None):
    destination = {}
    for key in source:
        if exceptions is None or key not in exceptions:
            if isinstance(source[key], list):
                continue

            if isinstance(source[key], dict):
                continue

        destination[key] = source[key]

    return destination


def _get_attr(value, key):
    if value is None:
        return '__ERROR'

    if ':' in key:
        subkey = key.split(':')[0]
        if subkey not in value:
            return '__ERROR'

        new_key = ':'.join(key.split(':')[1:])
        return _get_attr(value[subkey], new_key)

    if key in value:
        return value[key]

    return '__ERROR'

def get_attr(managed_object, key, on_error=None, on_none=None, cast=None):
    if managed_object is None:
        return on_error

    if not isinstance(managed_object, dict):
        if on_error is None and cast is not None:
            return cast
        return on_error

    value = _get_attr(managed_object, key)
    if value == '__ERROR':
        if on_error is None and cast is not None:
            return cast
        return on_error

    if value is None:
        if on_none is None and cast is not None:
            return cast
        return on_none

    return value

def _get(value, key):
    if value is None:
        return '__ERROR'

    if ':' in key:
        subkey = key.split(':')[0]
        if subkey not in value:
            return '__ERROR'

        new_key = ':'.join(key.split(':')[1:])
        return _get(value[subkey], new_key)

    if key in value:
        return value[key]

    return '__ERROR'

def get(managed_object, key, on_error=None, on_none=None):
    if managed_object is None:
        return on_error

    if not isinstance(managed_object, dict):
        return on_error

    value = _get(managed_object, key)
    if value == '__ERROR':
        return on_error

    if value is None:
        return on_none

    return value


def is_dict_in_dict(dict1, dict2):
    if dict1 is None or dict2 is None:
        return False
    
    if not isinstance(dict1, dict):
        return False
    
    if not isinstance(dict2, dict):
        return False

    for key in dict1:
        if key not in dict2:
            return False
        
        if dict1[key] != dict2[key]:
            return False
        
    return True


def compare_list(list1, list2):
    if list1 is None or list2 is None:
        return False
    
    if not isinstance(list1, list):
        return False
    
    if not isinstance(list2, list):
        return False
    
    if len(list1) != len(list2):
        return False
    
    for item in list1:
        if item not in list2:
            return False
        
    return True


def compare_dict(dict1, dict2):
    if dict1 is None or dict2 is None:
        return False
    
    if not isinstance(dict1, dict):
        return False
    
    if not isinstance(dict2, dict):
        return False
    
    if len(dict1) != len(dict2):
        return False
    
    for item in dict1:
        if item not in dict2:
            return False
        
        if type(dict1[item]) != type(dict2[item]):
            return False
        
        if isinstance(dict1[item], int):
            if dict1[item] != dict2[item]:
                return False
            
        if isinstance(dict1[item], str):
            if dict1[item] != dict2[item]:
                return False

        if isinstance(dict1[item], list):
            if not compare_list(dict1[item], dict2[item]):
                return False

        if isinstance(dict1[item], dict):
            if not compare_dict(dict1[item], dict2[item]):
                return False

    return True


def json_fixup(output):
    if output is None:
        return None

    if not isinstance(output, str):
        return None
    
    output = output.replace('"', '\\"')
    output = output.replace('\n', '')
    output = output.replace('}{', '},{')
    output = output.replace('\'', '\"')
    output = output.replace(': None', ': null')
    output = output.replace(': True', ': true')
    output = output.replace(': False', ': false')
    if len(output.split('},{')) > 0:
        if output.startswith('[') and output.endswith(']'):
            pass
        else:
            output = '[%s]' % (output)
    
    if len(output.replace(' ', '')) == 0:
        output = '{}'
        
    return output


def replace_attributes(content, variables):
    if content is None:
        return None

    if variables is None:
        return content

    my_variables = copy.deepcopy(variables)
    for key in my_variables:
        try:
            pattern = '${%s}' % (key)
            content = content.replace(pattern, str(my_variables[key]))

        except BaseException:
            pass

    return content
