from xml.dom import Node

# pylint: disable=assignment-from-no-return

class NetconfSSHLikeTransport():
    def __init__(self):
        self.buf = ""
        self.framing = 0
        self.eom_found = False
        self.trace = False

    def connect(self):
        # should be overridden by subclass
        pass

    def _send(self, buf):
        # should be overridden by subclass
        pass

    def _send_eom(self):
        # should be overridden by subclass
        pass

    def _flush(self):
        # should be overridden by subclass, if needed
        pass

    def _set_timeout(self, timeout=None):
        # should be overridden by subclass
        pass

    def _recv(self, bufsiz):
        # should be overridden by subclass
        pass

    def send(self, request):
        if self.framing == 1:
            self._send('\n#%d\n' % len(request) + request)
        else:
            self._send(request)

    def send_msg(self, request):
        self.send(request)
        self._send_eom()

    def send_eom(self):
        self._send_eom()

    def _get_eom(self):
        if self.framing == 0:
            return ']]>]]>'
        elif self.framing == 1:
            return '\n##\n'
        else:
            return ''

    def hello_msg(self, versions):
        body = '''<?xml version="1.0" encoding="UTF-8"?><hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"><capabilities>'''

        if '1.0' in versions:
            body += '<capability>urn:ietf:params:netconf:base:1.0</capability>'
        if '1.1' in versions:
            body += '<capability>urn:ietf:params:netconf:base:1.1</capability>\n'
        body += '''</capabilities></hello>'''
        return body

    def strip(self, node):
        """Remove empty text nodes, and non-element nodes.
        The result after strip () is a child list with non-empty text-nodes,
        and element nodes only."""
        child = node.firstChild
        while child is not None:
            remove = False
            if child.nodeType == Node.TEXT_NODE:
                if child.nodeValue.strip() == "":
                    remove = True
            else:
                if child.nodeType != Node.ELEMENT_NODE:
                    remove = True
            if remove:
                tmp = child.nextSibling
                node.removeChild(child)
                child.unlink()
                child = tmp
            else:
                child = child.nextSibling

    # ret: (-2, bytes) on framing error
    #      (-1, bytes) on socket EOF
    #      (0, "") on EOM
    #      (1, chunk-data) on data
    def recv_chunk(self, timeout=None):
        self._set_timeout(timeout)
        if self.framing == 0:
            if self.eom_found:
                self.eom_found = False
                return (0, "")
            bytes_value = self.buf
            self.buf = ""
            while len(bytes_value) < 6:
                x = self._recv(16384)
                if x == "":
                    return (-1, bytes_value)
                bytes_value += x.decode()
            idx = bytes_value.find("]]>]]>")
            if idx > -1:
                # eom marker found; store rest in buf
                self.eom_found = True
                self.buf = bytes_value[idx + 6:]
                return (1, bytes_value[:idx])
            else:
                # no eom marker found, keep the last 5 bytes_value
                # (might contain parts of the eom marker)
                self.buf = bytes_value[-5:]
                return (1, bytes_value[:-5])
        else:
            # new framing
            bytes_value = self.buf
            self.buf = ""
            # make sure we have at least 4 bytes_value; LF HASH INT/HASH LF
            while len(bytes_value) < 4:
                x = self._recv(16384)
                if x == "":
                    # error, return what we have
                    return (-1, bytes_value)
                bytes_value += x
            # check the first two bytes_value
            if bytes_value[0:2] != "\n#":
                # framing error
                return (-2, bytes_value)
            # read the chunk size
            sz = -1
            while sz == -1:
                # find the terminating LF
                idx = bytes_value.find("\n", 2)
                if idx > 12:
                    # framing error - too large integer or not correct
                    # chunk size specification
                    return (-2, bytes_value)
                if idx > -1:
                    # newline found, scan for number of bytes_value to read
                    try:
                        sz = int(bytes_value[2:idx])
                        if sz < 1 or sz > 4294967295:
                            # framing error - range error
                            return (-2, bytes_value)
                    except BaseException:
                        if bytes_value[2:idx] == "#":
                            # EOM
                            self.buf = bytes_value[idx + 1:]
                            return (0, "")
                        # framing error - not an integer, and not EOM
                        return (-2, bytes_value)
                    # skip the chunk size.  the while loop is now done
                    bytes_value = bytes_value[idx + 1:]
                else:
                    # terminating LF not found, read more
                    x = self._recv(16384)
                    if x == "":
                        # error, return what we have
                        return (-1, bytes_value)
                    bytes_value += x
            # read the chunk data
            while len(bytes_value) < sz:
                x = self._recv(16384)
                if x == "":
                    return (-1, bytes_value)
                bytes_value += x
            # save rest of data
            self.buf = bytes_value[sz:]
            return (1, bytes_value[:sz])

    def recv_msg(self, timeout=None):
        msg = ""
        while True:
            (code, bytes_value) = self.recv_chunk(timeout)
            if code == 1:
                msg += bytes_value
            elif code == 0:
                return msg
            else:
                # error
                return msg + bytes_value
