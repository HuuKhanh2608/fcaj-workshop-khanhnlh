---
title: "Event 5"
date: 2026-11-14
weight: 5
chapter: false
pre: "<b>4.5. </b>"
---

# Bài thu hoạch “AWSxFPTU Cloud Mastery 1”

### Thông tin sự kiện

&emsp; **Tên sự kiện:** AWSxFPTU Cloud Mastery 1

&emsp; **Thời gian:** Thứ Bảy, ngày 14/11/2026

&emsp; **Địa điểm:** Văn phòng AWS Việt Nam, Bitexco Financial Tower, TP.HCM

&emsp; **Hình thức:** Tham dự trực tiếp

&emsp; **Vai trò:** Người tham dự

AWSxFPTU Cloud Mastery 1 là buổi workshop dành cho sinh viên Đại học FPT, xoay quanh câu hỏi: làm thế nào để đưa một ứng dụng AI từ bản prototype lên môi trường production của doanh nghiệp một cách an toàn, ổn định và mở rộng được. Nội dung đi từ các nguyên tắc chung đến Amazon Bedrock AgentCore và kết thúc bằng phần demo kiến trúc thực tế. Sự kiện diễn ra vào cuối tuần 9, ngay sau khi tôi bắt đầu thu hẹp đề tài và phác thảo kiến trúc workshop cá nhân, nên đây là dịp tốt để đối chiếu hướng đi của mình.

### Mục tiêu tham dự

- Hiểu khoảng cách giữa một bản prototype AI và một hệ thống AI chạy ổn định trong doanh nghiệp.
- Tìm hiểu Amazon Bedrock AgentCore và các thành phần hỗ trợ đưa AI agent lên production.
- Xem cách bảo mật, giám sát và kiểm soát chi phí được đưa vào một kiến trúc thực tế.
- Rút ra những điểm cần lưu ý cho kiến trúc workshop cá nhân.

### Chương trình và diễn giả

| Phần | Nội dung | Diễn giả |
| --- | --- | --- |
| 1 | From Prototype to Production: Secure, Reliable, Scalable Enterprise AI on the Cloud | Khang Duong, thành viên FCAJ |
| 2 | AI in Enterprise: Enterprise Challenges and Amazon Bedrock AgentCore | Nguyen Lam Anh, AI Engineer, FCAJ |
| 3 | Các thành phần của Amazon Bedrock AgentCore: Identity, Gateway, Memory và Observability | Chờ cập nhật |
| 4 | Demo: điều phối agent với Strands Agents, quan sát bằng Langfuse và kiến trúc triển khai trên AWS | Chờ cập nhật |

Sự kiện không có trang giới thiệu công khai. Tên phiên và diễn giả lấy từ slide được chiếu tại sự kiện.

### Nội dung nổi bật

#### 1. From Prototype to Production

Phần mở đầu của diễn giả Khang Duong đi qua bốn mục: khoảng cách giữa prototype và production (The Gap), bốn trụ cột của một hệ thống AI doanh nghiệp (The Four Pillars), cách AWS đáp ứng (The AWS Answer) và hướng phát triển tiếp theo (The Road Ahead).

Cả phần được kể qua câu chuyện một nhà hàng: prototype giống căn bếp ở nhà, AI doanh nghiệp giống một chuỗi nhà hàng, còn cloud là bếp trung tâm phục vụ cả chuỗi. Trong doanh nghiệp, dữ liệu là nguyên liệu, mô hình AI là đầu bếp, tính năng là món ăn và người dùng là thực khách. AI thường không đứng riêng mà là một tính năng nằm trong sản phẩm, ví dụ gợi ý sản phẩm, chatbot hỗ trợ khách hàng hay phát hiện gian lận.

Hai trụ cột tôi ghi lại rõ nhất:

- **Bảo mật:** AWS KMS giữ bí mật “công thức” và thông tin khách hàng; IAM kiểm soát ai được vào kho, ai được nấu; Guardrails chặn các rủi ro riêng của AI, như khi người dùng cố tình lừa “đầu bếp” làm sai.
- **Khả năng mở rộng linh hoạt:** Lambda tự nhân bản khi tải tăng, Auto Scaling thêm hoặc bớt máy, Load Balancer chia đều tải.

![Slide mở đầu From Prototype to Production: Secure, Reliable, Scalable Enterprise AI on the Cloud của Khang Duong](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-title.jpg)

*Hình 1. Slide mở đầu phần chia sẻ của diễn giả Khang Duong, thành viên FCAJ.*

![Diễn giả Khang Duong giới thiệu agenda gồm The Gap, The Four Pillars, The AWS Answer và The Road Ahead](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-agenda.jpg)

*Hình 2. Agenda phần From Prototype to Production của diễn giả Khang Duong.*

