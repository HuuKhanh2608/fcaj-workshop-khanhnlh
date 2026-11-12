---
title: "Worklog Tuần 5"
date: 2026-11-05
weight: 5
chapter: false
pre: "<b>1.5. </b>"
---

### Mục tiêu tuần 5:

* Chọn đúng dịch vụ lưu trữ AWS và storage class S3 cho từng nhu cầu.
* Xuất bản website tĩnh an toàn với S3 và CloudFront.
* Tìm hiểu lưu trữ hybrid, di chuyển máy ảo và file share Windows được quản lý.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Học về lưu trữ trên AWS trong Module 04-01 và 04-02: <br>&emsp; + Lưu trữ object, block, file và trường hợp phù hợp của từng loại <br>&emsp; + Bucket, object và Access Point của Amazon S3 <br>&emsp; + Chọn storage class S3 theo tần suất truy cập dữ liệu | 12/10/26 | 12/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Học phần còn lại của Module 04: <br>&emsp; + Website tĩnh trên S3, CORS, kiểm soát truy cập và hiệu năng theo object key (04-03) <br>&emsp; + Lưu trữ dài hạn với S3 Glacier <br>&emsp; + Di chuyển dữ liệu bằng Snow Family và kết nối lưu trữ on-premises qua Storage Gateway (04-04) | 13/10/26 | 13/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - **Thực hành (Lab57):** <br>&emsp; + Xuất bản website tĩnh từ một bucket S3 <br>&emsp; + Điều chỉnh Block Public Access và quyền object để truy cập được website <br>&emsp; + Khóa bucket trở lại và phân phối website qua CloudFront <br>&emsp; + Bật versioning, di chuyển object giữa các bucket và thiết lập replication đa Region | 14/10/26 | 14/10/26 | <https://000057.awsfcaj.com/> |
| 5 | - **Thực hành (Lab24 – Storage Gateway):** <br>&emsp; + Triển khai file gateway trên EC2 với bucket S3 làm nơi lưu trữ <br>&emsp; + Tạo file share và mount từ máy client <br>- **Thực hành (Lab14 – VM Import/Export):** <br>&emsp; + Import image máy ảo vào AWS thành AMI và khởi chạy <br>&emsp; + Export instance ngược về S3 dưới dạng image máy ảo | 15/10/26 | 15/10/26 | <https://000024.awsfcaj.com/> <br> <https://000014.awsfcaj.com/> |
| 6 | - **Thực hành (Lab25 – Amazon FSx for Windows File Server):** <br>&emsp; + Tạo file system SSD và HDD Multi-AZ, so sánh hiệu năng <br>&emsp; + Tạo file share, bật deduplication, shadow copy và quota cho người dùng <br>&emsp; + Mở rộng throughput, dung lượng lưu trữ rồi xóa môi trường | 16/10/26 | 16/10/26 | <https://000025.awsfcaj.com/> |

### Kết quả đạt được tuần 5:

* Biết chọn dịch vụ phù hợp với từng nhu cầu lưu trữ:
  * S3 cho object, EBS cho block volume, EFS và FSx cho file dùng chung
  * Storage class truy cập không thường xuyên và Glacier cho dữ liệu hiếm khi đọc
* Phân phối website tĩnh qua CloudFront trong khi vẫn giữ bucket S3 ở chế độ private.
* Bảo vệ dữ liệu trước việc xóa nhầm và sự cố Region bằng versioning và replication.
* Hiểu cách Storage Gateway và VM Import/Export hỗ trợ đưa workload on-premises lên AWS.
