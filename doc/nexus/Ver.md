# Software and Hardware Version

## Sample output

```
# iserver get nx ver --device dom:milan

Device: ipn11,ipn12,ipn13,ipn14,ipn21,ipn22,ipn25,ipn26

Version [#8]
------------

+--------+-------------------------------+---------------------------------------+--------+
| Device | HW                            | CPU                                   | SW     |
+--------+-------------------------------+---------------------------------------+--------+
| ipn11  | Nexus9000 C9336C-FX2 Chassis  | Intel(R) Xeon(R) CPU D-1526 @ 1.80GHz | 9.3(9) | 
| ipn12  | Nexus9000 C9336C-FX2 Chassis  | Intel(R) Xeon(R) CPU D-1526 @ 1.80GHz | 9.3(9) | 
| ipn13  | Nexus9000 C9372PX chassis     | Intel(R) Core(TM) i3- CPU @ 2.50GHz   | 9.3(9) | 
| ipn14  | Nexus9000 C9372PX chassis     | Intel(R) Core(TM) i3- CPU @ 2.50GHz   | 9.3(9) | 
| ipn21  | Nexus9000 C93180YC-EX chassis | Intel(R) Xeon(R) CPU  @ 1.80GHz       | 9.3(9) | 
| ipn22  | Nexus9000 C93180YC-EX chassis | Intel(R) Xeon(R) CPU  @ 1.80GHz       | 9.3(9) | 
| ipn25  | Nexus9000 C9372PX chassis     | Intel(R) Core(TM) i3- CPU @ 2.50GHz   | 9.3(9) | 
| ipn26  | Nexus9000 C9372PX chassis     | Intel(R) Core(TM) i3- CPU @ 2.50GHz   | 9.3(9) | 
+--------+-------------------------------+---------------------------------------+--------+

Filter: --
View:   state (def)
```

## Command syntax

```
# iserver get nx ver --help

Usage: iserver.py get nx ver [OPTIONS]

  Get version

Options:
  --device TEXT                Device name
  --ip TEXT                    Device IP
  --username TEXT              Device Username
  --password TEXT              Device Password
  -v, --view TEXT              [state]  [default: state]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 44 ms and logs saved in /tmp/iserver\0f9c44db9ddc
```

[[Back]](./README.md)