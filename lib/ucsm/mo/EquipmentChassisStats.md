# EquipmentChassisStats

## Managed Object

```
Managed Object			:	EquipmentChassisStats
--------------
class_id                        :EquipmentChassisStats
chassis_i2_c_errors             :0
chassis_i2_c_errors_avg         :0
chassis_i2_c_errors_max         :0
chassis_i2_c_errors_min         :0
child_action                    :None
dn                              :sys/chassis-1/stats
input_power                     :1128.000000
input_power_avg                 :1128.000000
input_power_max                 :1152.000000
input_power_min                 :1104.000000
intervals                       :58982460
output_power                    :851.000000
output_power_avg                :852.533386
output_power_max                :920.000000
output_power_min                :782.000000
rn                              :stats
sacl                            :None
status                          :None
suspect                         :no
thresholded                     :
time_collected                  :2022-12-02T09:10:56.165
update                          :131072
```

## Properties

```
[2022-12-02 09:11:21.201192]	[debug_object]	[
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
    "chassis_i2_c_errors",
    "chassis_i2_c_errors_avg",
    "chassis_i2_c_errors_max",
    "chassis_i2_c_errors_min",
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
    "dirty_mask",
    "dn",
    "elem_create",
    "from_xml",
    "get_class_id",
    "get_handle",
    "input_power",
    "input_power_avg",
    "input_power_max",
    "input_power_min",
    "intervals",
    "is_dirty",
    "make_rn",
    "mark_clean",
    "mark_dirty",
    "mo_meta",
    "naming_props",
    "output_power",
    "output_power_avg",
    "output_power_max",
    "output_power_min",
    "parent_mo",
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
    "write_object"
]
```

## Meta

```
[2022-12-02 09:11:21.202198]	[debug_object]	[EquipmentChassis]
  |-EquipmentChassisStats
     |-EquipmentChassisStatsHist

ClassId                         EquipmentChassisStats
-------                         ---------------------
xml_attribute                   :equipmentChassisStats
rn                              :stats
min_version                     :1.1(1j)
access                          :OutputOnly
access_privilege                :['admin', 'operations', 'read-only']
parents                         :['equipmentChassis']
children                        :['equipmentChassisStatsHist']

Property                        chassis_i2_c_errors
--------                        -------------------
xml_attribute                   :ChassisI2CErrors
field_type                      :ulong
min_version                     :2.2(6c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_avg
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsAvg
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_max
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsMax
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_min
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsMin
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

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

Property                        input_power
--------                        -----------
xml_attribute                   :inputPower
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_avg
--------                        ---------------
xml_attribute                   :inputPowerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_max
--------                        ---------------
xml_attribute                   :inputPowerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_min
--------                        ---------------
xml_attribute                   :inputPowerMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
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

Property                        output_power
--------                        ------------
xml_attribute                   :outputPower
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_avg
--------                        ----------------
xml_attribute                   :outputPowerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_max
--------                        ----------------
xml_attribute                   :outputPowerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_min
--------                        ----------------
xml_attribute                   :outputPowerMin
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

[2022-12-02 09:11:21.203187]	[debug_object]
Managed Object			:	EquipmentChassisStats
--------------
class_id                        :EquipmentChassisStats
chassis_i2_c_errors             :0
chassis_i2_c_errors_avg         :0
chassis_i2_c_errors_max         :0
chassis_i2_c_errors_min         :0
child_action                    :None
dn                              :sys/chassis-2/stats
input_power                     :1416.000000
input_power_avg                 :1425.230713
input_power_max                 :1488.000000
input_power_min                 :1392.000000
intervals                       :58982460
output_power                    :1058.000000
output_power_avg                :1240.230835
output_power_max                :1472.000000
output_power_min                :1058.000000
rn                              :stats
sacl                            :None
status                          :None
suspect                         :no
thresholded                     :
time_collected                  :2022-12-02T09:10:59.170
update                          :65549


[2022-12-02 09:11:21.204186]	[debug_object]	[
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
    "chassis_i2_c_errors",
    "chassis_i2_c_errors_avg",
    "chassis_i2_c_errors_max",
    "chassis_i2_c_errors_min",
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
    "dirty_mask",
    "dn",
    "elem_create",
    "from_xml",
    "get_class_id",
    "get_handle",
    "input_power",
    "input_power_avg",
    "input_power_max",
    "input_power_min",
    "intervals",
    "is_dirty",
    "make_rn",
    "mark_clean",
    "mark_dirty",
    "mo_meta",
    "naming_props",
    "output_power",
    "output_power_avg",
    "output_power_max",
    "output_power_min",
    "parent_mo",
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
    "write_object"
]
[2022-12-02 09:11:21.205183]	[debug_object]	[EquipmentChassis]
  |-EquipmentChassisStats
     |-EquipmentChassisStatsHist

ClassId                         EquipmentChassisStats
-------                         ---------------------
xml_attribute                   :equipmentChassisStats
rn                              :stats
min_version                     :1.1(1j)
access                          :OutputOnly
access_privilege                :['admin', 'operations', 'read-only']
parents                         :['equipmentChassis']
children                        :['equipmentChassisStatsHist']

Property                        chassis_i2_c_errors
--------                        -------------------
xml_attribute                   :ChassisI2CErrors
field_type                      :ulong
min_version                     :2.2(6c)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_avg
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsAvg
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_max
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsMax
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        chassis_i2_c_errors_min
--------                        -----------------------
xml_attribute                   :ChassisI2CErrorsMin
field_type                      :ulong
min_version                     :2.2(7b)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

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

Property                        input_power
--------                        -----------
xml_attribute                   :inputPower
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_avg
--------                        ---------------
xml_attribute                   :inputPowerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_max
--------                        ---------------
xml_attribute                   :inputPowerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_power_min
--------                        ---------------
xml_attribute                   :inputPowerMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
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

Property                        output_power
--------                        ------------
xml_attribute                   :outputPower
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_avg
--------                        ----------------
xml_attribute                   :outputPowerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_max
--------                        ----------------
xml_attribute                   :outputPowerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        output_power_min
--------                        ----------------
xml_attribute                   :outputPowerMin
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

```
