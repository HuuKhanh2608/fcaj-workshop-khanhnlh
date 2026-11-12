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
| 2 | - **Thực hành (Lab33):** <br>&emsp; + Chuẩn bị IAM policy, role, group và user cho bài lab <br>&emsp; + Tạo KMS key và tải dữ liệu lên S3 được mã hóa bằng key đó <br>&emsp; + Ghi lại hoạt động API bằng CloudTrail và truy vấn log bằng Athena <br>&emsp; + Kiểm tra ai đọc được object đã mã hóa khi chia sẻ | 26/10/26 | 26/10/26 | <https://000033.awsfcaj.com/> |
| 3 | - **Thực hành (Lab48):** <br>&emsp; + Truy cập S3 từ EC2 bằng access key lưu trên máy chủ <br>&emsp; + Thay access key bằng IAM role gắn vào instance <br>- Ôn tập Module 05 và tài liệu đọc thêm (05-08) | 27/10/26 | 27/10/26 | <https://000048.awsfcaj.com/> <br> [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - Học nền tảng cơ sở dữ liệu trong Module 06-01: mô hình quan hệ và phi quan hệ, OLTP và OLAP, chỉ mục <br>- Học Amazon RDS và Amazon Aurora trong Module 06-02: triển khai Multi-AZ, read replica và sao lưu tự động | 28/10/26 | 28/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 5 | - Học Amazon Redshift và Amazon ElastiCache trong Module 06-03 <br>- **Thực hành (Lab05):** <br>&emsp; + Chuẩn bị VPC, security group và DB subnet group <br>&emsp; + Tạo RDS instance và kết nối ứng dụng mẫu chạy trên EC2 <br>&emsp; + Tạo snapshot và khôi phục cơ sở dữ liệu từ snapshot đó | 29/10/26 | 29/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000005.awsfcaj.com/> |
| 6 | - **Thực hành (Lab43 – phần 1):** <br>&emsp; + Chuẩn bị môi trường migration và kết nối cơ sở dữ liệu nguồn <br>&emsp; + Cấu hình cơ sở dữ liệu nguồn cho việc migration <br>&emsp; + Chuyển đổi schema nguồn bằng AWS Schema Conversion Tool và xem lại các mục cần chỉnh tay | 30/10/26 | 30/10/26 | <https://000043.awsfcaj.com/> |

### Kết quả đạt được tuần 7:

* Mã hóa dữ liệu S3 bằng KMS key của riêng mình và lần vết truy cập qua log CloudTrail trên Athena.
* Hiểu vì sao IAM role an toàn hơn access key lưu trên máy chủ: thông tin xác thực là tạm thời và được xoay vòng tự động.
* Phân biệt được các dịch vụ cơ sở dữ liệu:
  * RDS và Aurora cho workload giao dịch
  * Redshift cho phân tích dữ liệu
  * ElastiCache cho bộ nhớ đệm in-memory
* Triển khai ứng dụng dùng RDS và xác nhận khôi phục từ snapshot hoạt động.
