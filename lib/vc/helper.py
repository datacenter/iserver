def convert_memory(value, empty_for_zero=False):
    try:
        if value == 0 and empty_for_zero:
            return ''

        unit = ['KiB', 'MiB', 'GiB', 'TiB']
        for index in range(0, 4):
            value = value / 1024
            if value < 1000:
                break

        if value == 0:
            value = '0 [B]'
        else:
            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

    except BaseException:
        return None

    return value

def convert_cpu_capacity(value, empty_for_zero=False):
    try:
        if value == 0 and empty_for_zero:
            return ''

        unit = ['kHz', 'MHz', 'GHz']
        for index in range(0, 3):
            value = value / 1000
            if value < 1000:
                break

        if value == 0:
            value = '0 [Hz]'
        else:
            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

    except BaseException:
        return None
    return value

def convert_cpu_usage(value):
    try:
        value = '%s%%' % (int(value))
    except BaseException:
        return None
    return value

def convert_pct(pct, rounded=2):
    try:
        if rounded > 0:
            value = '%s%%' % (round(pct, rounded))
        else:
            value = '%s%%' % (int(pct))

    except BaseException:
        return None
    return value

def convert_storage(value, empty_for_zero=False):
    try:
        if value == 0 and empty_for_zero:
            return ''

        unit = ['KB', 'MB', 'GB', 'TB']
        for index in range(0, 4):
            value = value / 1024
            if value < 1024:
                break

        if value == 0:
            value = '0 [B]'
        else:
            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

    except BaseException:
        return None

    return value

def convert_speed(value, empty_for_zero=False):
    try:
        if value == 0 and empty_for_zero:
            return ''

        unit = ['kbps', 'mbps', 'gbps']
        for index in range(0, 4):
            value = value / 1000
            if value < 1000:
                break

        if value == 0:
            value = '0'
        else:
            value = '%s [%s]' % (
                round(value, 0),
                unit[index]
            )

    except BaseException:
        return None

    return value

def get_hypervisor_version(hypervisor, short=False):
    try:
        version = '%s (%s)' % (
            hypervisor.split(' ESXi ')[1].split(' ')[0],
            hypervisor.split(' build-')[1]
        )
    except BaseException:
        version = 'N/A'
        return version

    if short:
        if len(version.split(' (')) == 2:
            version = version.split(' (')[0]

    return version

def get_uptime(uptime):
    if not isinstance(uptime, int):
        return 'N/A'

    if uptime < 3600:
        return '%s mins' % (int(uptime/60))

    if uptime < 3600 * 24:
        return '%s hrs' % (int(uptime/3600))

    return '%s days' % (int(uptime/(3600 * 24)))
