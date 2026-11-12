---
title: "Week 7 Worklog"
date: 2026-11-05
weight: 7
chapter: false
pre: "<b>1.7. </b>"
---

### Week 7 Objectives:

* Encrypt data with AWS KMS and keep an audit trail with AWS CloudTrail.
* Give applications temporary credentials through IAM roles.
* Understand the AWS database services and run an application on Amazon RDS.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice (Lab33):** <br>&emsp; + Prepared the IAM policy, role, group, and user for the lab <br>&emsp; + Created a KMS key and uploaded data to S3 encrypted with that key <br>&emsp; + Recorded API activity with CloudTrail and queried the logs with Athena <br>&emsp; + Checked who can read the encrypted objects when they are shared | 26/10/26 | 26/10/26 | <https://000033.awsfcaj.com/> |
| 3 | - **Practice (Lab48):** <br>&emsp; + Accessed S3 from an EC2 instance with an access key stored on the server <br>&emsp; + Replaced the access key with an IAM role attached to the instance <br>- Reviewed Module 05 and its additional reading (05-08) | 27/10/26 | 27/10/26 | <https://000048.awsfcaj.com/> <br> [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - Studied database fundamentals in Module 06-01: relational and non-relational models, OLTP and OLAP, and indexing <br>- Studied Amazon RDS and Amazon Aurora in Module 06-02: Multi-AZ deployments, read replicas, and automated backups | 28/10/26 | 28/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 5 | - Studied Amazon Redshift and Amazon ElastiCache in Module 06-03 <br>- **Practice (Lab05):** <br>&emsp; + Prepared a VPC, security groups, and a DB subnet group <br>&emsp; + Created an RDS instance and connected the sample application running on EC2 <br>&emsp; + Took a snapshot and restored the database from it | 29/10/26 | 29/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000005.awsfcaj.com/> |
| 6 | - **Practice (Lab43 – part 1):** <br>&emsp; + Prepared the migration environment and connected to the source database <br>&emsp; + Configured the source database for migration <br>&emsp; + Converted the source schema with AWS Schema Conversion Tool and reviewed the items that need manual changes | 30/10/26 | 30/10/26 | <https://000043.awsfcaj.com/> |

### Week 7 Achievements:

* I encrypted S3 data with my own KMS key and traced access to it through CloudTrail logs in Athena.
* I understand why an IAM role is safer than an access key stored on a server: its credentials are temporary and rotate automatically.
* I can tell the database services apart:
  * RDS and Aurora for transactional workloads
  * Redshift for analytics
  * ElastiCache for in-memory caching
* I deployed an application backed by RDS and confirmed that a snapshot restore works.
