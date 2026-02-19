class Common():
    def __init__(self):
        pass

    def get_health_info(self, value):
        try:
            ivalue = int(value)
        except BaseException:
            return None, value

        if ivalue >= 75:
            return 'Green', value

        if ivalue >= 50:
            return 'Magenta', value

        return 'Red', value

    def is_any_fault(self, faults):
        for key in ['crit', 'maj', 'minor', 'warn']:
            if faults[key] != '0':
                return True
        return False

    def get_faults_info(self, faults):
        info = ''
        color = ':'

        info = '%s%s' % (
            info,
            faults['crit']
        )
        color = '%s%s' % (
            color,
            ''.rjust(len(str(faults['crit'])), 'R')
        )

        info = '%s %s' % (
            info,
            faults['maj']
        )
        color = '%s.%s' % (
            color,
            ''.rjust(len(str(faults['maj'])), 'M')
        )

        info = '%s %s' % (
            info,
            faults['minor']
        )
        color = '%s.%s' % (
            color,
            ''.rjust(len(str(faults['minor'])), 'Y')
        )

        info = '%s %s' % (
            info,
            faults['warn']
        )
        color = '%s.%s' % (
            color,
            ''.rjust(len(str(faults['warn'])), 'G')
        )

        return color, info
