---
title: "Week 3 Worklog"
date: 2026-11-05
weight: 3
chapter: false
pre: "<b>1.3. </b>"
---

### Week 3 Objectives:

* Connect a simulated on-premises network to AWS.
* Compare two ways of linking VPCs: VPC Peering and Transit Gateway.
* Learn from the community at AWS Cloud & AI Day and the Fireside Chat with Dr. Werner Vogels.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice (Lab03 – Site-to-Site VPN):** <br>&emsp; + Created a separate VPC with an EC2 instance acting as the on-premises side <br>&emsp; + Set up a Virtual Private Gateway, a Customer Gateway, and the VPN connection <br>&emsp; + Applied the tunnel settings on the customer gateway and checked the tunnel status <br>&emsp; + Tore down the VPN resources after testing | 28/09/26 | 28/09/26 | <https://000003.awsfcaj.com/> |
| 3 | - Attended the AWS Cloud & AI Day Hanoi watch party at the AWS Vietnam office with my teammates <br>- Took notes on AI-DLC, how TCBS organizes workspaces for agents, AWS Security Agent, and Agent Toolkit for AWS | 29/09/26 | 29/09/26 | [Event 2](../../4-EventParticipated/4.2-Event2/) |
| 4 | - **Practice (Lab19 – VPC Peering):** <br>&emsp; + Deployed two VPCs and their instances from a CloudFormation template <br>&emsp; + Opened the Network ACLs for traffic between the two CIDR ranges <br>&emsp; + Requested and accepted a peering connection, then added routes on both sides <br>&emsp; + Enabled DNS resolution across the peering connection | 30/09/26 | 30/09/26 | <https://000019.awsfcaj.com/> |
| 5 | - **Practice (Lab20 – Transit Gateway):** <br>&emsp; + Created a Transit Gateway and attached several VPCs to it <br>&emsp; + Configured Transit Gateway route tables to control which VPCs can talk to each other <br>&emsp; + Pointed each VPC route table at the Transit Gateway and tested connectivity <br>&emsp; + Removed the attachments and the gateway to stop the charges | 01/10/26 | 01/10/26 | <https://000020.awsfcaj.com/> |
| 6 | - Attended the Fireside Chat with Dr. Werner Vogels at the AWS office (morning) <br>- Compared VPC Peering and Transit Gateway in my notes in terms of cost, scale, and routing control <br>- Reviewed the Module 02 material | 02/10/26 | 02/10/26 | [Event 3](../../4-EventParticipated/4.3-Event3/) <br> [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |

### Week 3 Achievements:

* I connected a simulated data center to AWS over an IPsec Site-to-Site VPN.
* I understand the trade-off between the two VPC connectivity options:
  * VPC Peering is simple and inexpensive for a few VPCs, but it does not route traffic transitively
  * Transit Gateway acts as a central hub and scales better as the number of VPCs grows
* I can plan route tables on both sides of a connection so that traffic flows in both directions.
* I wrote reports for AWS Cloud & AI Day and the Fireside Chat, focusing on ideas I can apply to my own workshop.
