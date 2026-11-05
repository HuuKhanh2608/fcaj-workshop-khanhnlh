---
title: "Điều kiện tiên quyết"
date: 2026-11-05
weight: 2
chapter: false
pre: "<b>5.2. </b>"
---

> **Bản nháp đang hoàn thiện.** Nội dung sẽ được cập nhật từ quá trình học tập, triển khai và minh chứng thực tế của Nguyễn Lê Hữu Khánh.

## Tài khoản, Region và quyền hạn

| Yêu cầu | Giá trị / cách chuẩn bị | Tình trạng |
| --- | --- | --- |
| Tài khoản AWS và phương thức xác thực | Chờ xác định môi trường thực hành | Chưa xác nhận |
| Region triển khai | Chờ chọn theo dịch vụ, dữ liệu và chi phí | Chưa xác nhận |
| IAM Role / Policy | Chờ xác định quyền tối thiểu cho từng bước | Chưa xác nhận |
| Ngân sách và cảnh báo | Chờ xác định hạn mức cảnh báo phù hợp | Chưa xác nhận |

## Công cụ và phiên bản

| Công cụ | Phiên bản đã kiểm thử | Cách kiểm tra / cấu hình |
| --- | --- | --- |
| AWS CLI, Git và công cụ triển khai được chọn | Chờ xác định | Chờ câu lệnh đã kiểm chứng |

SAM, CDK, Terraform hoặc Docker chỉ được thêm nếu kiến trúc thực tế sử dụng. Cần ghi rõ môi trường máy, biến cấu hình và quyền cần thiết; thông tin bí mật sẽ được cung cấp qua cơ chế phù hợp, không hard-code trong mã nguồn.

## Kiểm tra trước khi bắt đầu

Chờ hướng dẫn xác nhận tài khoản, Region, danh tính, quyền và công cụ trước khi tạo tài nguyên.
