The Nautilus DevOps team is working on to create few jobs in Kubernetes cluster. They might come up with some real scripts/commands to use, but for now they are preparing the templates and testing the jobs with dummy commands. Please create a job template as per details given below:


Create a job countdown-datacenter.

The spec template should be named as countdown-datacenter (under metadata), and the container should be named as container-countdown-datacenter

Use image centos with latest tag only and remember to mention tag i.e centos:latest, and restart policy should be Never.

Use command sleep 5

Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.