![Slide One Restaurant so sánh prototype với bếp nhà, enterprise AI với chuỗi nhà hàng và cloud với bếp trung tâm](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-one-restaurant.jpg)

*Hình 3. Câu chuyện nhà hàng được dùng xuyên suốt phần chia sẻ.*

![Slide AI in the Enterprise với chuỗi Data, AI Model, Feature, Users và các ví dụ Recommendations, Support Chatbot, Fraud Detection](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-ai-in-enterprise.jpg)

*Hình 4. AI là một tính năng nằm trong sản phẩm của doanh nghiệp.*

![Slide Why Security với KMS cho data privacy, IAM cho access control và Guardrails cho rủi ro riêng của AI](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-why-security.jpg)

*Hình 5. Trụ cột bảo mật: KMS, IAM và Guardrails.*

![Slide Elastic Scalability với Lambda, Auto Scaling và Load Balancer](/images/4-EventParticipated/4.5-Cloud-Mastery/part1-elastic-scalability.jpg)

*Hình 6. Trụ cột mở rộng linh hoạt: Lambda, Auto Scaling và Load Balancer.*

#### 2. AI in Enterprise và Amazon Bedrock AgentCore

Phần thứ hai của diễn giả Nguyen Lam Anh nêu ba thách thức khi đưa AI agent vào doanh nghiệp:

- **Security & Scalability:** agent được phép chạm vào những gì và chịu được bao nhiêu tải?
- **Integration & Context:** agent có làm việc được với hệ thống thật và giữ được ngữ cảnh không?
- **Observability & Evaluation:** có biết agent đang làm gì và làm có đúng không?

Diễn giả đặt AgentCore vào bức tranh chung: mô hình hiểu và phản hồi, ứng dụng agent điều phối mô hình với các công cụ (ví dụ hệ thống đặt hàng), còn Amazon Bedrock AgentCore cung cấp sẵn các năng lực được quản lý cho agent.

Ví dụ tôi thấy thực tế nhất là một thiết kế hybrid kết nối với các dịch vụ của Mobileye: hệ thống ticket nằm on-premises và AWS không truy cập vào được. Một orchestrator chạy tại chỗ sẽ kéo ticket về rồi gửi câu trả lời lên. Support agent chạy trên AgentCore Runtime, lấy thông tin xác thực từ Secrets Manager để không lộ credential, và gọi các dịch vụ nội bộ qua MCP để lấy trạng thái, log và lỗi theo thời gian thực. AgentCore Observability ghi lại toàn bộ đường đi từ request, các lần gọi tool qua MCP đến câu trả lời. Nhờ vậy không cần mở đường vào mạng on-premises mà agent vẫn có dữ liệu mới nhất khi suy luận.

Phần này kết thúc bằng ý: agent không ném lỗi như phần mềm thông thường, nên cần quan sát và chấm điểm từng lượt chạy. Mỗi bước (input, output, độ trễ, token) đều được trace; kết quả được đánh giá bằng kiểm tra bằng code, LLM-as-a-judge và red teaming.

![Slide mở đầu AI in Enterprise: Enterprise Challenges and Amazon Bedrock AgentCore, Part 2 của Nguyen Lam Anh](/images/4-EventParticipated/4.5-Cloud-Mastery/part2-intro.jpg)

*Hình 7. Phần 2 của diễn giả Nguyen Lam Anh, AI Engineer tại FCAJ.*

![Slide 3 challenges gồm Security and Scalability, Integration and Context, Observability and Evaluation](/images/4-EventParticipated/4.5-Cloud-Mastery/part2-three-challenges.jpg)

*Hình 8. Ba thách thức khi đưa AI agent vào doanh nghiệp.*

![Slide Where AgentCore fits với ba lớp Model, Agent application và Amazon Bedrock AgentCore](/images/4-EventParticipated/4.5-Cloud-Mastery/part2-where-agentcore-fits.jpg)

*Hình 9. Vị trí của AgentCore so với mô hình và ứng dụng agent.*

![Slide Hybrid design: on-prem tickets meet a cloud agent với on-premises, AgentCore và các dịch vụ của Mobileye](/images/4-EventParticipated/4.5-Cloud-Mastery/part2-hybrid-design.jpg)

*Hình 10. Thiết kế hybrid: ticket on-premises kết nối với agent trên cloud.*

#### 3. Các thành phần của AgentCore

Phần thứ ba đi sâu vào từng thành phần:

