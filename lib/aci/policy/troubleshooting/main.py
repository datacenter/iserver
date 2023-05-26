from lib.aci.policy.troubleshooting.span.main import PolicyTroubleshootingSpan


class PolicyTroubleshooting(PolicyTroubleshootingSpan):
    def __init__(self, log_id=None):
        PolicyTroubleshootingSpan.__init__(self, log_id=log_id)
