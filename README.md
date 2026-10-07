# Báo cáo thực hành kiểm thử API bằng Postman

**Sinh viên:** Hoàng Tuấn Bảo — **MSSV:** 23010194

## 1. Mục tiêu
Tìm hiểu Postman, tổ chức request trong Collection, sử dụng biến URL, gửi GET/POST/PUT/DELETE và viết JavaScript kiểm tra phản hồi.

## 2. Giới thiệu công cụ
Postman giúp tạo yêu cầu HTTP, cấu hình URL, headers, body và quan sát status code, thời gian phản hồi, dữ liệu JSON. Collection gom các request; biến giúp tái sử dụng URL. Script sau phản hồi kiểm tra kết quả tự động.

## 3. Môi trường và dữ liệu
- Postman Desktop, Python 3 và API khóa học đi kèm `server.py`.
- URL: `http://127.0.0.1:8000`; không cần tài khoản hoặc API key.
- Khóa học có các trường `id`, `name`, `credits`.
- Dữ liệu lưu trong RAM, khởi động lại server sẽ đặt lại dữ liệu. Đây là API tự xây dựng phục vụ bài thực hành.

## 4. Các bước thực hiện
1. Mở terminal tại thư mục bài, chạy `py server.py` trên Windows (hoặc `python3 server.py`). Giữ terminal mở.
2. Mở Postman Desktop → Import → chọn `Postman_Assignment.postman_collection.json`.
3. Mở Collection → Variables, kiểm tra `base_url` là `http://127.0.0.1:8000`.
4. Chạy request theo thứ tự 01–07. Request 02 tự lưu ID vào biến `course_id`; các request sau dùng ID này.
5. Với POST/PUT, xem Body → raw → JSON. Sau khi Send, xem response và Test Results. Script nằm ở Scripts → Post-response (bản cũ có thể gọi là Tests).
6. Chọn Run Collection, chạy một vòng theo đúng thứ tự để tổng hợp kết quả.

## 5. Kịch bản kiểm thử
| Mã | Thao tác | Endpoint | Mong đợi | Kết quả Postman |
|---|---|---|---|---|
| TC01 | GET danh sách | `/courses` | 200, mảng JSON | Chưa chạy |
| TC02 | POST tạo mới | `/courses` | 201, tên đúng, có ID | Chưa chạy |
| TC03 | GET theo ID | `/courses/{{course_id}}` | 200, đúng ID | Chưa chạy |
| TC04 | PUT cập nhật | `/courses/{{course_id}}` | 200, tên và tín chỉ mới | Chưa chạy |
| TC05 | DELETE | `/courses/{{course_id}}` | 200, thông báo Deleted | Chưa chạy |
| TC06 | GET khóa học đã xóa | `/courses/{{course_id}}` | 404, Course not found | Chưa chạy |
| TC07 | POST tên rỗng, tín chỉ âm | `/courses` | 400, có thông báo lỗi | Chưa chạy |

404/400 ở TC06/TC07 là kết quả mong đợi của ca kiểm thử âm, không tự động có nghĩa là API bị lỗi.

## 6. Test script và biến
Mỗi request có hai phép kiểm tra: status code và nội dung JSON. Ví dụ request tạo khóa học:
```javascript
pm.test("Status 201", () => pm.response.to.have.status(201));
pm.test("Response data", () => {
  const d = pm.response.json();
  pm.expect(d.name).to.eql("Postman co ban");
  pm.expect(d.credits).to.eql(3);
  pm.expect(d.id).to.be.a("number");
  pm.collectionVariables.set("course_id", d.id);
});
```

## 7. Hình minh họa và kết quả thực tế
**Phần này cần hoàn thiện bằng ảnh chụp lần chạy Postman thực tế trước khi nộp.** Chưa có kết quả chạy Postman được xác nhận trong bản báo cáo này.

Lưu ảnh vào thư mục `images`, sau đó thêm các dòng Markdown sau khi đã có file:
```markdown
![Collection và biến URL](images/01-collection.png)
![GET danh sách](images/02-get.png)
![POST tạo khóa học và test](images/03-post.png)
![PUT cập nhật](images/04-put.png)
![DELETE khóa học](images/05-delete.png)
![GET sau xóa trả 404](images/06-not-found.png)
![POST dữ liệu sai trả 400](images/07-invalid.png)
![Kết quả Collection Runner](images/08-runner.png)
```
Ảnh request cần thấy method, URL, status code, response body và Test Results. Sau khi chạy, thay cột kết quả bằng status thực tế và Pass/Fail; ghi tổng số request và assertions từ Runner. Nếu tất cả đúng mong đợi, có 7 request và 14 assertions đạt.

## 8. Nhận xét
Bộ kiểm thử bao gồm luồng tạo → đọc → sửa → xóa và hai trường hợp lỗi. Các phép kiểm tra dữ liệu giúp phát hiện trường hợp status đúng nhưng response sai. Chưa kiểm thử xác thực, tải lớn hay truy cập đồng thời vì API demo chưa có các chức năng đó. Kết luận đạt/chưa đạt cần dựa trên lần chạy thực tế ở mục 7.

## 9. Tài liệu tham khảo
- Video được giao: https://www.youtube.com/watch?v=MFxk5BZulVU
- Tham khảo bố cục: https://github.com/quocbinh93/CallPostMan
- Postman: https://learning.postman.com/docs/introduction/overview/

Bài sử dụng API và Collection riêng; ảnh kết quả cần chụp từ bài thực hành này.
