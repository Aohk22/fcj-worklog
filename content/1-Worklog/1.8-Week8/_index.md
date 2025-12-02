---
title: "Week 8 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives

- Resolve Terraform deployment dependencies
- Implement targeted resource initialization strategy
- Conduct comprehensive infrastructure testing

### Tasks and Achievements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Learn and integrate AWS Image Builder:<br/>- Configure IAM roles and instance profiles<br/>- Create build component scripts<br/>- Define image recipes and infrastructure<br/>- Create automated pipelines for AMI generation<br/>|21-10-2025|23-10-2025|https://docs.aws.amazon.com/imagebuilder/<br/>https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html<br/>|
|Debug and test new Terraform structure:<br/>- Resolve module dependencies<br/>- Fix IAM permissions<br/>- Test Image Builder pipeline<br/>|23-10-2025|23-10-2025||
|Research Terraform dependency management.<br/>Analyze deployment failures and identify root cause.<br/>|24-10-2025|24-10-2025|https://developer.hashicorp.com/terraform/cli/commands/apply<br/>https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on<br/>|
|Implement targeted resource initialization:<br/>- Use -target option for Image Builder pre-initialization<br/>- Create phased deployment strategy<br/>- Test deployment order and dependency satisfaction<br/>|25-10-2025|26-10-2025|https://developer.hashicorp.com/terraform/cli/commands/plan#resource-targeting|

### Comments

#### Terraform Dependency Management

Encountered and resolved a critical dependency issue in the Terraform deployment workflow. The infrastructure required AMIs to be built by the Image Builder pipeline before the launch templates and auto-scaling groups could be created. However, the standard `terraform apply` command attempted to create all resources simultaneously, causing failures due to missing AMI references.

#### Targeted Resource Initialization

Implemented a strategic deployment approach using Terraform's `-target` option to control resource creation order. This technique allows for granular control over which resources are created first, ensuring dependencies are satisfied before dependent resources are provisioned.

**Image Builder Pre-Initialization Strategy**:
Created a phased deployment process:

1. **Phase 1 - Image Builder Infrastructure**: Used `terraform apply -target=module.image_builder` to initialize only the Image Builder pipeline components including:
   - IAM roles and instance profiles
   - Image Builder components (build scripts)
   - Image recipes and distributions
   - Pipeline configuration and schedules

2. **Phase 2 - AMI Generation**: Triggered the Image Builder pipeline either manually or waited for scheduled execution to generate the required AMIs. This step ensures that valid AMI IDs are available in the AWS account before proceeding.

3. **Phase 3 - Full Infrastructure**: Once AMIs were built and available, executed `terraform apply` without targets to provision the remaining infrastructure:
   - VPC and networking components
   - Security groups and routing tables
   - Launch templates referencing the newly created AMIs
   - Auto-scaling groups and load balancers
   - DynamoDB tables and other services

This phased approach solved the circular dependency problem where launch templates needed AMI IDs that didn't exist until Image Builder completed its first run.

#### Alternative Approaches Evaluated

Explored several alternative solutions before settling on the targeted initialization approach:

- **Data Source Lookups**: Considered using Terraform data sources to look up existing AMIs, but this required manual AMI creation for the first deployment
- **Null Resources with Provisioners**: Evaluated using null resources to trigger Image Builder and wait for completion, but found this approach less reliable
- **Separate Terraform Workspaces**: Considered splitting infrastructure into two separate Terraform projects, but this increased complexity and reduced maintainability
- **AMI ID Variables**: Attempted to use variables for AMI IDs, but this still required manual intervention for initial deployment

The `-target` option provided the best balance of simplicity, reliability, and automation.

