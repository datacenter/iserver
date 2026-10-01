# .bashrc

Check .bashrc settings on the cluster [management node](../ManagementServer.md)

## Workflow

- get .bashrc file

## Requirements

Cluster [connector](../Access.md) must be defined with management ip
Ssh access to management node must work

## Configurable options

```
# iserver get ocp cli-bashrc
  --cluster TEXT  OCP cluster name
```

## Example

```
# iserver get ocp cli-bashrc --cluster bm1 

OpenShift Workflow - CLI - Get .bashrc
======================================

OpenShift Cluster: bm1
Download /var/home/core/.bashrc
~~~
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

unset rc
~~~
```

[[Back]](./README.md)