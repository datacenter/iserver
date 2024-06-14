create ocp vm
	support day0 with cm

get helm
	chart
	release
		support day0 with cm

get nso
		cnfm
			-v state (def)
				add k8s events tick notifications
				change cluster count to cluster names
				maybe remove cnfi count as it is cluster specific
			-v notification  (incl live)?
			-v k8s (pod, service state, pvc)
			-v ... (how cnfm has been started - helm chart values)
			-v ... local chart list
			-v ... logs incl. live?

		chart
			-v list (def) - based on the option of either local cnfm or proper repository
			-v ... - get the values, helm details, test options i.e. how would the files look if they were deployed with def values or user-defined values
			-v ... - timestamps of files (?)
			-v ... - compare two charts, one of them can be local filesystem
			create/set/delete commands

		cluster
			-v state (def) for configuration and state
				incl. mapping to locally defined k8s clusters (?)
			-v ... k8s-objects
			-v cnfi
			-v notification  (incl live)?

		cnfd
			-v state (def) list
				check display with external repos
				check display with multiple chart versions
				cnf instance count must be version specific
				info (tick) about device(s) onboarding - not sure if tick or some details about device(s)
			-v ... list of values + a way to show if these are all values or subset
			-v ...

		cnfi
			-v ... kubernetes state
			-v ... helm state
			-v ... nso state
			-v ... device state
			-v ... values (mark what was differnet from default cnfd values)?
			-v notification  (incl live)?
			-v logs incl live?

		device

		vnfd

		vnfi

		nsd

		nsi

		package

ocp
	migrate
		image => pvc
		vnfd => cnfm (???)
		openstack vm => vm/vmi yaml
		vm migration (as for orange)