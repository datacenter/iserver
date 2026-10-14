# Splunk

[[Back]](../Operations.md)

![Logo](../images/splunk/logo.png) 

The Splunk Operator for Kubernetes enables you to quickly and easily deploy Splunk Enterprise.

## Knowledge Base

- [installation runbook](./kb/runbook.md)
- [official Splunk documentation](https://splunk.github.io/splunk-operator/)
- [official Splunk operator github](https://github.com/splunk/splunk-operator/blob/main/README.md)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp splunk | check the splunk operator and instances state | [Link](./get.md)
iserver set ocp splunk --mode operator | install splunk operator | [Link](./create_operator.md)
iserver set ocp splunk --mode instance | add splunk standalone instance | [Link](./create_instance.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp splunk --mode operator | delete splunk operator | [Link](./delete_operator.md)
iserver delete ocp splunk --mode instance | delete splunk standalone instance | [Link](./delete_instance.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)