---
title: "Week 7 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives

- Restructure Terraform codebase for better maintainability
- Implement modular architecture following Terraform best practices
- Learn and integrate AWS Image Builder for automated AMI creation

### Tasks and Achievements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Research Terraform best practices.<br/>Plan new folder structure for modules and environments.<br/>|17-10-2025|17-10-2025|https://developer.hashicorp.com/terraform/language/modules<br/>https://developer.hashicorp.com/terraform/tutorials/modules/module<br/>|
|Restructure Terraform codebase:<br/>- Create module structure with main.tf, variables.tf, outputs.tf<br/>- Extract VPC, Subnet, Launch Template, Instance Profile modules<br/>- Extract Service Auto Scale and Image Builder modules<br/>|18-10-2025|20-10-2025|https://developer.hashicorp.com/terraform/language/modules/develop<br/>https://www.terraform-best-practices.com/<br/>|
|Implement environment-specific configurations:<br/>- Create dev environment directory<br/>- Implement modules in environment context<br/>- Create .tfvars files for variable management<br/>|20-10-2025|21-10-2025||

### Comments

#### Terraform Code Restructuring

As the project grew in complexity, the original Terraform structure with all resources defined in flat files became increasingly difficult to maintain. The old structure consisted of multiple `.tf` files in a single directory, making it challenging to understand dependencies, reuse code, and manage different environments.

#### Implementing Terraform Module Standard

Restructured the entire Terraform codebase following industry best practices and the standard module structure. Each reusable component was extracted into its own module with the standard three-file pattern:

- `main.tf` - Contains the primary resource definitions
- `variables.tf` - Defines input variables with descriptions and types
- `outputs.tf` - Exports values for use by other modules

This modular approach significantly improves code reusability, testing capabilities, and overall maintainability. Modules can now be versioned independently and reused across different environments.

#### New Folder Structure Design

Designed and implemented a hierarchical folder structure separating concerns:

**Modules Directory**: Contains six reusable infrastructure modules:
- **VPC Module** - Virtual Private Cloud configuration with CIDR blocks and networking settings
- **Subnet Module** - Subnet creation with availability zone distribution
- **Launch Template Module** - EC2 launch configuration with user data and instance settings
- **Instance Profile Module** - IAM roles and instance profiles for EC2 permissions
- **Service Auto Scale Module** - Auto Scaling Groups and Target Groups for elasticity
- **Image Builder Module** - AWS Image Builder pipeline configuration for automated AMI creation

**Environments Directory**: Contains environment-specific configurations (dev, staging, production). Each environment implements the modules defined above with environment-specific variables through `.tfvars` files. The dev environment includes:
- Provider configuration for AWS
- Networking setup (VPC, subnets, routes)
- Load balancer and DNS configuration
- DynamoDB table definitions
- Security group rules
- Launch template with user data
- Image Builder pipeline configuration

This separation allows for easy management of multiple environments with different configurations while maintaining a single source of truth for infrastructure components.

#### Environment-Specific Configuration

Implemented environment-specific variable files (`.tfvars`) to manage different configurations for development, staging, and production environments. This approach enables:
- Different instance sizes and counts per environment
- Environment-specific networking configurations
- Separate security policies and access controls
- Cost optimization by using smaller resources in development
