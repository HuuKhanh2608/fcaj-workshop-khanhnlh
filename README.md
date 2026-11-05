# Internship Report — Nguyễn Lê Hữu Khánh

Báo cáo thực tập song ngữ Anh–Việt dùng Hugo và theme Learn.

Địa chỉ dự kiến sau khi bật GitHub Pages:
<https://huukhanh2608.github.io/fcaj-workshop-khanhnlh/>

## Build tại máy

Cài Hugo Extended **0.134.3**, cùng phiên bản với workflow, rồi chạy tại thư mục gốc:

```sh
hugo --minify --cleanDestinationDir
```

Kết quả nằm trong `public/` và được Git bỏ qua. Để xem thử bằng máy chủ local:

```sh
hugo server --disableFastRender
```

Mở địa chỉ Hugo in ra trong terminal, bao gồm đường dẫn `/fcaj-workshop-khanhnlh/`.

## Xuất bản lên GitHub Pages

1. Commit và push thay đổi lên nhánh `main`.
2. Trong tab **Actions**, chờ workflow **Deploy Hugo site to GitHub Pages** thành công. Workflow build website và đưa kết quả vào nhánh `gh-pages`.
3. Vào **Settings → Pages → Build and deployment**, chọn **Deploy from a branch**, nhánh **gh-pages**, thư mục **/ (root)**, rồi **Save**.
4. Chờ GitHub Pages xuất bản, sau đó mở địa chỉ website ở trên. Bản tiếng Việt nằm tại `/fcaj-workshop-khanhnlh/vi/`.

Các lần push tiếp theo lên `main` sẽ tự build và cập nhật website. Có thể chạy lại bằng **Actions → Deploy Hugo site to GitHub Pages → Run workflow**.

Nếu repository yêu cầu bật Actions, bật tại tab Actions trước khi chạy workflow. Nếu gặp lỗi quyền push vào `gh-pages`, kiểm tra chính sách **Settings → Actions → General → Workflow permissions**; workflow cần quyền ghi nội dung repository.

## Chỉnh sửa nội dung

- `content/`: nội dung Markdown; `_index.md` là tiếng Anh và `_index.vi.md` là tiếng Việt.
- `static/images/`: ảnh, được xuất ra `/images/` khi build.
- `layouts/`: tùy biến giao diện và xử lý đường dẫn để hoạt động trên GitHub Pages.
- `config.toml`: địa chỉ website và cấu hình ngôn ngữ.

Ảnh trong Markdown có thể dùng `/images/...`; render hook tự thêm đường dẫn repository. Liên kết nội bộ tới trang được chuyển thành URL Hugo tương ứng. Tên đường dẫn phân biệt chữ hoa/chữ thường trên GitHub Pages.

## Trạng thái báo cáo cá nhân

Nội dung đã chuyển thành bản nháp riêng của Nguyễn Lê Hữu Khánh. Báo cáo có 7 phần, 12 tuần worklog, 3 mục blog, 3 mục sự kiện và 9 mục tài liệu workshop; các nội dung chính đều có cặp tiếng Anh / tiếng Việt.

Các hoạt động, đề tài, chi phí, kết quả kiểm thử và demo chưa được cung cấp đều ghi rõ đang chờ cập nhật. Cấu trúc này chưa có nghĩa đã hoàn thành các yêu cầu nộp báo cáo. Xem [checklist biên soạn](docs/report-checklist.md).

Khi thay đổi dữ liệu thực tế, cập nhật cả hai bản ngôn ngữ và trạng thái tại trang tổng quan. Kỳ thực tập kéo dài từ 14/09 đến 14/12/2026. Worklog chia 12 tuần đầu và có mục ghi bổ sung hoạt động đến ngày kết thúc kỳ thực tập. Nội dung lab S3 và proposal IoT của template đã được thay bằng khung cho đề tài cá nhân. Các ảnh mẫu cũ vẫn nằm trong static nhưng không được dùng làm minh chứng của báo cáo.
