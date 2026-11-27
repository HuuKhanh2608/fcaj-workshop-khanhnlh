---
title: "Các bài blogs đã đăng"
date: 2026-11-05
weight: 3
chapter: false
pre: "<b>3. </b>"
---

Phần này liệt kê các bài blog tôi đã đăng trên [AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj).

###  [Blog 1 - Dọn dẹp tài nguyên AWS: Những khoản phí vẫn phát sinh sau khi đã "tắt"](3.1-Blog1/)
Tổng hợp từ tài liệu và trang pricing chính thức của AWS: vì sao tài nguyên đã "tắt" vẫn bị tính phí, các khoản dễ bỏ sót (NAT Gateway, public IPv4, snapshot và AMI, DMS, Quick Sight, Athena), giới hạn của AWS Budgets và quy trình dọn dẹp sau khi thực hành.

###  [Blog 2 - IAM role trên EC2 và IMDSv2: Ứng dụng lấy credentials từ đâu?](3.2-Blog2/)
Giải thích cơ chế instance profile cấp credentials tạm thời của IAM role cho EC2 qua Instance Metadata Service, luồng token của IMDSv2 (PUT lấy token, GET kèm token), vì sao IMDSv2 giảm rủi ro SSRF và proxy mở, các lỗi cấu hình thường gặp và cách bắt buộc dùng IMDSv2.

###  [Blog 3 - Amazon RDS: Multi-AZ hay Read Replica? Chọn đúng giữa high availability và read scaling](3.3-Blog3/)
So sánh Multi-AZ DB instance (synchronous standby, không phục vụ read traffic), Multi-AZ DB cluster (một writer, hai reader ở ba AZ, semisynchronous replication) và read replica (asynchronous replication, promote thủ công, có thể đặt ở Region khác): cơ chế replication, failover, giới hạn, cách kết hợp và những gì ứng dụng cần làm để xử lý failover.
