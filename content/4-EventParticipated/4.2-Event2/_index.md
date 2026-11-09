---
title: "AWS Cloud & AI Day Hanoi - Watch Party"
date: 2026-09-29
weight: 2
chapter: false
pre: "<b>4.2. </b>"
---

### Event information

&emsp; **Event Name:** AWS Cloud & AI Day Hanoi - Watch Party

&emsp; **Date & Time:** 08:00 a.m. to 05:00 p.m., Tuesday, September 29, 2026 (UTC+7), according to the published schedule

&emsp; **Location:** AWS Vietnam office, Bitexco Financial Tower, 2 Hai Trieu Street, Ho Chi Minh City. Badge collection on the 26th floor, as stated in the invitation.

&emsp; **Attendance Format:** Watch party in Ho Chi Minh City, following sessions broadcast from the main event in Hanoi

&emsp; **Role:** Attendee

&emsp; **Event Page:** [AWS Cloud and AI Day Hanoi](https://aws.amazon.com/events/cloud-day-hanoi/)

On September 29, I attended the watch party at the AWS office in Ho Chi Minh City with my teammates. The main event took place in Hanoi, and we followed the keynote and technical sessions on screens at the office. The topics I wanted to keep from the day concerned using AI in software development, from preparing work for an agent to checking its results and securing an application.

### Event objectives

- Introduce Cloud and AI use cases through presentations from AWS and businesses.
- Share approaches to using agentic AI in software development, testing, and operations.
- Allow the community in Ho Chi Minh City to follow the keynote and selected Builders x AI sessions from Hanoi together.

My aim was to find approaches I could try on a small scale while studying and preparing my personal workshop.

### Speakers

The table records selected speakers from the keynote and security session broadcast from Hanoi. These are presentations I used as references for this report.

| Order | Speaker | Position | Presentation topics |
| --- | --- | --- | --- |
| 1 | Eric Yeo | Country General Manager, Malaysia, Vietnam & Indochina, AWS | Cloud and AI adoption in Vietnam, with examples from businesses. |
| 2 | Werner Vogels | CTO, Amazon | Engineering decisions behind cloud services, including databases, compute infrastructure, and time synchronization. |
| 3 | Jens Lottner | CEO, Techcombank | Bringing AI into banking operations and preparing employees to work with it. |
| 4 | Mai Le | Director of Product Management, Katalon | Software validation during development with AI and human responsibility for the results. |
| 5 | Trung Nguyen | Technical Account Manager, AWS Vietnam | Joint presentation of AWS Security Agent: Proactive AppSec from Design to Deployment. |
| 6 | Tan Huynh | Technical Account Manager, AWS Vietnam | Joint presentation of AWS Security Agent and the security testing workflow. |

Names and positions were checked against the event page, keynote recording, and speaker introduction slide in my event photos.

### Key highlights

#### Keynote: cloud infrastructure and software validation

The keynote placed AI adoption stories alongside the engineering work behind a system. Werner Vogels discussed databases, Nitro, Lambda, and time synchronization. These are topics I want to revisit to understand why a service is designed a certain way and when to use it.

Mai Le's presentation connected with my own programming studies: as AI produces changes faster, the person doing the work still needs to check whether those changes meet the requirements. For my exercises, I want to keep test results and records of errors so I can explain what I have achieved with evidence.

#### AI-DLC and how TCBS organizes work for agents

I kept photos of the comparison between traditional SDLC and AI-DLC, along with the workspace diagram from TCBS. In the diagram, an orchestrator prepares and monitors workspaces for individual agents and tasks. Each workspace includes a task package, source code, MCP tools, verification steps, and a checkpoint.

What I want to learn from this example is how to prepare a task before assigning it to AI. If the requirement and completion criteria are unclear, it is also difficult for me to judge the result. I can start by defining the inputs, outputs, and checks for each small feature in my workshop.

#### AWS Security Agent and security testing during development

Session DVT305, presented by Trung Nguyen and Tan Huynh, covered application security from design through deployment. One slide outlined a workflow involving login, scanning, execution of testing tasks, further exploration based on findings, and resource cleanup.

This made me pay closer attention to the scope of a test: which system is being tested, what permissions are needed, and which resources must be removed afterward. These are also details I need to explain clearly in an AWS workshop. The session gave me subjects to explore, while applying them will require reading the documentation and practicing each step.

#### Agent Toolkit for AWS and MCP

The Agent Toolkit for AWS slides introduced ways to give coding agents tools, knowledge, and controls. The getting started sequence covered installing a plugin, checking the connection to the AWS MCP Server, and trying a specific request. I also photographed the slide containing QR codes for the source repository and further reading.

I am interested in where an agent gets its information and which actions it can perform. When I try these tools after the event, I want to begin with a small task, read the changes it produces, and check the outcome before expanding the scope.

### Key takeaways

#### Prepare the requirement before using AI

- Divide work into tasks with clear outputs.
- Provide source code, documentation, and constraints relevant to the task.
- Decide how to check the result before starting.

#### Take responsibility for the result

- Read and understand changes proposed by AI before including them in my work.
- Test successful behavior and error cases.
- Keep practice results so I can explain my decisions.

#### Include security in the practice plan

- Review permissions and resource scope before running a tool.
- Include verification and cleanup steps in the workshop instructions.
- Learn the limits of tools, especially those able to act on an AWS environment.

### Applying to work

I plan to begin with my personal workshop. For each feature, I will write a short requirement, identify the expected outcome, and define a check before asking AI for help. I will then review the changes, run the exercise, and record the results in my worklog.

For MCP and Agent Toolkit for AWS, I want to try a task in a practice environment with a defined scope. I will record the setup, any problems encountered, and the checks I complete after trying it.

### Event experience

#### Following the program with my team in Ho Chi Minh City

The watch party let me follow the program with my teammates at the AWS office in Ho Chi Minh City. Our photo collection includes a group picture with attendance badges and photos of technical sessions on screen. Looking back through them helps me connect each point in this report to a specific presentation.

#### What I want to explore next

The TCBS workspace diagram is an example I want to revisit when dividing up project work. The testing and security sessions also reminded me to make time for checks after writing code. My next step is to choose a small part to try, record the results, and then decide whether it belongs in my workshop.

#### Some event photos

These images come from my team's and my own attendance photo collection in Ho Chi Minh City. The slides belong to their presenters and organizations and were photographed from screens showing the program from Hanoi.

![My teammates and me holding attendance badges at the watch party in Ho Chi Minh City](/images/4-EventParticipated/4.2-Cloud-AI-Day/team-watch-party.jpg)

*Figure 1. Our group photo at the AWS office in Ho Chi Minh City during the watch party.*

![Slide comparing traditional SDLC and AI-DLC on the watch party screen](/images/4-EventParticipated/4.2-Cloud-AI-Day/sdlc-to-ai-dlc.jpg)

*Figure 2. A comparison of software development phases when AI is introduced into the workflow. Slide source: AWS.*

![Workspace diagram for coding agents in the TCBS presentation](/images/4-EventParticipated/4.2-Cloud-AI-Day/tcbs-agent-workspaces.jpg)

*Figure 3. TCBS explaining workspace preparation and task coordination for agents. Slide source: Techcom Securities.*

![AWS Security Agent session introduction naming Trung Nguyen and Tan Huynh](/images/4-EventParticipated/4.2-Cloud-AI-Day/aws-security-agent.jpg)

*Figure 4. Session DVT305 and its two speakers displayed on screen. Slide source: AWS.*

![Five phases of the workflow presented in the AWS Security Agent session](/images/4-EventParticipated/4.2-Cloud-AI-Day/security-testing-pipeline.jpg)

*Figure 5. The security testing workflow from login through resource cleanup. Slide source: AWS.*

![AWS Agent Toolkit slide with QR codes linking to source code and resources](/images/4-EventParticipated/4.2-Cloud-AI-Day/aws-agent-toolkit.jpg)

*Figure 6. Resources for learning more about AWS Agent Toolkit. Slide source: AWS.*

### References

The sources below provide context for the main event in Hanoi and the watch party in Ho Chi Minh City, where I attended. They support the report alongside my own photos.

#### Official event resources

1. **AWS:** [AWS Cloud and AI Day Hanoi](https://aws.amazon.com/events/cloud-day-hanoi/). Official event overview, main venue, topics, and featured speakers.
2. **AWS:** [Event agenda](https://aws.amazon.com/events/cloud-day-hanoi/agenda/). Reference for session titles, tracks, and the published schedule. The agenda alone does not establish which sessions I attended.
3. **AWS Events:** [AWS Cloud & AI Day Hanoi 2026 | Keynote](https://www.youtube.com/watch?v=6lQLOOQdW9Y). Recording of the keynote broadcast from Hanoi, provided for revisiting the presentations and customer stories.

#### Event coverage and articles

4. **About Amazon, September 29, 2026:** [Vietnam is transforming its AI ambitions into business impact](https://www.aboutamazon.sg/news/aws/vietnam-is-transforming-its-ai-ambitions-into-business-impact). Amazon's article about the AI adoption study released at the event, with a TCBS example that complements the software development topics shown in my photos.
5. **Vietnam Ministry of Science and Technology, September 29, 2026:** [Vietnam's AI infrastructure and the challenge of creating practical value](https://mst.gov.vn/ai-viet-nam-tu-mo-rong-ha-tang-den-bai-toan-bien-cong-nghe-thanh-gia-tri-19726093007364899.htm) (Vietnamese). Coverage of Deputy Minister Hoàng Minh's remarks at the Hanoi event and the foundations needed for wider AI adoption.
6. **Vietnam Journal of Science and Technology, September 29, 2026:** [International technology cooperation and Vietnam's innovation ecosystem](https://vjst.vn/cac-tap-doan-cong-nghe-quoc-te-khong-chi-cung-cap-dich-vu-ma-cung-viet-nam-doi-moi-sang-tao-va-phat-trien-he-sinh-thai-103338.html) (Vietnamese). Reporting on the Hanoi event, with context on infrastructure, workforce development, and cooperation with technology companies.

#### Ho Chi Minh City watch party

7. **AWS Events:** [AWS Cloud & AI Day Hanoi - Watch Party registration](https://apj.awsevents.com/sites/aws-cloud-day-hanoi-watch-party-attendee). Registration link for the watch party in Ho Chi Minh City. The page currently returns a 404 error; the original link is retained for reference.
