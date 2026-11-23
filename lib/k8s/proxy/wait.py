import time
from lib import filter_helper


class K8sProxyWait():
    def __init__(self):
        pass
    
    def wait_proxy_status(
            self, 
            http_proxy=None,
            https_proxy=None,
            no_proxy=None,
            my_output=None,
            max_time=360,
            log_error_on_timeout=True
        ):
        if my_output is not None:
            my_output.default('Wait proxy status', before_newline=True)
            if http_proxy is not None:
                my_output.default('- http proxy: %s' % (http_proxy))
            if https_proxy is not None:
                my_output.default('- https proxy: %s' % (https_proxy))
            if no_proxy is not None:
                my_output.default('- no proxy: %s' % (no_proxy))
        
        start_time = int(time.time())
        while True:
            proxy_mo = self.get_proxy('cluster', return_mo=True, cache_enabled=False)
            if proxy_mo is None:
                status_reached = False

            if proxy_mo is not None:
                status_reached = True

                if http_proxy is not None:
                    if not filter_helper.match_string(http_proxy, filter_helper.get(proxy_mo, 'status:httpProxy')):
                        status_reached = False

                if https_proxy is not None:
                    if not filter_helper.match_string(https_proxy, filter_helper.get(proxy_mo, 'status:httpsProxy')):
                        status_reached = False

                if no_proxy is not None:
                    no_proxy_status = filter_helper.get(proxy_mo, 'status:noProxy', on_error='', on_none='')
                    for item in no_proxy.split(','):
                        if item not in no_proxy_status.split(','):
                            status_reached = False

            if status_reached:
                return True
            
            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_proxy_status',
                        'Max time reached'
                    )

                if my_output is not None:
                    my_output.error('timed out')

                return False

            time.sleep(5)
