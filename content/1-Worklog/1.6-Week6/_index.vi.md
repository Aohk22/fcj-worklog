---
title: "Worklog Tuần 6"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu Tuần 6

- Cải thiện và tối ưu hóa codebase phân tích malware
- Tái cấu trúc kiến trúc code để dễ bảo trì hơn
- Refactor các hàm hiện có và triển khai các tiện ích helper mới

### Công việc và Thành tựu

|Công việc|Ngày bắt đầu|Ngày hoàn thành|Tài liệu tham khảo|
| --- | --- | --- | --- |
|Tái cấu trúc kiến trúc codebase.<br/>Chia nhỏ script nguyên khối thành các modules logic.<br/>|10-10-2025|11-10-2025|https://github.com/Aohk22/fcj-1-file-analyzer/blob/main/srvc_file/utils/core/file_processor.py|
|Refactor các hàm phân tích core:<br/>- Triển khai lazy loading cho malware hash database<br/>- Nâng cao phát hiện loại file với TrID<br/>- Triển khai tiện ích trích xuất chuỗi<br/>|11-10-2025|12-10-2025|https://mark0.net/soft-trid-e.html<br/>https://docs.python.org/3/library/subprocess.html<br/>|
|Phát triển các hàm helper phân tích PE:<br/>- Phân tích section với tính toán entropy<br/>- Phát hiện kiến trúc<br/>- Xác thực timestamp<br/>|12-10-2025|13-10-2025|https://github.com/erocarrera/pefile<br/>https://en.wikipedia.org/wiki/Portable_Executable<br/>|
|Triển khai các hàm helper phân tích ELF:<br/>- Phân tích header<br/>- Phân tích symbol table<br/>- Trích xuất thông tin segment<br/>|13-10-2025|14-10-2025|https://man7.org/linux/man-pages/man1/readelf.1.html<br/>https://en.wikipedia.org/wiki/Executable_and_Linkable_Format<br/>|
|Tích hợp Ghidra decompilation:<br/>- Cấu hình headless analyzer<br/>- Triển khai xử lý file an toàn<br/>- Thêm xử lý lỗi và validation<br/>|14-10-2025|16-10-2025|https://ghidra-sre.org/<br/>https://github.com/NationalSecurityAgency/ghidra<br/>|

### Nhận xét

#### Tái cấu trúc Code và Cải thiện Kiến trúc

Tiến hành tái cấu trúc toàn diện codebase phân tích malware để cải thiện tổ chức code và khả năng bảo trì. Script phân tích nguyên khối được chia nhỏ thành các modules logic, tách biệt các concerns như xác thực file hash, phân tích PE, phân tích ELF, và chức năng decompilation. Cách tiếp cận modular này giúp code dễ test, debug và mở rộng với các tính năng mới.

#### Refactor các Hàm Phân tích Core

Refactor đáng kể các hàm phân tích core để cải thiện chất lượng code và hiệu suất:

- **Hệ thống Phát hiện Hash**: Cải thiện hệ thống phát hiện malware hash bằng cách triển khai lazy loading cho cơ sở dữ liệu malware hash. Hàm `_loadMalwareHashes()` giờ đây load và cache các giá trị hash từ file database một cách hiệu quả, với xử lý lỗi phù hợp cho các file bị thiếu. Hàm `_checkMalwareBySha256()` cung cấp tra cứu nhanh O(1) sử dụng cấu trúc dữ liệu set.

- **Phát hiện Loại File**: Nâng cao phát hiện loại file sử dụng tích hợp thư viện TrID (TrIDent). Hàm `_getFileTypeTrid()` giờ cung cấp nhận dạng loại file chi tiết với tỷ lệ phần trăm độ tin cậy, giúp xác định các file có khả năng độc hại đang giả dạng là các loại file hợp lệ.

- **Trích xuất Chuỗi**: Triển khai trích xuất chuỗi hiệu quả từ các file binary sử dụng hàm helper `_getStrings()`, tận dụng tiện ích `strings` của Linux để trích xuất các chuỗi có thể đọc được, cung cấp thông tin chi tiết về hành vi và khả năng của malware.

#### Cải tiến Phân tích PE (Portable Executable)

Phát triển các hàm helper toàn diện để phân tích các file PE của Windows:

- **Phân tích Section**: Tạo hàm `_getPESections()` trích xuất thông tin chi tiết về các sections của file PE bao gồm địa chỉ ảo, kích thước, MD5 hashes, và giá trị entropy. Tính toán entropy giúp xác định các sections được packed hoặc encrypted phổ biến trong malware, đánh dấu các sections có entropy trên 7 hoặc dưới 3 là đáng ngờ.

- **Phát hiện Kiến trúc**: Triển khai `_getPEMetaArch()` để xác định file PE là 32-bit hay 64-bit dựa trên giá trị machine type trong PE header.

- **Xác thực Timestamp**: Phát triển hàm `_getPEMetaTimestamp()` không chỉ chuyển đổi PE timestamps sang định dạng có thể đọc được mà còn thực hiện kiểm tra hợp lý để phát hiện timestamps đáng ngờ (ngày trước năm 2000 hoặc ngày trong tương lai), là các chỉ báo phổ biến của executables bị giả mạo hoặc độc hại.

#### Công cụ Phân tích ELF (Executable and Linkable Format)

Triển khai các hàm helper mạnh mẽ để phân tích các binaries ELF của Linux:

- **Phân tích Header**: Tạo hàm `_getELFHeader()` sử dụng tiện ích `readelf` để trích xuất thông tin ELF header quan trọng bao gồm magic numbers, class (32/64-bit), data encoding, file type, và kiến trúc máy đích.

- **Phân tích Symbol Table**: Phát triển hàm `_getELFSymEntries()` phân tích symbol table để trích xuất tên hàm, loại, và thông tin visibility. Điều này giúp xác định các thư viện được import và các hàm được export có thể tiết lộ chức năng của malware.

- **Thông tin Segment**: Triển khai hàm placeholder `_getELFSegments()` để trích xuất thông tin program segment, sẽ được phát triển thêm để phân tích memory layout và permissions.

#### Tích hợp Decompilation

Tích hợp khả năng decompilation headless của Ghidra thông qua hàm `_getDecompilation()`:

- Triển khai xử lý file tạm thời an toàn cho decompilation input/output
- Cấu hình Ghidra headless analyzer với custom script paths
- Thêm thiết lập biến môi trường phù hợp cho Java runtime
- Triển khai xử lý lỗi và validation cho kết quả decompilation
- Hàm giờ đây tạo pseudocode có thể đọc được từ executables binary, cho phép phân tích sâu hơn về hành vi malware

#### Cải thiện Chất lượng Code

Trong suốt tuần, tập trung vào cải thiện chất lượng code tổng thể:

- Thêm xử lý lỗi nhất quán với các khối try-except
- Triển khai cleanup tài nguyên phù hợp sử dụng context managers
- Thêm logging và debug output có thông tin
- Cải thiện documentation và type hints cho hàm
- Tối ưu hóa các subprocess calls để có hiệu suất tốt hơn
- Chuẩn hóa quy ước đặt tên trên tất cả các helper functions

#### Các bước tiếp theo

- Triển khai unit tests cho tất cả các helper functions
- Tích hợp các helper functions vào các API endpoints chính
- Tiếp tục phát triển khả năng phân tích động
