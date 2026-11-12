---
title: "Week 5 Worklog"
date: 2026-11-05
weight: 5
chapter: false
pre: "<b>1.5. </b>"
---

### Week 5 Objectives:

* Choose the right AWS storage service and S3 storage class for each need.
* Publish a static website securely with S3 and CloudFront.
* Explore hybrid storage, VM migration, and managed Windows file shares.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Studied AWS storage in Module 04-01 and 04-02: <br>&emsp; + Object, block, and file storage, and where each fits <br>&emsp; + Amazon S3 buckets, objects, and Access Points <br>&emsp; + Choosing S3 storage classes based on how often data is accessed | 12/10/26 | 12/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Studied the rest of Module 04: <br>&emsp; + S3 static websites, CORS, access control, and object key performance (04-03) <br>&emsp; + Archiving data with S3 Glacier <br>&emsp; + Moving data with the Snow Family and connecting on-premises storage through Storage Gateway (04-04) | 13/10/26 | 13/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - **Practice (Lab57):** <br>&emsp; + Published a static website from an S3 bucket <br>&emsp; + Adjusted Block Public Access and object permissions to make the site reachable <br>&emsp; + Locked the bucket down again and served the site through CloudFront instead <br>&emsp; + Enabled versioning, moved objects between buckets, and set up cross-Region replication | 14/10/26 | 14/10/26 | <https://000057.awsfcaj.com/> |
| 5 | - **Practice (Lab24 – Storage Gateway):** <br>&emsp; + Deployed a file gateway on EC2 backed by an S3 bucket <br>&emsp; + Created file shares and mounted them from a client machine <br>- **Practice (Lab14 – VM Import/Export):** <br>&emsp; + Imported a virtual machine image into AWS as an AMI and launched it <br>&emsp; + Exported an instance back to S3 as a VM image | 15/10/26 | 15/10/26 | <https://000024.awsfcaj.com/> <br> <https://000014.awsfcaj.com/> |
| 6 | - **Practice (Lab25 – Amazon FSx for Windows File Server):** <br>&emsp; + Created SSD and HDD Multi-AZ file systems and compared their performance <br>&emsp; + Created file shares and enabled deduplication, shadow copies, and user quotas <br>&emsp; + Scaled throughput and storage capacity, then deleted the environment | 16/10/26 | 16/10/26 | <https://000025.awsfcaj.com/> |

### Week 5 Achievements:

* I can match a storage need to the right service:
  * S3 for objects, EBS for block volumes, EFS and FSx for shared files
  * Infrequent-access storage classes and Glacier for data that is rarely read
* I delivered a static website through CloudFront while keeping the S3 bucket private.
* I protected data against accidental deletion and Regional failure with versioning and replication.
* I understand how Storage Gateway and VM Import/Export help bring on-premises workloads to AWS.
