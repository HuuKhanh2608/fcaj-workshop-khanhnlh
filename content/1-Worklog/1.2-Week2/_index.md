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
| 2 | - Studied Amazon VPC in Module 02-01: <br>&emsp; + Planning CIDR ranges so that subnets never overlap <br>&emsp; + How each subnet lives in exactly one Availability Zone <br>&emsp; + How route tables decide where traffic goes next | 21/09/26 | 21/09/26 | [Module 02-01 – Amazon VPC](https://www.youtube.com/watch?v=O9Ac_vGHquM) <br> [Lab03 – 1.1 Subnets](https://000003.awsfcaj.com/1-introduce/1.1-subnets/) <br> [Lab03 – 1.2 Route Table](https://000003.awsfcaj.com/1-introduce/1.2-routetable/) |
| 3 | - Studied VPC security and multi-VPC features in Module 02-02 <br>- Studied hybrid connectivity and load balancing in Module 02-03: <br>&emsp; + Site-to-Site VPN and Direct Connect for linking on-premises networks <br>&emsp; + Application, Network, and Gateway Load Balancers and when to use each | 22/09/26 | 22/09/26 | [Module 02-02 – VPC security and multi-VPC features](https://www.youtube.com/watch?v=BPuD1l2hEQ4) <br> [Module 02-03 – VPN, Direct Connect, and Load Balancer](https://www.youtube.com/watch?v=CXU8D3kyxIc) |
| 4 | - Read through the Lab03 theory before building anything: <br>&emsp; + Why public subnets use an Internet Gateway while private subnets go out through a NAT Gateway <br>&emsp; + Stateful Security Groups versus stateless Network ACLs with numbered rules <br>&emsp; + Using the VPC Resource Map to see how resources connect | 23/09/26 | 23/09/26 | [Lab03 – 1.3 Internet Gateway](https://000003.awsfcaj.com/1-introduce/1.3-internetgateway/) <br> [Lab03 – 1.4 NAT Gateway](https://000003.awsfcaj.com/1-introduce/1.4-natgateway/) <br> [Lab03 – 2.1 Security Group](https://000003.awsfcaj.com/2-firewallinvpc/2.1-securitygroup/) <br> [Lab03 – 2.2 Network ACLs](https://000003.awsfcaj.com/2-firewallinvpc/2.2-networkacls/) <br> [Lab03 – 2.3 VPC Resource Map](https://000003.awsfcaj.com/2-firewallinvpc/2.3-vpc-resource-map/) |
| 5 | - **Practice (Lab03):** <br>&emsp; + Built a VPC with a public and a private subnet <br>&emsp; + Attached an Internet Gateway and routed the public subnet through it <br>&emsp; + Wrote security group rules that open only the ports each tier needs <br>&emsp; + Turned on VPC Flow Logs to record accepted and rejected traffic | 24/09/26 | 24/09/26 | [Lab03 – 3.1 Create VPC](https://000003.awsfcaj.com/3-prerequisite/3.1-createvpc/) <br> [Lab03 – 3.2 Create Subnet](https://000003.awsfcaj.com/3-prerequisite/3.2-createsubnet/) <br> [Lab03 – 3.4 Create Route Table](https://000003.awsfcaj.com/3-prerequisite/3.4-createroutetable/) <br> [Lab03 – 3.5 Create Security Group](https://000003.awsfcaj.com/3-prerequisite/3.5-createsecuritygroup/) <br> [Lab03 – 3.6 Enable VPC Flow Logs](https://000003.awsfcaj.com/3-prerequisite/3.6-enablevpcflowlogs/) |
| 6 | - **Practice (Lab03):** <br>&emsp; + Launched an instance in each subnet and checked which connections succeed <br>&emsp; + Added a NAT Gateway so that the private instance can download updates <br>&emsp; + Diagnosed connectivity with Reachability Analyzer <br>&emsp; + Reached the private instance through an EC2 Instance Connect Endpoint without giving it a public IP | 25/09/26 | 25/09/26 | [Lab03 – 4.1 Create EC2 Server](https://000003.awsfcaj.com/4-createec2server/4.1-createec2/) <br> [Lab03 – 4.2 Test Connection](https://000003.awsfcaj.com/4-createec2server/4.2-connectec2/) <br> [Lab03 – 4.3 Create NAT Gateway](https://000003.awsfcaj.com/4-createec2server/4.3-natgateway/) <br> [Lab03 – 4.4 Reachability Analyzer](https://000003.awsfcaj.com/4-createec2server/4.4-createreachabilityanalyzer/) <br> [Lab03 – 4.5 EC2 Instance Connect Endpoint](https://000003.awsfcaj.com/4-createec2server/4.5-eicendpoint/) |
| 7 | - Attended Buildrathon Kickoff: Code the Future with CMC Global at Bitexco Financial Tower <br>- Listened to the talk on the thinking behind building an AI bot | 26/09/26 | 26/09/26 | [Event 1 report](../../4-EventParticipated/4.1-Event1/) |

### Week 2 Achievements:

* **Knowledge:**
  * VPC and CIDR: a subnet belongs to a single Availability Zone, and AWS reserves five IP addresses in every subnet
  * Route tables: every table has a local route for traffic inside the VPC; 0.0.0.0/0 points to the Internet Gateway for public subnets and to the NAT Gateway for private subnets
  * Security Groups are stateful and attach to instances; Network ACLs are stateless, attach to subnets, and evaluate numbered rules in order
  * Site-to-Site VPN runs over the internet, while Direct Connect is a dedicated private link
* **Hands-on skills:**
  * Built a two-tier VPC with public and private subnets, route tables, and security groups
  * Recorded traffic with VPC Flow Logs and diagnosed paths with Reachability Analyzer
  * Reached a private instance through an EC2 Instance Connect Endpoint
* **Security and cost lessons:**
  * Private instances do not need public IPs, and security groups should open only the required ports
  * A NAT Gateway is billed by the hour and by the data it processes, so it should be deleted after the lab
* **Community:** wrote the report for the Buildrathon Kickoff
