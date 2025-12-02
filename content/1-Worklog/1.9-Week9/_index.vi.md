---
title: "Worklog Tuần 9"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu Tuần 9

- Viết lại ứng dụng frontend sử dụng Bun runtime
- Cải thiện giao diện người dùng cho báo cáo phân tích malware
- Triển khai tiện ích phân tích báo cáo tự động

### Công việc và Thành tựu

|Công việc|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Migrate frontend sang Bun runtime:<br/>- Tái cấu trúc project dependencies<br/>- Cập nhật build scripts và configuration<br/>- Test tương thích với APIs hiện có<br/>|31-10-2025|01-11-2025|https://bun.sh/<br/>https://bun.sh/docs<br/>|
|Triển khai cải thiện UI:<br/>- Thêm scrolling cho phần decompiled code<br/>- Thêm scrolling cho phần extracted strings<br/>- Cải thiện layout và khả năng đọc báo cáo<br/>|02-11-2025|03-11-2025||
|Phát triển tiện ích phân tích báo cáo tự động:<br/>- Tạo hàm objectWalk() cho recursive traversal<br/>- Triển khai headerize() cho chuyển đổi camelCase sang Title Case<br/>- Tổ chức utilities trong module util.js<br/>|03-11-2025|05-11-2025|https://github.com/Aohk22/fcj-1-file-analyzer/blob/main/srvc_web/app/util.js|

### Nhận xét

#### Migration Frontend sang Bun

Hoàn thành việc viết lại hoàn toàn ứng dụng frontend sử dụng Bun, một JavaScript runtime hiện đại cung cấp cải thiện hiệu suất đáng kể so với Node.js truyền thống. Bun cung cấp:
- Thời gian khởi động nhanh hơn và memory footprint giảm
- Bundler, transpiler, và package manager tích hợp sẵn
- Hỗ trợ TypeScript native không cần cấu hình bổ sung
- Cải thiện developer experience với hot reload nhanh hơn

Migration bao gồm tái cấu trúc dependencies của dự án, cập nhật build scripts, và đảm bảo tương thích với các API integrations hiện có. Frontend mới dựa trên Bun cho thấy thời gian load nhanh hơn đáng kể và responsiveness được cải thiện.

#### Cải thiện Giao diện Người dùng

Triển khai các cải thiện UI quan trọng để nâng cao trải nghiệm người dùng khi xem báo cáo phân tích malware:

**Scrolling cho Decompiled Code**:
Thêm scrollable containers cho phần decompiled code. Vì Ghidra decompilation có thể tạo ra hàng nghìn dòng pseudocode, việc hiển thị tất cả cùng lúc là không thực tế và gây ra vấn đề hiệu suất trình duyệt. Scrollable view mới:
- Giới hạn viewport ban đầu ở chiều cao có thể quản lý được
- Duy trì định dạng code và syntax
- Cung cấp scrolling mượt mà cho codebase lớn
- Cải thiện hiệu suất load trang bằng cách virtualizing content rendering

**Scrolling cho Extracted Strings**:
Tương tự triển khai scrollable containers cho phần strings. Binary files thường chứa hàng nghìn strings được trích xuất, khiến chúng khó điều hướng. Scrollable strings view:
- Tổ chức strings theo định dạng sạch sẽ, dễ đọc
- Cho phép users nhanh chóng scan qua các string collections lớn
- Duy trì chức năng search trong scrollable area
- Cải thiện khả năng đọc báo cáo tổng thể

#### Giải pháp Phân tích Báo cáo Tự động

Giải quyết một pain point phát triển đáng kể: việc phân tích thủ công các report objects lớn, lồng nhau từ analysis API đang trở nên ngày càng tẻ nhạt và dễ lỗi. Khi khả năng phân tích mở rộng, cấu trúc báo cáo trở nên phức tạp hơn với các objects lồng sâu chứa PE sections, ELF headers, symbol tables, và các metadata khác nhau.

