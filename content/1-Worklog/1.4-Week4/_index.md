---
title: "Week 4 Worklog"
date: 2026-11-05
weight: 4
chapter: false
pre: "<b>1.4. </b>"
---

### Week 4 Objectives:

* Resolve DNS names between AWS and on-premises with Route 53 Resolver.
* Gain hands-on experience with EC2, from launching an instance to rebuilding it.
* Automate backups and prove that the data can actually be restored.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice (Lab10 – Hybrid DNS):** <br>&emsp; + Deployed the lab environment with CloudFormation and connected through the Remote Desktop Gateway <br>&emsp; + Created an outbound endpoint and forwarding rules so that AWS can resolve on-premises names <br>&emsp; + Created an inbound endpoint so that on-premises servers can resolve private names in AWS <br>&emsp; + Tested name resolution in both directions, then cleaned up | 05/10/26 | 05/10/26 | <https://000010.awsfcaj.com/> |
| 3 | - Studied Amazon EC2 in Module 03-01: <br>&emsp; + Choosing an instance family based on CPU, memory, and storage needs <br>&emsp; + AMIs, key pairs, and backup approaches <br>&emsp; + Persistent EBS volumes versus temporary instance store <br>&emsp; + Using user data and instance metadata to configure an instance at launch | 06/10/26 | 06/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - **Practice (Lab04):** <br>&emsp; + Launched an Amazon Linux instance and a Windows Server instance and connected to both <br>&emsp; + Resized an instance by changing its type <br>&emsp; + Took EBS snapshots and built a custom AMI from a configured instance <br>&emsp; + Launched a new instance from that AMI to confirm it works | 07/10/26 | 07/10/26 | <https://000004.awsfcaj.com/> |
| 5 | - Studied Auto Scaling, EFS, FSx, Lightsail, and AWS Application Migration Service in Module 03-02 <br>- **Practice (Lab04):** <br>&emsp; + Installed a LAMP stack and Node.js on Amazon Linux 2023 and deployed the sample user management app <br>&emsp; + Wrote IAM policies that limit EC2 usage to approved Regions and instance types | 08/10/26 | 08/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000004.awsfcaj.com/> |
| 6 | - **Practice (Lab13 – AWS Backup):** <br>&emsp; + Deployed the sample infrastructure <br>&emsp; + Created a backup plan with a schedule and retention rules <br>&emsp; + Set up notifications for backup job results <br>&emsp; + Restored a resource from a recovery point, then cleaned up | 09/10/26 | 09/10/26 | <https://000013.awsfcaj.com/> |

### Week 4 Achievements:

* I understand how Route 53 Resolver endpoints let AWS and on-premises networks resolve each other's DNS names.
* I can launch, resize, and back up EC2 instances:
  * Pick an instance type that matches the workload
  * Use snapshots and custom AMIs to rebuild a server quickly
* I deployed a web application on EC2 and kept EC2 costs in check with IAM guardrails.
* I learned that a backup only proves its worth once a restore has been tested.
