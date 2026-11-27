---
title: "Worklog Tuần 10"
date: 2026-11-05
weight: 10
chapter: false
pre: "<b>1.10. </b>"
---

### Mục tiêu tuần 10:

* Tìm hiểu cách ứng dụng trên EC2 lấy credentials của IAM role và đăng Blog 2 về IAM role và IMDSv2.
* Cập nhật báo cáo với trang Blog 1 song ngữ và bài thu hoạch Event 4, Event 5.
* Bắt đầu lập kế hoạch workshop cá nhân: yêu cầu, dàn ý proposal và checklist thiết kế kiến trúc.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Nghiên cứu cho Blog 2 – IAM role trên EC2 và IMDSv2:** <br>&emsp; + Đọc lý do AWS khuyến nghị dùng credentials tạm thời của IAM role thay cho access key dài hạn với workload chạy trên AWS <br>&emsp; + Tìm hiểu instance profile: console tự tạo instance profile cùng tên với role, mỗi instance profile chỉ chứa một role, muốn đổi quyền thì thay instance profile <br>&emsp; + Lần theo nguồn cấp credentials: IMDS tại `169.254.169.254`, đường dẫn `iam/security-credentials/<role-name>`, cơ chế tự xoay vòng và việc cache để tránh IMDS bị giới hạn tần suất <br>&emsp; + Tìm hiểu luồng phiên của IMDSv2 (PUT lấy token với TTL tối đa 6 giờ, sau đó GET kèm header token) và cách nó chống open WAF, reverse proxy, SSRF và firewall mở | 16/11/2026 | 16/11/2026 | <https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html> <br> <https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/> |
| 3 | - **Blog 2:** hoàn thiện và đăng bài *IAM role trên EC2 và IMDSv2: Ứng dụng lấy credentials từ đâu?* lên AWS Study Group <br>&emsp; + Bổ sung các lỗi cấu hình thường gặp: hop limit 1 khiến container không lấy được token, curl không có `-f` lưu thông báo lỗi thành token, proxy gửi HTTP thay cho ứng dụng, và instance cũ vẫn dùng IMDSv1 dù đã đặt mặc định ở cấp tài khoản <br>&emsp; + Trình bày cách bắt buộc IMDSv2 khi khởi tạo (`HttpTokens=required`, hop limit 2 cho container) và ở cấp tài khoản <br>&emsp; + Chuẩn bị bản tiếng Việt để đăng Facebook và bản tiếng Anh cho báo cáo <br>- Đưa Blog 1 vào báo cáo thành trang song ngữ, kèm sơ đồ NAT gateway và nguồn hình <br>- Viết bài thu hoạch Event 4 (FCAJ Community Day, 31/10) và Event 5 (AWSxFPTU Cloud Mastery 1, 14/11) kèm ảnh check-in và ảnh các phiên | 17/11/2026 | 17/11/2026 | <https://www.facebook.com/groups/awsstudygroupfcj/posts/2340606156704343> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html> |
| 4 | - **Lập kế hoạch workshop – yêu cầu:** <br>&emsp; + Đọc lại yêu cầu workshop của FCAJ: use-case thực tế trên AWS (serverless, data pipeline, giám sát, event-driven, container…) với tối thiểu 3 dịch vụ AWS <br>&emsp; + Rà soát bộ tiêu chuẩn workshop: kiến trúc tuân theo Well-Architected Framework, hướng dẫn từng bước tái lập được, demo chạy thực tế, giám sát bằng log, metric, cảnh báo, dự toán bằng Pricing Calculator và hướng dẫn clean-up đầy đủ <br>&emsp; + Ghi chú quy tắc chấm điểm: thiếu COST nhận 0 điểm mục Trình bày, không có demo hoạt động nhận 0 điểm mục Demo <br>&emsp; + Đối chiếu từng yêu cầu với các mục 5.1–5.9 của báo cáo và chuyển thành checklist hoàn thành | 18/11/2026 | 18/11/2026 | <https://hcm-rules.awsfcaj.com/project/requirement> <br> <https://hcm-rules.awsfcaj.com/project/standard> |
| 5 | - **Lập kế hoạch workshop – dàn ý proposal:** <br>&emsp; + Tìm hiểu cấu trúc proposal mẫu: tóm tắt, bài toán, kiến trúc giải pháp, triển khai kỹ thuật, timeline, ngân sách, đánh giá rủi ro và kết quả kỳ vọng <br>&emsp; + Lập dàn ý proposal của mình: bài toán thực tế và đối tượng sử dụng, mục tiêu đo được và tiêu chí thành công, các dịch vụ AWS kèm lý do chọn từng dịch vụ <br>&emsp; + Liệt kê các rủi ro chính (chi phí ngoài dự kiến, cấp quyền thừa hoặc lộ secret, triển khai thất bại, trễ hạn nộp) và cách giảm thiểu từng rủi ro | 19/11/2026 | 19/11/2026 | <https://workshop-sample.awsfcaj.com/2-proposal/> <br> <https://github.com/thienluhoan/fcj-workshop-template> <br> <https://hcm-rules.awsfcaj.com/project/standard> |
| 6 | - **Lập kế hoạch workshop – kiến trúc và rà soát thiết kế:** <br>&emsp; + Chuẩn bị tự vẽ sơ đồ trên draw.io bằng bộ AWS Architecture Icons chính thức, ghi đúng tên dịch vụ và mũi tên luồng dữ liệu rõ ràng <br>&emsp; + Lập checklist thiết kế theo Well-Architected Framework, trọng tâm là bảo mật: IAM role theo least privilege, hạn chế đưa tài nguyên ra Internet (private subnet, VPC endpoint, security group chặt), không hard-code credentials <br>&emsp; + Bổ sung các điểm về độ tin cậy và vận hành: thiết kế event-driven hoặc dùng SQS để giảm tải, có log, metric và alarm CloudWatch ngay từ đầu | 20/11/2026 | 20/11/2026 | <https://www.youtube.com/watch?v=l8isyDe-GwY> <br> <https://aws.amazon.com/architecture/icons/> <br> <https://docs.aws.amazon.com/wellarchitected/latest/framework/framework.html> |

