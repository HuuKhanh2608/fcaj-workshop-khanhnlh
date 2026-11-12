# Kế hoạch công việc 12 tuần — khung để viết Worklog

Tài liệu nội bộ (không xuất bản). Lập ngày 12/11/2026 từ hai nguồn:

- Playlist **First Cloud Journey Bootcamp - 2025** (296 video, 7 module): <https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i> — `#n` là vị trí video trong playlist.
- Trang lab **The First Cloud Journey**: <https://cloudjourney.awsfcaj.com/> — Lab NN ứng với `https://0000NN.awsfcaj.com/`.

Chi tiết từng module/lab xem [learning-map.md](learning-map.md).

## Nguyên tắc phân bổ

- Kỳ thực tập 14/09 – 14/12/2026. Tuần 1–12: 14/09 – 06/12; bảng worklog ghi thứ 2 – thứ 6, hoạt động cuối tuần ghi thêm dòng.
- Tuần 1–8: đi đúng thứ tự Module 01 → 07 của playlist (lý thuyết trước, lab sau). Lab trùng giữa Module 03 và 04 (Lab13, 24, 57) chỉ làm một lần.
- Tuần 2–3 chừa thời gian cho 3 sự kiện đã có trong báo cáo: 26/09 (thứ 7), 29/09 (thứ 3, cả ngày), 02/10 (thứ 6, buổi sáng).
- Tuần 9–12: workshop cá nhân (proposal → triển khai → giám sát/kiểm thử → COST/clean-up/demo), 3 blog, hoàn thiện báo cáo song ngữ.
- **Tuần 1–8 là phân bổ đề xuất theo giáo trình — phải đối chiếu với việc đã làm thật trước khi đưa vào worklog.** Tuần 10–12 là kế hoạch, cập nhật lại theo kết quả thực tế.

## Tổng quan

| Tuần | Thời gian | Trọng tâm |
| --- | --- | --- |
| 1 | 14/09 – 18/09 | Onboarding, Module 01: cloud cơ bản, tài khoản, Budgets, Support |
| 2 | 21/09 – 25/09 | Module 02: VPC, subnet, routing, SG/NACL, EC2 trong VPC |
| 3 | 28/09 – 02/10 | Module 02: VPN, VPC Peering, Transit Gateway; 2 sự kiện |
| 4 | 05/10 – 09/10 | Hybrid DNS; Module 03: EC2, AMI, EBS, Auto Scaling, AWS Backup |
| 5 | 12/10 – 16/10 | Module 04: S3, CloudFront, Storage Gateway, VM Import/Export, FSx |
| 6 | 19/10 – 23/10 | Module 05: IAM, Cognito, KMS, Security Hub, tag, Lambda |
| 7 | 26/10 – 30/10 | Module 05 (KMS, IAM role); Module 06: RDS, Aurora, DMS |
| 8 | 02/11 – 06/11 | DMS; Module 07: DynamoDB, Data Lake, Glue, Athena, QuickSight |
| 9 | 09/11 – 13/11 | Analytics nâng cao; chọn đề tài workshop; chuẩn hóa báo cáo theo template |
| 10 | 16/11 – 20/11 | Proposal, sơ đồ kiến trúc, AWS Pricing Calculator, triển khai phần 1, blog 1 |
| 11 | 23/11 – 27/11 | Triển khai phần 2, CloudWatch logs/metrics/alarms, kiểm thử, blog 2 |
| 12 | 30/11 – 04/12 | Tối ưu chi phí, clean-up, demo, hoàn thiện workshop, blog 3 |
| Sau tuần 12 | 07/12 – 14/12 | Rà soát báo cáo, tự đánh giá, feedback, nộp bài |

## Chi tiết từng tuần

### Tuần 1 — 14/09 – 18/09
**Mục tiêu:** làm quen FCAJ; hiểu cloud và hạ tầng AWS; tạo tài khoản an toàn và kiểm soát chi phí.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 14/09 | Làm quen thành viên FCAJ, đọc nội quy; xem Kick-off và hướng dẫn làm workshop | #1, #3 |
| 3 | 15/09 | 01-01 → 01-04: điện toán đám mây, khác biệt của AWS, hành trình lên cloud, Region/AZ/Edge | #4–7 |
| 4 | 16/09 | 01-05, 01-06: công cụ quản lý, tối ưu chi phí, Support. **Lab01:** tạo tài khoản (Free Tier 2026), MFA, admin group/user | #8–9, #11–14, [000001](https://000001.awsfcaj.com/) |
| 5 | 17/09 | **Lab07:** AWS Budgets — template, Cost, Usage, RI, Savings Plans; clean-up | #15–20, [000007](https://000007.awsfcaj.com/) |
| 6 | 18/09 | **Lab09:** gói Support, loại request, quản lý case; 01-07 bổ sung; tổng kết tuần | #10, #21–24, [000009](https://000009.awsfcaj.com/) |

