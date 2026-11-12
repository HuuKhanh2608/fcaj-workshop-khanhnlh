---
title: "Week 2 Worklog"
date: 2026-11-05
weight: 2
chapter: false
pre: "<b>1.2. </b>"
---

### Week 2 Objectives:

* Understand how the building blocks of Amazon VPC fit together to form a private network.
* Build a two-tier network and control traffic at both the instance and the subnet level.
* Meet the community at the Buildrathon Kickoff.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Studied Amazon VPC in Module 02-01: <br>&emsp; + Planning CIDR ranges so that subnets never overlap <br>&emsp; + How route tables decide where traffic goes next <br>&emsp; + Why public subnets need an Internet Gateway while private subnets reach out through a NAT Gateway | 21/09/26 | 21/09/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 3 | - Studied VPC security and multi-VPC features in Module 02-02 <br>- Studied hybrid connectivity and load balancing in Module 02-03: <br>&emsp; + Site-to-Site VPN and Direct Connect for linking on-premises networks <br>&emsp; + Application, Network, and Gateway Load Balancers | 22/09/26 | 22/09/26 | [FCJ Bootcamp playlist](https://www.youtube.com/playlist?list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) |
| 4 | - Read through the Lab03 theory before building anything: <br>&emsp; + Traced the path of a packet through subnets, route tables, the Internet Gateway, and the NAT Gateway <br>&emsp; + Compared stateful Security Groups with stateless Network ACLs <br>&emsp; + Used the VPC Resource Map to see how resources connect | 23/09/26 | 23/09/26 | <https://000003.awsfcaj.com/> |
| 5 | - **Practice (Lab03):** <br>&emsp; + Built a VPC with one public and one private subnet <br>&emsp; + Attached an Internet Gateway and routed the public subnet through it <br>&emsp; + Wrote security group rules that open only the ports each tier needs <br>&emsp; + Turned on VPC Flow Logs to record accepted and rejected traffic | 24/09/26 | 24/09/26 | <https://000003.awsfcaj.com/> |
| 6 | - **Practice (Lab03):** <br>&emsp; + Launched an instance in each subnet and checked which connections succeed <br>&emsp; + Added a NAT Gateway so the private instance can download updates <br>&emsp; + Diagnosed connectivity with Reachability Analyzer <br>&emsp; + Reached the private instance through an EC2 Instance Connect Endpoint without giving it a public IP | 25/09/26 | 25/09/26 | <https://000003.awsfcaj.com/> |
| 7 | - Attended Buildrathon Kickoff: Code the Future with CMC Global at Bitexco Financial Tower <br>- Listened to the talk on the thinking behind building an AI bot | 26/09/26 | 26/09/26 | [Event 1](../../4-EventParticipated/4.1-Event1/) |

### Week 2 Achievements:

* I understand how a VPC is assembled:
  * Subnets divide the address space, and route tables decide the next hop
  * An Internet Gateway gives public subnets two-way internet access, while a NAT Gateway gives private subnets outbound-only access
* I can explain why Security Groups are stateful and Network ACLs are stateless, and when to rely on each layer.
* I deployed a working two-tier network and reached a private instance without exposing it to the internet.
* I made a habit of deleting the NAT Gateway after each lab because it is billed by the hour.
* I wrote my first event report, on the Buildrathon Kickoff.
