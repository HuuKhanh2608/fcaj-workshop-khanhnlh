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
| 2 | - **Practice (Lab03 – Site-to-Site VPN):** <br>&emsp; + Created a separate VPC with an EC2 instance acting as the on-premises side <br>&emsp; + Set up a Virtual Private Gateway, a Customer Gateway, and the VPN connection <br>&emsp; + Applied the tunnel settings on the customer gateway and checked the tunnel status <br>&emsp; + Tore down the VPN resources after testing | 28/09/26 | 28/09/26 | [Lab03 – 5.1.1 Create VPC for VPN](https://000003.awsfcaj.com/5-vpnsitetosite/5.1-createvpnenv/5.1.1-createvpnvpc/) <br> [Lab03 – 5.2.1 Create Virtual Private Gateway](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.1-createvpgw/) <br> [Lab03 – 5.2.2 Create Customer Gateway](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.2-createcustomergw/) <br> [Lab03 – 5.2.3 Create VPN Connection](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.3-createvpnconnection/) <br> [Lab03 – 5.2.4 Customer Gateway Configuration](https://000003.awsfcaj.com/5-vpnsitetosite/5.2-vpnsitetosite/5.2.4-configurecustomergw/) |
| 3 | - Attended the AWS Cloud & AI Day Hanoi watch party at the AWS Vietnam office with my teammates <br>- Took notes on AI-DLC, how TCBS organizes workspaces for agents, AWS Security Agent, and Agent Toolkit for AWS | 29/09/26 | 29/09/26 | [Event 2 report](../../4-EventParticipated/4.2-Event2/) |
| 4 | - **Practice (Lab19 – VPC Peering):** <br>&emsp; + Deployed two VPCs and their instances from a CloudFormation template <br>&emsp; + Opened the Network ACLs for traffic between the two CIDR ranges <br>&emsp; + Requested and accepted a peering connection, then added routes on both sides <br>&emsp; + Enabled DNS resolution across the peering connection | 30/09/26 | 30/09/26 | [Lab19 – 2.1 Initialize CloudFormation Template](https://000019.awsfcaj.com/2-prerequiste/2.1-launchcloudformation/) <br> [Lab19 – 3. Update Network ACL](https://000019.awsfcaj.com/3-updatenetworkacl/) <br> [Lab19 – 4. Create Peering Connection](https://000019.awsfcaj.com/4-vpcpeering/) <br> [Lab19 – 5. Route Tables](https://000019.awsfcaj.com/5-routetables/) <br> [Lab19 – 6. Cross-Peer DNS](https://000019.awsfcaj.com/6-crosspeerdns/) |
| 5 | - **Practice (Lab20 – Transit Gateway):** <br>&emsp; + Created a Transit Gateway and attached several VPCs to it <br>&emsp; + Configured Transit Gateway route tables to control which VPCs can talk to each other <br>&emsp; + Pointed each VPC route table at the Transit Gateway and tested connectivity <br>&emsp; + Removed the attachments and the gateway to stop the charges | 01/10/26 | 01/10/26 | [Lab20 – 3. Create Transit Gateway](https://000020.awsfcaj.com/3-transitgateway/) <br> [Lab20 – 5. Create Transit Gateway Route Tables](https://000020.awsfcaj.com/5-routetable/) <br> [Lab20 – 6. Add Transit Gateway Routes to VPC Route Tables](https://000020.awsfcaj.com/6-result/) <br> [Lab20 – 7. Clean Up Resources](https://000020.awsfcaj.com/7-cleanup/) |
| 6 | - Attended the Fireside Chat with Dr. Werner Vogels at the AWS office (morning) <br>- Compared VPC Peering and Transit Gateway in my notes in terms of cost, scale, and routing control <br>- Reviewed the multi-VPC part of Module 02 | 02/10/26 | 02/10/26 | [Event 3 report](../../4-EventParticipated/4.3-Event3/) <br> [Module 02-02 – VPC security and multi-VPC features](https://www.youtube.com/watch?v=BPuD1l2hEQ4) |

### Week 3 Achievements:

* **Knowledge:**
  * Site-to-Site VPN: the Virtual Private Gateway is the AWS side, the Customer Gateway represents the on-premises device, and each connection has two IPsec tunnels for redundancy
  * VPC Peering: a one-to-one link that is not transitive and requires non-overlapping CIDR ranges
  * Transit Gateway: a regional hub where VPCs and VPNs attach, with route tables that decide which attachments can reach each other
* **Hands-on skills:**
  * Connected a simulated data center to AWS over Site-to-Site VPN
  * Linked two VPCs with peering, including routes on both sides and cross-peer DNS
  * Connected several VPCs through a Transit Gateway and controlled routing with its route tables
* **Security and cost lessons:**
  * CIDR ranges must be planned early, because overlapping ranges cannot be peered
  * VPN connections and Transit Gateway attachments are billed by the hour, so they should be removed right after testing
* **Community:** wrote the reports for AWS Cloud & AI Day and the Fireside Chat, focusing on ideas I can apply to my workshop