**Kết quả cần có:** tài khoản bật MFA, không dùng root hằng ngày; budget cảnh báo chi phí; phân biệt Region/AZ/Edge và các gói Support.

### Tuần 2 — 21/09 – 25/09
**Mục tiêu:** nắm thành phần mạng VPC và triển khai EC2 public/private.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 21/09 | 02-01 Amazon VPC: CIDR, subnet, route table, IGW, NAT | #25 |
| 3 | 22/09 | 02-02 VPC security & multi-VPC; 02-03 VPN, Direct Connect, Load Balancer | #26–27 |
| 4 | 23/09 | **Lab03 (lý thuyết):** subnet, route table, IGW, NAT GW, SG, NACL, Resource Map | #28–35, [000003](https://000003.awsfcaj.com/) |
| 5 | 24/09 | **Lab03:** tạo VPC, subnet, IGW, route table, security group, VPC Flow Logs | #36–40 |
| 6 | 25/09 | **Lab03:** EC2 public/private, test kết nối, NAT GW, Reachability Analyzer, EC2 Instance Connect Endpoint | #41–44 |
| 7 | 26/09 | Sự kiện: Buildrathon Kickoff (Bitexco) | [Event 1](../content/4-EventParticipated/4.1-Event1/_index.md) |

**Kết quả cần có:** VPC 2 tầng public/private chạy được; giải thích khác biệt SG và NACL; dọn NAT GW sau lab.

