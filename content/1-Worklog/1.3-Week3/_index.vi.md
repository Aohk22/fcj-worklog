---
title: "Worklog Tuần 3"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu Tuần 3

- Quyết định chủ đề dự án
- Bắt đầu dự án

### Nhiệm vụ và Thành tựu

|Nhiệm vụ|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Quyết định chủ đề dự án (phân tích malware).|22-09-2025|22-09-2025||
|Thiết kế hạ tầng cho dự án.<br/>Xác định frontend, backend, dịch vụ AWS cần dùng.<br/>Bắt đầu làm dự án.<br/>|23-09-2025|23-09-2025|https://calculator.aws/#/<br/>https://docs.aws.amazon.com/dynamodb/<br/>https://fastapi.tiangolo.com/<br/>|
|Nghiên cứu các sandbox malware, chọn một (CAPEv2).|24-09-2025|25-09-2025|https://capev2.readthedocs.io/en/latest/index.html#<br/>https://panda-re.mit.edu/<br/>https://github.com/cert-ee/cuckoo3<br/>https://github.com/CERT-Polska/drakvuf-sandbox<br/>|
|Hoàn thành một phần của dự án:<br/>- Máy chủ API cơ bản, phân tích tệp tĩnh.<br/>|25-09-2025|25-09-2025||
|Tìm hiểu công nghệ ảo hóa Linux cho dự án.<br/>- kvm - qemu - libvirt stack.<br/>Tạo một máy ảo để sandbox.<br/>|26-09-2025|27-09-2025|https://documentation.ubuntu.com/server/how-to/virtualisation/libvirt/<br/>https://linux.die.net/man/1/virt-install<br/>https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install<br/>https://schneegans.de/windows/unattend-generator/<br/>|

### Bình luận

#### Tổng quát

Phần việc của tôi trong dự án này là tự động hóa phân tích malware, phần quản lý cơ sở dữ liệu người dùng chưa được giải thích ở đây.  
Quy trình cơ bản là máy chủ web sẽ gửi yêu cầu đến máy phân tích thông qua một API.  
API sẽ có 2 endpoint cho phân tích tĩnh và phân tích động (tác vụ tốn kém hơn).  
API sẽ được xây dựng bằng FastAPI, phân tích tĩnh sẽ được thực hiện bằng nhiều công cụ Linux.  
Script phân tích tĩnh đã hoàn thành trong tuần này và hiện tôi đang cố gắng triển khai các giải pháp sandbox.  
Hiện tại tôi đang tìm hiểu sandbox CAPEv2.  

#### Loại tệp có thể phân tích

Hiện tại chỉ có các tệp thực thi Windows (tệp PE) được lên kế hoạch triển khai.  

#### Cách lưu trữ dữ liệu

Các yêu cầu của người dùng đến máy chủ web sẽ chỉ liên hệ với máy phân tích nếu trong cơ sở dữ liệu (DynamoDB) chưa có báo cáo.  
Máy xử lý sau khi phân tích sẽ gửi báo cáo trở lại qua API cũng như lưu trữ báo cáo vào cơ sở dữ liệu.  
Bằng cách này chúng ta có thể tiết kiệm một lần đọc dữ liệu.  

