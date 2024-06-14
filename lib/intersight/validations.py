import click

from lib.intersight import settings as intersight_settings


def validate_cache_ttl(user_cache_ttl, log_id=None):
    settings_handler = intersight_settings.IntersightSettings(
        log_id=log_id
    )
    cache_ttl = settings_handler.get_intersight_cache_ttl()
    if user_cache_ttl is not None:
        try:
            cache_ttl = int(user_cache_ttl)
        except BaseException:
            cache_ttl = -1

    return cache_ttl


def validate_int_oper(value):
    for prefix in ['ge', '>=', 'le', '<=', 'gt', '>', 'lt', '<', 'ne', '!=']:
        if value.startswith(prefix):
            try:
                int_value = int(value.lstrip(prefix))
                return value, None

            except BaseException:
                pass

            return None, 'wrong value format'

    try:
        int_value = int(value)
        return value, None
    except BaseException:
        pass

    return None, 'int value expected'


def name_filter(ctx, param, user_input):
    filters = {}
    filters['logical'] = 'or'
    filters['rule'] = []

    for item in user_input:
        if item.lower() in ['_and_', 'and']:
            filters['logical'] = 'and'
            continue

        negative = False
        if item.startswith('!'):
            negative = True
            item = item[1:]

        rule = {}
        rule['negative'] = negative
        rule['value'] = item
        filters['rule'].append(
            rule
        )

    return filters


def serial_filter(ctx, param, user_input):
    filters = {}
    filters['logical'] = 'or'
    filters['rule'] = []

    for user_input_item in user_input:
        for item in user_input_item.split(','):
            if item.lower() in ['_and_', 'and']:
                filters['logical'] = 'and'
                continue

            negative = False
            if item.startswith('!'):
                negative = True
                item = item[1:]

            rule = {}
            rule['negative'] = negative
            rule['value'] = item
            filters['rule'].append(
                rule
            )

    return filters


def add_group_filter(serial_filters, group_filters):
    for item in group_filters:
        serial_filters['rule'].append(
            dict(
                negative=False,
                value=item
            )
        )
    return serial_filters


def get_serial_filter_from_mo(servers_mo):
    filters = {}
    filters['logical'] = 'or'
    filters['rule'] = []

    for server_mo in servers_mo:
        rule = {}
        rule['negative'] = False
        rule['value'] = server_mo['Serial']
        filters['rule'].append(
            rule
        )

    return filters


def model_filter(ctx, param, user_input):
    filters = {}
    filters['logical'] = 'or'
    filters['rule'] = []

    for item in user_input:
        if item.lower() in ['_and_', 'and']:
            filters['logical'] = 'and'
            continue

        negative = False
        if item.startswith('!'):
            negative = True
            item = item[1:]

        rule = {}
        rule['negative'] = negative
        rule['value'] = item
        filters['rule'].append(
            rule
        )

    return filters


def tag(ctx, param, user_input):
    tags = []

    for item in user_input:
        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Tag validation failed: key:value format expected')
            return None

        tags.append(
            item
        )

    return tags


def tag_filter(ctx, param, user_input):
    filters = {}
    filters['logical'] = 'or'
    filters['rule'] = []

    for item in user_input:
        if item.lower() in ['_and_', 'and']:
            filters['logical'] = 'and'
            continue

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Tag filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')

        if key == '!':
            if ctx is not None:
                raise click.BadParameter('Tag filter validation failed: key expected')
            return None

        if value == '':
            if ctx is not None:
                raise click.BadParameter('Tag filter validation failed: value expected')
            return None

        negative = False
        if key.startswith('!'):
            negative = True
            key = key[1:]

        rule = {}
        rule['negative'] = negative
        rule['key'] = key
        rule['value'] = value
        filters['rule'].append(
            rule
        )

    return filters


