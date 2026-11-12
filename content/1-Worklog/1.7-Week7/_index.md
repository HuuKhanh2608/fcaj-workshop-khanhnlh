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
| 2 | - **Practice (Lab33):** <br>&emsp; + Prepared the IAM policy, role, group, and user for the lab <br>&emsp; + Created a KMS key and uploaded data to S3 encrypted with that key <br>&emsp; + Recorded API activity with CloudTrail and queried the logs with Athena <br>&emsp; + Checked who can read the encrypted objects when they are shared | 26/10/26 | 26/10/26 | [Lab33 – 2.1 Create Policy and Role](https://000033.awsfcaj.com/2-create-role-user/2.1-create-role/) <br> [Lab33 – 3. Create Key Management Service](https://000033.awsfcaj.com/3-create-kms/) <br> [Lab33 – 4.2 Upload Data to S3](https://000033.awsfcaj.com/4-create-s3/4.2-upload-data/) <br> [Lab33 – 5.1 Create CloudTrail](https://000033.awsfcaj.com/5-create-cloudtrail/5.1-create-cloudtrail/) <br> [Lab33 – 5.4 Query Data with Athena](https://000033.awsfcaj.com/5-create-cloudtrail/5.4-test-athena/) |
| 3 | - **Practice (Lab48):** <br>&emsp; + Accessed S3 from an EC2 instance with an access key stored on the server <br>&emsp; + Replaced the access key with an IAM role attached to the instance <br>- Reviewed Module 05 and its additional reading (05-08) | 27/10/26 | 27/10/26 | [Lab48 – 2.2 Use access key](https://000048.awsfcaj.com/2-accesskey/2.2-useaccesskey/) <br> [Lab48 – 3.1 Create IAM role](https://000048.awsfcaj.com/3-iamroleec2/3.1-createrole/) <br> [Lab48 – 3.2 Using IAM role](https://000048.awsfcaj.com/3-iamroleec2/3.2-useiamrole/) <br> [Module 05-08 – Hands-on and additional research](https://www.youtube.com/watch?v=0SdpD2GPYz4) |
| 4 | - Studied database fundamentals in Module 06-01: relational and non-relational models, OLTP and OLAP, and indexing <br>- Studied Amazon RDS and Amazon Aurora in Module 06-02: Multi-AZ deployments, read replicas, and automated backups | 28/10/26 | 28/10/26 | [Module 06-01 – Database concepts](https://www.youtube.com/watch?v=OOD2RwWuLRw) <br> [Module 06-02 – Amazon RDS and Amazon Aurora](https://www.youtube.com/watch?v=qbrobQZrokY) |
| 5 | - Studied Amazon Redshift and Amazon ElastiCache in Module 06-03 <br>- **Practice (Lab05):** <br>&emsp; + Prepared a VPC, security groups, and a DB subnet group <br>&emsp; + Created an RDS instance and connected the sample application running on EC2 <br>&emsp; + Took a snapshot and restored the database from it | 29/10/26 | 29/10/26 | [Module 06-03 – Amazon Redshift and ElastiCache](https://www.youtube.com/watch?v=UvdiRW34aNI) <br> [Lab05 – 2.3 Create database subnet group](https://000005.awsfcaj.com/2-prerequiste/2.3-create-rds-subnet-group/) <br> [Lab05 – 3. Create RDS database instance](https://000005.awsfcaj.com/3-create-rds/) <br> [Lab05 – 5. Application deployment](https://000005.awsfcaj.com/5-deploy-app/) <br> [Lab05 – 6. Backup and restore](https://000005.awsfcaj.com/6-backup/) |
| 6 | - **Practice (Lab43 – part 1):** <br>&emsp; + Prepared the migration environment and connected to the source database <br>&emsp; + Configured the source database for migration <br>&emsp; + Converted the source schema with AWS Schema Conversion Tool and reviewed the items that need manual changes | 30/10/26 | 30/10/26 | [Lab43 – Database Schema Conversion & Migration](https://000043.awsfcaj.com/) <br> [Video Lab43-01 – Connect to EC2 with RDP](https://www.youtube.com/watch?v=cxwAOP1379s) <br> [Video Lab43-03 – SQL Server source configuration](https://www.youtube.com/watch?v=cXbuxFVL6mU) <br> [Video Lab43-08 – Create the conversion project](https://www.youtube.com/watch?v=bTWkX3xHN4s) <br> [Video Lab43-09 – Schema conversion to Aurora MySQL](https://www.youtube.com/watch?v=s-6mXTFXwG8) |

### Week 7 Achievements:

* **Knowledge:**
  * AWS KMS: a customer managed key is controlled by its key policy, and S3 can encrypt objects with it (SSE-KMS)
  * CloudTrail records API calls into an S3 bucket, and Athena can query those logs with SQL
  * An IAM role attached to EC2 provides temporary credentials through the instance profile, so no keys need to be stored on the server
  * RDS Multi-AZ keeps a synchronous standby for failover, while read replicas copy data asynchronously to scale reads
  * Redshift is a columnar data warehouse for analytics, and ElastiCache provides in-memory caching with Redis or Memcached
* **Hands-on skills:**
  * Encrypted S3 data with my own KMS key and traced access through CloudTrail logs in Athena
  * Deployed an application on EC2 backed by RDS and restored the database from a snapshot
  * Converted a database schema with AWS Schema Conversion Tool
* **Security and cost lessons:**
  * Access keys should never be stored on servers; IAM roles are the safe default
  * The database belongs in private subnets, with a security group that only accepts traffic from the application
  * RDS instances, snapshots, and KMS keys all carry ongoing costs, and a deleted KMS key enters a 7–30 day waiting period
