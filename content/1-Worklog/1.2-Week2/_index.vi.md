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
| 2 | - Học Amazon VPC trong Module 02-01: <br>&emsp; + Quy hoạch dải CIDR để các subnet không chồng lấn <br>&emsp; + Cách route table quyết định bước đi tiếp theo của lưu lượng <br>&emsp; + Lý do subnet public cần Internet Gateway còn subnet private đi ra ngoài qua NAT Gateway | 21/09/26 | 21/09/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Học bảo mật VPC và các tính năng multi-VPC trong Module 02-02 <br>- Học kết nối hybrid và cân bằng tải trong Module 02-03: <br>&emsp; + Site-to-Site VPN và Direct Connect để nối với mạng on-premises <br>&emsp; + Application, Network và Gateway Load Balancer | 22/09/26 | 22/09/26 | [Playlist FCJ Bootcamp](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - Đọc phần lý thuyết Lab03 trước khi bắt tay xây dựng: <br>&emsp; + Lần theo đường đi của gói tin qua subnet, route table, Internet Gateway và NAT Gateway <br>&emsp; + So sánh Security Group (stateful) với Network ACL (stateless) <br>&emsp; + Dùng VPC Resource Map để xem các tài nguyên liên kết với nhau thế nào | 23/09/26 | 23/09/26 | <https://000003.awsfcaj.com/> |
| 5 | - **Thực hành (Lab03):** <br>&emsp; + Dựng VPC gồm một subnet public và một subnet private <br>&emsp; + Gắn Internet Gateway và định tuyến subnet public qua đó <br>&emsp; + Viết rule security group chỉ mở những port mà từng tầng cần <br>&emsp; + Bật VPC Flow Logs để ghi lại lưu lượng được chấp nhận và bị từ chối | 24/09/26 | 24/09/26 | <https://000003.awsfcaj.com/> |
| 6 | - **Thực hành (Lab03):** <br>&emsp; + Tạo một instance ở mỗi subnet và kiểm tra kết nối nào thành công <br>&emsp; + Thêm NAT Gateway để instance private tải được bản cập nhật <br>&emsp; + Chẩn đoán kết nối bằng Reachability Analyzer <br>&emsp; + Truy cập instance private qua EC2 Instance Connect Endpoint mà không cấp IP public | 25/09/26 | 25/09/26 | <https://000003.awsfcaj.com/> |
| 7 | - Tham dự Buildrathon Kickoff: Code the Future with CMC Global tại Bitexco Financial Tower <br>- Nghe chia sẻ về tư duy đằng sau việc xây dựng một bot AI | 26/09/26 | 26/09/26 | [Event 1](../../4-EventParticipated/4.1-Event1/) |

### Kết quả đạt được tuần 2:

* Hiểu cách một VPC được ghép lại:
  * Subnet chia nhỏ không gian địa chỉ, route table quyết định bước đi tiếp theo
  * Internet Gateway cho subnet public truy cập internet hai chiều, còn NAT Gateway chỉ cho subnet private đi ra ngoài
* Giải thích được vì sao Security Group là stateful còn Network ACL là stateless, và khi nào nên dựa vào từng lớp.
* Triển khai được mạng hai tầng hoạt động và truy cập instance private mà không để lộ ra internet.
* Tạo thói quen xóa NAT Gateway sau mỗi lab vì dịch vụ này tính phí theo giờ.
* Hoàn thành bài thu hoạch sự kiện đầu tiên, về Buildrathon Kickoff.
