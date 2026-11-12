---
title: "Worklog Tuần 9"
date: 2026-11-05
weight: 9
chapter: false
pre: "<b>1.9. </b>"
---

### Mục tiêu tuần 9:

* Hoàn thành các lab phân tích dữ liệu còn lại.
* Chọn đề tài workshop giải quyết một bài toán thực tế với tối thiểu 3 dịch vụ AWS.
* Đưa báo cáo thực tập về đúng template chính thức.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành (Lab70):** <br>&emsp; + Profiling và làm sạch bộ dữ liệu của lab bằng AWS Glue DataBrew <br>&emsp; + Chuyển dữ liệu sang định dạng Parquet bằng AWS Glue <br>&emsp; + So sánh truy vấn Athena khi có và không có phân vùng, định dạng cột | 09/11/26 | 09/11/26 | [Lab70 – 2.2 Data Profiling](https://000070.awsfcaj.com/2-datapre/2.2-profiling/) <br> [Lab70 – 2.3 Clean & Transform Data](https://000070.awsfcaj.com/2-datapre/2.3-cleantransform/) <br> [Lab70 – 3.3 Transform to Parquet](https://000070.awsfcaj.com/3-ingestglue/3.3-transformparquet/) <br> [Lab70 – 4.6 Data Partition](https://000070.awsfcaj.com/5-athena/5.6-partition/) <br> [Lab70 – 4.7 Columnar vs Row based](https://000070.awsfcaj.com/5-athena/5.7-columnar/) |
| 3 | - **Thực hành (Lab72 – Analytics on AWS):** <br>&emsp; + Thu thập dữ liệu streaming bằng Firehose và lập catalog bằng Glue <br>&emsp; + Biến đổi dữ liệu bằng Glue Studio và DataBrew <br>&emsp; + Truy vấn kết quả bằng Athena và trả ra qua một Lambda function | 10/11/26 | 10/11/26 | [Lab72 – 3.1 Creating Kinesis Firehose](https://000072.awsfcaj.com/3.ingestandstore/3.1-create-kinesis-firehose/) <br> [Lab72 – 4.2 Creating AWS Glue Crawlers](https://000072.awsfcaj.com/4.catalogdata/4.2-create-aws-glue-crawlers/) <br> [Lab72 – 6. Transform with AWS Glue Studio](https://000072.awsfcaj.com/6-graphical-interface/) <br> [Lab72 – 9. Analysis with Athena](https://000072.awsfcaj.com/9-athena/) <br> [Lab72 – 12. Serve with Lambda](https://000072.awsfcaj.com/12-lambda/) |
| 4 | - Ôn lại Module 01 → 07 và ghi chú những dịch vụ mình nắm chắc nhất <br>- Đọc lại yêu cầu workshop: kiến trúc, hướng dẫn tái lập, giám sát, dự toán chi phí, clean-up và demo <br>- Liệt kê các đề tài workshop sử dụng tối thiểu 3 dịch vụ AWS | 11/11/26 | 11/11/26 | [Video – Hướng dẫn làm workshop AWS](https://www.youtube.com/watch?v=mXRqgMr_97U) <br> [FCAJ – Yêu cầu workshop](https://hcm-rules.awsfcaj.com/project/requirement) |
| 5 | - Đối chiếu báo cáo với template workshop FCJ chính thức <br>- Chỉnh lại cấu trúc các trang Worklog, Proposal, Blogs và Self-assessment theo template <br>- Lập kế hoạch 12 tuần dựa trên playlist và các lab FCJ | 12/11/26 | 12/11/26 | [Template workshop FCJ (GitHub)](https://github.com/thienluhoan/fcj-workshop-template) <br> [Trang workshop mẫu FCJ](https://workshop-sample.awsfcaj.com/) |
| 6 | - Xem hướng dẫn vẽ sơ đồ kiến trúc AWS bằng draw.io <br>- Thu hẹp lựa chọn đề tài workshop và phác thảo bản nháp kiến trúc đầu tiên | 13/11/26 | 13/11/26 | [Video – Hướng dẫn vẽ kiến trúc AWS trên draw.io](https://www.youtube.com/watch?v=l8isyDe-GwY) |

### Kết quả đạt được tuần 9:

* **Kiến thức:**
  * Glue DataBrew phân tích tổng quan bộ dữ liệu và áp dụng các bước làm sạch dưới dạng recipe dùng lại được
  * Parquet lưu dữ liệu theo cột nên Athena chỉ đọc các cột truy vấn cần; phân vùng giúp bỏ qua cả thư mục dữ liệu
  * Một nền tảng phân tích có thể kết hợp thu thập streaming, ETL bằng Glue hoặc EMR, SQL bằng Athena, kho dữ liệu Redshift và API qua Lambda
  * Workshop cần có sơ đồ kiến trúc, hướng dẫn tái lập, giám sát bằng log, metric, cảnh báo, dự toán chi phí, các bước clean-up và demo hoạt động
* **Kỹ năng thực hành:**
  * Xây dựng luồng ETL chuyển dữ liệu thô thành bảng Parquet có phân vùng
  * Truy vấn và trả kết quả phân tích bằng Athena và Lambda
  * Chỉnh lại báo cáo thực tập theo đúng template chính thức
* **Bước tiếp theo:**
  * Chốt đề tài workshop và hoàn thiện sơ đồ kiến trúc
  * Viết proposal và dự toán chi phí bằng AWS Pricing Calculator
