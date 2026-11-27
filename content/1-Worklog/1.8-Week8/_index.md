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
| 2 | - **Practice (Lab43 – part 2):** <br>&emsp; + Created a replication instance, source and target endpoints, and a migration task <br>&emsp; + Ran a migration with DMS Serverless, which adjusts its capacity on its own <br>&emsp; + Followed the task through CloudWatch metrics and logs and worked through the troubleshooting scenarios | 11/02/2026 | 11/02/2026 | <https://000043.awsfcaj.com/> <br> <https://www.youtube.com/watch?v=4LoLN6D1UU8> <br> <https://www.youtube.com/watch?v=tWGwAz_Ewk4> <br> <https://www.youtube.com/watch?v=TDlc5bRh6H8> <br> <https://www.youtube.com/watch?v=MU8XHe3OoxQ> |
| 3 | - **Practice (Lab60 – Amazon DynamoDB):** <br>&emsp; + Learned how partition keys, sort keys, and secondary indexes shape the queries you can run <br>&emsp; + Created a table and wrote, read, and queried items in the console and CloudShell <br>&emsp; + Repeated the same operations in Python with boto3 | 11/03/2026 | 11/03/2026 | <https://000060.awsfcaj.com/1-introduce/1.2-primarykey/> <br> <https://000060.awsfcaj.com/1-introduce/1.3-secondaryindexes/> <br> <https://000060.awsfcaj.com/1-introduce/1.6-readwritecapacitymode/> <br> <https://000060.awsfcaj.com/2-prerequiste/2.2-useawscloudshell/> <br> <https://000060.awsfcaj.com/3-gettingstartedwithawssdk/3.2-pythonandynamodb/> |
| 4 | - **Practice (Lab39 – DynamoDB Immersion Day):** <br>&emsp; + Compared Query and Scan on the same data <br>&emsp; + Added a global secondary index to support a new access pattern <br>&emsp; + Turned on point-in-time recovery and created on-demand backups | 11/04/2026 | 11/04/2026 | <https://000039.awsfcaj.com/1-lhol/1.2/> <br> <https://000039.awsfcaj.com/1-lhol/1.3/> <br> <https://000039.awsfcaj.com/1-lhol/1.4/> |
| 5 | - **Practice (Lab35 – Data Lake):** <br>&emsp; + Streamed sample data into S3 with Amazon Data Firehose <br>&emsp; + Ran a Glue Crawler to build the Data Catalog <br>&emsp; + Queried the data with Athena and built charts in QuickSight | 11/05/2026 | 11/05/2026 | <https://000035.awsfcaj.com/3-ingestandstore/3.2-createdeliverystream/> <br> <https://000035.awsfcaj.com/3-ingestandstore/3.3-generatesampledata/> <br> <https://000035.awsfcaj.com/4-createdatacatalog/4.1-creategluecrawler/> <br> <https://000035.awsfcaj.com/6-analyzeandvisualize/6.1-analyzedatawithathena/> <br> <https://000035.awsfcaj.com/6-analyzeandvisualize/6.2-visualizewithquicksight/> |
| 6 | - **Practice (Lab40):** queried cost and usage data with AWS Glue and Amazon Athena to see where the spending goes and how tags allocate cost <br>- **Practice (Lab73):** built a QuickSight dashboard with line, KPI, and pie charts, then added filters and interactive actions | 11/06/2026 | 11/06/2026 | <https://000040.awsfcaj.com/3-costandusageanalysis/3.2-cost/> <br> <https://000040.awsfcaj.com/3-costandusageanalysis/3.3-taggingandcost/> <br> <https://000073.awsfcaj.com/2-first-dashboard/> <br> <https://000073.awsfcaj.com/4-add-interactivity/> |

### Week 8 Achievements:

* Understood the following concepts:
  * AWS DMS: a replication instance runs tasks between a source and a target endpoint, with a full load followed by ongoing change data capture
  * DynamoDB: the partition key spreads data across partitions, the sort key orders items within one, and a global secondary index adds another access pattern
  * Capacity modes: on-demand for unpredictable traffic and provisioned for steady traffic; reads are eventually consistent by default
  * Data lake flow: Firehose buffers data into S3, a Glue Crawler registers tables in the Data Catalog, Athena runs SQL directly on S3, and QuickSight visualizes the results

* Migrated a database with DMS and DMS Serverless, and monitored it through CloudWatch and task logs.

* Created, queried, and backed up DynamoDB tables from the console, CloudShell, and boto3.

* Built a working ingest → catalog → query → dashboard pipeline.

* Learned the following security and cost lessons:
  * A DynamoDB Scan reads the whole table, so designing for Query keeps both latency and cost down
  * Athena charges by the amount of data scanned, and DMS replication instances and QuickSight subscriptions must be removed after the lab
