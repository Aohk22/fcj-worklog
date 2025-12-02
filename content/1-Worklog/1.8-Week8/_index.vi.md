---
title: "Worklog Tuần 8"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu Tuần 8

- Giải quyết các dependencies trong deployment Terraform
- Triển khai chiến lược khởi tạo resource có mục tiêu
- Tiến hành testing hạ tầng toàn diện

### Công việc và Thành tựu

|Công việc|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Học và tích hợp AWS Image Builder:<br/>- Cấu hình IAM roles và instance profiles<br/>- Tạo build component scripts<br/>- Định nghĩa image recipes và infrastructure<br/>- Tạo pipelines tự động cho việc tạo AMI<br/>|21-10-2025|23-10-2025|https://docs.aws.amazon.com/imagebuilder/<br/>https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html<br/>|
|Debug và test cấu trúc Terraform mới:<br/>- Giải quyết module dependencies<br/>- Sửa IAM permissions<br/>- Test Image Builder pipeline<br/>|23-10-2025|23-10-2025||
|Nghiên cứu quản lý dependency của Terraform.<br/>Phân tích deployment failures và xác định nguyên nhân gốc rễ.<br/>|24-10-2025|24-10-2025|https://developer.hashicorp.com/terraform/cli/commands/apply<br/>https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on<br/>|
|Triển khai khởi tạo resource có mục tiêu:<br/>- Sử dụng tùy chọn -target cho pre-initialization Image Builder<br/>- Tạo chiến lược deployment theo giai đoạn<br/>- Test thứ tự deployment và thỏa mãn dependency<br/>|25-10-2025|26-10-2025|https://developer.hashicorp.com/terraform/cli/commands/plan#resource-targeting|

### Nhận xét

#### Quản lý Dependency của Terraform

Gặp phải và giải quyết vấn đề dependency quan trọng trong workflow deployment Terraform. Hạ tầng yêu cầu các AMIs được xây dựng bởi Image Builder pipeline trước khi launch templates và auto-scaling groups có thể được tạo. Tuy nhiên, lệnh `terraform apply` chuẩn cố gắng tạo tất cả resources đồng thời, gây ra lỗi do thiếu tham chiếu AMI.

#### Khởi tạo Resource có Mục tiêu

Triển khai phương pháp deployment chiến lược sử dụng tùy chọn `-target` của Terraform để kiểm soát thứ tự tạo resource. Kỹ thuật này cho phép kiểm soát chi tiết về resources nào được tạo trước, đảm bảo dependencies được thỏa mãn trước khi các dependent resources được cung cấp.

**Chiến lược Pre-Initialization Image Builder**:
Tạo quy trình deployment theo giai đoạn:

1. **Giai đoạn 1 - Hạ tầng Image Builder**: Sử dụng `terraform apply -target=module.image_builder` để chỉ khởi tạo các components của Image Builder pipeline bao gồm:
   - IAM roles và instance profiles
   - Image Builder components (build scripts)
   - Image recipes và distributions
   - Pipeline configuration và schedules

2. **Giai đoạn 2 - Tạo AMI**: Trigger Image Builder pipeline thủ công hoặc chờ scheduled execution để tạo các AMIs cần thiết. Bước này đảm bảo rằng các AMI IDs hợp lệ có sẵn trong AWS account trước khi tiếp tục.

3. **Giai đoạn 3 - Hạ tầng Hoàn chỉnh**: Khi AMIs được xây dựng và có sẵn, thực thi `terraform apply` không có targets để cung cấp hạ tầng còn lại:
   - VPC và networking components
   - Security groups và routing tables
   - Launch templates tham chiếu các AMIs mới tạo
   - Auto-scaling groups và load balancers
   - DynamoDB tables và các services khác

Phương pháp theo giai đoạn này giải quyết vấn đề circular dependency khi launch templates cần AMI IDs không tồn tại cho đến khi Image Builder hoàn thành lần chạy đầu tiên.

#### Đánh giá các Phương pháp Thay thế

Khám phá một số giải pháp thay thế trước khi quyết định phương pháp khởi tạo có mục tiêu:

- **Data Source Lookups**: Xem xét sử dụng Terraform data sources để tra cứu các AMIs hiện có, nhưng điều này yêu cầu tạo AMI thủ công cho deployment đầu tiên
- **Null Resources with Provisioners**: Đánh giá việc sử dụng null resources để trigger Image Builder và chờ hoàn thành, nhưng thấy phương pháp này kém tin cậy hơn
- **Separate Terraform Workspaces**: Xem xét chia hạ tầng thành hai dự án Terraform riêng biệt, nhưng điều này tăng độ phức tạp và giảm khả năng bảo trì
- **AMI ID Variables**: Cố gắng sử dụng variables cho AMI IDs, nhưng điều này vẫn yêu cầu can thiệp thủ công cho deployment ban đầu

Tùy chọn `-target` cung cấp sự cân bằng tốt nhất giữa đơn giản, độ tin cậy và tự động hóa.

