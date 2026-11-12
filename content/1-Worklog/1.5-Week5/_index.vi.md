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
| 2 | - Học về lưu trữ trên AWS trong Module 04-01 và 04-02: <br>&emsp; + Lưu trữ object, block, file và trường hợp phù hợp của từng loại <br>&emsp; + Bucket, object và Access Point của Amazon S3 <br>&emsp; + Chọn storage class S3 theo tần suất truy cập dữ liệu | 12/10/26 | 12/10/26 | [Module 04-01 – Dịch vụ lưu trữ trên AWS](https://www.youtube.com/watch?v=hsCfP0IxoaM) <br> [Module 04-02 – Amazon S3, Access Point, storage class](https://www.youtube.com/watch?v=_yunukwcAwc) |
| 3 | - Học phần còn lại của Module 04: <br>&emsp; + Website tĩnh trên S3, CORS, kiểm soát truy cập và hiệu năng theo object key (04-03) <br>&emsp; + Lưu trữ dài hạn với S3 Glacier <br>&emsp; + Di chuyển dữ liệu bằng Snow Family và kết nối lưu trữ on-premises qua Storage Gateway (04-04) | 13/10/26 | 13/10/26 | [Module 04-03 – S3 static website, kiểm soát truy cập, Glacier](https://www.youtube.com/watch?v=mPBjB6Ltl_Q) <br> [Module 04-04 – Snow Family, Storage Gateway, Backup](https://www.youtube.com/watch?v=YXn8Q_Hpsu4) |
| 4 | - **Thực hành (Lab57):** <br>&emsp; + Xuất bản website tĩnh từ một bucket S3 <br>&emsp; + Điều chỉnh Block Public Access và quyền object để truy cập được website <br>&emsp; + Khóa bucket trở lại và phân phối website qua CloudFront <br>&emsp; + Bật versioning, di chuyển object giữa các bucket và thiết lập replication đa Region | 14/10/26 | 14/10/26 | [Lab57 – 3. Enable static website feature](https://000057.awsfcaj.com/3-staticwebsite/) <br> [Lab57 – 4. Configuring public access block](https://000057.awsfcaj.com/4-blockpublicaccess/) <br> [Lab57 – 7.2 Configure Amazon CloudFront](https://000057.awsfcaj.com/7-cloudfront/7.2-configure_amazon_cloudfront/) <br> [Lab57 – 8. Bucket Versioning](https://000057.awsfcaj.com/8-versioning/) <br> [Lab57 – 10. Cross-Region Replication](https://000057.awsfcaj.com/10-s3ccr/) |
| 5 | - **Thực hành (Lab24 – Storage Gateway):** <br>&emsp; + Triển khai file gateway trên EC2 với bucket S3 làm nơi lưu trữ <br>&emsp; + Tạo file share và mount từ máy client <br>- **Thực hành (Lab14 – VM Import/Export):** <br>&emsp; + Import image máy ảo vào AWS thành AMI, sau đó export một instance ngược về S3 | 15/10/26 | 15/10/26 | [Lab24 – 2.1 Create Storage Gateway](https://000024.awsfcaj.com/2-useawsstoragegw/2.1-createstoragegw/) <br> [Lab24 – 2.2 Create File Shares](https://000024.awsfcaj.com/2-useawsstoragegw/2.2-createfileshare/) <br> [Lab14 – 2.3 Import virtual machine to AWS](https://000014.awsfcaj.com/2-import-vm-to-aws/3-import-vm-to-ami/) <br> [Lab14 – 3.2 Export virtual machine from Instance](https://000014.awsfcaj.com/3-export-vm-from-aws/2-export-from-instance/) |
| 6 | - **Thực hành (Lab25 – Amazon FSx for Windows File Server):** <br>&emsp; + Tạo file system SSD và HDD Multi-AZ, so sánh hiệu năng <br>&emsp; + Tạo file share, bật deduplication, shadow copy và quota cho người dùng <br>&emsp; + Mở rộng throughput, dung lượng lưu trữ rồi xóa môi trường | 16/10/26 | 16/10/26 | [Lab25 – 2.2 Create an SSD Multi-AZ file system](https://000025.awsfcaj.com/2-prerequiste/2.2-create-maz-ssd-file-system/) <br> [Lab25 – 4. Test Performance](https://000025.awsfcaj.com/4-test-performance/) <br> [Lab25 – 6. Enable data deduplication](https://000025.awsfcaj.com/6-enable-data-dedup/) <br> [Lab25 – 7. Enable shadow copies](https://000025.awsfcaj.com/7-enable-shadow-copies/) <br> [Lab25 – 12. Scale storage capacity](https://000025.awsfcaj.com/12-scale-storage-capacity/) |

### Kết quả đạt được tuần 5:

* **Kiến thức:**
  * Các loại lưu trữ: S3 cho object, EBS cho block volume gắn vào một instance, EFS và FSx cho file system dùng chung nhiều máy
  * Storage class S3 trải từ Standard cho dữ liệu truy cập thường xuyên đến Infrequent Access, Intelligent-Tiering và các lớp Glacier cho lưu trữ dài hạn
  * Website endpoint của S3 phục vụ nội dung công khai qua HTTP, còn CloudFront bổ sung HTTPS, bộ nhớ đệm và có thể đọc từ bucket private
  * Versioning giữ lại mọi phiên bản object, còn replication yêu cầu bật versioning ở cả bucket nguồn và đích
  * Storage Gateway nối ứng dụng on-premises với S3 qua giao diện file, volume hoặc tape, còn Snow Family di chuyển dữ liệu lớn theo hình thức offline
* **Kỹ năng thực hành:**
  * Phân phối website tĩnh qua CloudFront trong khi giữ bucket S3 ở chế độ private
  * Thiết lập versioning và replication đa Region
  * Triển khai file gateway, import và export máy ảo, quản lý file system FSx for Windows
* **Bài học bảo mật và chi phí:**
  * Nên luôn bật Block Public Access và chỉ cho CloudFront đọc bucket
  * File system FSx và instance gateway vẫn chạy và tính phí cho đến khi bị xóa
