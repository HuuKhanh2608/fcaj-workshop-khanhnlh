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
| 2 | - **Practice (Lab43 – part 2):** <br>&emsp; + Created a replication instance, source and target endpoints, and a migration task <br>&emsp; + Ran a migration with DMS Serverless, which adjusts its capacity on its own <br>&emsp; + Followed the task through CloudWatch metrics and logs and worked through the troubleshooting scenarios | 02/11/26 | 02/11/26 | [Lab43 – Database Schema Conversion & Migration](https://000043.awsfcaj.com/) <br> [Video Lab43-11 – Create migration task and endpoints](https://www.youtube.com/watch?v=4LoLN6D1UU8) <br> [Video Lab43-13 – Create a serverless migration](https://www.youtube.com/watch?v=tWGwAz_Ewk4) <br> [Video Lab43-15 – Task logs](https://www.youtube.com/watch?v=TDlc5bRh6H8) <br> [Video Lab43-17 – Troubleshoot table errors](https://www.youtube.com/watch?v=MU8XHe3OoxQ) |
| 3 | - **Practice (Lab60 – Amazon DynamoDB):** <br>&emsp; + Learned how partition keys, sort keys, and secondary indexes shape the queries you can run <br>&emsp; + Created a table and wrote, read, and queried items in the console and CloudShell <br>&emsp; + Repeated the same operations in Python with boto3 | 03/11/26 | 03/11/26 | [Lab60 – 1.2 Primary Key](https://000060.awsfcaj.com/1-introduce/1.2-primarykey/) <br> [Lab60 – 1.3 Secondary Index](https://000060.awsfcaj.com/1-introduce/1.3-secondaryindexes/) <br> [Lab60 – 1.6 Read/Write Capacity Mode](https://000060.awsfcaj.com/1-introduce/1.6-readwritecapacitymode/) <br> [Lab60 – 2.2 Use AWS CloudShell](https://000060.awsfcaj.com/2-prerequiste/2.2-useawscloudshell/) <br> [Lab60 – 3.2 Python and DynamoDB](https://000060.awsfcaj.com/3-gettingstartedwithawssdk/3.2-pythonandynamodb/) |
| 4 | - **Practice (Lab39 – DynamoDB Immersion Day):** <br>&emsp; + Compared Query and Scan on the same data <br>&emsp; + Added a global secondary index to support a new access pattern <br>&emsp; + Turned on point-in-time recovery and created on-demand backups | 04/11/26 | 04/11/26 | [Lab39 – 1.2 Explore DynamoDB with the CLI](https://000039.awsfcaj.com/1-lhol/1.2/) <br> [Lab39 – 1.3 Explore the DynamoDB Console](https://000039.awsfcaj.com/1-lhol/1.3/) <br> [Lab39 – 1.4 Backups](https://000039.awsfcaj.com/1-lhol/1.4/) |
| 5 | - **Practice (Lab35 – Data Lake):** <br>&emsp; + Streamed sample data into S3 with Amazon Data Firehose <br>&emsp; + Ran a Glue Crawler to build the Data Catalog <br>&emsp; + Queried the data with Athena and built charts in QuickSight | 05/11/26 | 05/11/26 | [Lab35 – 3.2 Create Firehose Stream](https://000035.awsfcaj.com/3-ingestandstore/3.2-createdeliverystream/) <br> [Lab35 – 3.3 Create Sample Data](https://000035.awsfcaj.com/3-ingestandstore/3.3-generatesampledata/) <br> [Lab35 – 4.1 Create Glue Crawler](https://000035.awsfcaj.com/4-createdatacatalog/4.1-creategluecrawler/) <br> [Lab35 – 6.1 Analysis with Athena](https://000035.awsfcaj.com/6-analyzeandvisualize/6.1-analyzedatawithathena/) <br> [Lab35 – 6.2 Visualize with Amazon Quick](https://000035.awsfcaj.com/6-analyzeandvisualize/6.2-visualizewithquicksight/) |
| 6 | - **Practice (Lab40):** queried cost and usage data with AWS Glue and Amazon Athena to see where the spending goes and how tags allocate cost <br>- **Practice (Lab73):** built a QuickSight dashboard with line, KPI, and pie charts, then added filters and interactive actions | 06/11/26 | 06/11/26 | [Lab40 – 3.2 Cost Research](https://000040.awsfcaj.com/3-costandusageanalysis/3.2-cost/) <br> [Lab40 – 3.3 Tagging and Cost Allocation](https://000040.awsfcaj.com/3-costandusageanalysis/3.3-taggingandcost/) <br> [Lab73 – 3. Build dashboard](https://000073.awsfcaj.com/2-first-dashboard/) <br> [Lab73 – 5. Create Interactive Dashboard](https://000073.awsfcaj.com/4-add-interactivity/) |

### Week 8 Achievements:

* **Knowledge:**
  * AWS DMS: a replication instance runs tasks between a source and a target endpoint, with a full load followed by ongoing change data capture
  * DynamoDB: the partition key spreads data across partitions, the sort key orders items within one, and a global secondary index adds another access pattern
  * Capacity modes: on-demand for unpredictable traffic and provisioned for steady traffic; reads are eventually consistent by default
  * Data lake flow: Firehose buffers data into S3, a Glue Crawler registers tables in the Data Catalog, Athena runs SQL directly on S3, and QuickSight visualizes the results
* **Hands-on skills:**
  * Migrated a database with DMS and DMS Serverless, and monitored it through CloudWatch and task logs
  * Created, queried, and backed up DynamoDB tables from the console, CloudShell, and boto3
  * Built a working ingest → catalog → query → dashboard pipeline
* **Security and cost lessons:**
  * A DynamoDB Scan reads the whole table, so designing for Query keeps both latency and cost down
  * Athena charges by the amount of data scanned, and DMS replication instances and QuickSight subscriptions must be removed after the lab
