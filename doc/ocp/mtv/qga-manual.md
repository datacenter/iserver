# QEMU Guest Agent Manual Installation

## RHEL/Fedora/CentOS

Step: install

```
$ sudo yum install -y qemu-guest-agent
```

Step: enable

```
$ sudo systemctl enable --now qemu-guest-agent
```

## Debian/Ubuntu

Step: install

```
$ sudo apt-get install -y qemu-guest-agent
```

Step: enable

```
$ sudo systemctl enable --now qemu-guest-agent
```

[[Back]](./README.md)