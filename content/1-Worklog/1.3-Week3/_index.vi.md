---
title: "Worklog Tuần 3"
date: 2026-11-05
weight: 3
chapter: false
pre: "<b>1.3. </b>"
---

### Mục tiêu tuần 3:

* Kết nối một mạng on-premises giả lập với AWS.
* So sánh hai cách liên kết VPC: VPC Peering và Transit Gateway.
* Học hỏi từ cộng đồng tại AWS Cloud & AI Day và Fireside Chat với Dr. Werner Vogels.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành (Lab03 – Site-to-Site VPN):** <br>&emsp; + Tạo một VPC riêng với EC2 đóng vai phía on-premises <br>&emsp; + Thiết lập Virtual Private Gateway, Customer Gateway và VPN connection <br>&emsp; + Áp dụng cấu hình tunnel lên customer gateway và kiểm tra trạng thái tunnel <br>&emsp; + Xóa tài nguyên VPN sau khi kiểm thử | 28/09/26 | 28/09/26 | [Lab03 – 5.1.1 Create VPC for VPN](https://000003.awsfcaj.com/5-vpnsitetosite/5.1-createvpnenv/5.1.1-createvpnvpc/) <br> [Lab03 – 5.2.1 Create Virtual Private Gateway](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.1-createvpgw/) <br> [Lab03 – 5.2.2 Create Customer Gateway](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.2-createcustomergw/) <br> [Lab03 – 5.2.3 Create VPN Connection](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.3-createvpnconnection/) <br> [Lab03 – 5.2.4 Customer Gateway Configuration](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.4-configurecustomergw/) |
| 3 | - Cùng nhóm tham dự watch party AWS Cloud & AI Day Hanoi tại văn phòng AWS Việt Nam <br>- Ghi chép về AI-DLC, cách TCBS tổ chức workspace cho agent, AWS Security Agent và Agent Toolkit for AWS | 29/09/26 | 29/09/26 | [Bài thu hoạch Event 2](../../4-EventParticipated/4.2-Event2/) |
| 4 | - **Thực hành (Lab19 – VPC Peering):** <br>&emsp; + Triển khai hai VPC cùng các instance từ CloudFormation template <br>&emsp; + Mở Network ACL cho lưu lượng giữa hai dải CIDR <br>&emsp; + Gửi và chấp nhận yêu cầu peering, sau đó thêm route ở cả hai phía <br>&emsp; + Bật phân giải DNS qua kết nối peering | 30/09/26 | 30/09/26 | [Lab19 – 2.1 Initialize CloudFormation Template](https://000019.awsfcaj.com/2-prerequiste/2.1-launchcloudformation/) <br> [Lab19 – 3. Update Network ACL](https://000019.awsfcaj.com/3-updatenetworkacl/) <br> [Lab19 – 4. Create Peering Connection](https://000019.awsfcaj.com/4-vpcpeering/) <br> [Lab19 – 5. Route Tables](https://000019.awsfcaj.com/5-routetables/) <br> [Lab19 – 6. Cross-Peer DNS](https://000019.awsfcaj.com/6-crosspeerdns/) |
| 5 | - **Thực hành (Lab20 – Transit Gateway):** <br>&emsp; + Tạo Transit Gateway và gắn nhiều VPC vào đó <br>&emsp; + Cấu hình Transit Gateway route table để kiểm soát VPC nào được liên lạc với nhau <br>&emsp; + Trỏ route table của từng VPC về Transit Gateway và kiểm tra kết nối <br>&emsp; + Gỡ attachment và xóa gateway để dừng tính phí | 01/10/26 | 01/10/26 | [Lab20 – 3. Create Transit Gateway](https://000020.awsfcaj.com/3-transitgateway/) <br> [Lab20 – 5. Create Transit Gateway Route Tables](https://000020.awsfcaj.com/5-routetable/) <br> [Lab20 – 6. Add Transit Gateway Routes to VPC Route Tables](https://000020.awsfcaj.com/6-result/) <br> [Lab20 – 7. Clean Up Resources](https://000020.awsfcaj.com/7-cleanup/) |
| 6 | - Tham dự Fireside Chat với Dr. Werner Vogels tại văn phòng AWS (buổi sáng) <br>- So sánh VPC Peering và Transit Gateway trong ghi chú theo chi phí, quy mô và khả năng kiểm soát định tuyến <br>- Ôn lại phần multi-VPC của Module 02 | 02/10/26 | 02/10/26 | [Bài thu hoạch Event 3](../../4-EventParticipated/4.3-Event3/) <br> [Module 02-02 – Bảo mật VPC và tính năng multi-VPC](https://www.youtube.com/watch?v=BPuD1l2hEQ4) |

### Kết quả đạt được tuần 3:

* **Kiến thức:**
  * Site-to-Site VPN: Virtual Private Gateway là phía AWS, Customer Gateway đại diện cho thiết bị on-premises, mỗi kết nối có hai tunnel IPsec để dự phòng
  * VPC Peering: kết nối một-một, không có tính bắc cầu và yêu cầu dải CIDR không chồng lấn
  * Transit Gateway: trung tâm cấp Region để gắn VPC và VPN, route table của nó quyết định attachment nào được liên lạc với nhau
* **Kỹ năng thực hành:**
  * Kết nối trung tâm dữ liệu giả lập với AWS qua Site-to-Site VPN
  * Liên kết hai VPC bằng peering, gồm route ở cả hai phía và cross-peer DNS
  * Kết nối nhiều VPC qua Transit Gateway và kiểm soát định tuyến bằng route table
* **Bài học bảo mật và chi phí:**
  * Cần quy hoạch CIDR từ sớm vì các dải chồng lấn không thể peering
  * VPN connection và Transit Gateway attachment tính phí theo giờ nên cần xóa ngay sau khi kiểm thử
* **Cộng đồng:** viết bài thu hoạch AWS Cloud & AI Day và Fireside Chat, tập trung vào ý tưởng áp dụng được cho workshop
