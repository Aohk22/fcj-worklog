---
title: "Week 2 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives

* Learn about more AWS services.  
* Create a Hugo theme for final report.  
* Gather ideas for first project, and start early.  
* Design a basic diagram for project, assign objectives to team members.  

### Tasks and Achivements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Create a Hugo theme for learning.|15-09-2025|19-09-2025|https://stackoverflow.com/questions/4098195/can-ordered-list-produce-result-that-looks-like-1-1-1-2-1-3-instead-of-just-1<br/>https://miro.com/app/board/uXjVJGykszQ=/?share_link_id=988177864442<br/>https://discourse.gohugo.io/<br/>|
|Finish labs:<br/>- 000058 Manage Session Logs.<br/>- 000019 VPC Peering.<br/>- 000020 Transit Gateway.<br/>|16-09-2025|16-09-2025|https://cloudjourney.awsstudygroup.com/|
|- Finish labs:<br/>- 000010 Hybrid DNS resolution using Route 53.<br/>- 000005 RDS.<br/>- Try out CloudFront with S3 static website.<br/>|17-09-2025|17-09-2025|https://cloudjourney.awsstudygroup.com/<br/>https://www.youtube.com/live/lZtHCpXal-c?si=79TLFFSo9xfZGCfG<br/>https://tutorialsdojo.com/navigating-dns-management-unveiling-amazon-route-53-inbound-and-outbound-resolver-endpoints/<br/>https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html<br/>|

#### On Hybrid DNS

Hybrid DNS allows devices on VPCs to resolve on-premise internal host names and vice versa.  
AWS allows hybrid DNS by letting users create Outbound and Inbound Gateways, with the help of Route 53 Resolver.  
Inbound gateways are used for DNS requests that originate from on-premise devices to the VPC.  
Outbound gateways are used for DNS requests from within AWS VPC to on-premise network.  
The DNS builtin resolver takes the second usable IP address. Example:  
> Network 192.168.0.0/24 -> DNS resolver 192.168.0.2.

Difference between Route 53 and Route 53 Resolver:
| R53               | R53R                     |
|-------------------|--------------------------|
| Holds DNS records | Recursive DNS resolution |

#### Hugo Theme

Sample of what I created this week:  

![theme sample image 1](t1.png)
{width="900" height="600"}

Collapsible nav bar:  

![theme sample image 2](t2.png)
{width="900" height="600"}
