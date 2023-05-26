from lib import log_helper


class PolicySwitch():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
