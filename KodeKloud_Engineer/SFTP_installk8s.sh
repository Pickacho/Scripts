#!/bin/bash


export KUBECONFIG=/etc/kubernetes/admin.conf", "", "
You should now deploy a pod network to the cluster.", "
Run \"
kubectl apply -f [podnetwork].yaml\" with one of the options listed at:", "
https://kubernetes.io/docs/concepts/cluster-administration/addons/", "", "
Then you can join any number of worker nodes by running the following on each as root:", "", "
kubeadm join 192.168.1.46:6443 --token yf4xpy.p21fh9m5inp6evg3 \\", "\t--discovery-token-ca-cert-hash sha256:44c3aa16c2fa96fd6f71249a92d2b8d87e7afeba6d5c0dfb4808bb5a21a87c2e "]}
