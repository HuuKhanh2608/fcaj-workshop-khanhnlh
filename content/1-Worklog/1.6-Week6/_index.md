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
| 2 | - Studied the Shared Responsibility Model (Module 05-01) <br>- Studied AWS IAM in depth (Module 05-02): <br>&emsp; + Users, groups, roles, and the policies attached to them <br>&emsp; + How a request is evaluated, including the effect of an explicit deny | 10/19/2026 | 10/19/2026 | <https://www.youtube.com/watch?v=tsobAlSg19g> <br> <https://www.youtube.com/watch?v=N_vlJGAqZxo> |
| 3 | - Studied the identity and security services in Module 05-03 → 05-07: <br>&emsp; + Amazon Cognito for application users and AWS Organizations for managing multiple accounts <br>&emsp; + IAM Identity Center for single sign-on and AWS KMS for encryption keys <br>- **Practice (Lab18):** enabled Security Hub and reviewed the score and findings for each security standard | 10/20/2026 | 10/20/2026 | <https://www.youtube.com/watch?v=pZ2fgEFK3Vs> <br> <https://www.youtube.com/watch?v=5oQY8Rogz9Y> <br> <https://www.youtube.com/watch?v=NW1xrMkNMjU> <br> <https://www.youtube.com/watch?v=GMihNQojhZc> <br> <https://www.youtube.com/watch?v=clj2E0rNBEs> <br> <https://000018.awsfcaj.com/2-enable-sec-hub/> |
| 4 | - **Practice (Lab27):** tagged EC2 resources from the console and the AWS CLI, then grouped them in a Resource Group <br>- **Practice (Lab28):** <br>&emsp; + Wrote an IAM policy that allows EC2 actions only on correctly tagged resources in the allowed Region <br>&emsp; + Switched to the restricted role and confirmed what it can and cannot do | 10/21/2026 | 10/21/2026 | <https://000027.awsfcaj.com/2-using-tags/2.1-using-tags-console/2.1.1-create-ec2-with-tag/> <br> <https://000027.awsfcaj.com/2-using-tags/2.2-using-tags-cli/> <br> <https://000027.awsfcaj.com/3-resource-group/> <br> <https://000028.awsfcaj.com/3-createiampolicy/> <br> <https://000028.awsfcaj.com/5-checkpolicy/5.2-checkiampolicy/5.2.3-ec2createtagsexisting/> |
| 5 | - **Practice (Lab22):** <br>&emsp; + Prepared a VPC, a security group, and a tagged EC2 instance <br>&emsp; + Set up a Slack incoming webhook for notifications <br>&emsp; + Created an IAM role and two Lambda functions that stop and start instances by tag <br>&emsp; + Checked the instance state and the Slack messages, then cleaned up | 10/22/2026 | 10/22/2026 | <https://000022.awsfcaj.com/2-prerequiste/2.4-incomingwebhooksslack/> <br> <https://000022.awsfcaj.com/4-createroleforlambda/> <br> <https://000022.awsfcaj.com/5-createlambdafunction/5.1-createlambdafunction-stop/> <br> <https://000022.awsfcaj.com/5-createlambdafunction/5.2-createlambdafunction-start/> <br> <https://000022.awsfcaj.com/6-testingresults/> |
| 6 | - **Practice (Lab30):** capped what an IAM user can do with a permission boundary, even when the user's own policy grants more <br>- **Practice (Lab44):** <br>&emsp; + Created an admin role and allowed a user to switch into it <br>&emsp; + Added conditions so that the role can be assumed only from a given IP address and within a time window | 10/23/2026 | 10/23/2026 | <https://000030.awsfcaj.com/2-createpolicy/> <br> <https://000030.awsfcaj.com/4-checkuser/> <br> <https://000044.awsfcaj.com/4-configure-iam-role-with-condition/2-configure-switch-role/> <br> <https://000044.awsfcaj.com/4-configure-iam-role-with-condition/3-condition/3.1-ip/> <br> <https://000044.awsfcaj.com/4-configure-iam-role-with-condition/3-condition/3.2-timebase/> |

### Week 6 Achievements:

* Understood the following concepts:
  * Shared Responsibility Model: AWS secures the infrastructure that runs its services, while I am responsible for identities, data, network rules, and the guest operating system on EC2
  * IAM policy evaluation: an explicit deny always wins, an explicit allow is required, and everything else is implicitly denied
  * Condition keys such as aws:RequestedRegion, aws:ResourceTag, aws:SourceIp, and aws:CurrentTime narrow when a permission applies
  * A permission boundary sets the maximum permissions of a user or role; the effective permissions are the overlap with its own policies
  * Organizations manages many accounts, Identity Center provides single sign-on, Cognito handles application users, and Security Hub gathers findings against standards

* Wrote tag-based and Region-based IAM policies and tested them through switch role.

* Applied a permission boundary and IP- and time-based role conditions.

* Automated EC2 stop and start with Lambda and sent results to Slack.

* Learned the following security and cost lessons:
  * Least privilege works best in layers: identity policies, boundaries, and conditions
  * Consistent tags make access control, automation, and cost tracking much easier
