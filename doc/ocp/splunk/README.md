# Splunk Operator

The Splunk Operator for Kubernetes enables you to quickly and easily deploy Splunk Enterprise as explained in [Splunk documentation](https://splunk.github.io/splunk-operator/).

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp splunk | check the splunk operator and instances state | [Link](./get.md)
iserver set ocp splunk --mode operator | install splunk operator | [Link](./create_operator.md)
iserver set ocp splunk --mode instance | add splunk standalone instance | [Link](./create_instance.md)
iserver set ocp splunk --mode all | install splunk opertor and add splunk standalone instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp splunk --mode operator | delete splunk operator | [Link](./delete_operator.md)
iserver delete ocp splunk --mode instance | delete splunk standalone instance | [Link](./delete_instance.md)
iserver delete ocp splunk --mode all | delete splunk standalone instance and delete operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)