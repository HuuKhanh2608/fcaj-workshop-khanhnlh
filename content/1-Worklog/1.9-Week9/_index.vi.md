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
| 2 | - **Thực hành (Lab70):** <br>&emsp; + Profiling và làm sạch bộ dữ liệu của lab bằng AWS Glue DataBrew <br>&emsp; + Chuyển dữ liệu sang định dạng Parquet bằng AWS Glue <br>&emsp; + So sánh truy vấn Athena khi có và không có phân vùng, định dạng cột | 09/11/2026 | 09/11/2026 | <https://000070.awsfcaj.com/2-datapre/2.2-profiling/> <br> <https://000070.awsfcaj.com/2-datapre/2.3-cleantransform/> <br> <https://000070.awsfcaj.com/3-ingestglue/3.3-transformparquet/> <br> <https://000070.awsfcaj.com/5-athena/5.6-partition/> <br> <https://000070.awsfcaj.com/5-athena/5.7-columnar/> |
| 3 | - **Thực hành (Lab72 – Analytics on AWS):** <br>&emsp; + Thu thập dữ liệu streaming bằng Firehose và lập catalog bằng Glue <br>&emsp; + Biến đổi dữ liệu bằng Glue Studio và DataBrew <br>&emsp; + Truy vấn kết quả bằng Athena và trả ra qua một Lambda function | 10/11/2026 | 10/11/2026 | <https://000072.awsfcaj.com/3.ingestandstore/3.1-create-kinesis-firehose/> <br> <https://000072.awsfcaj.com/4.catalogdata/4.2-create-aws-glue-crawlers/> <br> <https://000072.awsfcaj.com/6-graphical-interface/> <br> <https://000072.awsfcaj.com/9-athena/> <br> <https://000072.awsfcaj.com/12-lambda/> |
| 4 | - Ôn lại Module 01 → 07 và ghi chú những dịch vụ mình nắm chắc nhất <br>- Đọc lại yêu cầu workshop: kiến trúc, hướng dẫn tái lập, giám sát, dự toán chi phí, clean-up và demo <br>- Liệt kê các đề tài workshop sử dụng tối thiểu 3 dịch vụ AWS | 11/11/2026 | 11/11/2026 | <https://www.youtube.com/watch?v=mXRqgMr_97U> <br> <https://hcm-rules.awsfcaj.com/project/requirement> |
| 5 | - Đối chiếu báo cáo với template workshop FCJ chính thức <br>- Chỉnh lại cấu trúc các trang Worklog, Proposal, Blogs và Self-assessment theo template <br>- Lập kế hoạch 12 tuần dựa trên playlist và các lab FCJ | 12/11/2026 | 12/11/2026 | <https://github.com/thienluhoan/fcj-workshop-template> <br> <https://workshop-sample.awsfcaj.com/> |
| 6 | - Xem hướng dẫn vẽ sơ đồ kiến trúc AWS bằng draw.io <br>- Thu hẹp lựa chọn đề tài workshop và phác thảo bản nháp kiến trúc đầu tiên <br>- **Blog 1:** đăng bài *Dọn dẹp tài nguyên AWS: Những khoản phí vẫn phát sinh sau khi đã "tắt"* lên AWS Study Group <br>&emsp; + Đối chiếu trang giá chính thức của các khoản phí còn lại sau khi làm lab: giờ chạy NAT gateway, địa chỉ IPv4 public, snapshot EBS và AMI, replication instance của DMS, người dùng Quick Sight và kết quả truy vấn Athena <br>&emsp; + Giải thích vì sao EC2 đã stop vẫn tính phí EBS và Elastic IP, và vì sao AWS Budgets chỉ gửi cảnh báo <br>&emsp; + Đề xuất thứ tự dọn dẹp và bước kiểm tra cuối bằng AWS Resource Explorer và Billing | 13/11/2026 | 13/11/2026 | <https://www.youtube.com/watch?v=l8isyDe-GwY> <br> <https://www.facebook.com/groups/awsstudygroupfcj/posts/2336113367153622> <br> <https://aws.amazon.com/vpc/pricing/> <br> <https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html> |

### Kết quả đạt được tuần 9:

* Hiểu được các kiến thức sau:
  * Glue DataBrew phân tích tổng quan bộ dữ liệu và áp dụng các bước làm sạch dưới dạng recipe dùng lại được
  * Parquet lưu dữ liệu theo cột nên Athena chỉ đọc các cột truy vấn cần; phân vùng giúp bỏ qua cả thư mục dữ liệu
  * Một nền tảng phân tích có thể kết hợp thu thập streaming, ETL bằng Glue hoặc EMR, SQL bằng Athena, kho dữ liệu Redshift và API qua Lambda
  * Instance đã stop vẫn tính phí volume EBS và Elastic IP; NAT gateway và địa chỉ IPv4 public tính phí theo giờ kể cả khi không có traffic
  * Workshop cần có sơ đồ kiến trúc, hướng dẫn tái lập, giám sát bằng log, metric, cảnh báo, dự toán chi phí, các bước clean-up và demo hoạt động

* Xây dựng luồng ETL chuyển dữ liệu thô thành bảng Parquet có phân vùng.

* Truy vấn và trả kết quả phân tích bằng Athena và Lambda.

* Chỉnh lại báo cáo thực tập theo đúng template chính thức.

* Viết và đăng blog đầu tiên lên AWS Study Group, dựa trên tài liệu và trang giá chính thức của AWS.

* Xác định các bước tiếp theo:
  * Chốt đề tài workshop và hoàn thiện sơ đồ kiến trúc
  * Viết proposal và dự toán chi phí bằng AWS Pricing Calculator
