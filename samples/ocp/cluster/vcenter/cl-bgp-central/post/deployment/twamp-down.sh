#!/bin/bash

kubectl delete -f deployment/twamp-secure-reflector.yaml
kubectl delete -f deployment/twamp-insecure-reflector.yaml
