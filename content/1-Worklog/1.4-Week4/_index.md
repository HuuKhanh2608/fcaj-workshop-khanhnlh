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
| 2 | - **Practice (Lab10 – Hybrid DNS):** <br>&emsp; + Deployed the lab environment with CloudFormation and connected through the Remote Desktop Gateway <br>&emsp; + Created an outbound endpoint and forwarding rules so that AWS can resolve on-premises names <br>&emsp; + Created an inbound endpoint so that on-premises servers can resolve private names in AWS <br>&emsp; + Tested name resolution in both directions, then cleaned up | 05/10/26 | 05/10/26 | [Lab10 – 2.2 Initialize CloudFormation Template](https://000010.awsfcaj.com/2-prerequiste/2.2-launchcloudformation/) <br> [Lab10 – 5.1 Create Route 53 Outbound Endpoint](https://000010.awsfcaj.com/5-setuphyriddns/5.1-createoe/) <br> [Lab10 – 5.2 Create Route 53 Resolver Rules](https://000010.awsfcaj.com/5-setuphyriddns/5.2-createroute53/) <br> [Lab10 – 5.3 Create Route 53 Inbound Endpoints](https://000010.awsfcaj.com/5-setuphyriddns/5.3-createie/) <br> [Lab10 – 5.4 Test results](https://000010.awsfcaj.com/5-setuphyriddns/5.4-results/) |
| 3 | - Studied Amazon EC2 in Module 03-01: <br>&emsp; + Choosing an instance family based on CPU, memory, and storage needs <br>&emsp; + AMIs, key pairs, and backup approaches <br>&emsp; + Persistent EBS volumes versus temporary instance store <br>&emsp; + Using user data and instance metadata to configure an instance at launch | 06/10/26 | 06/10/26 | [Module 03-01-01 – EC2 instance types](https://www.youtube.com/watch?v=e7XeKdOVq40) <br> [Module 03-01-02 – EC2 AMI, backup, and key pair](https://www.youtube.com/watch?v=yAR6QRT3N1k) <br> [Module 03-01-03 – Elastic Block Store](https://www.youtube.com/watch?v=hKr_TfGP7NY) <br> [Module 03-01-04 – Instance store](https://www.youtube.com/watch?v=6IHNDJ85aoQ) <br> [Module 03-01-05 – User data](https://www.youtube.com/watch?v=_v_43Wi7zjo) <br> [Module 03-01-06 – Instance metadata](https://www.youtube.com/watch?v=Ew3QRaKJQSA) |
| 4 | - **Practice (Lab04):** <br>&emsp; + Launched an Amazon Linux instance and a Windows Server instance and connected to both <br>&emsp; + Resized an instance by changing its type <br>&emsp; + Took EBS snapshots and built a custom AMI from a configured instance <br>&emsp; + Launched a new instance from that AMI to confirm it works | 07/10/26 | 07/10/26 | [Lab04 – 3.1 Launch Windows Server 2025 Instance](https://000004.awsfcaj.com/3-launchwindowsinstance/3.1-createwindowssintance/) <br> [Lab04 – 4.1 Launch Amazon Linux Instance](https://000004.awsfcaj.com/4-launchlinuxinstance/4.1-createlinuxinstance/) <br> [Lab04 – 5.1 Modify EC2 Instance Type](https://000004.awsfcaj.com/5-amazonec2basic/5.1-changeconfigureec2/) <br> [Lab04 – 5.2 Create and Manage EBS Snapshots](https://000004.awsfcaj.com/5-amazonec2basic/5.2-createec2snapshot/) <br> [Lab04 – 5.3 Create Custom AMI](https://000004.awsfcaj.com/5-amazonec2basic/5.3-createcustomami/) |
| 5 | - Studied Auto Scaling, EFS, FSx, Lightsail, and AWS Application Migration Service (Module 03-01-07, 03-02) <br>- **Practice (Lab04):** <br>&emsp; + Installed a LAMP stack and Node.js on Amazon Linux 2023 and deployed the sample user management app <br>&emsp; + Wrote IAM policies that limit EC2 usage to approved Regions and instance types | 08/10/26 | 08/10/26 | [Module 03-01-07 – EC2 Auto Scaling](https://www.youtube.com/watch?v=bbLcPitXJSY) <br> [Module 03-02 – Auto Scaling, EFS/FSx, Lightsail, MGN](https://www.youtube.com/watch?v=hFVYG8WqfU0) <br> [Lab04 – 6.1 Install LAMP Web Server](https://000004.awsfcaj.com/6-awsfcjmanagement-linux/6.1-lampserveronec2linux/) <br> [Lab04 – 6.3 Deploy the application on Linux](https://000004.awsfcaj.com/6-awsfcjmanagement-linux/6.3-awsfcjmanagement/) <br> [Lab04 – 8.1 Restrict service usage by Region](https://000004.awsfcaj.com/8-costusagegovernance/8.1-iamretrictregion/) |
| 6 | - **Practice (Lab13 – AWS Backup):** <br>&emsp; + Deployed the sample infrastructure <br>&emsp; + Created a backup plan with a schedule and retention rules <br>&emsp; + Set up notifications for backup job results <br>&emsp; + Restored a resource from a recovery point, then cleaned up | 09/10/26 | 09/10/26 | [Lab13 – 2.2 Deploy infrastructure](https://000013.awsfcaj.com/2-prerequiste/2.2-deployinfras/) <br> [Lab13 – 3. Create Backup plan](https://000013.awsfcaj.com/3-createbackupplan/) <br> [Lab13 – 4. Set up notifications](https://000013.awsfcaj.com/4-enablenoti/) <br> [Lab13 – 5. Test Restore](https://000013.awsfcaj.com/5-testrestore/) <br> [Lab13 – 6. Clean up resources](https://000013.awsfcaj.com/6-cleanup/) |

### Week 4 Achievements:

* **Knowledge:**
  * Route 53 Resolver: outbound endpoints and forwarding rules send queries from AWS to on-premises DNS, while inbound endpoints let on-premises servers query names in AWS
  * EC2: instance families are optimized for compute, memory, or storage; an AMI is a launch template that includes the snapshots of its volumes
  * Storage for EC2: EBS volumes persist independently of the instance, while instance store data is lost when the instance stops
  * User data runs scripts at first boot, and instance metadata exposes details such as the instance ID and IAM role credentials
  * AWS Backup: a backup plan defines the schedule and retention, and every run creates a recovery point in a backup vault
* **Hands-on skills:**
  * Set up two-way DNS resolution between a simulated data center and a VPC
  * Launched, resized, snapshotted, and rebuilt EC2 instances from a custom AMI
  * Deployed a LAMP and Node.js web application on Amazon Linux 2023
* **Security and cost lessons:**
  * IAM conditions on Region and instance type stop expensive launches before they happen
  * A backup only proves its worth once a restore has been tested, and old snapshots and AMIs keep costing money until deleted