- **Identity:** AgentCore tách xác thực chiều vào và chiều ra như “hai cánh cửa, hai ổ khóa”. Chiều vào trả lời câu hỏi người dùng là ai và có được gọi agent không; chiều ra trả lời agent có đúng là agent đó không và có được truy cập tài nguyên thay mặt người dùng không. Khi chạy, agent giữ một workload access token gắn với cả agent lẫn người dùng.
- **Gateway:** là điểm kết nối chung giữa nhiều agent (hỗ trợ khách hàng, mua sắm, định giá) với API, công cụ và tài nguyên, hỗ trợ MCP, tạo và tìm kiếm tool, phân quyền chi tiết, kết nối riêng tư và lọc tool. Luồng phân quyền gồm token OAuth chiều vào (ví dụ xác thực qua Amazon Cognito), sau đó Gateway đổi workload access token lấy token OAuth chiều ra để gọi API. AgentCore Identity đóng vai trò kho lưu token an toàn.
- **Memory:** trong các thành phần của context window (system prompt, tài liệu RAG, tool, hướng dẫn, lịch sử hội thoại), memory là phần hay bị bỏ qua, nhưng thiếu nó thì agent không học được và không cá nhân hóa được. AgentCore Memory gồm bộ nhớ ngắn hạn lưu nguyên các tương tác và bộ nhớ dài hạn lưu các thông tin rút ra vào vector store; dịch vụ là serverless, tích hợp CloudWatch, cho phép đặt thời gian lưu sự kiện ngắn hạn tối đa 365 ngày, chia namespace và mã hóa dữ liệu khi lưu trữ lẫn khi truyền. Agent ghi tin nhắn và trạng thái vào bộ nhớ ngắn hạn theo kiểu đồng bộ; một module trích xuất tự động chạy bất đồng bộ để chuyển thông tin sang bộ nhớ dài hạn theo các chiến lược như semantic, sở thích người dùng, tóm tắt, episodic hoặc chiến lược tùy chỉnh.
- **Observability:** “không sửa được thứ mình không nhìn thấy”. Observability phục vụ tuân thủ, truy vết, phân tích chi phí, tìm nguyên nhân lỗi trong các luồng không xác định trước, theo dõi độ trễ và đánh giá liên tục. AgentCore thu telemetry theo chuẩn OpenTelemetry từ agent và từ các dịch vụ như Memory, Identity, Gateway, rồi hiển thị trên dashboard hoặc gửi sang công cụ observability bên thứ ba.

![Slide AgentCore separates Inbound from Outbound với Inbound Auth và Outbound Auth](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-inbound-outbound-auth.jpg)

*Hình 11. AgentCore Identity tách xác thực chiều vào và chiều ra.*

![Slide Amazon Bedrock AgentCore Gateway kết nối nhiều agent với API, tool và tài nguyên](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-gateway-overview.jpg)

*Hình 12. AgentCore Gateway là điểm kết nối chung giữa agent và công cụ.*

![Slide Authorization in Bedrock AgentCore Gateway mô tả luồng token OAuth chiều vào và chiều ra](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-gateway-authorization.jpg)

*Hình 13. Luồng phân quyền trong AgentCore Gateway.*

![Slide Building context for Agents liệt kê các thành phần của context window, nhấn mạnh Memory](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-building-context.jpg)

*Hình 14. Memory là thành phần hay bị bỏ qua khi xây dựng ngữ cảnh cho agent.*

![Slide AgentCore Memory với short-term memory, long-term memory và các tính năng đi kèm](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-agentcore-memory.jpg)

*Hình 15. Bộ nhớ ngắn hạn và dài hạn của AgentCore Memory.*

![Slide kiến trúc AgentCore Memory với events, short-term memory, long-term memory và module trích xuất tự động](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-memory-architecture.jpg)

*Hình 16. Luồng ghi và truy xuất giữa agent với bộ nhớ ngắn hạn, dài hạn.*

![Slide You cannot fix what you cannot see liệt kê các lý do cần observability cho agent](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-observability-why.jpg)

*Hình 17. Những lý do cần observability cho AI agent.*

![Slide AgentCore Observability mô tả telemetry từ Runtime, Memory, Identity, Gateway đến dashboard](/images/4-EventParticipated/4.5-Cloud-Mastery/part3-agentcore-observability.jpg)

*Hình 18. AgentCore Observability thu telemetry từ agent và các dịch vụ AgentCore.*

#### 4. Demo: từ agent đến kiến trúc triển khai

Phần cuối là demo một hệ thống agent hoàn chỉnh. Strands Agents được dùng để điều phối có kiểm soát: request đi qua FastAPI, một router chuyển đến agent phù hợp (ví dụ agent hỏi đáp, agent tạo ticket, agent nghiên cứu), và các thao tác quan trọng đi qua bước phê duyệt trước khi trả kết quả. Langfuse được dùng để trace luồng làm việc và các lần gọi tool, điều tra độ trễ và lỗi, theo dõi lượng sử dụng mô hình.

Kiến trúc triển khai trên AWS gồm: image lưu trên Amazon ECR, agent chạy trên Amazon ECS với Fargate trong private subnet ở hai Availability Zone, Application Load Balancer nhận request, NAT gateway cho kết nối ra ngoài, Amazon Bedrock cho mô hình, Amazon DynamoDB lưu dữ liệu và Amazon CloudWatch để giám sát. Phần bảo mật dùng IAM và Secrets Manager; phần tối ưu chi phí dùng Cost Explorer và AWS Budgets.

