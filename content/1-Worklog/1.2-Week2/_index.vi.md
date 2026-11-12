---
title: "Worklog Tuần 2"
date: 2026-11-05
weight: 2
chapter: false
pre: "<b>1.2. </b>"
---

### Mục tiêu tuần 2:

* Hiểu cách các thành phần của Amazon VPC kết hợp thành một mạng riêng.
* Xây dựng mạng hai tầng và kiểm soát lưu lượng ở cả cấp instance lẫn cấp subnet.
* Gặp gỡ cộng đồng tại sự kiện Buildrathon Kickoff.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Học Amazon VPC trong Module 02-01: <br>&emsp; + Quy hoạch dải CIDR để các subnet không chồng lấn <br>&emsp; + Mỗi subnet chỉ nằm trong đúng một Availability Zone <br>&emsp; + Cách route table quyết định bước đi tiếp theo của lưu lượng | 21/09/26 | 21/09/26 | [Module 02-01 – Amazon VPC](https://www.youtube.com/watch?v=O9Ac_vGHquM) <br> [Lab03 – 1.1 Subnets](https://000003.awsfcaj.com/1-introduce/1.1-subnets/) <br> [Lab03 – 1.2 Route Table](https://000003.awsfcaj.com/1-introduce/1.2-routetable/) |
| 3 | - Học bảo mật VPC và các tính năng multi-VPC trong Module 02-02 <br>- Học kết nối hybrid và cân bằng tải trong Module 02-03: <br>&emsp; + Site-to-Site VPN và Direct Connect để nối với mạng on-premises <br>&emsp; + Application, Network, Gateway Load Balancer và trường hợp dùng từng loại | 22/09/26 | 22/09/26 | [Module 02-02 – Bảo mật VPC và tính năng multi-VPC](https://www.youtube.com/watch?v=BPuD1l2hEQ4) <br> [Module 02-03 – VPN, Direct Connect và Load Balancer](https://www.youtube.com/watch?v=CXU8D3kyxIc) |
| 4 | - Đọc phần lý thuyết Lab03 trước khi bắt tay xây dựng: <br>&emsp; + Lý do subnet public dùng Internet Gateway còn subnet private đi ra ngoài qua NAT Gateway <br>&emsp; + Security Group (stateful) so với Network ACL (stateless, rule có đánh số thứ tự) <br>&emsp; + Dùng VPC Resource Map để xem các tài nguyên liên kết với nhau thế nào | 23/09/26 | 23/09/26 | [Lab03 – 1.3 Internet Gateway](https://000003.awsfcaj.com/1-introduce/1.3-internetgateway/) <br> [Lab03 – 1.4 NAT Gateway](https://000003.awsfcaj.com/1-introduce/1.4-natgateway/) <br> [Lab03 – 2.1 Security Group](https://000003.awsfcaj.com/2-firewallinvpc/2.1-securitygroup/) <br> [Lab03 – 2.2 Network ACLs](https://000003.awsfcaj.com/2-firewallinvpc/2.2-networkacls/) <br> [Lab03 – 2.3 VPC Resource Map](https://000003.awsfcaj.com/2-firewallinvpc/2.3-vpc-resource-map/) |
| 5 | - **Thực hành (Lab03):** <br>&emsp; + Dựng VPC gồm một subnet public và một subnet private <br>&emsp; + Gắn Internet Gateway và định tuyến subnet public qua đó <br>&emsp; + Viết rule security group chỉ mở những port mà từng tầng cần <br>&emsp; + Bật VPC Flow Logs để ghi lại lưu lượng được chấp nhận và bị từ chối | 24/09/26 | 24/09/26 | [Lab03 – 3.1 Create VPC](https://000003.awsfcaj.com/3-prerequisite/3.1-createvpc/) <br> [Lab03 – 3.2 Create Subnet](https://000003.awsfcaj.com/3-prerequisite/3.2-createsubnet/) <br> [Lab03 – 3.4 Create Route Table](https://000003.awsfcaj.com/3-prerequisite/3.4-createroutetable/) <br> [Lab03 – 3.5 Create Security Group](https://000003.awsfcaj.com/3-prerequisite/3.5-createsecuritygroup/) <br> [Lab03 – 3.6 Enable VPC Flow Logs](https://000003.awsfcaj.com/3-prerequisite/3.6-enablevpcflowlogs/) |
| 6 | - **Thực hành (Lab03):** <br>&emsp; + Tạo một instance ở mỗi subnet và kiểm tra kết nối nào thành công <br>&emsp; + Thêm NAT Gateway để instance private tải được bản cập nhật <br>&emsp; + Chẩn đoán kết nối bằng Reachability Analyzer <br>&emsp; + Truy cập instance private qua EC2 Instance Connect Endpoint mà không cấp IP public | 25/09/26 | 25/09/26 | [Lab03 – 4.1 Create EC2 Server](https://000003.awsfcaj.com/4-createec2server/4.1-createec2/) <br> [Lab03 – 4.2 Test Connection](https://000003.awsfcaj.com/4-createec2server/4.2-connectec2/) <br> [Lab03 – 4.3 Create NAT Gateway](https://000003.awsfcaj.com/4-createec2server/4.3-natgateway/) <br> [Lab03 – 4.4 Reachability Analyzer](https://000003.awsfcaj.com/4-createec2server/4.4-createreachabilityanalyzer/) <br> [Lab03 – 4.5 EC2 Instance Connect Endpoint](https://000003.awsfcaj.com/4-createec2server/4.5-eicendpoint/) |
| 7 | - Tham dự Buildrathon Kickoff: Code the Future with CMC Global tại Bitexco Financial Tower <br>- Nghe chia sẻ về tư duy đằng sau việc xây dựng một bot AI | 26/09/26 | 26/09/26 | [Bài thu hoạch Event 1](../../4-EventParticipated/4.1-Event1/) |

### Kết quả đạt được tuần 2:

* **Kiến thức:**
  * VPC và CIDR: mỗi subnet thuộc một Availability Zone và AWS giữ lại năm địa chỉ IP trong mỗi subnet
  * Route table: bảng nào cũng có local route cho lưu lượng nội bộ VPC; 0.0.0.0/0 trỏ tới Internet Gateway với subnet public và tới NAT Gateway với subnet private
  * Security Group là stateful và gắn vào instance; Network ACL là stateless, gắn vào subnet và xét rule theo thứ tự số
  * Site-to-Site VPN đi qua internet, còn Direct Connect là đường truyền riêng chuyên dụng
* **Kỹ năng thực hành:**
  * Dựng VPC hai tầng gồm subnet public, private, route table và security group
  * Ghi lại lưu lượng bằng VPC Flow Logs và chẩn đoán đường đi bằng Reachability Analyzer
  * Truy cập instance private qua EC2 Instance Connect Endpoint
* **Bài học bảo mật và chi phí:**
  * Instance private không cần IP public, security group chỉ nên mở những port cần thiết
  * NAT Gateway tính phí theo giờ và theo lượng dữ liệu xử lý nên cần xóa sau lab
* **Cộng đồng:** viết bài thu hoạch sự kiện Buildrathon Kickoff
