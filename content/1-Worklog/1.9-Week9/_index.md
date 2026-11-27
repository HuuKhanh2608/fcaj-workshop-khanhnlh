---
title: "Week 9 Worklog"
date: 2026-11-05
weight: 9
chapter: false
pre: "<b>1.9. </b>"
---

### Week 9 Objectives:

* Finish the remaining analytics labs.
* Choose a workshop topic that solves a real problem with at least 3 AWS services.
* Bring the internship report in line with the official template.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice (Lab70):** <br>&emsp; + Profiled and cleaned the lab dataset with AWS Glue DataBrew <br>&emsp; + Converted the data to Parquet with AWS Glue <br>&emsp; + Compared Athena queries with and without partitioning and a columnar format | 11/09/2026 | 11/09/2026 | [Lab70 – 2.2 Data Profiling](https://000070.awsfcaj.com/2-datapre/2.2-profiling/) <br> [Lab70 – 2.3 Clean & Transform Data](https://000070.awsfcaj.com/2-datapre/2.3-cleantransform/) <br> [Lab70 – 3.3 Transform to Parquet](https://000070.awsfcaj.com/3-ingestglue/3.3-transformparquet/) <br> [Lab70 – 4.6 Data Partition](https://000070.awsfcaj.com/5-athena/5.6-partition/) <br> [Lab70 – 4.7 Columnar vs Row based](https://000070.awsfcaj.com/5-athena/5.7-columnar/) |
| 3 | - **Practice (Lab72 – Analytics on AWS):** <br>&emsp; + Ingested streaming data with Firehose and catalogued it with Glue <br>&emsp; + Transformed the data with Glue Studio and DataBrew <br>&emsp; + Queried the results with Athena and exposed them through a Lambda function | 11/10/2026 | 11/10/2026 | [Lab72 – 3.1 Creating Kinesis Firehose](https://000072.awsfcaj.com/3.ingestandstore/3.1-create-kinesis-firehose/) <br> [Lab72 – 4.2 Creating AWS Glue Crawlers](https://000072.awsfcaj.com/4.catalogdata/4.2-create-aws-glue-crawlers/) <br> [Lab72 – 6. Transform with AWS Glue Studio](https://000072.awsfcaj.com/6-graphical-interface/) <br> [Lab72 – 9. Analysis with Athena](https://000072.awsfcaj.com/9-athena/) <br> [Lab72 – 12. Serve with Lambda](https://000072.awsfcaj.com/12-lambda/) |
| 4 | - Reviewed Modules 01 → 07 and noted the services I am most confident with <br>- Re-read the workshop requirements: architecture, reproducible guide, monitoring, cost estimate, clean-up, and demo <br>- Listed candidate workshop topics that use at least 3 AWS services | 11/11/2026 | 11/11/2026 | [Video – How to build an AWS workshop](https://www.youtube.com/watch?v=mXRqgMr_97U) <br> [FCAJ – Workshop requirements](https://hcm-rules.awsfcaj.com/project/requirement) |
| 5 | - Compared my report with the official FCJ workshop template <br>- Restructured the Worklog, Proposal, Blogs, and Self-assessment pages to follow the template <br>- Planned the 12-week timeline based on the FCJ playlist and labs | 11/12/2026 | 11/12/2026 | [FCJ workshop template (GitHub)](https://github.com/thienluhoan/fcj-workshop-template) <br> [FCJ workshop sample site](https://workshop-sample.awsfcaj.com/) |
| 6 | - Watched the guide on drawing AWS architecture diagrams with draw.io <br>- Narrowed down the workshop topic and sketched a first draft of the architecture <br>- **Blog 1:** posted *Cleaning up AWS resources: The costs that continue after you "turn things off"* to AWS Study Group <br>&emsp; + Checked the official pricing pages for the costs that remain after a lab: NAT gateway hours, public IPv4 addresses, EBS snapshots and AMIs, DMS replication instances, Quick Sight users, and Athena query results <br>&emsp; + Explained why a stopped EC2 instance still incurs EBS and Elastic IP charges, and why AWS Budgets only sends alerts <br>&emsp; + Proposed a clean-up order and a final check with AWS Resource Explorer and Billing | 11/13/2026 | 11/13/2026 | [Video – Drawing AWS architecture with draw.io](https://www.youtube.com/watch?v=l8isyDe-GwY) <br> [Blog 1 – AWS Study Group post](https://www.facebook.com/groups/awsstudygroupfcj/posts/2336113367153622) <br> [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/) <br> [AWS Budgets – Managing your costs](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |

### Week 9 Achievements:

* **Knowledge:**
  * Glue DataBrew profiles a dataset and applies cleaning steps as a reusable recipe
  * Parquet stores data by column, so Athena reads only the columns a query needs; partitions let it skip whole folders
  * An analytics platform can combine streaming ingestion, ETL with Glue or EMR, SQL with Athena, a warehouse in Redshift, and an API through Lambda
  * A stopped instance still pays for its EBS volumes and Elastic IP; NAT gateways and public IPv4 addresses are billed by the hour even with no traffic
  * The workshop must show an architecture diagram, a reproducible guide, monitoring with logs, metrics, and alerts, a cost estimate, clean-up steps, and a working demo
* **Hands-on skills:**
  * Built an ETL flow that turns raw data into partitioned Parquet tables
  * Queried and served analytics results with Athena and Lambda
  * Restructured the internship report to match the official template
  * Wrote and posted my first blog to AWS Study Group, based on official AWS documentation and pricing pages
* **Next steps:**
  * Decide on the workshop topic and finish the architecture diagram
  * Write the proposal and the cost estimate with AWS Pricing Calculator
