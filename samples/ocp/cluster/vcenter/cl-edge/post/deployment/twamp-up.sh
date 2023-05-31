#!/bin/bash

kubectl create -f deployment/twamp-secure.yaml
kubectl create -f deployment/twamp-insecure.yaml