### Tuần 3 — 28/09 – 02/10
**Mục tiêu:** kết nối nhiều VPC và hybrid; tham gia sự kiện cộng đồng.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 28/09 | **Lab03 phần 5:** Site-to-Site VPN (VGW, CGW, VPN connection), clean-up | [000003](https://000003.awsfcaj.com/) |
| 3 | 29/09 | Sự kiện: AWS Cloud & AI Day Hanoi – Watch Party (cả ngày) | [Event 2](../content/4-EventParticipated/4.2-Event2/_index.md) |
| 4 | 30/09 | **Lab19:** VPC Peering — CloudFormation, NACL, peering, route table, cross-peer DNS | #56–64, [000019](https://000019.awsfcaj.com/) |
| 5 | 01/10 | **Lab20:** Transit Gateway — attachments, TGW route table, route trong VPC | #65–71, [000020](https://000020.awsfcaj.com/) |
| 6 | 02/10 | Sáng: Fireside Chat với Dr. Werner Vogels. Chiều: so sánh Peering và Transit Gateway, ghi chú | [Event 3](../content/4-EventParticipated/4.3-Event3/_index.md) |

**Kết quả cần có:** kết nối 2 VPC bằng peering và nhiều VPC qua TGW; bài thu hoạch 2 sự kiện.

### Tuần 4 — 05/10 – 09/10
**Mục tiêu:** DNS hybrid; làm chủ EC2 và sao lưu.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 05/10 | **Lab10:** Hybrid DNS — key pair, CloudFormation, RDGW, Route 53 Resolver inbound/outbound, rules | #45–55, [000010](https://000010.awsfcaj.com/) |
| 3 | 06/10 | 03-01: instance type, AMI/backup/key pair, EBS, instance store, user data, metadata | #72–79 |
| 4 | 07/10 | **Lab04:** EC2 Linux/Windows, đổi instance type, EBS snapshot, custom AMI | [000004](https://000004.awsfcaj.com/) |
| 5 | 08/10 | 03-02: Auto Scaling, EFS/FSx, Lightsail, MGN. **Lab04:** LAMP + Node.js app, IAM giới hạn Region/instance type | #80, [000004](https://000004.awsfcaj.com/) |
| 6 | 09/10 | **Lab13:** AWS Backup — backup plan, notification, test restore, clean-up | #81–85, #107–112, [000013](https://000013.awsfcaj.com/) |

**Kết quả cần có:** triển khai app trên EC2; tạo AMI/snapshot; khôi phục từ backup.

### Tuần 5 — 12/10 – 16/10
**Mục tiêu:** nắm các dịch vụ lưu trữ và phân phối nội dung.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 12/10 | 04-01, 04-02: dịch vụ lưu trữ, S3, Access Point, Storage Class | #103–104 |
| 3 | 13/10 | 04-03, 04-04: static website & CORS, phân quyền, Glacier, Snow Family, Storage Gateway | #105–106 |
| 4 | 14/10 | **Lab57:** S3 static website, public access block, CloudFront, versioning, replication đa Region | #90–102, [000057](https://000057.awsfcaj.com/) |
| 5 | 15/10 | **Lab24:** Storage Gateway (File Gateway). **Lab14:** VM Import/Export | #86–89, #113–124, [000024](https://000024.awsfcaj.com/), [000014](https://000014.awsfcaj.com/) |
| 6 | 16/10 | **Lab25:** FSx for Windows — Multi-AZ, file share, hiệu năng, dedup, quota | #125–136, [000025](https://000025.awsfcaj.com/) |

**Kết quả cần có:** website tĩnh qua CloudFront với bucket private; chọn đúng storage class theo nhu cầu.

### Tuần 6 — 19/10 – 23/10
**Mục tiêu:** bảo mật và quản lý định danh trên AWS.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 19/10 | 05-01 Shared Responsibility Model; 05-02 IAM | #150–151 |
| 3 | 20/10 | 05-03 → 05-07: Cognito, Organizations, Identity Center, KMS, Security Hub. **Lab18:** bật Security Hub | #152–160, [000018](https://000018.awsfcaj.com/) |
| 4 | 21/10 | **Lab27:** tag, Resource Group. **Lab28:** IAM policy theo tag và Region, switch role | #171–186, [000027](https://000027.awsfcaj.com/), [000028](https://000028.awsfcaj.com/) |
| 5 | 22/10 | **Lab22:** Lambda stop/start EC2 theo tag, thông báo Slack | #161–170, [000022](https://000022.awsfcaj.com/) |
| 6 | 23/10 | **Lab30:** Permission Boundary. **Lab44:** IAM Role & Condition (IP, thời gian) | #187–190, #202–209, [000030](https://000030.awsfcaj.com/), [000044](https://000044.awsfcaj.com/) |

**Kết quả cần có:** áp dụng least privilege bằng policy, condition, boundary; tự động hóa với Lambda.

### Tuần 7 — 26/10 – 30/10
**Mục tiêu:** mã hóa dữ liệu, IAM role cho ứng dụng; cơ sở dữ liệu quan hệ.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 26/10 | **Lab33:** KMS mã hóa S3, CloudTrail, truy vấn log bằng Athena | #191–201, [000033](https://000033.awsfcaj.com/) |
| 3 | 27/10 | **Lab48:** access key và IAM role trên EC2; 05-08 tổng hợp Module 05 | #157, #210–216, [000048](https://000048.awsfcaj.com/) |
| 4 | 28/10 | 06-01 khái niệm database; 06-02 RDS & Aurora | #217–218 |
| 5 | 29/10 | 06-03 Redshift, ElastiCache. **Lab05:** RDS — VPC, SG, DB subnet group, EC2 kết nối RDS, backup/restore | #219–228, [000005](https://000005.awsfcaj.com/) |
| 6 | 30/10 | **Lab43 (phần 1):** chuẩn bị môi trường, Schema Conversion Tool | #229–238, [000043](https://000043.awsfcaj.com/) |

**Kết quả cần có:** app trên EC2 dùng RDS; dữ liệu S3 mã hóa KMS và có audit CloudTrail.

### Tuần 8 — 02/11 – 06/11
**Mục tiêu:** di chuyển dữ liệu; NoSQL và nền tảng phân tích dữ liệu.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 02/11 | **Lab43 (phần 2):** DMS migration task, DMS Serverless, giám sát, troubleshooting | #239–245, [000043](https://000043.awsfcaj.com/) |
| 3 | 03/11 | **Lab60:** DynamoDB — Console, CloudShell, SDK Python | #273–275, [000060](https://000060.awsfcaj.com/) |
| 4 | 04/11 | **Lab39:** DynamoDB Immersion Day — CLI/Console, GSI, backup | #257–261, [000039](https://000039.awsfcaj.com/) |
| 5 | 05/11 | **Lab35:** Data Lake — S3, Firehose, Glue Crawler, Athena, QuickSight | #246–256, [000035](https://000035.awsfcaj.com/) |
| 6 | 06/11 | **Lab40:** Glue + Athena phân tích chi phí. **Lab73:** QuickSight dashboard | #265–272, #294–296, [000040](https://000040.awsfcaj.com/), [000073](https://000073.awsfcaj.com/) |

**Kết quả cần có:** pipeline ingest → catalog → query → dashboard chạy được; phân biệt RDS và DynamoDB.

### Tuần 9 — 09/11 – 13/11
**Mục tiêu:** hoàn tất Module 07; chọn đề tài workshop; chuẩn hóa báo cáo.

| Thứ | Ngày | Công việc | Nguồn |
| --- | --- | --- | --- |
| 2 | 09/11 | **Lab70:** Data lake với dữ liệu riêng — DataBrew, Glue → Parquet, Athena | #276–281, [000070](https://000070.awsfcaj.com/) |
| 3 | 10/11 | **Lab72:** Analytics on AWS — Firehose, Glue, EMR, Athena, Lambda, Redshift (chọn lọc) | #282–293, [000072](https://000072.awsfcaj.com/) |
| 4 | 11/11 | Ôn tập 7 module; xem hướng dẫn làm workshop; lên danh sách đề tài (≥ 3 dịch vụ AWS) | #3 |
| 5 | 12/11 | Đối chiếu báo cáo với template FCJ gốc; chuẩn hóa Worklog, Proposal, Blogs, Self-evaluation; lập kế hoạch 12 tuần (**đã làm thật**) | [fcj-workshop-template](https://github.com/thienluhoan/fcj-workshop-template) |
| 6 | 13/11 | Chốt đề tài; xem hướng dẫn vẽ kiến trúc draw.io; vẽ sơ đồ nháp | #2 |

### Tuần 10 — 16/11 – 20/11 (kế hoạch)
**Mục tiêu:** hoàn thành Proposal và bắt đầu triển khai.

| Thứ | Ngày | Công việc |
| --- | --- | --- |
| 2 | 16/11 | Viết Proposal: bài toán, mục tiêu, phạm vi, dịch vụ và lý do chọn |
| 3 | 17/11 | Hoàn thiện sơ đồ kiến trúc (icon AWS chính thức), data flow, Well-Architected |
| 4 | 18/11 | Dự toán AWS Pricing Calculator, bảng COST, timeline, rủi ro |
| 5 | 19/11 | Triển khai phần 1: hạ tầng nền (IAM, mạng/lưu trữ), ghi lại từng bước |
| 6 | 20/11 | Viết và đăng blog 1 lên AWS Study Group |

### Tuần 11 — 23/11 – 27/11 (kế hoạch)
**Mục tiêu:** hoàn thành chức năng chính, giám sát và kiểm thử.

| Thứ | Ngày | Công việc |
| --- | --- | --- |
| 2 | 23/11 | Triển khai phần 2: xử lý nghiệp vụ chính |
| 3 | 24/11 | Triển khai phần 3: tích hợp, bảo mật (least privilege, secrets) |
| 4 | 25/11 | CloudWatch logs, metrics, alarms, SNS cảnh báo ([000008](https://000008.awsfcaj.com/)) |
| 5 | 26/11 | Kiểm thử luồng đúng và luồng lỗi; ghi actual vs expected, ảnh minh chứng |
| 6 | 27/11 | Viết và đăng blog 2 |

### Tuần 12 — 30/11 – 04/12 (kế hoạch)
**Mục tiêu:** hoàn thiện workshop đạt chuẩn và có demo.

| Thứ | Ngày | Công việc |
| --- | --- | --- |
| 2 | 30/11 | Tối ưu chi phí, cập nhật COST theo thực tế |
| 3 | 01/12 | Viết hướng dẫn clean-up, chạy thử clean-up |
| 4 | 02/12 | Quay video demo / chuẩn bị live demo |
| 5 | 03/12 | Hoàn thiện tài liệu Workshop 5.1–5.9 song ngữ |
| 6 | 04/12 | Viết và đăng blog 3 |

### Sau tuần 12 — 07/12 – 14/12 (kế hoạch)
Rà soát toàn bộ báo cáo song ngữ, Self-evaluation, Feedback, xóa các ghi chú nháp, kiểm tra đủ điều kiện nhận mộc (≥ 10 buổi văn phòng, 3 sự kiện, 3 blog), nộp bài.

## Cần bổ sung từ thực tế

- Ngày lên văn phòng (≥ 10 buổi) để ghi vào bảng điểm danh.
- Lab nào chưa làm / làm khác ngày; khó khăn gặp phải (lab outdated, lỗi console, chi phí phát sinh…).
- Đề tài workshop đã chốt (tuần 9–10).
