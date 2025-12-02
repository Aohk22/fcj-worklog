---
title: "Worklog Tuần 7"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu Tuần 7

- Tái cấu trúc codebase Terraform để dễ bảo trì hơn
- Triển khai kiến trúc modular theo best practices của Terraform
- Học và tích hợp AWS Image Builder cho việc tạo AMI tự động

### Công việc và Thành tựu

|Công việc|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Nghiên cứu best practices của Terraform.<br/>Lập kế hoạch cấu trúc thư mục mới cho modules và environments.<br/>|17-10-2025|17-10-2025|https://developer.hashicorp.com/terraform/language/modules<br/>https://developer.hashicorp.com/terraform/tutorials/modules/module<br/>|
|Tái cấu trúc codebase Terraform:<br/>- Tạo cấu trúc module với main.tf, variables.tf, outputs.tf<br/>- Trích xuất VPC, Subnet, Launch Template, Instance Profile modules<br/>- Trích xuất Service Auto Scale và Image Builder modules<br/>|18-10-2025|20-10-2025|https://developer.hashicorp.com/terraform/language/modules/develop<br/>https://www.terraform-best-practices.com/<br/>|
|Triển khai cấu hình specific cho môi trường:<br/>- Tạo thư mục môi trường dev<br/>- Triển khai modules trong context môi trường<br/>- Tạo file .tfvars để quản lý biến<br/>|20-10-2025|21-10-2025||

### Nhận xét

#### Tái cấu trúc Code Terraform

Khi dự án phát triển về độ phức tạp, cấu trúc Terraform ban đầu với tất cả resources được định nghĩa trong các file phẳng trở nên ngày càng khó bảo trì. Cấu trúc cũ bao gồm nhiều file `.tf` trong một thư mục duy nhất, khiến việc hiểu dependencies, tái sử dụng code, và quản lý các môi trường khác nhau trở nên khó khăn.

#### Triển khai Chuẩn Module Terraform

Tái cấu trúc toàn bộ codebase Terraform theo best practices của ngành và cấu trúc module chuẩn. Mỗi component có thể tái sử dụng được trích xuất thành module riêng với mẫu ba file chuẩn:

- `main.tf` - Chứa các định nghĩa resource chính
- `variables.tf` - Định nghĩa các biến đầu vào với mô tả và kiểu dữ liệu
- `outputs.tf` - Xuất các giá trị để sử dụng bởi các modules khác

Cách tiếp cận modular này cải thiện đáng kể khả năng tái sử dụng code, khả năng testing, và tính bảo trì tổng thể. Các modules giờ có thể được version độc lập và tái sử dụng trên các môi trường khác nhau.

#### Thiết kế Cấu trúc Thư mục Mới

Thiết kế và triển khai cấu trúc thư mục phân cấp tách biệt các concerns:

**Thư mục Modules**: Chứa sáu infrastructure modules có thể tái sử dụng:
- **VPC Module** - Cấu hình Virtual Private Cloud với CIDR blocks và networking settings
- **Subnet Module** - Tạo subnet với phân phối availability zone
- **Launch Template Module** - Cấu hình EC2 launch với user data và instance settings
- **Instance Profile Module** - IAM roles và instance profiles cho quyền EC2
- **Service Auto Scale Module** - Auto Scaling Groups và Target Groups cho elasticity
- **Image Builder Module** - Cấu hình AWS Image Builder pipeline cho việc tạo AMI tự động

**Thư mục Environments**: Chứa các cấu hình specific cho từng môi trường (dev, staging, production). Mỗi môi trường triển khai các modules được định nghĩa ở trên với các biến specific cho môi trường thông qua các file `.tfvars`. Môi trường dev bao gồm:
- Cấu hình provider cho AWS
- Thiết lập networking (VPC, subnets, routes)
- Cấu hình load balancer và DNS
- Định nghĩa bảng DynamoDB
- Quy tắc security group
- Launch template với user data
- Cấu hình Image Builder pipeline

Sự tách biệt này cho phép quản lý dễ dàng nhiều môi trường với các cấu hình khác nhau trong khi duy trì một nguồn chân lý duy nhất cho các infrastructure components.

#### Cấu hình cho Môi trường

Triển khai các file biến cho môi trường (`.tfvars`) để quản lý các cấu hình khác nhau cho development, staging, và production environments. Cách tiếp cận này cho phép:
- Kích thước và số lượng instance khác nhau cho mỗi môi trường
- Cấu hình networking specific cho môi trường
- Tối ưu hóa chi phí bằng cách sử dụng resources nhỏ hơn trong development
