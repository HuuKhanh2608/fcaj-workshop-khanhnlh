---
title: "Worklog Tuần 6"
date: 2026-11-05
weight: 6
chapter: false
pre: "<b>1.6. </b>"
---

### Mục tiêu tuần 6:

* Hiểu ranh giới giữa trách nhiệm bảo mật của AWS và của người dùng.
* Áp dụng least privilege bằng IAM policy, condition và permission boundary.
* Dùng tag và Lambda để tổ chức tài nguyên và tự động hóa tác vụ lặp lại.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Học Shared Responsibility Model (Module 05-01) <br>- Học sâu về AWS IAM (Module 05-02): <br>&emsp; + User, group, role và các policy gắn với chúng <br>&emsp; + Cách một request được đánh giá, bao gồm tác động của explicit deny | 19/10/26 | 19/10/26 | [Module 05-01 – Mô hình trách nhiệm chia sẻ](https://www.youtube.com/watch?v=tsobAlSg19g) <br> [Module 05-02 – AWS Identity and Access Management](https://www.youtube.com/watch?v=N_vlJGAqZxo) |
| 3 | - Học các dịch vụ định danh và bảo mật trong Module 05-03 → 05-07: <br>&emsp; + Amazon Cognito cho người dùng ứng dụng và AWS Organizations để quản lý nhiều tài khoản <br>&emsp; + IAM Identity Center cho đăng nhập một lần và AWS KMS để quản lý khóa mã hóa <br>- **Thực hành (Lab18):** bật Security Hub và xem điểm số, các phát hiện theo từng bộ tiêu chuẩn bảo mật | 20/10/26 | 20/10/26 | [Module 05-03 – Amazon Cognito](https://www.youtube.com/watch?v=pZ2fgEFK3Vs) <br> [Module 05-04 – AWS Organizations](https://www.youtube.com/watch?v=5oQY8Rogz9Y) <br> [Module 05-05 – IAM Identity Center](https://www.youtube.com/watch?v=NW1xrMkNMjU) <br> [Module 05-06 – AWS Key Management Service](https://www.youtube.com/watch?v=GMihNQojhZc) <br> [Module 05-07 – AWS Security Hub](https://www.youtube.com/watch?v=clj2E0rNBEs) <br> [Lab18 – 2. Enable Security Hub](https://000018.awsfcaj.com/2-enable-sec-hub/) |
| 4 | - **Thực hành (Lab27):** gắn tag cho tài nguyên EC2 từ console và AWS CLI, sau đó gom vào Resource Group <br>- **Thực hành (Lab28):** <br>&emsp; + Viết IAM policy chỉ cho phép thao tác EC2 trên tài nguyên có tag đúng và trong Region được phép <br>&emsp; + Chuyển sang role bị giới hạn và xác nhận role được làm gì, không được làm gì | 21/10/26 | 21/10/26 | [Lab27 – 2.1.1 Create EC2 Instance with tag](https://000027.awsfcaj.com/2-using-tags/2.1-using-tags-console/2.1.1-create-ec2-with-tag/) <br> [Lab27 – 2.2 Using tags with CLI](https://000027.awsfcaj.com/2-using-tags/2.2-using-tags-cli/) <br> [Lab27 – 3. Create a Resource Group](https://000027.awsfcaj.com/3-resource-group/) <br> [Lab28 – 3. Create IAM Policy](https://000028.awsfcaj.com/3-createiampolicy/) <br> [Lab28 – 5.2.3 Create EC2 with and without matching tags](https://000028.awsfcaj.com/5-checkpolicy/5.2-checkiampolicy/5.2.3-ec2createtagsexisting/) |
| 5 | - **Thực hành (Lab22):** <br>&emsp; + Chuẩn bị VPC, security group và EC2 instance có gắn tag <br>&emsp; + Thiết lập Slack incoming webhook để nhận thông báo <br>&emsp; + Tạo IAM role và hai Lambda function dừng, khởi động instance theo tag <br>&emsp; + Kiểm tra trạng thái instance và tin nhắn Slack rồi dọn dẹp | 22/10/26 | 22/10/26 | [Lab22 – 2.4 Incoming Webhooks Slack](https://000022.awsfcaj.com/2-prerequiste/2.4-incomingwebhooksslack/) <br> [Lab22 – 4. Create Role for Lambda](https://000022.awsfcaj.com/4-createroleforlambda/) <br> [Lab22 – 5.1 Function stop instance](https://000022.awsfcaj.com/5-createlambdafunction/5.1-createlambdafunction-stop/) <br> [Lab22 – 5.2 Function start instance](https://000022.awsfcaj.com/5-createlambdafunction/5.2-createlambdafunction-start/) <br> [Lab22 – 6. Testing results](https://000022.awsfcaj.com/6-testingresults/) |
| 6 | - **Thực hành (Lab30):** giới hạn quyền tối đa của IAM user bằng permission boundary, kể cả khi policy của user cho phép nhiều hơn <br>- **Thực hành (Lab44):** <br>&emsp; + Tạo admin role và cho phép user chuyển sang role này <br>&emsp; + Thêm condition để role chỉ được dùng từ một địa chỉ IP nhất định và trong khung thời gian cho trước | 23/10/26 | 23/10/26 | [Lab30 – 2. Create Restriction Policy](https://000030.awsfcaj.com/2-createpolicy/) <br> [Lab30 – 4. Test IAM User Limits](https://000030.awsfcaj.com/4-checkuser/) <br> [Lab44 – 4.2 Configure Switch role](https://000044.awsfcaj.com/4-configure-iam-role-with-condition/2-configure-switch-role/) <br> [Lab44 – 4.3.1 Limit switch role by IP](https://000044.awsfcaj.com/4-configure-iam-role-with-condition/3-condition/3.1-ip/) <br> [Lab44 – 4.3.2 Limit switch role by Time](https://000044.awsfcaj.com/4-configure-iam-role-with-condition/3-condition/3.2-timebase/) |

### Kết quả đạt được tuần 6:

* **Kiến thức:**
  * Shared Responsibility Model: AWS bảo vệ hạ tầng chạy dịch vụ, còn tôi chịu trách nhiệm về định danh, dữ liệu, rule mạng và hệ điều hành trên EC2
  * Cách IAM đánh giá policy: explicit deny luôn thắng, cần có explicit allow, mọi trường hợp còn lại bị từ chối ngầm định
  * Các condition key như aws:RequestedRegion, aws:ResourceTag, aws:SourceIp và aws:CurrentTime thu hẹp phạm vi áp dụng quyền
  * Permission boundary đặt mức quyền tối đa cho user hoặc role; quyền thực tế là phần giao với policy của chính nó
  * Organizations quản lý nhiều tài khoản, Identity Center cung cấp đăng nhập một lần, Cognito quản lý người dùng ứng dụng, Security Hub tổng hợp phát hiện theo các bộ tiêu chuẩn
* **Kỹ năng thực hành:**
  * Viết IAM policy theo tag và Region, kiểm tra qua switch role
  * Áp dụng permission boundary và condition của role theo IP, thời gian
  * Tự động dừng, khởi động EC2 bằng Lambda và gửi kết quả về Slack
* **Bài học bảo mật và chi phí:**
  * Least privilege hiệu quả nhất khi áp dụng nhiều lớp: identity policy, boundary và condition
  * Gắn tag nhất quán giúp phân quyền, tự động hóa và theo dõi chi phí dễ dàng hơn nhiều
