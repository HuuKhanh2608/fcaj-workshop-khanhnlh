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
| 2 | - Học Shared Responsibility Model (Module 05-01) <br>- Học sâu về AWS IAM (Module 05-02): <br>&emsp; + User, group và role <br>&emsp; + Cách policy được đánh giá, bao gồm tác động của explicit deny | 19/10/26 | 19/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Học các dịch vụ định danh và bảo mật trong Module 05-03 → 05-07: Amazon Cognito, AWS Organizations, IAM Identity Center, AWS KMS và AWS Security Hub <br>- **Thực hành (Lab18):** bật Security Hub và xem điểm số, các phát hiện theo từng bộ tiêu chuẩn bảo mật | 20/10/26 | 20/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000018.awsfcaj.com/> |
| 4 | - **Thực hành (Lab27):** <br>&emsp; + Gắn tag cho tài nguyên EC2 từ console và AWS CLI <br>&emsp; + Lọc tài nguyên theo tag và gom vào Resource Group <br>- **Thực hành (Lab28):** <br>&emsp; + Viết IAM policy chỉ cho phép thao tác EC2 trên tài nguyên có tag đúng và trong Region được phép <br>&emsp; + Chuyển sang role bị giới hạn và xác nhận role được làm gì, không được làm gì | 21/10/26 | 21/10/26 | <https://000027.awsfcaj.com/> <br> <https://000028.awsfcaj.com/> |
| 5 | - **Thực hành (Lab22):** <br>&emsp; + Chuẩn bị VPC, security group và EC2 instance có gắn tag <br>&emsp; + Thiết lập Slack incoming webhook để nhận thông báo <br>&emsp; + Tạo IAM role và hai Lambda function dừng, khởi động instance theo tag <br>&emsp; + Kiểm tra trạng thái instance và tin nhắn Slack rồi dọn dẹp | 22/10/26 | 22/10/26 | <https://000022.awsfcaj.com/> |
| 6 | - **Thực hành (Lab30):** giới hạn quyền tối đa của IAM user bằng permission boundary, kể cả khi policy của user cho phép nhiều hơn <br>- **Thực hành (Lab44):** <br>&emsp; + Tạo admin role và cho phép user chuyển sang role này <br>&emsp; + Thêm condition để role chỉ được dùng từ một địa chỉ IP nhất định và trong khung thời gian cho trước | 23/10/26 | 23/10/26 | <https://000030.awsfcaj.com/> <br> <https://000044.awsfcaj.com/> |

### Kết quả đạt được tuần 6:

* Giải thích được Shared Responsibility Model qua ví dụ cụ thể với EC2 và dịch vụ được quản lý.
* Áp dụng least privilege theo nhiều lớp:
  * Identity policy kèm condition theo tag và Region
  * Permission boundary giới hạn quyền tối đa
  * Condition của role dựa trên IP nguồn và thời gian
* Tổ chức tài nguyên bằng tag, giúp việc phân quyền và theo dõi chi phí thuận tiện hơn.
* Tự động hóa tác vụ lặp lại bằng Lambda, tắt instance nhàn rỗi để tiết kiệm chi phí.
