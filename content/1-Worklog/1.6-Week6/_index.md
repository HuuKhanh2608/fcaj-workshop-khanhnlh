---
title: "Week 6 Worklog"
date: 2026-11-05
weight: 6
chapter: false
pre: "<b>1.6. </b>"
---

### Week 6 Objectives:

* Understand where AWS's security responsibility ends and mine begins.
* Apply least privilege with IAM policies, conditions, and permission boundaries.
* Use tags and Lambda to organize resources and automate routine operations.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Studied the Shared Responsibility Model (Module 05-01) <br>- Studied AWS IAM in depth (Module 05-02): <br>&emsp; + Users, groups, and roles <br>&emsp; + How policies are evaluated, including the effect of an explicit deny | 19/10/26 | 19/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Studied the identity and security services in Module 05-03 → 05-07: Amazon Cognito, AWS Organizations, IAM Identity Center, AWS KMS, and AWS Security Hub <br>- **Practice (Lab18):** enabled Security Hub and reviewed the score and findings for each security standard | 20/10/26 | 20/10/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) <br> <https://000018.awsfcaj.com/> |
| 4 | - **Practice (Lab27):** <br>&emsp; + Tagged EC2 resources from the console and the AWS CLI <br>&emsp; + Filtered resources by tag and grouped them in a Resource Group <br>- **Practice (Lab28):** <br>&emsp; + Wrote an IAM policy that allows EC2 actions only on correctly tagged resources in the allowed Region <br>&emsp; + Switched to the restricted role and confirmed what it can and cannot do | 21/10/26 | 21/10/26 | <https://000027.awsfcaj.com/> <br> <https://000028.awsfcaj.com/> |
| 5 | - **Practice (Lab22):** <br>&emsp; + Prepared a VPC, a security group, and a tagged EC2 instance <br>&emsp; + Set up a Slack incoming webhook for notifications <br>&emsp; + Created an IAM role and two Lambda functions that stop and start instances by tag <br>&emsp; + Checked the instance state and the Slack messages, then cleaned up | 22/10/26 | 22/10/26 | <https://000022.awsfcaj.com/> |
| 6 | - **Practice (Lab30):** capped what an IAM user can do with a permission boundary, even when the user's own policy grants more <br>- **Practice (Lab44):** <br>&emsp; + Created an admin role and allowed a user to switch into it <br>&emsp; + Added conditions so that the role can be assumed only from a given IP address and within a time window | 23/10/26 | 23/10/26 | <https://000030.awsfcaj.com/> <br> <https://000044.awsfcaj.com/> |

### Week 6 Achievements:

* I can explain the Shared Responsibility Model with concrete examples for EC2 and for managed services.
* I apply least privilege in several layers:
  * Identity policies with tag and Region conditions
  * Permission boundaries that cap the maximum permissions
  * Role conditions based on source IP and time
* I organize resources with tags, which also makes access control and cost tracking easier.
* I automated a routine task with Lambda by turning idle instances off to save money.
