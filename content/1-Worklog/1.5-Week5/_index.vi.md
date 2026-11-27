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
| 2 | - Học về lưu trữ trên AWS trong Module 04-01 và 04-02: <br>&emsp; + Lưu trữ object, block, file và trường hợp phù hợp của từng loại <br>&emsp; + Bucket, object và Access Point của Amazon S3 <br>&emsp; + Chọn storage class S3 theo tần suất truy cập dữ liệu | 12/10/2026 | 12/10/2026 | <https://www.youtube.com/watch?v=hsCfP0IxoaM> <br> <https://www.youtube.com/watch?v=_yunukwcAwc> |
| 3 | - Học phần còn lại của Module 04: <br>&emsp; + Website tĩnh trên S3, CORS, kiểm soát truy cập và hiệu năng theo object key (04-03) <br>&emsp; + Lưu trữ dài hạn với S3 Glacier <br>&emsp; + Di chuyển dữ liệu bằng Snow Family và kết nối lưu trữ on-premises qua Storage Gateway (04-04) | 13/10/2026 | 13/10/2026 | <https://www.youtube.com/watch?v=mPBjB6Ltl_Q> <br> <https://www.youtube.com/watch?v=YXn8Q_Hpsu4> |
| 4 | - **Thực hành (Lab57):** <br>&emsp; + Xuất bản website tĩnh từ một bucket S3 <br>&emsp; + Điều chỉnh Block Public Access và quyền object để truy cập được website <br>&emsp; + Khóa bucket trở lại và phân phối website qua CloudFront <br>&emsp; + Bật versioning, di chuyển object giữa các bucket và thiết lập replication đa Region | 14/10/2026 | 14/10/2026 | <https://000057.awsfcaj.com/3-staticwebsite/> <br> <https://000057.awsfcaj.com/4-blockpublicaccess/> <br> <https://000057.awsfcaj.com/7-cloudfront/7.2-configure_amazon_cloudfront/> <br> <https://000057.awsfcaj.com/8-versioning/> <br> <https://000057.awsfcaj.com/10-s3ccr/> |
| 5 | - **Thực hành (Lab24 – Storage Gateway):** <br>&emsp; + Triển khai file gateway trên EC2 với bucket S3 làm nơi lưu trữ <br>&emsp; + Tạo file share và mount từ máy client <br>- **Thực hành (Lab14 – VM Import/Export):** <br>&emsp; + Import image máy ảo vào AWS thành AMI, sau đó export một instance ngược về S3 | 15/10/2026 | 15/10/2026 | <https://000024.awsfcaj.com/2-useawsstoragegw/2.1-createstoragegw/> <br> <https://000024.awsfcaj.com/2-useawsstoragegw/2.2-createfileshare/> <br> <https://000014.awsfcaj.com/2-import-vm-to-aws/3-import-vm-to-ami/> <br> <https://000014.awsfcaj.com/3-export-vm-from-aws/2-export-from-instance/> |
| 6 | - **Thực hành (Lab25 – Amazon FSx for Windows File Server):** <br>&emsp; + Tạo file system SSD và HDD Multi-AZ, so sánh hiệu năng <br>&emsp; + Tạo file share, bật deduplication, shadow copy và quota cho người dùng <br>&emsp; + Mở rộng throughput, dung lượng lưu trữ rồi xóa môi trường | 16/10/2026 | 16/10/2026 | <https://000025.awsfcaj.com/2-prerequiste/2.2-create-maz-ssd-file-system/> <br> <https://000025.awsfcaj.com/4-test-performance/> <br> <https://000025.awsfcaj.com/6-enable-data-dedup/> <br> <https://000025.awsfcaj.com/7-enable-shadow-copies/> <br> <https://000025.awsfcaj.com/12-scale-storage-capacity/> |

### Kết quả đạt được tuần 5:

* Hiểu được các kiến thức sau:
  * Các loại lưu trữ: S3 cho object, EBS cho block volume gắn vào một instance, EFS và FSx cho file system dùng chung nhiều máy
  * Storage class S3 trải từ Standard cho dữ liệu truy cập thường xuyên đến Infrequent Access, Intelligent-Tiering và các lớp Glacier cho lưu trữ dài hạn
  * Website endpoint của S3 phục vụ nội dung công khai qua HTTP, còn CloudFront bổ sung HTTPS, bộ nhớ đệm và có thể đọc từ bucket private
  * Versioning giữ lại mọi phiên bản object, còn replication yêu cầu bật versioning ở cả bucket nguồn và đích
  * Storage Gateway nối ứng dụng on-premises với S3 qua giao diện file, volume hoặc tape, còn Snow Family di chuyển dữ liệu lớn theo hình thức offline

* Phân phối website tĩnh qua CloudFront trong khi giữ bucket S3 ở chế độ private.

* Thiết lập versioning và replication đa Region.

* Triển khai file gateway, import và export máy ảo, quản lý file system FSx for Windows.

* Rút ra các bài học về bảo mật và chi phí:
  * Nên luôn bật Block Public Access và chỉ cho CloudFront đọc bucket
  * File system FSx và instance gateway vẫn chạy và tính phí cho đến khi bị xóa
