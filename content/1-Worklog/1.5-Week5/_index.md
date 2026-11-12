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
| 2 | - Studied AWS storage in Module 04-01 and 04-02: <br>&emsp; + Object, block, and file storage, and where each fits <br>&emsp; + Amazon S3 buckets, objects, and Access Points <br>&emsp; + Choosing S3 storage classes based on how often data is accessed | 12/10/26 | 12/10/26 | [Module 04-01 – Storage services on AWS](https://www.youtube.com/watch?v=hsCfP0IxoaM) <br> [Module 04-02 – Amazon S3, Access Points, storage classes](https://www.youtube.com/watch?v=_yunukwcAwc) |
| 3 | - Studied the rest of Module 04: <br>&emsp; + S3 static websites, CORS, access control, and object key performance (04-03) <br>&emsp; + Archiving data with S3 Glacier <br>&emsp; + Moving data with the Snow Family and connecting on-premises storage through Storage Gateway (04-04) | 13/10/26 | 13/10/26 | [Module 04-03 – S3 static website, access control, Glacier](https://www.youtube.com/watch?v=mPBjB6Ltl_Q) <br> [Module 04-04 – Snow Family, Storage Gateway, Backup](https://www.youtube.com/watch?v=YXn8Q_Hpsu4) |
| 4 | - **Practice (Lab57):** <br>&emsp; + Published a static website from an S3 bucket <br>&emsp; + Adjusted Block Public Access and object permissions to make the site reachable <br>&emsp; + Locked the bucket down again and served the site through CloudFront instead <br>&emsp; + Enabled versioning, moved objects between buckets, and set up cross-Region replication | 14/10/26 | 14/10/26 | [Lab57 – 3. Enable static website feature](https://000057.awsfcaj.com/3-staticwebsite/) <br> [Lab57 – 4. Configuring public access block](https://000057.awsfcaj.com/4-blockpublicaccess/) <br> [Lab57 – 7.2 Configure Amazon CloudFront](https://000057.awsfcaj.com/7-cloudfront/7.2-configure_amazon_cloudfront/) <br> [Lab57 – 8. Bucket Versioning](https://000057.awsfcaj.com/8-versioning/) <br> [Lab57 – 10. Cross-Region Replication](https://000057.awsfcaj.com/10-s3ccr/) |
| 5 | - **Practice (Lab24 – Storage Gateway):** <br>&emsp; + Deployed a file gateway on EC2 backed by an S3 bucket <br>&emsp; + Created file shares and mounted them from a client machine <br>- **Practice (Lab14 – VM Import/Export):** <br>&emsp; + Imported a virtual machine image into AWS as an AMI, then exported an instance back to S3 | 15/10/26 | 15/10/26 | [Lab24 – 2.1 Create Storage Gateway](https://000024.awsfcaj.com/2-useawsstoragegw/2.1-createstoragegw/) <br> [Lab24 – 2.2 Create File Shares](https://000024.awsfcaj.com/2-useawsstoragegw/2.2-createfileshare/) <br> [Lab14 – 2.3 Import virtual machine to AWS](https://000014.awsfcaj.com/2-import-vm-to-aws/3-import-vm-to-ami/) <br> [Lab14 – 3.2 Export virtual machine from Instance](https://000014.awsfcaj.com/3-export-vm-from-aws/2-export-from-instance/) |
| 6 | - **Practice (Lab25 – Amazon FSx for Windows File Server):** <br>&emsp; + Created SSD and HDD Multi-AZ file systems and compared their performance <br>&emsp; + Created file shares and enabled deduplication, shadow copies, and user quotas <br>&emsp; + Scaled throughput and storage capacity, then deleted the environment | 16/10/26 | 16/10/26 | [Lab25 – 2.2 Create an SSD Multi-AZ file system](https://000025.awsfcaj.com/2-prerequiste/2.2-create-maz-ssd-file-system/) <br> [Lab25 – 4. Test Performance](https://000025.awsfcaj.com/4-test-performance/) <br> [Lab25 – 6. Enable data deduplication](https://000025.awsfcaj.com/6-enable-data-dedup/) <br> [Lab25 – 7. Enable shadow copies](https://000025.awsfcaj.com/7-enable-shadow-copies/) <br> [Lab25 – 12. Scale storage capacity](https://000025.awsfcaj.com/12-scale-storage-capacity/) |

### Week 5 Achievements:

* **Knowledge:**
  * Storage types: S3 for objects, EBS for block volumes attached to one instance, EFS and FSx for file systems shared by many clients
  * S3 storage classes range from Standard for frequent access to Infrequent Access, Intelligent-Tiering, and the Glacier classes for archives
  * An S3 website endpoint serves content publicly over HTTP, while CloudFront adds HTTPS and caching and can read from a private bucket
  * Versioning keeps every version of an object, and replication requires versioning on both the source and destination buckets
  * Storage Gateway links on-premises applications to S3 through file, volume, or tape interfaces, while the Snow Family moves large datasets offline
* **Hands-on skills:**
  * Delivered a static website through CloudFront while keeping the S3 bucket private
  * Set up versioning and cross-Region replication
  * Deployed a file gateway, imported and exported a virtual machine, and managed an FSx for Windows file system
* **Security and cost lessons:**
  * Block Public Access should stay on, with CloudFront as the only reader of the bucket
  * FSx file systems and gateway instances keep running and billing until they are deleted
