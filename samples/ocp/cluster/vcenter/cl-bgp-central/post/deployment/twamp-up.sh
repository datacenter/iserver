#!/bin/bash

kubectl create -f deployment/twamp-secure-reflector.yaml
kubectl create -f deployment/twamp-insecure-reflector.yaml
