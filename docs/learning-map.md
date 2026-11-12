# Bản đồ nội dung học FCJ — tham chiếu viết Worklog

Tài liệu nội bộ (không xuất bản lên website). Tổng hợp ngày 12/11/2026 từ:

- Trang tổng hợp lab: <https://cloudjourney.awsfcaj.com/>
- Playlist YouTube **First Cloud Journey Bootcamp - 2025** (AWS Study Group, 296 video, cập nhật 08/03/2026): <https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i>

Nguồn chính thức theo trang hướng dẫn FCAJ (<https://hcm-rules.awsfcaj.com/instructions/document>): kênh YouTube AWS Study Group, playlist trên, trang lab cloudjourney, và AWS Architecture Blog (<https://aws.amazon.com/blogs/architecture/>) để đọc thêm. Platform Bootcamp (amplifyapp) không còn truy cập được nên không dùng. Trang hướng dẫn cũng lưu ý một số lab có thể đã cũ, nên khi làm lab cần đối chiếu với console hiện tại và ghi lại điểm khác biệt vào worklog.

Quy ước: số **LabNN** trong tiêu đề video tương ứng với site lab `https://0000NN.awsfcaj.com/` (ví dụ Lab03 → `000003`, Lab57 → `000057`). Số `#` là vị trí video trong playlist.

> Bản đồ này chỉ mô tả **nội dung có sẵn**. Worklog chỉ ghi những gì đã thực sự học/làm, đúng ngày thực tế.

## Video mở đầu

| # | Video |
| --- | --- |
| 1 | First Cloud Journey Bootcamp - 2025 (2:09:35) |
| 2 | Hướng dẫn vẽ kiến trúc AWS trên draw.io (48:03) — dùng cho sơ đồ Proposal/Workshop |
| 3 | Hướng dẫn làm workshop AWS (35:10) — dùng cho phần Workshop |

## Module 01 — Cloud cơ bản, tài khoản, chi phí, support (#4–24)

Lý thuyết (#4–10): 01-01 Điện toán đám mây là gì · 01-02 Điều gì tạo nên khác biệt của AWS · 01-03 Bắt đầu hành trình lên mây · 01-04 Hạ tầng toàn cầu (Region/AZ/Edge) · 01-05 AWS Service Management Tools · 01-06 Cost Optimization & AWS Support · 01-07 Supplementary Practice.

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab01 (#11–14) | [000001](https://000001.awsfcaj.com/) | Tạo tài khoản, Free Tier 2026 (Free/Paid plan, credit), MFA, admin group/user, xác thực tài khoản |
| Lab07 (#15–20) | [000007](https://000007.awsfcaj.com/) | AWS Budgets: template, Cost, Usage, RI, Savings Plans budget, clean up |
| Lab09 (#21–24) | [000009](https://000009.awsfcaj.com/) | AWS Support plans, loại request, đổi gói, quản lý case |

## Module 02 — Networking (#25–71)

Lý thuyết: 02-01 Amazon VPC (38:03) · 02-02 VPC Security & Multi-VPC (28:35) · 02-03 VPN, Direct Connect, Load Balancer (23:44).

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab03 (#28–44) | [000003](https://000003.awsfcaj.com/) | Subnet, Route table, IGW, NAT GW, Security Group, NACL, Resource Map, Flow Logs, EC2 public/private, Reachability Analyzer, EC2 Instance Connect Endpoint, Session Manager, CloudWatch; Site-to-Site VPN (VGW/CGW, strongSwan + Transit Gateway) |
| Lab10 (#45–55) | [000010](https://000010.awsfcaj.com/) | Hybrid DNS: key pair, CloudFormation, RDGW, Microsoft AD, Route 53 Resolver inbound/outbound endpoint, rules |
| Lab19 (#56–64) | [000019](https://000019.awsfcaj.com/) | VPC Peering: CloudFormation, SG, EC2, NACL, peering connection, route table, cross-peer DNS |
| Lab20 (#65–71) | [000020](https://000020.awsfcaj.com/) | Transit Gateway: attachments, TGW route tables, route trong VPC |

## Module 03 — Compute (#72–102)

Lý thuyết: 03-01 Compute VM · EC2 instance type · AMI/Backup/Key pair · EBS · Instance store · User data · Metadata · Auto Scaling · 03-02 Auto Scaling, EFS/FSx, Lightsail, MGN (24:56).

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab04 (không có video riêng) | [000004](https://000004.awsfcaj.com/) | EC2 Windows/Linux, đổi instance type, EBS snapshot, custom AMI, khôi phục truy cập, LAMP + Node.js app, IAM giới hạn Region/instance type |
| Lab13 (#81–85) | [000013](https://000013.awsfcaj.com/) | AWS Backup: backup plan, notification, test restore |
| Lab24 (#86–89) | [000024](https://000024.awsfcaj.com/) | Storage Gateway (File Gateway) |
| Lab57 (#90–102) | [000057](https://000057.awsfcaj.com/) | S3 static website, public access block, CloudFront, versioning, replication đa Region |

## Module 04 — Storage (#103–149)

Lý thuyết: 04-01 Dịch vụ lưu trữ · 04-02 S3, Access Point, Storage Class (21:02) · 04-03 Static website & CORS, Control access, Object key & performance, Glacier (22:45) · 04-04 Snow Family, Storage Gateway, Backup (25:27).

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab13 (#107–112) | [000013](https://000013.awsfcaj.com/) | AWS Backup (bản quay đầy đủ hơn) |
| Lab14 (#113–120) | [000014](https://000014.awsfcaj.com/) | VM Import/Export: export VM on-prem, upload S3, import thành AMI, export ngược |
| Lab24 (#121–124) | [000024](https://000024.awsfcaj.com/) | Storage Gateway, mount file share on-prem |
| Lab25 (#125–136) | [000025](https://000025.awsfcaj.com/) | FSx for Windows: SSD/HDD Multi-AZ, file share, hiệu năng, dedup, shadow copy, quota, scale |
| Lab57 (#137–149) | [000057](https://000057.awsfcaj.com/) | S3 + CloudFront (bản quay lại) |

## Module 05 — Security & Identity (#150–216)

Lý thuyết: 05-01 Shared Responsibility Model · 05-02 IAM (32:46) · 05-03 Cognito · 05-04 Organizations · 05-05 Identity Center · 05-06 KMS · 05-07 Security Hub · 05-08 Hands-on & research.

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab18 (#158–160) | [000018](https://000018.awsfcaj.com/) | Bật Security Hub, điểm theo bộ tiêu chuẩn |
| Lab22 (#161–170) | [000022](https://000022.awsfcaj.com/) | Lambda tự động stop/start EC2 theo tag, báo Slack webhook |
| Lab27 (#171–176) | [000027](https://000027.awsfcaj.com/) | Tag trên Console/CLI, lọc theo tag, Resource Group |
| Lab28 (#177–186) | [000028](https://000028.awsfcaj.com/) | IAM policy theo tag + Region, switch role |
| Lab30 (#187–190) | [000030](https://000030.awsfcaj.com/) | IAM Permission Boundary |
| Lab33 (#191–201) | [000033](https://000033.awsfcaj.com/) | KMS mã hóa S3, CloudTrail, Athena truy vấn log |
| Lab44 (#202–209) | [000044](https://000044.awsfcaj.com/) | IAM Role & Condition: giới hạn switch role theo IP/thời gian |
| Lab48 (#210–216) | [000048](https://000048.awsfcaj.com/) | Access key vs IAM role trên EC2 truy cập S3 |

## Module 06 — Database (#217–245)

Lý thuyết: 06-01 Database concepts (37:19) · 06-02 RDS & Aurora (29:50) · 06-03 Redshift, ElastiCache (19:49).

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab05 (#220–228) | [000005](https://000005.awsfcaj.com/) | RDS: VPC, SG, DB subnet group, EC2 app kết nối RDS, backup/restore |
| Lab43 (#229–245) | [000043](https://000043.awsfcaj.com/) | DMS + Schema Conversion: Oracle/SQL Server → Aurora, DMS Serverless, giám sát, troubleshooting |

## Module 07 — Data, Analytics, DynamoDB (#246–296)

Không có video lý thuyết riêng; toàn bộ là lab.

| Lab | Site | Nội dung chính |
| --- | --- | --- |
| Lab35 (#246–256) | [000035](https://000035.awsfcaj.com/) | Data Lake: S3, Firehose, Glue Crawler, Athena, QuickSight |
| Lab39 (#257–264) | [000039](https://000039.awsfcaj.com/) | DynamoDB Immersion Day: CLI/Console, GSI, backup, design patterns, global tables, event-driven |
| Lab40 (#265–272) | [000040](https://000040.awsfcaj.com/) | Glue + Athena phân tích chi phí/hiệu năng, tag cost allocation |
| Lab60 (#273–275) | [000060](https://000060.awsfcaj.com/) | DynamoDB cơ bản: Console, CloudShell, SDK Python |
| Lab70 (#276–281) | [000070](https://000070.awsfcaj.com/) | Data lake với dữ liệu riêng: DataBrew, Glue → Parquet, Athena, QuickSight |
| Lab72 (#282–293) | [000072](https://000072.awsfcaj.com/) | Analytics on AWS: Firehose, Glue, DataBrew, EMR, Athena, Kinesis Analytics, Lambda, Redshift |
| Lab73 (#294–296) | [000073](https://000073.awsfcaj.com/) | QuickSight dashboard tương tác |

## Lịch tuần thực tập (thứ Hai–Chủ Nhật)

| Tuần | Khoảng ngày |
| --- | --- |
| 1 | 14/09 – 20/09/2026 |
| 2 | 21/09 – 27/09/2026 |
| 3 | 28/09 – 04/10/2026 |
| 4 | 05/10 – 11/10/2026 |
| 5 | 12/10 – 18/10/2026 |
| 6 | 19/10 – 25/10/2026 |
| 7 | 26/10 – 01/11/2026 |
| 8 | 02/11 – 08/11/2026 |
| 9 | 09/11 – 15/11/2026 |
| 10 | 16/11 – 22/11/2026 |
| 11 | 23/11 – 29/11/2026 |
| 12 | 30/11 – 06/12/2026 |

Sự kiện đã có trong báo cáo: 26/09 (tuần 2), 29/09 và 02/10 (tuần 3).
