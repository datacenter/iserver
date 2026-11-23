from lib import filter_helper
from lib import ip_helper


class K8sProxyNoproxy():
    def __init__(self):
        pass

    def match_noproxy(self, noproxy, value):
        if value in ['localhost', '.svc', '.cluster.local']:
            return False
        
        if ip_helper.is_valid_ipv4_address(noproxy):
            if not ip_helper.is_valid_ipv4_address(value) and not ip_helper.is_valid_ipv4_cidr(value):
                return False
                
            if ip_helper.is_valid_ipv4_address(value):
                if noproxy != value:
                    return False
                
                return True

            return ip_helper.is_ipv4_in_cidr(noproxy, value)
        
        if ip_helper.is_valid_ipv4_cidr(noproxy):
            if not ip_helper.is_valid_ipv4_cidr(value):
                return False
            
            return ip_helper.is_subnet_in_subnet(noproxy, value)
        
        if noproxy.endswith(value):
            return True
        
        return False

    def is_noproxy(self, value, my_output=None):
        if my_output is not None:
            my_output.default('Collecting proxy settings...', before_newline=True)

        proxy_mo = self.get_proxy('cluster', return_mo=True, cache_enabled=False)
        if proxy_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster proxy settings')
            return False

        if my_output is not None:
            my_output.default('Checkin noproxy match for [%s]' % (value), before_newline=True)

        current = filter_helper.get(proxy_mo, 'status:noProxy')
        if current is None:
            my_output.error('Failed to get cluster noProxy stata')
            return False

        configured = None
        for item in current.split(','):
            if self.match_noproxy(value, item):
                configured = item
                if my_output is not None:
                    my_output.default('- %s (%s)' % (item, my_output.add_color('match', 'Green')))
            else:
                my_output.default('- %s' % (item))

        if configured is None:
            if my_output is not None:
                my_output.default(
                    'noproxy [%s] currently %s' % (value, my_output.add_color('not configured', 'Red')),
                    before_newline=True
                )
            return False
        
        return True

    def add_noproxy(
            self, 
            no_proxy,
            confirmation=False, 
            my_output=None,
            wait=True
        ):
        proxy_mo = self.get_proxy('cluster', return_mo=True, cache_enabled=False)
        if proxy_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster proxy settings')
            return False

        current = filter_helper.get(proxy_mo, 'status:noProxy')
        if current is None:
            my_output.error('Failed to get cluster noProxy stata')
            return False

        target = '%s,%s' % (current, no_proxy)

        success = self.set_proxy(
            no_proxy=target,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
        return success
    