---
title: "Week 11 Worklog"
date: 2026-11-05
weight: 11
chapter: false
pre: "<b>1.11. </b>"
---

### Week 11 Objectives:

* Publish Blog 3 comparing the Amazon RDS options for high availability and read scaling.
* Align the whole worklog with the official FCJ template.
* Finish planning the workshop: cost estimate approach, clean-up, testing, and monitoring.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Blog 3:** finished and posted *Amazon RDS: Multi-AZ or read replica? Choosing between high availability and read scaling* to AWS Study Group <br>&emsp; + Compared the Multi-AZ DB instance, Multi-AZ DB cluster, and read replica by replication mode, failover, readable copies, placement, and supported engines <br>&emsp; + Multi-AZ DB instance: synchronous standby that serves no reads, DNS-based failover in about 60–120 seconds, backups taken from the standby <br>&emsp; + Multi-AZ DB cluster: one writer and two readers in three AZs, semisynchronous replication, failover usually under 35 seconds, writer/reader/instance endpoints and its limitations <br>&emsp; + Read replica: asynchronous replication, up to 15 replicas (5 for Oracle), cross-Region, manual promotion to a standalone instance <br>&emsp; + Listed what the application must do: connect through endpoints, keep the DNS TTL at 60 seconds or less, reconnect and retry, separate reads from writes, alarm on `ReplicaLag`, and test failover <br>&emsp; + Added two diagrams from the RDS User Guide with their sources | 11/23/2026 | 11/23/2026 | <https://www.facebook.com/groups/awsstudygroupfcj/posts/2347065196058439> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html> <br> <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Monitoring.html> |
| 3 | - **Workshop planning – cost and clean-up:** <br>&emsp; + Learned how AWS Pricing Calculator works: groups that follow the architecture, the calculation behind each price, a saved link to share, and export to CSV or PDF <br>&emsp; + Planned the estimate from a realistic load: number of requests, storage, and network traffic, with the Region and date of the estimate <br>&emsp; + Listed cost optimizations to evaluate: Free Tier, pay-per-use serverless services, S3 Lifecycle policies, and right-sized compute <br>&emsp; + Drafted the clean-up checklist (delete stacks, empty and delete S3 buckets, delete alarms, release Elastic IPs), reusing the lessons from Blog 1 | 11/24/2026 | 11/24/2026 | <https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html> <br> <https://calculator.aws/#/> <br> <https://hcm-rules.awsfcaj.com/project/standard> |
| 4 | - Compared the worklog with the official FCJ template and sample site <br>- Kept each week to exactly five weekday rows; Saturday events stay in the Events section <br>- Changed dates to the template formats: MM/DD/YYYY in English and DD/MM/YYYY in Vietnamese | 11/25/2026 | 11/25/2026 | <https://github.com/thienluhoan/fcj-workshop-template> <br> <https://workshop-sample.awsfcaj.com/1-worklog/> |
| 5 | - **Workshop planning – testing and observability:** <br>&emsp; + Read the updated Lab08 CloudWatch workshop to plan monitoring: metrics with search and math expressions, Logs Insights queries, metric filters that turn error lines into a metric, an alarm that emails through Amazon SNS, and a dashboard <br>&emsp; + Planned the test cases: the main flow plus error cases such as malformed requests and overload, sent with cURL or Postman and checked in CloudWatch Logs and the stored data <br>&emsp; + Planned the demo evidence (live link or recorded video) and set the Week 12 timeline: build, test, COST, clean-up, and demo | 11/26/2026 | 11/26/2026 | <https://000008.awsfcaj.com/3-cloud-watch-metric/> <br> <https://000008.awsfcaj.com/4-cloud-watch-logs/4.2-logs-insights/> <br> <https://000008.awsfcaj.com/4-cloud-watch-logs/4.3-metric-filter/> <br> <https://000008.awsfcaj.com/5-cloud-watch-alarm/> <br> <https://000008.awsfcaj.com/6-cloud-watch-dashboard/> |
| 6 | - Updated the Blogs Posted section: <br>&emsp; + Added the AWS Study Group post link and posting date to the English and Vietnamese pages of all three blogs <br>&emsp; + Checked each link against the post on Facebook to confirm the title and posting time <br>- Brought the worklog up to date with the blogs: <br>&emsp; + Added the Blog 1 posting to Week 9 (11/13) <br>&emsp; + Wrote the Blog 2 research and posting days in Week 10 (11/16–11/17) and the Blog 3 posting and template alignment days in Week 11 (11/23, 11/25) <br>&emsp; + Linked each task to the AWS documentation the blog cites and updated the Week 10 and Week 11 titles on the Worklog page <br>- Aligned the whole report with the FCJ sample site and template: <br>&emsp; + Worklog: described the three-month internship (09/14–12/14/2026), listed the weekly achievements as sentences, and used bare URLs in the Reference Material column <br>&emsp; + Blogs: moved each post link and posting date to the end of the article <br>&emsp; + Events: used the template headings and removed the source notes <br>&emsp; + Workshop: switched the section page to Overview and Content and used the template headings and page names <br>- Filled in the Self-Assessment and Sharing and Feedback pages following the template <br>- Updated the home page with my class (FCAJ - FPT - Season 4) and profile photo <br>- Checked all 211 links in the worklog and made the Lab01 links readable <br>- Installed Hugo 0.134.3, the version used by the deploy workflow, to build and check the site locally before publishing | 11/27/2026 | 11/27/2026 | <https://www.facebook.com/groups/awsstudygroupfcj/posts/2336113367153622> <br> <https://www.facebook.com/groups/awsstudygroupfcj/posts/2340606156704343> <br> <https://www.facebook.com/groups/awsstudygroupfcj/posts/2347065196058439> <br> <https://github.com/thienluhoan/fcj-workshop-template> <br> <https://workshop-sample.awsfcaj.com/> <br> <https://github.com/gohugoio/hugo/releases/tag/v0.134.3> |

### Week 11 Achievements:

* Understood the following concepts:
  * Multi-AZ is for surviving failures, while read replicas are for sharing read load; the two can be combined
  * The standby of a Multi-AZ DB instance cannot serve reads, and synchronous replication adds write and commit latency
  * A Multi-AZ DB cluster commits once at least one reader acknowledges a change and fails over faster, but it supports only MySQL and PostgreSQL on certain instance classes
  * A read replica can lag behind its source, and promoting it is manual and one-way
  * Failover changes the IP behind an endpoint, so applications must use endpoints, a short DNS TTL, and reconnect logic
  * AWS Pricing Calculator estimates are grouped by architecture, can be shared by link, and exported to CSV or PDF
  * CloudWatch can turn error log lines into a metric with a metric filter and alert on it through an alarm and SNS

* Wrote and posted a third technical blog based on the Amazon RDS User Guide.

* Reviewed all 12 weekly tables against the official template.

* Completed the Blogs Posted section with verified post links and dates for all three blogs.

* Aligned the whole report with the FCJ template and filled in the Self-Assessment and Sharing and Feedback pages.

* Set up Hugo locally to build the site and check links before deploying.

* Planned the cost estimate, clean-up, test cases, monitoring, and demo for the workshop.

* Identified the next steps:
  * Write the proposal and draw the architecture diagram
  * Build, test, and monitor the workshop, then complete COST, clean-up, and the demo in Week 12
