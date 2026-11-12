---
title: "Worklog Tuần 8"
date: 2026-11-05
weight: 8
chapter: false
pre: "<b>1.8. </b>"
---

### Mục tiêu tuần 8:

* Di chuyển dữ liệu giữa các hệ quản trị cơ sở dữ liệu bằng AWS DMS.
* Mô hình hóa và truy vấn dữ liệu trên Amazon DynamoDB.
* Xây dựng một data lake nhỏ, từ thu thập dữ liệu đến dashboard.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành (Lab43 – phần 2):** <br>&emsp; + Tạo replication instance, endpoint nguồn, endpoint đích và migration task <br>&emsp; + Chạy migration bằng DMS Serverless, dịch vụ tự điều chỉnh năng lực xử lý <br>&emsp; + Theo dõi task qua metric, log CloudWatch và xử lý các tình huống lỗi mẫu | 02/11/26 | 02/11/26 | <https://000043.awsfcaj.com/> |
| 3 | - **Thực hành (Lab60 – Amazon DynamoDB):** <br>&emsp; + Tìm hiểu partition key, sort key và secondary index quyết định những truy vấn nào thực hiện được <br>&emsp; + Tạo table, ghi, đọc và truy vấn item trên console và CloudShell <br>&emsp; + Thực hiện lại các thao tác bằng Python với boto3 | 03/11/26 | 03/11/26 | <https://000060.awsfcaj.com/> |
| 4 | - **Thực hành (Lab39 – DynamoDB Immersion Day):** <br>&emsp; + So sánh Query và Scan trên cùng một tập dữ liệu <br>&emsp; + Thêm global secondary index để phục vụ cách truy cập mới <br>&emsp; + Bật point-in-time recovery và tạo on-demand backup | 04/11/26 | 04/11/26 | <https://000039.awsfcaj.com/> |
| 5 | - **Thực hành (Lab35 – Data Lake):** <br>&emsp; + Đẩy dữ liệu mẫu vào S3 bằng Amazon Data Firehose <br>&emsp; + Chạy Glue Crawler để tạo Data Catalog <br>&emsp; + Truy vấn dữ liệu bằng Athena và vẽ biểu đồ trên QuickSight | 05/11/26 | 05/11/26 | <https://000035.awsfcaj.com/> |
| 6 | - **Thực hành (Lab40):** truy vấn dữ liệu chi phí và mức sử dụng bằng AWS Glue và Amazon Athena để xem chi phí tập trung ở đâu <br>- **Thực hành (Lab73):** xây dựng dashboard QuickSight có bộ lọc và thao tác tương tác | 06/11/26 | 06/11/26 | <https://000040.awsfcaj.com/> <br> <https://000073.awsfcaj.com/> |

### Kết quả đạt được tuần 8:

* Di chuyển cơ sở dữ liệu bằng AWS DMS và biết cần xem ở đâu khi task gặp lỗi.
* Học cách thiết kế table DynamoDB xuất phát từ các truy vấn ứng dụng cần, thay vì từ các thực thể.
* Xây dựng được pipeline phân tích hoạt động:
  * Thu thập bằng Firehose
  * Lập catalog bằng Glue
  * Truy vấn bằng Athena
  * Trực quan hóa bằng QuickSight
* Dùng được Athena để phân tích dữ liệu chi phí, hỗ trợ cho phần dự toán chi phí của workshop.
