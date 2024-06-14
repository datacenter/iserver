import os
import re
import socket
import struct
import hashlib
import uuid
import requests
import validators
import sshpubkeys


def generate_uuid(seed):
    md5_handler = hashlib.md5()
    md5_handler.update(seed.encode('utf-8'))
    return str(uuid.UUID(md5_handler.hexdigest()))


def normalize_mac_address(mac_address):
    return mac_address.lower().replace(':', '').replace('.', '')


def is_mac_address(mac):
    mac = normalize_mac_address(mac)
    if len(mac) != 12:
        return False

    for char in mac:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            return False

    return True


def is_mac_equal(mac_a, mac_b):
    if normalize_mac_address(mac_a) == normalize_mac_address(mac_b):
        return True
    return False


def is_mac_match(mac_a, mac_b):
    mac_a = mac_a.replace(':', '').lower()
    mac_b = mac_b.replace(':', '').replace('.', '').lower()
    if mac_a in mac_b:
        return True
    return False


def is_valid_mac_address(address, mac_address_format='colon'):
    try:
        if mac_address_format == 'colon':
            if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", address.lower()):
                return True
        if mac_address_format == 'dotted':
            if re.match("[0-9a-f]{4}([.]?)[0-9a-f]{4}([.]?)[0-9a-f]{4}$", address.lower()):
                return True
    except BaseException:
        pass
    return False


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    except BaseException:
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def is_valid_ipv6_cidr(cidr):
    valid = False
    try:
        network, net_bits = cidr.split('/')
        if is_valid_ipv6_address(network) and int(net_bits) < 129 and int(net_bits) > 8:
            valid = True
    except BaseException:
        pass

    return valid


def is_valid_ipv4_cidr(cidr):
    valid = False
    try:
        if cidr == '0.0.0.0/0':
            return True

        network, net_bits = cidr.split('/')
        if is_valid_ipv4_address(network) and int(
                net_bits) < 33 and int(net_bits) >= 8:
            valid = True
    except BaseException:
        pass

    return valid


def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask


def netmask_to_prefix(mask):
    try:
        prefix = sum(bin(int(x)).count('1') for x in mask.split('.'))
        return prefix
    except BaseException:
        return None


def prefix_to_netmask(prefix):
    host_bits = 32 - prefix
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return netmask


def ipv4_to_int(address):
    return struct.unpack('>L', socket.inet_aton(address))[0]


def is_ipv4_in_cidr(address, cidr):
    if not is_valid_ipv4_address(address):
        return False

    netaddr, bits = cidr.split('/')
    if not is_valid_ipv4_address(netaddr):
        return False
    if int(bits) < 8 or int(bits) > 32:
        return False

    ip_address = struct.unpack('>L', socket.inet_aton(address))[0]
    ip_address_cidr = ip_address & (4294967295 << (32 - int(bits)))
    ip_network = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    ip_network_cidr = ip_network & (4294967295 << (32 - int(bits)))

    return ip_address_cidr == ip_network_cidr


def get_network_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')

    if not is_valid_ipv4_address(netaddr):
        return None
    if int(bits) < 8 or int(bits) > 32:
        return None

    ip_network = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    ip_network_cidr = ip_network & (4294967295 << (32 - int(bits)))

    return socket.inet_ntoa(struct.pack('>L', ip_network_cidr))


def get_first_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')
    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + 1
    return socket.inet_ntoa(struct.pack('>L', address))


def get_nth_ipv4_in_cidr(cidr, index):
    if not is_valid_ipv4_cidr(cidr):
        return None

    size = get_ipv4_cidr_size(cidr)
    if size is None:
        return None

    if index >= size:
        return None

    netaddr, bits = cidr.split('/')
    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + index
    return socket.inet_ntoa(struct.pack('>L', address))


def get_last_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')
    if netaddr == '0.0.0.0':
        return '0.0.0.0'

    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + 2**(32 - int(bits)) - 2
    return socket.inet_ntoa(struct.pack('>L', address))