def bot_cpu_filter(value):
    try:
        filter = cpu_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def cpu_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('CPU filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['core', 'socket', 'thread', 'vendor', 'arch', 'model']:
            if ctx is not None:
                raise click.BadParameter('CPU filter validation failed: unsupported key')
            return None

        if key == 'core':
            core_value, core_error = validate_int_oper(value)
            if core_value is None:
                if ctx is not None:
                    raise click.BadParameter('CPU filter validation failed: %s' % (core_error))
                return None

            filters['core'] = value

        if key == 'socket':
            socket_value, socket_error = validate_int_oper(value)
            if socket_value is None:
                if ctx is not None:
                    raise click.BadParameter('CPU filter validation failed: %s' % (socket_error))
                return None

            filters['socket'] = value

        if key == 'thread':
            thread_value, thread_error = validate_int_oper(value)
            if thread_value is None:
                if ctx is not None:
                    raise click.BadParameter('CPU filter validation failed: %s' % (thread_error))
                return None

            filters['thread'] = value

        if key == 'vendor':
            filters['info'] = True
            if value.lower() not in ['intel', 'amd']:
                if ctx is not None:
                    raise click.BadParameter('CPU filter validation failed: unsupported vendor')
                return None

            filters['vendor'] = value.lower()

        if key == 'arch':
            filters['info'] = True
            if value.lower() not in ['xeon', 'zen']:
                if ctx is not None:
                    raise click.BadParameter('CPU filter validation failed: unsupported architecture')
                return None

            filters['arch'] = value.lower()

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

    return filters


def bot_gpu_filter(value):
    try:
        filter = gpu_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def gpu_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('GPU filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['slot', 'model']:
            if ctx is not None:
                raise click.BadParameter('GPU filter validation failed: unsupported key')
            return None

        if key == 'slot':
            filters['info'] = True
            socket_value, socket_error = validate_int_oper(value)
            if socket_value is None:
                if ctx is not None:
                    raise click.BadParameter('GPU filter validation failed: %s' % (socket_error))
                return None

            filters['slot'] = value

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

    return filters


def bot_memory_filter(value):
    try:
        filter = memory_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def memory_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Memory filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['size', 'dimm', 'model', 'serial']:
            if ctx is not None:
                raise click.BadParameter('Memory filter validation failed: unsupported key')
            return None

        if key == 'size':
            size_value, size_error = validate_int_oper(value)
            if size_value is None:
                if ctx is not None:
                    raise click.BadParameter('Memory filter validation failed: %s' % (size_error))
                return None

            filters['size'] = value

        if key == 'dimm':
            filters['info'] = True
            dimm_value, dimm_error = validate_int_oper(value)
            if dimm_value is None:
                if ctx is not None:
                    raise click.BadParameter('Memory filter validation failed: %s' % (dimm_error))
                return None

            filters['dimm'] = value

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

        if key == 'serial':
            filters['info'] = True
            filters['serial'] = value

    return filters


def bot_pci_filter(value):
    try:
        filter = pci_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def pci_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('PCI filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['slot', 'model', 'pid']:
            if ctx is not None:
                raise click.BadParameter('PCI filter validation failed: unsupported key')
            return None

        if key == 'slot':
            filters['info'] = True
            slot_value, slot_error = validate_int_oper(value)
            if slot_value is None:
                raise click.BadParameter('GPU filter validation failed: %s' % (slot_error))

            filters['slot'] = value

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

        if key == 'pid':
            filters['info'] = True
            filters['pid'] = value

    return filters


def bot_sc_filter(value):
    try:
        filter = sc_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def sc_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Storage controller filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['vendor', 'serial']:
            if ctx is not None:
                raise click.BadParameter('Storage controller filter validation failed: unsupported key')
            return None

        if key == 'vendor':
            filters['info'] = True
            filters['vendor'] = value

        if key == 'serial':
            filters['info'] = True
            filters['serial'] = value

    return filters


def bot_pd_filter(value):
    try:
        filter = pd_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def pd_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Physical disk filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['type', 'proto', 'pid', 'model', 'serial', 'vendor', 'count']:
            if ctx is not None:
                raise click.BadParameter('Physical disk filter validation failed: unsupported key')
            return None

        if key == 'type':
            filters['info'] = True
            filters['type'] = value

        if key == 'proto':
            filters['info'] = True
            filters['proto'] = value

        if key == 'pid':
            filters['info'] = True
            filters['pid'] = value

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

        if key == 'serial':
            filters['info'] = True
            filters['serial'] = value

        if key == 'vendor':
            filters['info'] = True
            filters['vendor'] = value

        if key == 'count':
            filters['info'] = True
            count_value, count_error = validate_int_oper(value)
            if count_value is None:
                if ctx is not None:
                    raise click.BadParameter('Physical disk filter validation failed: %s' % (count_error))
                return None

            filters['count'] = value

    return filters


def bot_vd_filter(value):
    try:
        filter = vd_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def vd_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Virtual drive filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['count']:
            if ctx is not None:
                raise click.BadParameter('Virtual drive filter validation failed: unsupported key')
            return None

        if key == 'count':
            filters['info'] = True
            count_value, count_error = validate_int_oper(value)
            if count_value is None:
                if ctx is not None:
                    raise click.BadParameter('Virtual drive filter validation failed: %s' % (count_error))
                return None

            filters['count'] = value

    return filters


def bot_fan_filter(value):
    try:
        filter = fan_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def fan_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('Fan filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['mod', 'unit', 'state']:
            if ctx is not None:
                raise click.BadParameter('Fan filter validation failed: unsupported key')
            return None

        if key == 'mod':
            filters['info'] = True
            mod_value, mod_error = validate_int_oper(value)
            if mod_value is None:
                if ctx is not None:
                    raise click.BadParameter('Fan filter validation failed: %s' % (mod_error))
                return None

            filters['mod'] = value

        if key == 'unit':
            filters['info'] = True
            unit_value, unit_error = validate_int_oper(value)
            if unit_value is None:
                if ctx is not None:
                    raise click.BadParameter('Fan filter validation failed: %s' % (unit_error))
                return None

            filters['unit'] = value

        if key == 'state':
            filters['info'] = True
            if value.lower() not in ['ok', 'nok']:
                if ctx is not None:
                    raise click.BadParameter('Fan filter validation failed: expected state ok or nok')
                return None

            filters['state'] = value.lower()

    return filters


def bot_psu_filter(value):
    try:
        filter = psu_filter(None, None, value)
    except BaseException:
        filter = None

    return filter


def psu_filter(ctx, param, user_input):
    filters = {}
    filters['info'] = False
    filters['enabled'] = False

    for item in user_input:
        filters['enabled'] = True

        if len(item.split(':')) != 2:
            if ctx is not None:
                raise click.BadParameter('PSU filter validation failed: key:value format expected')
            return None

        (key, value) = item.split(':')
        if key not in ['model', 'serial', 'vendor', 'state']:
            if ctx is not None:
                raise click.BadParameter('PSU filter validation failed: unsupported key')
            return None

        if key == 'state':
            filters['info'] = True
            if value.lower() not in ['ok', 'nok']:
                if ctx is not None:
                    raise click.BadParameter('Fan filter validation failed: expected state ok or nok')
                return None

            filters['state'] = value.lower()

        if key == 'model':
            filters['info'] = True
            filters['model'] = value

        if key == 'serial':
            filters['info'] = True
            filters['serial'] = value

        if key == 'vendor':
            filters['info'] = True
            filters['vendor'] = value

    return filters
