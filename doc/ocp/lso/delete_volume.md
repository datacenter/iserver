# Local Storage - Delete volume

[[Back]](./README.md)

## Workflow

- delete local volume, local volume set and local volume discovery resources
- unlabel storage nodes

## Configurable options

```
# iserver delete ocp lso --mode volume
  --cluster TEXT                  Cluster Name
```

## Example

>[!NOTE]
>While the command is the same, the workflow and outputs depend on how volumes were created

Volumes create mode | Output 
--- | --- | ---
All-nodes with device discovery | [example](./delete_volume_all.md)
Selected nodes with device discovery | [example](./delete_volume_node.md)
Explicit nodes and devices | [example](./delete_volume_explicit.md)

[[Back]](./README.md)