#!/bin/bash

kubectl delete -f deployment/twamp-secure.yaml
kubectl delete -f deployment/twamp-insecure.yaml
