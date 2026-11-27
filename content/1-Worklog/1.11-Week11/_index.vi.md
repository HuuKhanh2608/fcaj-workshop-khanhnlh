---
title: "Worklog Tuần 11"
date: 2026-11-05
weight: 11
chapter: false
pre: "<b>1.11. </b>"
---

### Mục tiêu tuần 11:

* Đăng Blog 3 so sánh các lựa chọn của Amazon RDS cho high availability và read scaling.
* Chuẩn hóa toàn bộ worklog theo template FCJ chính thức.
* Hoàn tất kế hoạch workshop: phương án dự toán chi phí, clean-up, kiểm thử và giám sát.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Blog 3:** hoàn thiện và đăng bài *Amazon RDS: Multi-AZ hay Read Replica? Chọn đúng giữa high availability và read scaling* lên AWS Study Group <br>&emsp; + So sánh Multi-AZ DB instance, Multi-AZ DB cluster và read replica theo cơ chế sao chép, failover, khả năng đọc từ bản sao, vị trí đặt và engine hỗ trợ <br>&emsp; + Multi-AZ DB instance: standby đồng bộ, không phục vụ đọc, failover qua DNS khoảng 60–120 giây, backup lấy từ standby <br>&emsp; + Multi-AZ DB cluster: 1 writer và 2 reader ở 3 AZ, sao chép bán đồng bộ, failover thường dưới 35 giây, các endpoint writer/reader/instance và các giới hạn <br>&emsp; + Read replica: sao chép bất đồng bộ, tối đa 15 replica (Oracle là 5), đặt được ở Region khác, promote thủ công thành instance độc lập <br>&emsp; + Liệt kê những việc ứng dụng phải làm: kết nối qua endpoint, giữ DNS TTL không quá 60 giây, kết nối lại và retry, tách đọc/ghi, đặt cảnh báo cho `ReplicaLag` và thử failover <br>&emsp; + Bổ sung 2 sơ đồ từ RDS User Guide kèm nguồn | 23/11/2026 | 23/11/2026 | <https://www.facebook.com/groups/awsstudygroupfcj/posts/2347065196058439> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Monitoring.html> |
| 3 | - **Lập kế hoạch workshop – chi phí và clean-up:** <br>&emsp; + Tìm hiểu cách dùng AWS Pricing Calculator: nhóm dịch vụ theo kiến trúc, xem cách tính từng mức giá, lưu link để chia sẻ và xuất ra CSV hoặc PDF <br>&emsp; + Lên phương án dự toán theo tải thực tế: số request, dung lượng lưu trữ và băng thông mạng, kèm Region và ngày lập dự toán <br>&emsp; + Liệt kê các phương án tối ưu chi phí cần đánh giá: Free Tier, dịch vụ serverless trả theo lượt dùng, S3 Lifecycle policy và chọn compute đúng cỡ <br>&emsp; + Soạn checklist clean-up (xóa stack, làm rỗng và xóa S3 bucket, xóa alarm, giải phóng Elastic IP), dùng lại kinh nghiệm từ Blog 1 | 24/11/2026 | 24/11/2026 | <https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html> <br> <https://calculator.aws/#/> <br> <https://hcm-rules.awsfcaj.com/project/standard> |
| 4 | - Đối chiếu worklog với template FCJ chính thức và trang mẫu <br>- Giữ mỗi tuần đúng 5 dòng từ thứ 2 đến thứ 6; sự kiện thứ 7 chỉ ghi ở mục Sự kiện <br>- Đổi ngày về định dạng của template: MM/DD/YYYY ở bản tiếng Anh và DD/MM/YYYY ở bản tiếng Việt | 25/11/2026 | 25/11/2026 | <https://github.com/thienluhoan/fcj-workshop-template> <br> <https://workshop-sample.awsfcaj.com/1-worklog/> |
| 5 | - **Lập kế hoạch workshop – kiểm thử và giám sát:** <br>&emsp; + Đọc bản cập nhật của Lab08 CloudWatch để lên phương án giám sát: metric với search expression và math expression, truy vấn Logs Insights, metric filter chuyển dòng lỗi thành metric, alarm gửi email qua Amazon SNS và dashboard <br>&emsp; + Lên các kịch bản kiểm thử: luồng chính và các trường hợp lỗi như request sai định dạng, quá tải; gửi bằng cURL hoặc Postman và kiểm tra trong CloudWatch Logs và dữ liệu được lưu <br>&emsp; + Lên phương án minh chứng demo (link chạy thực tế hoặc video) và chốt timeline tuần 12: triển khai, kiểm thử, COST, clean-up và demo | 26/11/2026 | 26/11/2026 | <https://000008.awsfcaj.com/3-cloud-watch-metric/> <br> <https://000008.awsfcaj.com/4-cloud-watch-logs/4.2-logs-insights/> <br> <https://000008.awsfcaj.com/4-cloud-watch-logs/4.3-metric-filter/> <br> <https://000008.awsfcaj.com/5-cloud-watch-alarm/> <br> <https://000008.awsfcaj.com/6-cloud-watch-dashboard/> |
| 6 | - Cập nhật mục Blogs đã đăng: <br>&emsp; + Bổ sung link bài đăng trên AWS Study Group và ngày đăng vào trang tiếng Anh và tiếng Việt của cả 3 blog <br>&emsp; + Mở từng link trên Facebook để đối chiếu tiêu đề và thời gian đăng <br>- Cập nhật worklog theo các blog: <br>&emsp; + Thêm việc đăng Blog 1 vào tuần 9 (13/11) <br>&emsp; + Ghi các ngày nghiên cứu và đăng Blog 2 ở tuần 10 (16/11–17/11), ngày đăng Blog 3 và ngày chuẩn hóa theo template ở tuần 11 (23/11, 25/11) <br>&emsp; + Dẫn nguồn mỗi công việc tới tài liệu AWS mà blog trích dẫn và cập nhật tiêu đề tuần 10, tuần 11 trên trang Worklog | 27/11/2026 | 27/11/2026 | <https://www.facebook.com/groups/awsstudygroupfcj/posts/2336113367153622> <br> <https://www.facebook.com/groups/awsstudygroupfcj/posts/2340606156704343> <br> <https://www.facebook.com/groups/awsstudygroupfcj/posts/2347065196058439> <br> <https://github.com/thienluhoan/fcj-workshop-template> |

