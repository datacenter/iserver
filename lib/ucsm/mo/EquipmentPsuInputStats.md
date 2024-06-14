# EquipmentPsuInputStats

## Managed Object

```
Managed Object			:	EquipmentPsuInputStats
--------------
class_id                        :EquipmentPsuInputStats
child_action                    :None
current                         :0.421875
current_avg                     :0.423438
current_max                     :0.429688
current_min                     :0.421875
dn                              :sys/switch-A/psu-2/input-stats
input_status                    :ok
intervals                       :58982460
power                           :95.765625
power_avg                       :96.310173
power_max                       :97.754021
power_min                       :95.765625
rn                              :input-stats
sacl                            :None
status                          :None
suspect                         :no
thresholded                     :
time_collected                  :2022-12-01T19:53:23.943
update                          :131082
voltage                         :227.000000
voltage_avg                     :227.449997
voltage_max                     :228.500000
voltage_min                     :226.500000
```

## Properties

```
[2022-12-01 19:53:41.317507]	[debug_object]	[
    "DUMMY_DIRTY",
    "_ManagedObject__internal_prop",
    "_ManagedObject__parent_dn",
    "_ManagedObject__parent_mo",
    "_ManagedObject__set_prop",
    "_ManagedObject__status",
    "_ManagedObject__xtra_props",
    "_ManagedObject__xtra_props_dirty_mask",
    "__class__",
    "__deepcopy__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__json__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "_child",
    "_class_id",
    "_dirty_mask",
    "_dn_set",
    "_handle",
    "_is_unknown_property",
    "_rn_set",
    "_set_child_of_parent_mo",
    "_set_mo_prop_value",
    "_set_parent_mo_or_dn",
    "attr_get",
    "attr_set",
    "check_prop_match",
    "child",
    "child_action",
    "child_add",
    "child_count",
    "child_is_dirty",
    "child_mark_clean",
    "child_remove",
    "child_to_xml",
    "clone",
    "consts",
    "current",
    "current_avg",
    "current_max",
    "current_min",
    "dirty_mask",
    "dn",
    "elem_create",
    "from_xml",
    "get_class_id",
    "get_handle",
    "input_status",
    "intervals",
    "is_dirty",
    "make_rn",
    "mark_clean",
    "mark_dirty",
    "mo_meta",
    "naming_props",
    "parent_mo",
    "power",
    "power_avg",
    "power_max",
    "power_min",
    "prop_map",
    "prop_meta",
    "rn",
    "rn_get_special_case",
    "rn_is_special_case",
    "sacl",
    "set_prop_multiple",
    "show_hierarchy",
    "show_tree",
    "status",
    "suspect",
    "sync_mo",
    "thresholded",
    "time_collected",
    "to_xml",
    "update",
    "voltage",
    "voltage_avg",
    "voltage_max",
    "voltage_min",
    "write_object"
]
```

## Meta

```
[2022-12-01 19:53:41.319501]	[debug_object]	[EquipmentPsu]
  |-EquipmentPsuInputStats
     |-EquipmentPsuInputStatsHist

ClassId                         EquipmentPsuInputStats
-------                         ----------------------
xml_attribute                   :equipmentPsuInputStats
rn                              :input-stats
min_version                     :1.1(1j)
access                          :OutputOnly
access_privilege                :['admin', 'operations', 'read-only']
parents                         :['equipmentPsu']
children                        :['equipmentPsuInputStatsHist']

Property                        child_action
--------                        ------------
xml_attribute                   :childAction
field_type                      :string
min_version                     :1.1(1j)
access                          :INTERNAL
min_length                      :None
max_length                      :None
pattern                         :((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}
value_set                       :[]
range_val                       :[]

Property                        current
--------                        -------
xml_attribute                   :current
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        current_avg
--------                        -----------
xml_attribute                   :currentAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        current_max
--------                        -----------
xml_attribute                   :currentMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        current_min
--------                        -----------
xml_attribute                   :currentMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        dn
--------                        --
xml_attribute                   :dn
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_status
--------                        ------------
xml_attribute                   :inputStatus
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :0
max_length                      :510
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        intervals
--------                        ---------
xml_attribute                   :intervals
field_type                      :uint
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        power
--------                        -----
xml_attribute                   :power
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        power_avg
--------                        ---------
xml_attribute                   :powerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        power_max
--------                        ---------
xml_attribute                   :powerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        power_min
--------                        ---------
xml_attribute                   :powerMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        rn
--------                        --
xml_attribute                   :rn
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :0
max_length                      :256
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        sacl
--------                        ----
xml_attribute                   :sacl
field_type                      :string
min_version                     :3.0(2c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}
value_set                       :[]
range_val                       :[]

Property                        status
--------                        ------
xml_attribute                   :status
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_WRITE
min_length                      :None
max_length                      :None
pattern                         :((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}
value_set                       :[]
range_val                       :[]

Property                        suspect
--------                        -------
xml_attribute                   :suspect
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :['false', 'no', 'true', 'yes']
range_val                       :[]

Property                        thresholded
--------                        -----------
xml_attribute                   :thresholded
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        time_collected
--------                        --------------
xml_attribute                   :timeCollected
field_type                      :string
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}
value_set                       :[]
range_val                       :[]

Property                        update
--------                        ------
xml_attribute                   :update
field_type                      :uint
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        voltage
--------                        -------
xml_attribute                   :voltage
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        voltage_avg
--------                        -----------
xml_attribute                   :voltageAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        voltage_max
--------                        -----------
xml_attribute                   :voltageMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        voltage_min
--------                        -----------
xml_attribute                   :voltageMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]
```