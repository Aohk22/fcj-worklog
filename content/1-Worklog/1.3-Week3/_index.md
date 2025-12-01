---
title: "Week 3 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives

- Decide on project topic
- Start project

### Tasks and Achivements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Decide on project topic (malware analysis).|22-09-2025|22-09-2025||
|Design infrastructure for project.<br/>Identify frontend, backend, AWS services to use.<br/>Start working on project.<br/>|23-09-2025|23-09-2025|https://calculator.aws/#/<br/>https://docs.aws.amazon.com/dynamodb/<br/>https://fastapi.tiangolo.com/<br/>|
|Research malware sandboxes.|24-09-2025|25-09-2025|https://capev2.readthedocs.io/en/latest/index.html#<br/>https://panda-re.mit.edu/<br/>https://github.com/cert-ee/cuckoo3<br/>https://github.com/CERT-Polska/drakvuf-sandbox<br/>|
|Finish one part of project:<br/>- Basic API server, static file analysis.<br/>|25-09-2025|25-09-2025||
|Learn about Linux virtualization techologies for project.<br/>- kvm - qemu - libvirt stack.<br/>Create a virtual machine for sandboxing.<br/>|26-09-2025|27-09-2025|https://documentation.ubuntu.com/server/how-to/virtualisation/libvirt/<br/>https://linux.die.net/man/1/virt-install<br/>https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install<br/>https://schneegans.de/windows/unattend-generator/<br/>|

### Comments

#### General

My part for this project is automating malware analysis, user database management is unexplained here.  
Basic procedure is the web server will send a request to the analysis machine through an API.  
The API will have 2 endpoints for static and dynamic (the more expensive operation) analysis.  
API will be built using FastAPI, the static analysis will be done using many Linux tools.  
The static analysis script is completed for this week and I'm now trying to implement sandbox solutions.  
Currently CAPEv2 sandbox is what I'm looking into.  

#### What kind of files can be analyzed

As of now only Windows executables (PE files) are planned for implementation.  

#### How the data will be stored

User requests to the web server will only contact the analysis server if there are no reports already in the database (DynamoDB).  
The processing machine after analyzing will send reports back to via API as well as store the report on the database.  
This way we can save a read operation.  
