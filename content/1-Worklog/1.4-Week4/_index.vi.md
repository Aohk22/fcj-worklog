---
title: "Worklog Tuần 4"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu Tuần 4

- Triển khai lớp cơ sở dữ liệu với DynamoDB
- Thiết lập tự động hóa hạ tầng và pipeline CI/CD
- Cấu hình auto-scaling cho dự án

### Công việc tóm tắt

|Công việc|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Nghiên cứu DynamoDB với mô hình CQRS.|28-09-2025|30-09-2025|https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/<br/>https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.Accessing.html<br/>|
|Tìm hiểu auto scaling cho hạ tầng.|01-10-2025|01-10-2025|https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html|
|Triển khai Terraform cho việc cung cấp hạ tầng.<br/>Hoàn thành triển khai Terraform tạm thời.<br/>|01-10-2025|02-10-2025|https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation<br/>https://www.geeksforgeeks.org/system-design/microservices-design-patterns/<br/>|
|Thiết lập CI/CD pipeline:<br/>- Nghiên cứu tích hợp GitHub với CodePipeline.<br/>- Triển khai instance refreshing cho deployments.<br/>|03-10-2025|03-10-2025|https://docs.github.com/en/actions/get-started/quickstart|

### Nhận xét

#### Triển khai DynamoDB

Nghiên cứu thành công DynamoDB cho dự án sử dụng mô hình CQRS (Command Query Responsibility Segregation). Mô hình này tách biệt các thao tác đọc và ghi, giúp tối ưu hóa hiệu suất và khả năng mở rộng cho hệ thống phân tích malware. Cơ sở dữ liệu hiện xử lý hiệu quả các yêu cầu của người dùng và lưu trữ báo cáo phân tích.

#### Infrastructure as Code

Hoàn thành việc triển khai Terraform cho việc cung cấp hạ tầng. Thiết lập hiện tại bao gồm các thành phần hạ tầng cơ bản. Terraform quản lý việc tạo các tài nguyên AWS bao gồm CodePipeline cho triển khai tự động.

#### CI/CD Pipeline

Đang nghiên cứu để thiết lập một pipeline CI/CD hoàn chỉnh tích hợp GitHub với AWS CodePipeline. Pipeline sẽ tự động triển khai các thay đổi sau khi commits được đẩy lên repository. Ngoài ra, đang triển khai instance refreshing để đảm bảo triển khai không có downtime và duy trì tính khả dụng của dịch vụ trong quá trình cập nhật.

#### Auto Scaling

Đã tìm hiểu cấu hình auto-scaling cho hạ tầng dự án để xử lý các tải khác nhau một cách hiệu quả.

#### Các bước tiếp theo

- Hoàn thiện tích hợp GitHub với CodePipeline
- Tiếp tục làm việc trên các thành phần dự án cá nhân
