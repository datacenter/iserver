import time
import traceback

from lib.netconf import ssh
from lib import log_helper


class NetconfNotification():
    def __init__(self, netconf_ip, netconf_port, netconf_username, netconf_password, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

        self.netconf_ip = netconf_ip
        self.netconf_port = netconf_port
        self.netconf_username = netconf_username
        self.netconf_password = netconf_password

        self.netconf_handler = ssh.NetconfSsh(
            self.netconf_ip,
            self.netconf_port,
            self.netconf_username,
            self.netconf_password
        )

    def is_working(self):
        if self.netconf_handler.connect():
            self.netconf_handler.disconnect()
            return True
        return False

    def is_stream(self, stream):
        msg = '''<?xml version="1.0" encoding="UTF-8"?>
        <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
          <create-subscription xmlns=
            "urn:ietf:params:xml:ns:netconf:notification:1.0">
            <stream>%s</stream>
          </create-subscription>
        </rpc>''' % stream

        try:
            if self.netconf_handler.connect():
                success, xmlint = self.netconf_handler.hello()
                if not success:
                    self.netconf_handler.disconnect()
                    return False

                self.netconf_handler.send_msg(msg)
                ret = self.netconf_handler.recv_msg(timeout=3)
                self.netconf_handler.disconnect()

                if ret is None:
                    self.log.error('is_stream', 'No message received')
                    return False

                self.log.debug('is_stream', ret)
                if 'no such stream' in ret:
                    return False

        except BaseException:
            self.log.error('is_stream', traceback.format_exc())
            return False

        return True

    def get_notifications(self, stream, timeout=60):
        msg = '''<?xml version="1.0" encoding="UTF-8"?>
        <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
          <create-subscription xmlns=
            "urn:ietf:params:xml:ns:netconf:notification:1.0">
            <stream>%s</stream>
          </create-subscription>
        </rpc>''' % stream

        try:
            if self.netconf_handler.connect():
                success, xmlint = self.netconf_handler.hello()
                if not success:
                    self.netconf_handler.disconnect()
                    return False

                start_time = int(time.time())
                while True:
                    if msg is not None:
                        self.netconf_handler.send_msg(msg)
                        msg = None

                    while True:
                        try:
                            (code, chunk) = self.netconf_handler.recv_chunk(timeout=5)
                            print(code)
                            print(chunk)
                        except BaseException:
                            print('timeout')

                        if int(time.time()) - start_time > timeout:
                            break

                    if int(time.time()) - start_time > timeout:
                        break

        except BaseException:
            self.log.error('get_notifications', traceback.format_exc())
            return

        self.netconf_handler.disconnect()
