---
title: "Week 1 Worklog"
date: 2026-11-05
weight: 1
chapter: false
pre: "<b>1.1. </b>"
---

### Week 1 Objectives:

* Settle into the FCAJ program and understand what I need to deliver by the end of the internship.
* Build a solid mental model of cloud computing and the AWS global infrastructure.
* Prepare a personal AWS account that is secure from day one and protected against unexpected bills.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Joined the FCAJ onboarding and got to know the team and fellow interns <br>- Went through the program requirements: office bookings, events, blogs, and the final workshop <br>- Watched the Bootcamp kick-off and the workshop guide to see how the 12 weeks are organized | 09/14/2026 | 09/14/2026 | <https://www.youtube.com/watch?v=AQlsd0nWdZk> <br> <https://www.youtube.com/watch?v=mXRqgMr_97U> <br> <https://hcm-rules.awsfcaj.com/project/requirement> |
| 3 | - Studied the cloud fundamentals in Module 01-01 → 01-04: <br>&emsp; + On-demand resources and pay-as-you-go pricing versus buying hardware up front <br>&emsp; + What sets AWS apart: breadth of services, global reach, and a large community <br>&emsp; + The steps an organization takes when it starts moving to the cloud <br>&emsp; + Regions, Availability Zones, and Edge Locations, and how they support availability and low latency | 09/15/2026 | 09/15/2026 | <https://www.youtube.com/watch?v=HxYZAK1coOI> <br> <https://www.youtube.com/watch?v=IK59Zdd1poE> <br> <https://www.youtube.com/watch?v=HSzrWGqo3ME> <br> <https://www.youtube.com/watch?v=pjr5a-HYAjI> |
| 4 | - Studied the ways to work with AWS in Module 01-05: Management Console, AWS CLI, SDKs, and CloudShell <br>- **Practice (Lab01 – AWS Free Tier 2026):** <br>&emsp; + Signed up with the new sign-up flow, created the first project, and checked the $100 sign-up credit <br>&emsp; + Upgraded to the Paid plan with a monthly spend limit so that lab costs stay predictable <br>&emsp; + Reviewed the five activities that earn extra credits and the services that drain credits quickly | 09/16/2026 | 09/16/2026 | <https://www.youtube.com/watch?v=2PQYqH_HkXw> <br> <https://000001.awsfcaj.com/3-chi%E1%BA%BFn-l%C6%B0%E1%BB%A3c-nh%E1%BA%ADn-%C4%91%E1%BB%A7-200-credit/> <br> <https://000001.awsfcaj.com/4-h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-chi-ti%E1%BA%BFt-5-nhi%E1%BB%87m-v%E1%BB%A5-ki%E1%BA%BFm-ti%E1%BB%81n/> <br> <https://000001.awsfcaj.com/6-danh-s%C3%A1ch-s%C3%A1t-th%E1%BB%A7-credit-c%E1%BA%A7n-tr%C3%A1nh/> |
| 5 | - Studied cost optimization and the AWS Support plans in Module 01-06 <br>- **Practice (securing the account):** <br>&emsp; + Enabled a virtual MFA device for the root user <br>&emsp; + Created an Admins group with administrator permissions and an IAM admin user in it <br>&emsp; + Signed in through the account sign-in URL with the IAM user and reviewed the account recovery options | 09/17/2026 | 09/17/2026 | <https://www.youtube.com/watch?v=IY61YlmXQe8> <br> <https://www.youtube.com/watch?v=1dG5xutGbr4> <br> <https://www.youtube.com/watch?v=b9pK1oG534Q> <br> <https://000002.awsfcaj.com/2-create-admin-user-and-group/2.2-create-admin-user/> <br> <https://www.youtube.com/watch?v=69iKhwI7k2Y> |
| 6 | - **Practice (Lab07 – AWS Budgets):** <br>&emsp; + Created a monthly cost budget with an email alert when spending crosses the threshold <br>&emsp; + Added usage, Reserved Instance, and Savings Plans budgets to see what each one tracks, then deleted them <br>- **Practice (Lab09 – AWS Support):** compared the Support plans and reviewed the request types and severity levels <br>- Summarized the key points of Module 01 in my notes | 09/18/2026 | 09/18/2026 | <https://000007.awsfcaj.com/2-cost-budgets/> <br> <https://000007.awsfcaj.com/3-usage-budget/> <br> <https://000009.awsfcaj.com/1-support-plans/> <br> <https://000009.awsfcaj.com/3-manage-cases/3.2-select-severity/> <br> <https://www.youtube.com/watch?v=Hku7exDBURo> |

### Week 1 Achievements:

* Understood the following concepts:
  * Cloud computing: on-demand resources, elasticity, and pay-as-you-go pricing instead of up-front hardware investment
  * AWS global infrastructure: each Region contains several isolated Availability Zones, while Edge Locations bring content closer to users through CloudFront
  * AWS Free Tier 2026: the difference between the Free and Paid plans, how credits are earned, and which services consume them fastest
  * AWS Support: what each plan offers and how the severity of a case affects response time

* Created an AWS account with the new sign-up flow and set a monthly spend limit.

* Secured the root user with MFA and moved daily work to an IAM admin user.

* Configured cost and usage budgets with email alerts.

* Learned the following security and cost lessons:
  * The root user is only for account-level tasks, and its MFA device must be kept safe
  * Spend limits and budgets should be in place before any lab so that forgotten resources are noticed early
