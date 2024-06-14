import sys
import base64
import socket
import xml.dom.minidom
import paramiko
import traceback

from lib.netconf.transport import NetconfSSHLikeTransport


class NetconfSsh(NetconfSSHLikeTransport):
    def __init__(
        self,
        hostname,
        port,
        username,
        password,
        private_key=None,
        public_key_type=None,
        private_key_file='',
        private_key_type=''
    ):
        NetconfSSHLikeTransport.__init__(self)
        self.hostname = str(hostname)
        self.port = int(port)

        self.private_key_file = private_key_file
        self.private_key_type = private_key_type
        self.public_key = private_key
        self.public_key_type = public_key_type
        self.password = password
        self.username = username
        self.saved = ""
        self.ssh = None
        self.chan = None

    def _send(self, buf):
        try:
            #            self.chan.sendall(buf)
            #            return
            if self.saved:
                buf = self.saved + buf
            # sending too little data in each SSH packet makes the
            # transfer slow.
            # paramiko still has  bug (?) where it doesn't send a full
            # SSH message, but keeps 64 bytes.  so we will send MAX-64, 64,
            # MAX-64, 64, ... instead of MAX all the time.
            if len(buf) < 16384:
                self.saved = buf
            else:
                self.chan.sendall(buf[:16384])
                self.saved = buf[16384:]
        except socket.error as x:
            print('socket error:', str(x))

    def _send_eom(self):
        try:
            self.chan.sendall(self.saved + self._get_eom())
            self.saved = ""
        except socket.error as x:
            self.saved = ""
            print('socket error:', str(x))

    def _flush(self):
        try:
            self.chan.sendall(self.saved)
            self.saved = ""
        except socket.error as x:
            self.saved = ""
            print('socket error:', str(x))

    def _recv(self, bufsiz):
        s = self.chan.recv(bufsiz)
        if self.trace:
            sys.stdout.write(s)
            sys.stdout.flush()
        return s

    def _set_timeout(self, timeout=None):
        self.chan.settimeout(timeout)

    def create_connection(self, host, port):
        sock_err = None
        sock = None
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                sock = socket.socket(af, socktype, proto)
            except socket.error as err:
                sock_err = err
                sock = None
                continue
            try:
                sock.connect(sa)
            except socket.error as err:
                sock_err = err
                sock.close()
                sock = None
                continue
            break

        if sock is None:
            print("Failed to connect to %s: %s" % (host, str(sock_err)))
            return None

        return sock

    def connect(self):
        sock = self.create_connection(self.hostname, self.port)
        if sock is None:
            return False

        self.ssh = paramiko.Transport(sock)

        if self.public_key_type is None:
            agent_public_key = None
        else:
            if self.public_key_type == 'rsa':
                # TODO: The decodestring method is deprecated in python3
                agent_public_key = paramiko.RSAKey(
                    data=base64.decodestring(self.private_key))
            elif self.public_key_type == 'dss':
                # TODO: The decodestring method is deprecated in python3
                agent_public_key = paramiko.DSSKey(
                    data=base64.decodestring(self.private_key))

        if not self.private_key_file == '':
            if self.private_key_type == "rsa":
                user_private_key = paramiko.RSAKey.from_private_key_file(
                    self.private_key_file)
            else:
                user_private_key = paramiko.DSSKey.from_private_key_file(
                    self.private_key_file)

            try:
                self.ssh.connect(hostkey=agent_public_key,
                                 username=self.username,
                                 pkey=user_private_key)
            except paramiko.AuthenticationException:
                print("Authentication failed.")
                return False

        else:
            try:
                self.ssh.connect(hostkey=agent_public_key,
                                 username=self.username,
                                 password=self.password)
            except paramiko.AuthenticationException:
                print("Authentication failed.")
                return False

        self.chan = self.ssh.open_session()
        self.chan.invoke_subsystem("netconf")

        return True

    def hello(self):
        try:
            # figure out which versions to advertise
            versions = []
            versions.append('1.0')

            # hello exchange
            self.send_msg(self.hello_msg(versions))
            hello_reply = self.recv_msg()

            # parse the hello message to figure out which framing
            # protocol to use
            item = xml.dom.minidom.parseString(hello_reply)
            if item is not None:
                item = item.firstChild

            if item is not None:
                self.strip(item)
                if (item.namespaceURI == 'urn:ietf:params:xml:ns:netconf:base:1.0' and item.localName == 'hello' and item.firstChild is not None):
                    item = item.firstChild
                    self.strip(item)
                    if (item.namespaceURI == 'urn:ietf:params:xml:ns:netconf:base:1.0' and item.localName == 'capabilities'):
                        item = item.firstChild
                        self.strip(item)
                        while (item is not None):
                            if (item.namespaceURI == 'urn:ietf:params:xml:ns:netconf:base:1.0' and item.localName == 'capability'):
                                if ('1.1' in versions and item.firstChild.nodeValue.strip() == 'urn:ietf:params:netconf:base:1.1'):
                                    item.framing = 1
                            item = item.nextSibling

            xmllint = "xmllint --format - "
            success = True

        except BaseException:
            print(traceback.format_exc())
            success = False
            xmllint = None

        return success, xmllint

    def disconnect(self):
        self.ssh.close()
        self.ssh = None
        self.chan = None
        return True
