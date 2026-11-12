---
title: "Week 8 Worklog"
date: 2026-11-05
weight: 8
chapter: false
pre: "<b>1.8. </b>"
---

### Week 8 Objectives:

* Move data between database engines with AWS DMS.
* Model and query data in Amazon DynamoDB.
* Build a small data lake, from ingestion to dashboard.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice (Lab43 – part 2):** <br>&emsp; + Created a replication instance, source and target endpoints, and a migration task <br>&emsp; + Ran a migration with DMS Serverless, which adjusts its capacity on its own <br>&emsp; + Followed the task through CloudWatch metrics and logs and worked through the troubleshooting scenarios | 02/11/26 | 02/11/26 | <https://000043.awsfcaj.com/> |
| 3 | - **Practice (Lab60 – Amazon DynamoDB):** <br>&emsp; + Learned how partition keys, sort keys, and secondary indexes shape the queries you can run <br>&emsp; + Created a table and wrote, read, and queried items in the console and CloudShell <br>&emsp; + Repeated the same operations in Python with boto3 | 03/11/26 | 03/11/26 | <https://000060.awsfcaj.com/> |
| 4 | - **Practice (Lab39 – DynamoDB Immersion Day):** <br>&emsp; + Compared Query and Scan on the same data <br>&emsp; + Added a global secondary index to support a new access pattern <br>&emsp; + Turned on point-in-time recovery and created on-demand backups | 04/11/26 | 04/11/26 | <https://000039.awsfcaj.com/> |
| 5 | - **Practice (Lab35 – Data Lake):** <br>&emsp; + Streamed sample data into S3 with Amazon Data Firehose <br>&emsp; + Ran a Glue Crawler to build the Data Catalog <br>&emsp; + Queried the data with Athena and built charts in QuickSight | 05/11/26 | 05/11/26 | <https://000035.awsfcaj.com/> |
| 6 | - **Practice (Lab40):** queried cost and usage data with AWS Glue and Amazon Athena to see where the spending goes <br>- **Practice (Lab73):** built a QuickSight dashboard with filters and interactive actions | 06/11/26 | 06/11/26 | <https://000040.awsfcaj.com/> <br> <https://000073.awsfcaj.com/> |

### Week 8 Achievements:

* I migrated a database with AWS DMS and know where to look when a task fails.
* I learned to design DynamoDB tables around the queries the application needs rather than around the entities.
* I built a working analytics pipeline:
  * Ingest with Firehose
  * Catalog with Glue
  * Query with Athena
  * Visualize with QuickSight
* I can use Athena to analyze cost data, which will help with the cost estimate for my workshop.
