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
| 2 | - **Thực hành (Lab03 – Site-to-Site VPN):** <br>&emsp; + Tạo một VPC riêng với EC2 đóng vai phía on-premises <br>&emsp; + Thiết lập Virtual Private Gateway, Customer Gateway và VPN connection <br>&emsp; + Áp dụng cấu hình tunnel lên customer gateway và kiểm tra trạng thái tunnel <br>&emsp; + Xóa tài nguyên VPN sau khi kiểm thử | 28/09/2026 | 28/09/2026 | <https://000003.awsfcaj.com/5-vpnsitetosite/5.1-createvpnenv/5.1.1-createvpnvpc/> <br> <https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.1-createvpgw/> <br> <https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.2-createcustomergw/> <br> <https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.3-createvpnconnection/> <br> <https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.4-configurecustomergw/> |
| 3 | - Cùng nhóm tham dự watch party AWS Cloud & AI Day Hanoi tại văn phòng AWS Việt Nam <br>- Ghi chép về AI-DLC, cách TCBS tổ chức workspace cho agent, AWS Security Agent và Agent Toolkit for AWS | 29/09/2026 | 29/09/2026 | <https://huukhanh2608.github.io/fcaj-workshop-khanhnlh/vi/4-eventparticipated/4.2-event2/> |
| 4 | - **Thực hành (Lab19 – VPC Peering):** <br>&emsp; + Triển khai hai VPC cùng các instance từ CloudFormation template <br>&emsp; + Mở Network ACL cho lưu lượng giữa hai dải CIDR <br>&emsp; + Gửi và chấp nhận yêu cầu peering, sau đó thêm route ở cả hai phía <br>&emsp; + Bật phân giải DNS qua kết nối peering | 30/09/2026 | 30/09/2026 | <https://000019.awsfcaj.com/2-prerequiste/2.1-launchcloudformation/> <br> <https://000019.awsfcaj.com/3-updatenetworkacl/> <br> <https://000019.awsfcaj.com/4-vpcpeering/> <br> <https://000019.awsfcaj.com/5-routetables/> <br> <https://000019.awsfcaj.com/6-crosspeerdns/> |
| 5 | - **Thực hành (Lab20 – Transit Gateway):** <br>&emsp; + Tạo Transit Gateway và gắn nhiều VPC vào đó <br>&emsp; + Cấu hình Transit Gateway route table để kiểm soát VPC nào được liên lạc với nhau <br>&emsp; + Trỏ route table của từng VPC về Transit Gateway và kiểm tra kết nối <br>&emsp; + Gỡ attachment và xóa gateway để dừng tính phí | 01/10/2026 | 01/10/2026 | <https://000020.awsfcaj.com/3-transitgateway/> <br> <https://000020.awsfcaj.com/5-routetable/> <br> <https://000020.awsfcaj.com/6-result/> <br> <https://000020.awsfcaj.com/7-cleanup/> |
| 6 | - Tham dự Fireside Chat với Dr. Werner Vogels tại văn phòng AWS (buổi sáng) <br>- So sánh VPC Peering và Transit Gateway trong ghi chú theo chi phí, quy mô và khả năng kiểm soát định tuyến <br>- Ôn lại phần multi-VPC của Module 02 | 02/10/2026 | 02/10/2026 | <https://huukhanh2608.github.io/fcaj-workshop-khanhnlh/vi/4-eventparticipated/4.3-event3/> <br> <https://www.youtube.com/watch?v=BPuD1l2hEQ4> |

### Kết quả đạt được tuần 3:

* Hiểu được các kiến thức sau:
  * Site-to-Site VPN: Virtual Private Gateway là phía AWS, Customer Gateway đại diện cho thiết bị on-premises, mỗi kết nối có hai tunnel IPsec để dự phòng
  * VPC Peering: kết nối một-một, không có tính bắc cầu và yêu cầu dải CIDR không chồng lấn
  * Transit Gateway: trung tâm cấp Region để gắn VPC và VPN, route table của nó quyết định attachment nào được liên lạc với nhau

* Kết nối trung tâm dữ liệu giả lập với AWS qua Site-to-Site VPN.

* Liên kết hai VPC bằng peering, gồm route ở cả hai phía và cross-peer DNS.

* Kết nối nhiều VPC qua Transit Gateway và kiểm soát định tuyến bằng route table.

* Rút ra các bài học về bảo mật và chi phí:
  * Cần quy hoạch CIDR từ sớm vì các dải chồng lấn không thể peering
  * VPN connection và Transit Gateway attachment tính phí theo giờ nên cần xóa ngay sau khi kiểm thử

* Viết bài thu hoạch AWS Cloud & AI Day và Fireside Chat, tập trung vào ý tưởng áp dụng được cho workshop.