def get_ipv4_cidr_size(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None
    netaddr, bits = cidr.split('/')
    return 2**(32 - int(bits)) - 2


def get_nth_ipv4_from_address(address, index):
    if not is_valid_ipv4_address(address):
        return None

    numeric_address = struct.unpack('>L', socket.inet_aton(address))[0]
    numeric_address = numeric_address + index
    return socket.inet_ntoa(struct.pack('>L', numeric_address))


def get_ipv4_addresses_in_range(start_address, end_address):
    if not is_valid_ipv4_address(start_address):
        return None

    if len(end_address.split('.')) == 4:
        if not is_valid_ipv4_address(end_address):
            return None
    else:
        end_address_octets = len(end_address.split('.'))
        start_address_octets = 4 - end_address_octets
        octets = start_address.split('.')[:start_address_octets] + end_address.split('.')
        end_address = '.'.join(octets)

        if not is_valid_ipv4_address(end_address):
            return None

    addresses = [start_address]
    while True:
        start_address = get_next_ipv4_address(start_address)
        addresses.append(start_address)
        if start_address == end_address:
            break

    return addresses


def get_ipv4_address_count(start_address, end_address):
    if not is_valid_ipv4_address(start_address):
        return None

    if not is_valid_ipv4_address(end_address):
        return None

    numeric_start_address = struct.unpack('>L', socket.inet_aton(start_address))[0]
    numeric_end_address = struct.unpack('>L', socket.inet_aton(end_address))[0]
    if numeric_end_address < numeric_start_address:
        return None

    count = numeric_end_address - numeric_start_address + 1

    return count


def get_lower_ipv4(ip_a, ip_b):
    if not is_valid_ipv4_address(ip_a):
        return None

    if not is_valid_ipv4_address(ip_b):
        return None

    numeric_address_a = struct.unpack('>L', socket.inet_aton(ip_a))[0]
    numeric_address_b = struct.unpack('>L', socket.inet_aton(ip_b))[0]

    if numeric_address_a < numeric_address_b:
        return ip_a

    return ip_b


def is_subnet_in_subnet(subnet_a, subnet_b):
    if not is_valid_ipv4_cidr(subnet_a):
        return False

    if not is_valid_ipv4_cidr(subnet_b):
        return False

    subnet_a = '%s/%s' % (
        get_network_ipv4_in_cidr(subnet_a),
        subnet_a.split('/')[1]
    )
    subnet_b = '%s/%s' % (
        get_network_ipv4_in_cidr(subnet_b),
        subnet_b.split('/')[1]
    )

    subnet_a_min = get_first_ipv4_in_cidr(subnet_a)
    subnet_a_max = get_last_ipv4_in_cidr(subnet_a)
    subnet_b_min = get_first_ipv4_in_cidr(subnet_b)
    subnet_b_max = get_last_ipv4_in_cidr(subnet_b)
    if get_lower_ipv4(subnet_a_min, subnet_b_min) == subnet_b_min:
        if get_lower_ipv4(subnet_a_max, subnet_b_max) == subnet_a_max:
            return True

    return False


def get_next_ipv4_address(ip_address):
    return get_nth_ipv4_from_address(ip_address, 1)


def is_url_valid(value):
    return validators.url(value)


def is_url_accessible(url, timeout=1):
    try:
        if len(url.split(' ')) > 1:
            return False
        handler = requests.head(url, timeout=timeout)
        if 'Content-Type' in handler.headers:
            return True
    except BaseException:
        pass
    return False


def download_url(url, filename, timeout=5):
    try:
        response = requests.get(
            url,
            timeout=timeout
        )
        with open(filename, "wb") as file_handler:
            file_handler.write(response.content)
    except BaseException:
        return None
    return filename


def is_public_key_valid(value):
    ssh = sshpubkeys.SSHKey(value, strict=True)
    try:
        ssh.parse()
    except BaseException:
        return False
    return True


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return None
    hasher = hashlib.md5()
    blocksize = 65536
    with open(filename, 'rb') as file_handler:
        buf = file_handler.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file_handler.read(blocksize)
    md5 = hasher.hexdigest()
    return md5


def get_ip(name):
    try:
        ip_address = socket.gethostbyname(name)
    except BaseException:
        return None
    return ip_address


def get_string_ipv4s(line):
    ips = []
    candidates = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
    for candidate in candidates:
        if is_valid_ipv4_address(candidate):
            ips.append(
                candidate
            )
    return ips


def get_obscured_ipv4(address, allow_private_lead=True):
    if not is_valid_ipv4_address(address):
        return None

    octets = address.split('.')
    new_octets = []
    for octet in octets:
        new_octets.append(
            '*' * len(octet)
        )

    if allow_private_lead:
        if octets[0] in ['10', '172', '192']:
            new_octets[0] = octets[0]

    return '.'.join(new_octets)


def get_string_macs_colon(line):
    macs = []
    candidates = re.findall(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', line, re.IGNORECASE)
    for candidate in candidates:
        if is_valid_mac_address(candidate, mac_address_format='colon'):
            macs.append(
                candidate
            )
    return macs


def get_string_macs_dotted(line):
    macs = []
    candidates = re.findall(r'([0-9a-f]{4}(?:.[0-9a-f]{4}){2})', line, re.IGNORECASE)
    for candidate in candidates:
        if is_valid_mac_address(candidate, mac_address_format='dotted'):
            macs.append(
                candidate
            )
    return macs


def get_string_macs(line):
    macs = []
    macs = macs + get_string_macs_colon(line)
    macs = macs + get_string_macs_dotted(line)
    return macs


def get_obscured_mac(address):
    if is_valid_mac_address(address, mac_address_format='colon'):
        return '**:**:**:**:**:**'

    if is_valid_mac_address(address, mac_address_format='dotted'):
        return '****.****.****'

    return None