### Kết quả đạt được tuần 10:

* Hiểu được các kiến thức sau:
  * EC2 nhận IAM role qua instance profile; SDK và AWS CLI đọc credentials tạm thời của role từ IMDS nên không cần lưu access key trên instance
  * Credentials của role được tự động xoay vòng, bộ mới có sẵn ít nhất 5 phút trước khi bộ cũ hết hạn
  * IMDSv2 yêu cầu PUT để lấy session token rồi mới GET kèm token; token gắn với instance đã tạo ra nó, token sai trả về 401
  * IMDSv2 từ chối PUT có header `X-Forwarded-For` và phản hồi token có hop limit 1, nhờ đó chặn được phần lớn request chuyển tiếp và SSRF
  * IMDSv2 không thay thế least privilege: code chạy trên instance vẫn dùng được quyền của role
  * Workshop đạt chuẩn FCAJ cần thiết kế theo Well-Architected, hướng dẫn tái lập, giám sát, dự toán bằng Pricing Calculator, các bước clean-up và demo hoạt động; thiếu COST hoặc demo sẽ mất trọn một mục điểm

* Viết và đăng blog kỹ thuật thứ hai dựa trên EC2 User Guide, IAM User Guide và AWS Security Blog.

* Cập nhật báo cáo với các trang blog và sự kiện song ngữ.

* Chuyển yêu cầu workshop thành checklist hoàn thành, dàn ý proposal và checklist thiết kế.

* Xác định các bước tiếp theo:
  * Nghiên cứu và viết Blog 3 về tính sẵn sàng cao của Amazon RDS
  * Hoàn tất kế hoạch workshop: dự toán chi phí, clean-up, kiểm thử và giám sát
