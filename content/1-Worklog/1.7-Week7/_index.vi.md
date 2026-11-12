---
title: "Worklog Tuần 7"
date: 2026-11-05
weight: 7
chapter: false
pre: "<b>1.7. </b>"
---

### Mục tiêu tuần 7:

* Mã hóa dữ liệu bằng AWS KMS và lưu vết truy cập với AWS CloudTrail.
* Cấp thông tin xác thực tạm thời cho ứng dụng qua IAM role.
* Hiểu các dịch vụ cơ sở dữ liệu của AWS và chạy ứng dụng trên Amazon RDS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành (Lab33):** <br>&emsp; + Chuẩn bị IAM policy, role, group và user cho bài lab <br>&emsp; + Tạo KMS key và tải dữ liệu lên S3 được mã hóa bằng key đó <br>&emsp; + Ghi lại hoạt động API bằng CloudTrail và truy vấn log bằng Athena <br>&emsp; + Kiểm tra ai đọc được object đã mã hóa khi chia sẻ | 26/10/26 | 26/10/26 | [Lab33 – 2.1 Create Policy and Role](https://000033.awsfcaj.com/2-create-role-user/2.1-create-role/) <br> [Lab33 – 3. Create Key Management Service](https://000033.awsfcaj.com/3-create-kms/) <br> [Lab33 – 4.2 Upload Data to S3](https://000033.awsfcaj.com/4-create-s3/4.2-upload-data/) <br> [Lab33 – 5.1 Create CloudTrail](https://000033.awsfcaj.com/5-create-cloudtrail/5.1-create-cloudtrail/) <br> [Lab33 – 5.4 Query Data with Athena](https://000033.awsfcaj.com/5-create-cloudtrail/5.4-test-athena/) |
| 3 | - **Thực hành (Lab48):** <br>&emsp; + Truy cập S3 từ EC2 bằng access key lưu trên máy chủ <br>&emsp; + Thay access key bằng IAM role gắn vào instance <br>- Ôn tập Module 05 và tài liệu đọc thêm (05-08) | 27/10/26 | 27/10/26 | [Lab48 – 2.2 Use access key](https://000048.awsfcaj.com/2-accesskey/2.2-useaccesskey/) <br> [Lab48 – 3.1 Create IAM role](https://000048.awsfcaj.com/3-iamroleec2/3.1-createrole/) <br> [Lab48 – 3.2 Using IAM role](https://000048.awsfcaj.com/3-iamroleec2/3.2-useiamrole/) <br> [Module 05-08 – Thực hành và nghiên cứu bổ sung](https://www.youtube.com/watch?v=0SdpD2GPYz4) |
| 4 | - Học nền tảng cơ sở dữ liệu trong Module 06-01: mô hình quan hệ và phi quan hệ, OLTP và OLAP, chỉ mục <br>- Học Amazon RDS và Amazon Aurora trong Module 06-02: triển khai Multi-AZ, read replica và sao lưu tự động | 28/10/26 | 28/10/26 | [Module 06-01 – Khái niệm cơ sở dữ liệu](https://www.youtube.com/watch?v=OOD2RwWuLRw) <br> [Module 06-02 – Amazon RDS và Amazon Aurora](https://www.youtube.com/watch?v=qbrobQZrokY) |
| 5 | - Học Amazon Redshift và Amazon ElastiCache trong Module 06-03 <br>- **Thực hành (Lab05):** <br>&emsp; + Chuẩn bị VPC, security group và DB subnet group <br>&emsp; + Tạo RDS instance và kết nối ứng dụng mẫu chạy trên EC2 <br>&emsp; + Tạo snapshot và khôi phục cơ sở dữ liệu từ snapshot đó | 29/10/26 | 29/10/26 | [Module 06-03 – Amazon Redshift và ElastiCache](https://www.youtube.com/watch?v=UvdiRW34aNI) <br> [Lab05 – 2.3 Create database subnet group](https://000005.awsfcaj.com/2-prerequiste/2.3-create-rds-subnet-group/) <br> [Lab05 – 3. Create RDS database instance](https://000005.awsfcaj.com/3-create-rds/) <br> [Lab05 – 5. Application deployment](https://000005.awsfcaj.com/5-deploy-app/) <br> [Lab05 – 6. Backup and restore](https://000005.awsfcaj.com/6-backup/) |
| 6 | - **Thực hành (Lab43 – phần 1):** <br>&emsp; + Chuẩn bị môi trường migration và kết nối cơ sở dữ liệu nguồn <br>&emsp; + Cấu hình cơ sở dữ liệu nguồn cho việc migration <br>&emsp; + Chuyển đổi schema nguồn bằng AWS Schema Conversion Tool và xem lại các mục cần chỉnh tay | 30/10/26 | 30/10/26 | [Lab43 – Database Schema Conversion & Migration](https://000043.awsfcaj.com/) <br> [Video Lab43-01 – Kết nối EC2 bằng RDP](https://www.youtube.com/watch?v=cxwAOP1379s) <br> [Video Lab43-03 – Cấu hình nguồn SQL Server](https://www.youtube.com/watch?v=cXbuxFVL6mU) <br> [Video Lab43-08 – Tạo project chuyển đổi](https://www.youtube.com/watch?v=bTWkX3xHN4s) <br> [Video Lab43-09 – Chuyển đổi schema sang Aurora MySQL](https://www.youtube.com/watch?v=s-6mXTFXwG8) |

### Kết quả đạt được tuần 7:

* **Kiến thức:**
  * AWS KMS: customer managed key được kiểm soát bằng key policy và S3 có thể mã hóa object bằng key đó (SSE-KMS)
  * CloudTrail ghi lại lời gọi API vào bucket S3 và Athena truy vấn được các log đó bằng SQL
  * IAM role gắn vào EC2 cung cấp thông tin xác thực tạm thời qua instance profile, không cần lưu key trên máy chủ
  * RDS Multi-AZ duy trì một bản standby đồng bộ để failover, còn read replica sao chép bất đồng bộ để mở rộng khả năng đọc
  * Redshift là kho dữ liệu dạng cột cho phân tích, ElastiCache cung cấp bộ nhớ đệm in-memory với Redis hoặc Memcached
* **Kỹ năng thực hành:**
  * Mã hóa dữ liệu S3 bằng KMS key của mình và lần vết truy cập qua log CloudTrail trên Athena
  * Triển khai ứng dụng trên EC2 dùng RDS và khôi phục cơ sở dữ liệu từ snapshot
  * Chuyển đổi schema cơ sở dữ liệu bằng AWS Schema Conversion Tool
* **Bài học bảo mật và chi phí:**
  * Không bao giờ lưu access key trên máy chủ; IAM role là lựa chọn an toàn mặc định
  * Cơ sở dữ liệu nên nằm trong subnet private, với security group chỉ nhận lưu lượng từ ứng dụng
  * RDS instance, snapshot và KMS key đều phát sinh chi phí liên tục, và KMS key khi xóa phải chờ 7–30 ngày
