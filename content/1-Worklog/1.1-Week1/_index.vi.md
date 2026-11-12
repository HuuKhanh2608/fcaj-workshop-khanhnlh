---
title: "Worklog Tuần 1"
date: 2026-11-05
weight: 1
chapter: false
pre: "<b>1.1. </b>"
---

### Mục tiêu tuần 1:

* Hòa nhập với chương trình FCAJ và nắm rõ những gì cần hoàn thành khi kết thúc kỳ thực tập.
* Hình thành nền tảng vững chắc về điện toán đám mây và hạ tầng toàn cầu của AWS.
* Chuẩn bị tài khoản AWS cá nhân an toàn ngay từ đầu và tránh phát sinh chi phí ngoài ý muốn.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tham gia buổi onboarding FCAJ, làm quen với đội ngũ và các bạn thực tập <br>- Tìm hiểu yêu cầu của chương trình: đặt lịch lên văn phòng, sự kiện, blog và workshop cuối kỳ <br>- Xem video kick-off Bootcamp và hướng dẫn làm workshop để nắm cách tổ chức 12 tuần | 14/09/26 | 14/09/26 | [Video – First Cloud Journey Kick-off](https://www.youtube.com/watch?v=AQlsd0nWdZk) <br> [Video – Hướng dẫn làm workshop AWS](https://www.youtube.com/watch?v=mXRqgMr_97U) <br> [FCAJ – Yêu cầu workshop](https://hcm-rules.awsfcaj.com/project/requirement) |
| 3 | - Học kiến thức cloud nền tảng trong Module 01-01 → 01-04: <br>&emsp; + Tài nguyên theo nhu cầu và trả theo mức dùng so với đầu tư phần cứng từ trước <br>&emsp; + Điểm khác biệt của AWS: số lượng dịch vụ, độ phủ toàn cầu và cộng đồng lớn <br>&emsp; + Các bước một tổ chức thực hiện khi bắt đầu chuyển lên cloud <br>&emsp; + Region, Availability Zone, Edge Location và vai trò của chúng đối với tính sẵn sàng, độ trễ | 15/09/26 | 15/09/26 | [Module 01-01 – Điện toán đám mây là gì?](https://www.youtube.com/watch?v=HxYZAK1coOI) <br> [Module 01-02 – Điều gì tạo nên sự khác biệt của AWS?](https://www.youtube.com/watch?v=IK59Zdd1poE) <br> [Module 01-03 – Bắt đầu hành trình lên mây](https://www.youtube.com/watch?v=HSzrWGqo3ME) <br> [Module 01-04 – Hạ tầng toàn cầu của AWS](https://www.youtube.com/watch?v=pjr5a-HYAjI) |
| 4 | - Học các cách làm việc với AWS trong Module 01-05: Management Console, AWS CLI, SDK và CloudShell <br>- **Thực hành (Lab01 – AWS Free Tier 2026):** <br>&emsp; + Đăng ký theo quy trình mới, tạo project đầu tiên và kiểm tra credit $100 khi đăng ký <br>&emsp; + Nâng lên Paid plan kèm giới hạn chi tiêu hằng tháng để chi phí lab luôn trong tầm kiểm soát <br>&emsp; + Tìm hiểu 5 hoạt động nhận thêm credit và các dịch vụ dễ làm cạn credit | 16/09/26 | 16/09/26 | [Module 01-05 – Công cụ quản lý dịch vụ AWS](https://www.youtube.com/watch?v=2PQYqH_HkXw) <br> [Lab01 – 3. Create your AWS account](https://000001.awsfcaj.com/3-chi%E1%BA%BFn-l%C6%B0%E1%BB%A3c-nh%E1%BA%ADn-%C4%91%E1%BB%A7-200-credit/) <br> [Lab01 – 4. Earn up to $100 more](https://000001.awsfcaj.com/4-h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-chi-ti%E1%BA%BFt-5-nhi%E1%BB%87m-v%E1%BB%A5-ki%E1%BA%BFm-ti%E1%BB%81n/) <br> [Lab01 – 6. Services to avoid on the Free Plan](https://000001.awsfcaj.com/6-danh-s%C3%A1ch-s%C3%A1t-th%E1%BB%A7-credit-c%E1%BA%A7n-tr%C3%A1nh/) |
| 5 | - Học tối ưu chi phí và các gói AWS Support trong Module 01-06 <br>- **Thực hành (bảo mật tài khoản):** <br>&emsp; + Bật virtual MFA cho root user <br>&emsp; + Tạo nhóm Admins có quyền quản trị và một IAM admin user thuộc nhóm này <br>&emsp; + Đăng nhập bằng IAM user qua đường dẫn đăng nhập của tài khoản và xem các cách khôi phục tài khoản | 17/09/26 | 17/09/26 | [Module 01-06 – Tối ưu chi phí và AWS Support](https://www.youtube.com/watch?v=IY61YlmXQe8) <br> [Video Lab01-02 – Thiết lập virtual MFA](https://www.youtube.com/watch?v=1dG5xutGbr4) <br> [Video Lab01-03 – Tạo admin group và admin user](https://www.youtube.com/watch?v=b9pK1oG534Q) <br> [Lab IAM – 2.2 Create Admin User](https://000002.awsfcaj.com/2-create-admin-user-and-group/2.2-create-admin-user/) <br> [Video Lab01-04 – Hỗ trợ xác thực tài khoản](https://www.youtube.com/watch?v=69iKhwI7k2Y) |
| 6 | - **Thực hành (Lab07 – AWS Budgets):** <br>&emsp; + Tạo cost budget hằng tháng, gửi cảnh báo qua email khi chi phí vượt ngưỡng <br>&emsp; + Thêm usage budget, budget cho Reserved Instances và Savings Plans để hiểu mỗi loại theo dõi gì, sau đó xóa <br>- **Thực hành (Lab09 – AWS Support):** so sánh các gói Support, tìm hiểu loại yêu cầu và mức độ nghiêm trọng <br>- Tổng hợp các điểm chính của Module 01 vào ghi chú | 18/09/26 | 18/09/26 | [Lab07 – 2. Create Cost Budget](https://000007.awsfcaj.com/2-cost-budgets/) <br> [Lab07 – 3. Create Usage Budget](https://000007.awsfcaj.com/3-usage-budget/) <br> [Lab09 – 1. AWS Support Plans](https://000009.awsfcaj.com/1-support-plans/) <br> [Lab09 – 3.2 Select Severity Level](https://000009.awsfcaj.com/3-manage-cases/3.2-select-severity/) <br> [Module 01-07 – Thực hành và nghiên cứu bổ sung](https://www.youtube.com/watch?v=Hku7exDBURo) |

### Kết quả đạt được tuần 1:

* **Kiến thức:**
  * Điện toán đám mây: tài nguyên theo nhu cầu, khả năng co giãn và trả theo mức dùng thay vì đầu tư phần cứng từ trước
  * Hạ tầng toàn cầu của AWS: mỗi Region gồm nhiều Availability Zone tách biệt, còn Edge Location đưa nội dung đến gần người dùng qua CloudFront
  * AWS Free Tier 2026: khác biệt giữa Free plan và Paid plan, cách nhận credit và những dịch vụ tiêu tốn credit nhanh nhất
  * AWS Support: quyền lợi của từng gói và ảnh hưởng của mức độ nghiêm trọng tới thời gian phản hồi
* **Kỹ năng thực hành:**
  * Tạo tài khoản AWS theo quy trình đăng ký mới và đặt giới hạn chi tiêu hằng tháng
  * Bảo vệ root user bằng MFA và chuyển công việc hằng ngày sang IAM admin user
  * Cấu hình cost budget, usage budget kèm cảnh báo qua email
* **Bài học bảo mật và chi phí:**
  * Root user chỉ dùng cho tác vụ cấp tài khoản và thiết bị MFA cần được giữ an toàn
  * Cần đặt giới hạn chi tiêu và budget trước khi làm lab để sớm phát hiện tài nguyên bị bỏ quên
