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
| 2 | - **Thực hành (Lab10 – Hybrid DNS):** <br>&emsp; + Triển khai môi trường lab bằng CloudFormation và kết nối qua Remote Desktop Gateway <br>&emsp; + Tạo outbound endpoint và rule chuyển tiếp để AWS phân giải được tên miền on-premises <br>&emsp; + Tạo inbound endpoint để máy chủ on-premises phân giải được tên miền private trên AWS <br>&emsp; + Kiểm tra phân giải theo cả hai chiều rồi dọn dẹp | 05/10/26 | 05/10/26 | [Lab10 – 2.2 Initialize CloudFormation Template](https://000010.awsfcaj.com/2-prerequiste/2.2-launchcloudformation/) <br> [Lab10 – 5.1 Create Route 53 Outbound Endpoint](https://000010.awsfcaj.com/5-setuphyriddns/5.1-createoe/) <br> [Lab10 – 5.2 Create Route 53 Resolver Rules](https://000010.awsfcaj.com/5-setuphyriddns/5.2-createroute53/) <br> [Lab10 – 5.3 Create Route 53 Inbound Endpoints](https://000010.awsfcaj.com/5-setuphyriddns/5.3-createie/) <br> [Lab10 – 5.4 Test results](https://000010.awsfcaj.com/5-setuphyriddns/5.4-results/) |
| 3 | - Học Amazon EC2 trong Module 03-01: <br>&emsp; + Chọn dòng instance theo nhu cầu CPU, bộ nhớ và lưu trữ <br>&emsp; + AMI, key pair và các cách sao lưu <br>&emsp; + EBS lưu trữ bền vững so với instance store tạm thời <br>&emsp; + Dùng user data và instance metadata để cấu hình instance khi khởi tạo | 06/10/26 | 06/10/26 | [Module 03-01-01 – EC2 instance type](https://www.youtube.com/watch?v=e7XeKdOVq40) <br> [Module 03-01-02 – EC2 AMI, backup và key pair](https://www.youtube.com/watch?v=yAR6QRT3N1k) <br> [Module 03-01-03 – Elastic Block Store](https://www.youtube.com/watch?v=hKr_TfGP7NY) <br> [Module 03-01-04 – Instance store](https://www.youtube.com/watch?v=6IHNDJ85aoQ) <br> [Module 03-01-05 – User data](https://www.youtube.com/watch?v=_v_43Wi7zjo) <br> [Module 03-01-06 – Instance metadata](https://www.youtube.com/watch?v=Ew3QRaKJQSA) |
| 4 | - **Thực hành (Lab04):** <br>&emsp; + Khởi tạo một instance Amazon Linux, một instance Windows Server và kết nối vào cả hai <br>&emsp; + Thay đổi cấu hình bằng cách đổi instance type <br>&emsp; + Tạo EBS snapshot và dựng custom AMI từ instance đã cấu hình <br>&emsp; + Khởi tạo instance mới từ AMI đó để xác nhận hoạt động đúng | 07/10/26 | 07/10/26 | [Lab04 – 3.1 Launch Windows Server 2025 Instance](https://000004.awsfcaj.com/3-launchwindowsinstance/3.1-createwindowssintance/) <br> [Lab04 – 4.1 Launch Amazon Linux Instance](https://000004.awsfcaj.com/4-launchlinuxinstance/4.1-createlinuxinstance/) <br> [Lab04 – 5.1 Modify EC2 Instance Type](https://000004.awsfcaj.com/5-amazonec2basic/5.1-changeconfigureec2/) <br> [Lab04 – 5.2 Create and Manage EBS Snapshots](https://000004.awsfcaj.com/5-amazonec2basic/5.2-createec2snapshot/) <br> [Lab04 – 5.3 Create Custom AMI](https://000004.awsfcaj.com/5-amazonec2basic/5.3-createcustomami/) |
| 5 | - Học Auto Scaling, EFS, FSx, Lightsail và AWS Application Migration Service (Module 03-01-07, 03-02) <br>- **Thực hành (Lab04):** <br>&emsp; + Cài LAMP stack và Node.js trên Amazon Linux 2023, triển khai ứng dụng quản lý người dùng mẫu <br>&emsp; + Viết IAM policy giới hạn việc dùng EC2 trong các Region và instance type được phép | 08/10/26 | 08/10/26 | [Module 03-01-07 – EC2 Auto Scaling](https://www.youtube.com/watch?v=bbLcPitXJSY) <br> [Module 03-02 – Auto Scaling, EFS/FSx, Lightsail, MGN](https://www.youtube.com/watch?v=hFVYG8WqfU0) <br> [Lab04 – 6.1 Install LAMP Web Server](https://000004.awsfcaj.com/6-awsfcjmanagement-linux/6.1-lampserveronec2linux/) <br> [Lab04 – 6.3 Deploy the application on Linux](https://000004.awsfcaj.com/6-awsfcjmanagement-linux/6.3-awsfcjmanagement/) <br> [Lab04 – 8.1 Restrict service usage by Region](https://000004.awsfcaj.com/8-costusagegovernance/8.1-iamretrictregion/) |
| 6 | - **Thực hành (Lab13 – AWS Backup):** <br>&emsp; + Triển khai hạ tầng mẫu <br>&emsp; + Tạo backup plan với lịch chạy và quy tắc lưu giữ <br>&emsp; + Thiết lập thông báo kết quả các backup job <br>&emsp; + Khôi phục tài nguyên từ recovery point rồi dọn dẹp | 09/10/26 | 09/10/26 | [Lab13 – 2.2 Deploy infrastructure](https://000013.awsfcaj.com/2-prerequiste/2.2-deployinfras/) <br> [Lab13 – 3. Create Backup plan](https://000013.awsfcaj.com/3-createbackupplan/) <br> [Lab13 – 4. Set up notifications](https://000013.awsfcaj.com/4-enablenoti/) <br> [Lab13 – 5. Test Restore](https://000013.awsfcaj.com/5-testrestore/) <br> [Lab13 – 6. Clean up resources](https://000013.awsfcaj.com/6-cleanup/) |

### Kết quả đạt được tuần 4:

* **Kiến thức:**
  * Route 53 Resolver: outbound endpoint và rule chuyển tiếp gửi truy vấn từ AWS tới DNS on-premises, còn inbound endpoint cho phép máy chủ on-premises truy vấn tên miền trên AWS
  * EC2: các dòng instance được tối ưu cho tính toán, bộ nhớ hoặc lưu trữ; AMI là mẫu khởi tạo kèm snapshot của các volume
  * Lưu trữ cho EC2: EBS tồn tại độc lập với instance, còn dữ liệu instance store mất khi instance dừng
  * User data chạy script ở lần khởi động đầu, instance metadata cung cấp thông tin như instance ID và thông tin xác thực của IAM role
  * AWS Backup: backup plan quy định lịch chạy và thời gian lưu giữ, mỗi lần chạy tạo một recovery point trong backup vault
* **Kỹ năng thực hành:**
  * Thiết lập phân giải DNS hai chiều giữa trung tâm dữ liệu giả lập và VPC
  * Khởi tạo, đổi cấu hình, tạo snapshot và dựng lại EC2 từ custom AMI
  * Triển khai ứng dụng web LAMP và Node.js trên Amazon Linux 2023
* **Bài học bảo mật và chi phí:**
  * Condition IAM theo Region và instance type ngăn việc khởi tạo tài nguyên đắt tiền ngay từ đầu
  * Bản sao lưu chỉ có giá trị khi đã thử khôi phục, và snapshot, AMI cũ vẫn tính phí cho đến khi bị xóa
