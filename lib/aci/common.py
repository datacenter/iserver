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
        # "childAction": "",
        # "crit": "0",
        # "critAcked": "0",
        # "critAckedandDelegated": "0",
        # "critDelegated": "0",
        # "maj": "0",
        # "majAcked": "0",
        # "majAckedandDelegated": "0",
        # "majDelegated": "0",
        # "minor": "0",
        # "minorAcked": "0",
        # "minorAckedandDelegated": "0",
        # "minorDelegated": "0",
        # "rn": "fltCnts",
        # "status": "",
        # "warn": "0",
        # "warnAcked": "0",
        # "warnAckedandDelegated": "0",
        # "warnDelegated": "0"

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
