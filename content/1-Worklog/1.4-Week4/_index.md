---
title: "Week 4 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---


### Week 4 Objectives

- Implement database layer with DynamoDB
- Set up infrastructure automation and CI/CD pipeline
- Configure auto-scaling for the project

### Tasks and Achievements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Research DynamoDB with CQRS Pattern.|28-09-2025|30-09-2025|https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/<br/>https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.Accessing.html<br/>|
|Figure out auto scaling for infrastructure.|01-10-2025|01-10-2025|https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html|
|Implement Terraform for infrastructure provisioning.<br/>Finish temporary terraform implementation.<br/>|01-10-2025|02-10-2025|https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation<br/>https://www.geeksforgeeks.org/system-design/microservices-design-patterns/<br/>|
|Set up CI/CD pipeline:<br/>- Research GitHub integration with CodePipeline.<br/>- Implement instance refreshing for deployments.<br/>|03-10-2025|03-10-2025|https://docs.github.com/en/actions/get-started/quickstart|

### Comments

#### DynamoDB Implementation

Successfully implemented DynamoDB for the project using the CQRS (Command Query Responsibility Segregation) pattern. This pattern separates read and write operations, which helps optimize performance and scalability for the malware analysis system. The database now efficiently handles user requests and stores analysis reports.

#### Infrastructure as Code

Completed Terraform implementation for infrastructure provisioning. The current setup includes basic infrastructure components without HTTPS configuration yet. Terraform manages the creation of AWS resources including CodePipeline for automated deployments.

#### CI/CD Pipeline

Working on establishing a complete CI/CD pipeline that integrates GitHub with AWS CodePipeline. The pipeline will automatically deploy changes after commits are pushed to the repository. Additionally, implementing instance refreshing to ensure zero-downtime deployments and maintain service availability during updates.

#### Auto Scaling

Figured out auto-scaling configuration for the project infrastructure to handle varying loads efficiently.

#### Next Steps

- Implement HTTPS support in Terraform configuration
- Complete GitHub integration with CodePipeline
- Continue work on personal project components
