# ComputeMbPowerStats

## Managed Object

```
Managed Object			:	ComputeMbPowerStats
--------------
class_id                        :ComputeMbPowerStats
child_action                    :None
consumed_power                  :138.000000
consumed_power_avg              :139.800003
consumed_power_max              :144.000000
consumed_power_min              :138.000000
dn                              :sys/chassis-1/blade-1/board/power-stats
input_current                   :11.465603
input_current_avg               :11.615154
input_current_max               :11.964108
input_current_min               :11.465603
input_voltage                   :12.036000
input_voltage_avg               :12.036000
input_voltage_max               :12.036000
input_voltage_min               :12.036000
intervals                       :58982460
rn                              :power-stats
sacl                            :None
status                          :None
suspect                         :no
thresholded                     :
time_collected                  :2022-12-02T09:51:08.333
update                          :393226
```

## Properties

```
[2022-12-02 09:51:45.107775]	[debug_object]	[
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
    "consumed_power",
    "consumed_power_avg",
    "consumed_power_max",
    "consumed_power_min",
    "dirty_mask",
    "dn",
    "elem_create",
    "from_xml",
    "get_class_id",
    "get_handle",
    "input_current",
    "input_current_avg",
    "input_current_max",
    "input_current_min",
    "input_voltage",
    "input_voltage_avg",
    "input_voltage_max",
    "input_voltage_min",
    "intervals",
    "is_dirty",
    "make_rn",
    "mark_clean",
    "mark_dirty",
    "mo_meta",
    "naming_props",
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
[2022-12-02 09:51:45.108745]	[debug_object]	[ComputeBoard]
[ComputeExtBoard]
  |-ComputeMbPowerStats
     |-ComputeMbPowerStatsHist

ClassId                         ComputeMbPowerStats
-------                         -------------------
xml_attribute                   :computeMbPowerStats
rn                              :power-stats
min_version                     :1.1(1j)
access                          :OutputOnly
access_privilege                :['admin', 'operations', 'read-only']
parents                         :['computeBoard', 'computeExtBoard']
children                        :['computeMbPowerStatsHist']

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

Property                        consumed_power
--------                        --------------
xml_attribute                   :consumedPower
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        consumed_power_avg
--------                        ------------------
xml_attribute                   :consumedPowerAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        consumed_power_max
--------                        ------------------
xml_attribute                   :consumedPowerMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        consumed_power_min
--------                        ------------------
xml_attribute                   :consumedPowerMin
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

Property                        input_current
--------                        -------------
xml_attribute                   :inputCurrent
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_current_avg
--------                        -----------------
xml_attribute                   :inputCurrentAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_current_max
--------                        -----------------
xml_attribute                   :inputCurrentMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_current_min
--------                        -----------------
xml_attribute                   :inputCurrentMin
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_voltage
--------                        -------------
xml_attribute                   :inputVoltage
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_voltage_avg
--------                        -----------------
xml_attribute                   :inputVoltageAvg
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_voltage_max
--------                        -----------------
xml_attribute                   :inputVoltageMax
field_type                      :float
min_version                     :1.1(1j)
access                          :READ_ONLY
min_length                      :None
max_length                      :None
pattern                         :None
value_set                       :[]
range_val                       :[]

Property                        input_voltage_min
--------                        -----------------
xml_attribute                   :inputVoltageMin
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