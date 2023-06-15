def get_tenant_name(value):
    if len(value.split('/')) == 1:
        return (None, value)

    if len(value.split('/')) == 2:
        return value.split('/')

    return None


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


def match_string(key, value, strict=False):
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
