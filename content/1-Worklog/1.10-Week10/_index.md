---
title: "Week 10 Worklog"
date: 2026-11-05
weight: 10
chapter: false
pre: "<b>1.10. </b>"
---

### Week 10 Objectives:

* Research how applications on EC2 get IAM role credentials and publish Blog 2 on IAM roles and IMDSv2.
* Bring the report up to date with the bilingual Blog 1 page and the reports for Event 4 and Event 5.
* Start planning the personal workshop: requirements, proposal outline, and an architecture design checklist.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Research for Blog 2 – IAM roles on EC2 and IMDSv2:** <br>&emsp; + Read why AWS recommends temporary IAM role credentials instead of long-term access keys for workloads on AWS <br>&emsp; + Studied instance profiles: the console creates one with the same name as the role, an instance profile holds only one role, and permissions change by replacing the instance profile <br>&emsp; + Traced where credentials come from: IMDS at `169.254.169.254`, the `iam/security-credentials/<role-name>` path, automatic rotation, and caching to avoid IMDS throttling <br>&emsp; + Studied the IMDSv2 session flow (PUT for a token with a TTL of up to six hours, then GET with the token header) and how it defends against open WAFs, reverse proxies, SSRF, and open firewalls | 11/16/2026 | 11/16/2026 | [IAM – Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) <br> [IAM – IAM role for applications on EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) <br> [EC2 – Retrieve security credentials from instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html) <br> [EC2 – Use the Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) <br> [AWS Security Blog – Defense in depth with IMDSv2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/) |
| 3 | - **Blog 2:** finished and posted *IAM roles on EC2 and IMDSv2: Where does your application get its credentials?* to AWS Study Group <br>&emsp; + Added the common mistakes: hop limit 1 blocking containers, curl without `-f` storing an error as the token, proxies that make HTTP calls for the application, and older instances still on IMDSv1 after an account-level default <br>&emsp; + Showed how to require IMDSv2 at launch (`HttpTokens=required`, hop limit 2 for containers) and at the account level <br>&emsp; + Prepared the Vietnamese post for Facebook and the English page for the report <br>- Added Blog 1 to the report as a bilingual page with the NAT gateway diagram and its source <br>- Wrote the reports for Event 4 (FCAJ Community Day, 10/31) and Event 5 (AWSxFPTU Cloud Mastery 1, 11/14) with check-in and session photos | 11/17/2026 | 11/17/2026 | [Blog 2 – AWS Study Group post](https://www.facebook.com/groups/awsstudygroupfcj/posts/2340606156704343) <br> [EC2 – Access instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) <br> [EC2 – Configure instance metadata options for new instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html) <br> [EC2 – IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) |
| 4 | - **Workshop planning – requirements:** <br>&emsp; + Re-read the FCAJ workshop requirements: a real use case on AWS (serverless, data pipeline, observability, event-driven, containers…) with at least 3 AWS services <br>&emsp; + Went through the workshop standards: architecture that follows the Well-Architected Framework, a reproducible step-by-step guide, a working demo, monitoring with logs, metrics, and alerts, a Pricing Calculator estimate, and a full clean-up guide <br>&emsp; + Noted the scoring rules: no COST section means 0 for Presentation, and no working demo means 0 for Demo <br>&emsp; + Mapped each requirement to the report sections 5.1–5.9 and turned them into a completion checklist | 11/18/2026 | 11/18/2026 | [FCAJ – Workshop requirements](https://hcm-rules.awsfcaj.com/project/requirement) <br> [FCAJ – Workshop standards](https://hcm-rules.awsfcaj.com/project/standard) |
| 5 | - **Workshop planning – proposal outline:** <br>&emsp; + Studied the structure of the sample proposal: executive summary, problem statement, solution architecture, technical implementation, timeline, budget, risk assessment, and expected outcomes <br>&emsp; + Outlined my own proposal: the real problem and target users, measurable objectives and success criteria, and the AWS services with the reason for choosing each one <br>&emsp; + Listed the main risks (unexpected cost, excess permissions or leaked secrets, failed deployment, missed deadline) and how to reduce each | 11/19/2026 | 11/19/2026 | [FCJ workshop sample – Proposal](https://workshop-sample.awsfcaj.com/2-proposal/) <br> [FCJ workshop template (GitHub)](https://github.com/thienluhoan/fcj-workshop-template) <br> [FCAJ – Workshop standards](https://hcm-rules.awsfcaj.com/project/standard) |
| 6 | - **Workshop planning – architecture and design review:** <br>&emsp; + Prepared to draw the diagram myself in draw.io with the official AWS Architecture Icons, correct service names, and clear data-flow arrows <br>&emsp; + Built a design checklist from the Well-Architected Framework, focusing on security: least-privilege IAM roles, keeping resources out of the internet (private subnets, VPC endpoints, tight security groups), and no hard-coded credentials <br>&emsp; + Added reliability and operations points: event-driven design or SQS to absorb load, and CloudWatch logs, metrics, and alarms from the start | 11/20/2026 | 11/20/2026 | [Video – Drawing AWS architecture with draw.io](https://www.youtube.com/watch?v=l8isyDe-GwY) <br> [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/) <br> [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/framework.html) |

### Week 10 Achievements:

* **Knowledge:**
  * EC2 gets an IAM role through an instance profile; the SDKs and AWS CLI read the role's temporary credentials from IMDS, so no access key is stored on the instance
  * Role credentials are rotated automatically, and new ones are available at least five minutes before the old ones expire
  * IMDSv2 requires a PUT for a session token and then GET requests carrying that token; the token is bound to the instance and an invalid one returns 401
  * IMDSv2 rejects PUT requests with `X-Forwarded-For`, and its token response has a hop limit of 1, which blocks most relayed and SSRF requests
  * IMDSv2 does not replace least privilege: code running on the instance can still use the role's permissions
  * A workshop that meets the FCAJ standard needs a Well-Architected design, a reproducible guide, monitoring, a Pricing Calculator estimate, clean-up steps, and a working demo; missing COST or the demo costs a whole scoring category
* **Hands-on skills:**
  * Wrote and posted a second technical blog based on the EC2 and IAM user guides and the AWS Security Blog
  * Kept the report up to date with bilingual blog and event pages
  * Turned the workshop requirements into a checklist, a proposal outline, and a design checklist
* **Next steps:**
  * Research and write Blog 3 on Amazon RDS high availability
  * Finish planning the workshop: cost estimate, clean-up, testing, and monitoring
