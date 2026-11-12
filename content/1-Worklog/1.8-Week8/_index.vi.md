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
| 2 | - **Thực hành (Lab43 – phần 2):** <br>&emsp; + Tạo replication instance, endpoint nguồn, endpoint đích và migration task <br>&emsp; + Chạy migration bằng DMS Serverless, dịch vụ tự điều chỉnh năng lực xử lý <br>&emsp; + Theo dõi task qua metric, log CloudWatch và xử lý các tình huống lỗi mẫu | 02/11/26 | 02/11/26 | [Lab43 – Database Schema Conversion & Migration](https://000043.awsfcaj.com/) <br> [Video Lab43-11 – Tạo migration task và endpoint](https://www.youtube.com/watch?v=4LoLN6D1UU8) <br> [Video Lab43-13 – Tạo serverless migration](https://www.youtube.com/watch?v=tWGwAz_Ewk4) <br> [Video Lab43-15 – Task log](https://www.youtube.com/watch?v=TDlc5bRh6H8) <br> [Video Lab43-17 – Xử lý lỗi bảng](https://www.youtube.com/watch?v=MU8XHe3OoxQ) |
| 3 | - **Thực hành (Lab60 – Amazon DynamoDB):** <br>&emsp; + Tìm hiểu partition key, sort key và secondary index quyết định những truy vấn nào thực hiện được <br>&emsp; + Tạo table, ghi, đọc và truy vấn item trên console và CloudShell <br>&emsp; + Thực hiện lại các thao tác bằng Python với boto3 | 03/11/26 | 03/11/26 | [Lab60 – 1.2 Primary Key](https://000060.awsfcaj.com/1-introduce/1.2-primarykey/) <br> [Lab60 – 1.3 Secondary Index](https://000060.awsfcaj.com/1-introduce/1.3-secondaryindexes/) <br> [Lab60 – 1.6 Read/Write Capacity Mode](https://000060.awsfcaj.com/1-introduce/1.6-readwritecapacitymode/) <br> [Lab60 – 2.2 Use AWS CloudShell](https://000060.awsfcaj.com/2-prerequiste/2.2-useawscloudshell/) <br> [Lab60 – 3.2 Python and DynamoDB](https://000060.awsfcaj.com/3-gettingstartedwithawssdk/3.2-pythonandynamodb/) |
| 4 | - **Thực hành (Lab39 – DynamoDB Immersion Day):** <br>&emsp; + So sánh Query và Scan trên cùng một tập dữ liệu <br>&emsp; + Thêm global secondary index để phục vụ cách truy cập mới <br>&emsp; + Bật point-in-time recovery và tạo on-demand backup | 04/11/26 | 04/11/26 | [Lab39 – 1.2 Explore DynamoDB with the CLI](https://000039.awsfcaj.com/1-lhol/1.2/) <br> [Lab39 – 1.3 Explore the DynamoDB Console](https://000039.awsfcaj.com/1-lhol/1.3/) <br> [Lab39 – 1.4 Backups](https://000039.awsfcaj.com/1-lhol/1.4/) |
| 5 | - **Thực hành (Lab35 – Data Lake):** <br>&emsp; + Đẩy dữ liệu mẫu vào S3 bằng Amazon Data Firehose <br>&emsp; + Chạy Glue Crawler để tạo Data Catalog <br>&emsp; + Truy vấn dữ liệu bằng Athena và vẽ biểu đồ trên QuickSight | 05/11/26 | 05/11/26 | [Lab35 – 3.2 Create Firehose Stream](https://000035.awsfcaj.com/3-ingestandstore/3.2-createdeliverystream/) <br> [Lab35 – 3.3 Create Sample Data](https://000035.awsfcaj.com/3-ingestandstore/3.3-generatesampledata/) <br> [Lab35 – 4.1 Create Glue Crawler](https://000035.awsfcaj.com/4-createdatacatalog/4.1-creategluecrawler/) <br> [Lab35 – 6.1 Analysis with Athena](https://000035.awsfcaj.com/6-analyzeandvisualize/6.1-analyzedatawithathena/) <br> [Lab35 – 6.2 Visualize with Amazon Quick](https://000035.awsfcaj.com/6-analyzeandvisualize/6.2-visualizewithquicksight/) |
| 6 | - **Thực hành (Lab40):** truy vấn dữ liệu chi phí và mức sử dụng bằng AWS Glue và Amazon Athena để xem chi phí tập trung ở đâu và tag phân bổ chi phí ra sao <br>- **Thực hành (Lab73):** xây dựng dashboard QuickSight gồm biểu đồ đường, KPI, biểu đồ tròn, sau đó thêm bộ lọc và thao tác tương tác | 06/11/26 | 06/11/26 | [Lab40 – 3.2 Cost Research](https://000040.awsfcaj.com/3-costandusageanalysis/3.2-cost/) <br> [Lab40 – 3.3 Tagging and Cost Allocation](https://000040.awsfcaj.com/3-costandusageanalysis/3.3-taggingandcost/) <br> [Lab73 – 3. Build dashboard](https://000073.awsfcaj.com/2-first-dashboard/) <br> [Lab73 – 5. Create Interactive Dashboard](https://000073.awsfcaj.com/4-add-interactivity/) |

### Kết quả đạt được tuần 8:

* **Kiến thức:**
  * AWS DMS: replication instance chạy task giữa endpoint nguồn và đích, gồm full load rồi đến change data capture liên tục
  * DynamoDB: partition key phân tán dữ liệu ra các partition, sort key sắp xếp item trong một partition, global secondary index bổ sung một cách truy cập mới
  * Capacity mode: on-demand cho lưu lượng khó dự đoán, provisioned cho lưu lượng ổn định; mặc định đọc theo eventual consistency
  * Luồng data lake: Firehose gom dữ liệu vào S3, Glue Crawler đăng ký bảng trong Data Catalog, Athena chạy SQL trực tiếp trên S3 và QuickSight trực quan hóa kết quả
* **Kỹ năng thực hành:**
  * Di chuyển cơ sở dữ liệu bằng DMS và DMS Serverless, giám sát qua CloudWatch và task log
  * Tạo, truy vấn và sao lưu table DynamoDB từ console, CloudShell và boto3
  * Xây dựng pipeline thu thập → lập catalog → truy vấn → dashboard hoạt động
* **Bài học bảo mật và chi phí:**
  * Scan đọc toàn bộ table, nên thiết kế để dùng Query giúp giảm cả độ trễ lẫn chi phí
  * Athena tính phí theo lượng dữ liệu quét, còn replication instance của DMS và gói QuickSight cần được gỡ sau lab
