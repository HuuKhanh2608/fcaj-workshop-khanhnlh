---
title: "Worklog Tuần 4"
date: 2026-11-05
weight: 4
chapter: false
pre: "<b>1.4. </b>"
---

### Mục tiêu tuần 4:

* Phân giải tên miền giữa AWS và on-premises bằng Route 53 Resolver.
* Thực hành EC2 từ khâu khởi tạo đến dựng lại instance.
* Tự động hóa sao lưu và chứng minh dữ liệu thực sự khôi phục được.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành (Lab10 – Hybrid DNS):** <br>&emsp; + Triển khai môi trường lab bằng CloudFormation và kết nối qua Remote Desktop Gateway <br>&emsp; + Tạo outbound endpoint và rule chuyển tiếp để AWS phân giải được tên miền on-premises <br>&emsp; + Tạo inbound endpoint để máy chủ on-premises phân giải được tên miền private trên AWS <br>&emsp; + Kiểm tra phân giải theo cả hai chiều rồi dọn dẹp | 05/10/26 | 05/10/26 | <https://000010.awsfcaj.com/> |
| 3 | - Học Amazon EC2 trong Module 03-01: <br>&emsp; + Chọn dòng instance theo nhu cầu CPU, bộ nhớ và lưu trữ <br>&emsp; + AMI, key pair và các cách sao lưu <br>&emsp; + EBS lưu trữ bền vững so với instance store tạm thời <br>&emsp; + Dùng user data và instance metadata để cấu hình instance khi khởi tạo | 06/10/26 | 06/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - **Thực hành (Lab04):** <br>&emsp; + Khởi tạo một instance Amazon Linux, một instance Windows Server và kết nối vào cả hai <br>&emsp; + Thay đổi cấu hình bằng cách đổi instance type <br>&emsp; + Tạo EBS snapshot và dựng custom AMI từ instance đã cấu hình <br>&emsp; + Khởi tạo instance mới từ AMI đó để xác nhận hoạt động đúng | 07/10/26 | 07/10/26 | <https://000004.awsfcaj.com/> |
| 5 | - Học Auto Scaling, EFS, FSx, Lightsail và AWS Application Migration Service trong Module 03-02 <br>- **Thực hành (Lab04):** <br>&emsp; + Cài LAMP stack và Node.js trên Amazon Linux 2023, triển khai ứng dụng quản lý người dùng mẫu <br>&emsp; + Viết IAM policy giới hạn việc dùng EC2 trong các Region và instance type được phép | 08/10/26 | 08/10/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000004.awsfcaj.com/> |
| 6 | - **Thực hành (Lab13 – AWS Backup):** <br>&emsp; + Triển khai hạ tầng mẫu <br>&emsp; + Tạo backup plan với lịch chạy và quy tắc lưu giữ <br>&emsp; + Thiết lập thông báo kết quả các backup job <br>&emsp; + Khôi phục tài nguyên từ recovery point rồi dọn dẹp | 09/10/26 | 09/10/26 | <https://000013.awsfcaj.com/> |

### Kết quả đạt được tuần 4:

* Hiểu cách Route 53 Resolver endpoint giúp AWS và mạng on-premises phân giải tên miền của nhau.
* Có thể khởi tạo, thay đổi cấu hình và sao lưu EC2:
  * Chọn instance type phù hợp với workload
  * Dùng snapshot và custom AMI để dựng lại máy chủ nhanh chóng
* Triển khai được ứng dụng web trên EC2 và kiểm soát chi phí EC2 bằng giới hạn IAM.
* Rút ra rằng bản sao lưu chỉ có giá trị khi việc khôi phục đã được kiểm chứng.
