---
title: "Blogs Posted"
date: 2026-11-05
weight: 3
chapter: false
pre: "<b>3. </b>"
---

This section lists the blogs I have posted to [AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj).

###  [Blog 1 - Cleaning up AWS resources: The costs that continue after you "turn things off"](3.1-Blog1/)
A summary based on the official AWS documentation and pricing pages: why "stopped" resources can still be billed, the costs that are easy to miss (NAT gateways, public IPv4, snapshots and AMIs, DMS, Quick Sight, Athena), the limits of AWS Budgets, and a clean-up process after practicing.

###  [Blog 2 - IAM roles on EC2 and IMDSv2: Where does your application get its credentials?](3.2-Blog2/)
How an instance profile delivers temporary IAM role credentials to EC2 through the Instance Metadata Service, the IMDSv2 token flow (PUT for a token, GET with the token), why IMDSv2 reduces the risk from SSRF and open proxies, common configuration mistakes, and how to require IMDSv2.

###  [Blog 3 - Amazon RDS: Multi-AZ or read replica? Choosing between high availability and read scaling](3.3-Blog3/)
A comparison of Multi-AZ DB instances (synchronous standby, not readable), Multi-AZ DB clusters (one writer and two readers in three AZs, semisynchronous replication), and read replicas (asynchronous, manually promoted, can be cross-Region): how they replicate and fail over, their limits, how to combine them, and what the application must do to handle failover.