### Kết quả đạt được tuần 11:

* Hiểu được các kiến thức sau:
  * Multi-AZ dùng để chịu lỗi, read replica dùng để chia tải đọc; có thể kết hợp cả hai
  * Standby của Multi-AZ DB instance không phục vụ đọc, và sao chép đồng bộ làm tăng độ trễ ghi và commit
  * Multi-AZ DB cluster commit khi ít nhất một reader xác nhận thay đổi và failover nhanh hơn, nhưng chỉ hỗ trợ MySQL, PostgreSQL trên một số instance class
  * Read replica có thể trễ so với nguồn, và việc promote là thủ công, không đảo ngược được
  * Failover làm đổi IP phía sau endpoint, nên ứng dụng phải dùng endpoint, DNS TTL ngắn và có cơ chế kết nối lại
  * Dự toán trên AWS Pricing Calculator được nhóm theo kiến trúc, chia sẻ được bằng link và xuất ra CSV hoặc PDF
  * CloudWatch có thể chuyển dòng log lỗi thành metric bằng metric filter và cảnh báo qua alarm và SNS

* Viết và đăng blog kỹ thuật thứ ba dựa trên Amazon RDS User Guide.

* Rà soát bảng công việc của cả 12 tuần theo template chính thức.

* Hoàn thiện mục Blogs đã đăng với link và ngày đăng đã đối chiếu của cả 3 blog.

* Lên kế hoạch dự toán chi phí, clean-up, kịch bản kiểm thử, giám sát và demo cho workshop.

* Xác định các bước tiếp theo:
  * Viết proposal và vẽ sơ đồ kiến trúc
  * Triển khai, kiểm thử và giám sát workshop, sau đó hoàn thiện COST, clean-up và demo trong tuần 12