Kiến trúc này dùng lại nhiều thành phần tôi đã thực hành: VPC hai tầng public/private với NAT gateway (Lab03), IAM và KMS (Module 05), DynamoDB (Lab60, Lab39) và AWS Budgets (Lab07). Điều khác biệt là tất cả được ghép lại quanh một bài toán AI cụ thể, có giám sát và kiểm soát chi phí ngay từ thiết kế.

![Slide Strands: Controlled Agent Orchestration với sơ đồ router chuyển request đến các agent](/images/4-EventParticipated/4.5-Cloud-Mastery/part4-strands-orchestration.jpg)

*Hình 19. Điều phối agent có kiểm soát với Strands Agents.*

![Slide Langfuse – Agent Observability với ba mục trace workflow, điều tra độ trễ và theo dõi lượng sử dụng mô hình](/images/4-EventParticipated/4.5-Cloud-Mastery/part4-langfuse.jpg)

*Hình 20. Dùng Langfuse để quan sát agent trong phần demo.*

![Sơ đồ AWS Architecture với ECR, ALB, ECS Fargate trên hai Availability Zone, Bedrock, DynamoDB, CloudWatch, IAM, Secrets Manager và Budgets](/images/4-EventParticipated/4.5-Cloud-Mastery/part4-aws-architecture.jpg)

*Hình 21. Kiến trúc triển khai hệ thống agent trên AWS trong phần demo.*

### Bài học rút ra

- **Prototype chạy được chưa phải là sản phẩm:** Một hệ thống AI cho doanh nghiệp cần bảo mật, mở rộng, tích hợp và giám sát ngay từ đầu, không phải làm thêm ở cuối.
- **Bảo mật cho AI rộng hơn IAM:** Ngoài mã hóa và phân quyền, cần tính đến rủi ro riêng như prompt injection, và tách rõ quyền của người dùng với quyền của agent.
- **Không giấu credential trong code:** Dùng Secrets Manager hoặc token vault để agent lấy thông tin xác thực khi cần.
- **Agent cần được quan sát và chấm điểm:** Agent có thể trả lời sai mà không báo lỗi, nên phải trace từng bước và đánh giá kết quả thường xuyên.
- **Memory là một phần của thiết kế:** Phân biệt rõ dữ liệu cần nhớ trong phiên và dữ liệu cần giữ lâu dài, kèm thời gian lưu và mã hóa.

### Áp dụng vào công việc

Với workshop cá nhân, tôi sẽ dùng bốn câu hỏi của buổi chia sẻ để rà soát kiến trúc: dữ liệu được bảo vệ thế nào, hệ thống mở rộng ra sao khi tải tăng, các thành phần tích hợp với nhau thế nào và làm sao biết hệ thống đang chạy đúng. Thông tin bí mật sẽ được quản lý bằng Secrets Manager thay vì ghi trong code hoặc biến môi trường.

Phần kiểm thử và giám sát của workshop sẽ không chỉ dừng ở log và metric CloudWatch, mà có cả các trường hợp kiểm tra kết quả đầu ra. Nếu workshop có dùng AI, tôi sẽ ghi lại từng bước xử lý để có thể truy vết khi kết quả không như mong đợi.

### Trải nghiệm tham gia sự kiện

Buổi workshop có nhiều nội dung mới với tôi, nhất là các thành phần của AgentCore. Cách phần đầu dùng câu chuyện nhà hàng giúp tôi theo kịp những khái niệm khá trừu tượng, còn phần demo cho thấy các dịch vụ được ghép lại thành một kiến trúc chạy được. Nhiều phần chia sẻ do các thành viên cộng đồng FCAJ trình bày, nên tôi cũng thấy rõ hơn những gì mình có thể đạt được sau kỳ thực tập.

![Ảnh check-in của tôi tại khu vực khán giả trong phần demo Langfuse ở sự kiện AWSxFPTU Cloud Mastery 1](/images/4-EventParticipated/4.5-Cloud-Mastery/check-in.jpg)

*Hình 22. Ảnh check-in của tôi trong phần demo tại sự kiện ngày 14/11/2026. Các ảnh trong bài thuộc bộ ảnh tham dự cá nhân của tôi.*

### Tài liệu tham khảo

1. **AWS Documentation:** [Amazon Bedrock AgentCore – Overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html).
2. **AWS Documentation:** [AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html), [AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), [AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) và [AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).
3. **Strands Agents:** [Trang chủ dự án Strands Agents](https://strandsagents.com/).
4. **Langfuse:** [Trang chủ Langfuse](https://langfuse.com/).
