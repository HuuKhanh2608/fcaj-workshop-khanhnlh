---
title: "Kiểm thử và giám sát"
date: 2026-11-05
weight: 5
chapter: false
pre: "<b>5.5. </b>"
---

> **Bản nháp đang hoàn thiện.** Nội dung sẽ được cập nhật từ quá trình học tập, triển khai và minh chứng thực tế của Nguyễn Lê Hữu Khánh.

## Kế hoạch kiểm thử

| Kịch bản cần chuẩn bị | Đầu vào / thao tác | Kết quả mong đợi | Kết quả thực tế | Minh chứng |
| --- | --- | --- | --- | --- |
| Luồng chức năng chính | Chờ xác định | Chờ tiêu chí | Chưa chạy | Chưa có |
| Dữ liệu không hợp lệ | Chờ xác định | Chờ tiêu chí | Chưa chạy | Chưa có |
| Truy cập không được cấp quyền | Chờ xác định | Chờ tiêu chí | Chưa chạy | Chưa có |
| Lỗi phụ thuộc / retry / tải nếu phù hợp | Chờ xác định | Chờ tiêu chí | Chưa chạy | Chưa có |

Chờ câu lệnh cURL, request Postman hoặc thao tác giao diện phù hợp sản phẩm. Kết quả mong đợi sẽ được đối chiếu với dữ liệu đầu ra, mã phản hồi và log thực tế.

## Logs, Metrics và Alerts

| Thành phần | Log / metric | Ngưỡng alarm và hành động | Cách kích hoạt kiểm tra | Minh chứng |
| --- | --- | --- | --- | --- |
| Chưa xác định | Chưa xác định | Chưa xác định | Chưa xác định | Chưa có |

Chờ cấu hình CloudWatch hoặc công cụ phù hợp, thời gian lưu log, dashboard, alarm và kênh nhận cảnh báo. Cần lưu bằng chứng alarm thực sự đổi trạng thái hoặc gửi thông báo khi chạy kịch bản kiểm tra.

## Kết quả đo lường

Chưa có số đo. Khi kiểm thử sẽ ghi tải đầu vào, thời gian đo, độ trễ / tỉ lệ lỗi hoặc chỉ số phù hợp, cùng giới hạn của phép đo.
