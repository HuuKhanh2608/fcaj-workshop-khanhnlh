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
| 2 | - **Thực hành (Lab03 – Site-to-Site VPN):** <br>&emsp; + Tạo một VPC riêng với EC2 đóng vai phía on-premises <br>&emsp; + Thiết lập Virtual Private Gateway, Customer Gateway và VPN connection <br>&emsp; + Áp dụng cấu hình tunnel lên customer gateway và kiểm tra trạng thái tunnel <br>&emsp; + Xóa tài nguyên VPN sau khi kiểm thử | 28/09/26 | 28/09/26 | <https://000003.awsfcaj.com/> |
| 3 | - Cùng nhóm tham dự watch party AWS Cloud & AI Day Hanoi tại văn phòng AWS Việt Nam <br>- Ghi chép về AI-DLC, cách TCBS tổ chức workspace cho agent, AWS Security Agent và Agent Toolkit for AWS | 29/09/26 | 29/09/26 | [Event 2](../../4-EventParticipated/4.2-Event2/) |
| 4 | - **Thực hành (Lab19 – VPC Peering):** <br>&emsp; + Triển khai hai VPC cùng các instance từ CloudFormation template <br>&emsp; + Mở Network ACL cho lưu lượng giữa hai dải CIDR <br>&emsp; + Gửi và chấp nhận yêu cầu peering, sau đó thêm route ở cả hai phía <br>&emsp; + Bật phân giải DNS qua kết nối peering | 30/09/26 | 30/09/26 | <https://000019.awsfcaj.com/> |
| 5 | - **Thực hành (Lab20 – Transit Gateway):** <br>&emsp; + Tạo Transit Gateway và gắn nhiều VPC vào đó <br>&emsp; + Cấu hình Transit Gateway route table để kiểm soát VPC nào được liên lạc với nhau <br>&emsp; + Trỏ route table của từng VPC về Transit Gateway và kiểm tra kết nối <br>&emsp; + Gỡ attachment và xóa gateway để dừng tính phí | 01/10/26 | 01/10/26 | <https://000020.awsfcaj.com/> |
| 6 | - Tham dự Fireside Chat với Dr. Werner Vogels tại văn phòng AWS (buổi sáng) <br>- So sánh VPC Peering và Transit Gateway trong ghi chú theo chi phí, quy mô và khả năng kiểm soát định tuyến <br>- Ôn lại nội dung Module 02 | 02/10/26 | 02/10/26 | [Event 3](../../4-EventParticipated/4.3-Event3/) <br> [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |

### Kết quả đạt được tuần 3:

* Kết nối một trung tâm dữ liệu giả lập với AWS qua Site-to-Site VPN (IPsec).
* Hiểu sự đánh đổi giữa hai cách kết nối VPC:
  * VPC Peering đơn giản, chi phí thấp khi có ít VPC nhưng không định tuyến bắc cầu
  * Transit Gateway đóng vai trò trung tâm và mở rộng tốt hơn khi số VPC tăng
* Biết lập route table ở cả hai phía của kết nối để lưu lượng đi được hai chiều.
* Viết bài thu hoạch cho AWS Cloud & AI Day và Fireside Chat, tập trung vào những ý tưởng áp dụng được cho workshop của mình.
