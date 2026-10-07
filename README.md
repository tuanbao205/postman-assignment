# Báo cáo kiểm thử API bằng Postman

**Sinh viên:** Hoàng Tuấn Bảo  
**MSSV:** 23010194  
**Đối tượng kiểm thử:** API quản lý khóa học

## 1. Giới thiệu Postman và mục tiêu

Postman là công cụ gửi request HTTP và kiểm tra phản hồi API. Người kiểm thử có thể cấu hình URL, header, body, xem status code và dữ liệu JSON, tổ chức request trong Collection và viết script kiểm tra tự động.

Bài thực hành sử dụng GET, POST, PUT, DELETE để kiểm thử chức năng quản lý khóa học; dùng biến URL, biến ID và kiểm tra cả dữ liệu hợp lệ lẫn dữ liệu không hợp lệ.

## 2. Môi trường và phương pháp kiểm thử

- **Công cụ:** Postman Desktop.
- **API:** API demo khóa học chạy bằng Python 3 tại `http://127.0.0.1:8000`.
- **Dữ liệu:** khóa học có `id`, `name`, `credits`; dữ liệu lưu trong RAM.
- **Phương pháp:** gửi request thủ công, quan sát response và dùng script Post-response để kiểm tra status code, nội dung JSON.
- **Biến Collection:** `base_url` lưu URL API; `course_id` lưu ID từ response của request 02.
- **Sản phẩm:** [Collection kiểm thử](https://github.com/tuanbao205/postman-assignment/blob/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/Postman_Assignment.postman_collection.json) và 7 ảnh kết quả bên dưới.

Để chạy lại, tải [server của lần thực hành](https://github.com/tuanbao205/postman-assignment/blob/d3f4da5f58a47dce77c7cb069b189e259818df72/server.py), chạy `py server.py`, rồi Import collection vào Postman. Giữ server hoạt động và chạy request theo thứ tự **01–07**. Server và collection được lưu trong lịch sử repo; bản nộp hiện tại chỉ gồm README, với ảnh minh họa liên kết từ phiên bản đã lưu.

## 3. Tổng hợp kịch bản kiểm thử

| Mã | Thao tác | Endpoint | Mong đợi | Kết quả Postman |
|---|---|---|---|---|
| TC01 | GET danh sách | `/courses` | 200, mảng JSON | 200 — Pass (2/2) |
| TC02 | POST tạo mới | `/courses` | 201, tên đúng, có ID | 201 — Pass (2/2) |
| TC03 | GET theo ID | `/courses/{{course_id}}` | 200, đúng ID | 200 — Pass (2/2) |
| TC04 | PUT cập nhật | `/courses/{{course_id}}` | 200, tên và tín chỉ mới | 200 — Pass (2/2) |
| TC05 | DELETE | `/courses/{{course_id}}` | 200, thông báo Deleted | 200 — Pass (2/2) |
| TC06 | GET khóa học đã xóa | `/courses/{{course_id}}` | 404, Course not found | 404 — Pass (2/2) |
| TC07 | POST tên rỗng, tín chỉ âm | `/courses` | 400, có thông báo lỗi | 400 — Pass (2/2) |

404/400 ở TC06/TC07 là kết quả mong đợi của ca kiểm thử âm, không tự động có nghĩa là API bị lỗi.

## 4. Thực hiện và hình ảnh kết quả

### TC01 — GET danh sách

**Mục đích:** lấy danh sách khóa học. **Phương thức:** GET. **URL:** `{{base_url}}/courses`. **Mong đợi:** HTTP 200, dữ liệu là mảng JSON.

**Kết quả thực tế:** Trả về mảng chứa khóa học ban đầu, HTTP 200; Test Results 2/2.

![TC01: GET danh sách](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/01-get-list.png)

### TC02 — POST tạo khóa học

**Mục đích:** tạo khóa học mới. **Phương thức:** POST. **URL:** `{{base_url}}/courses`. **Body:** `{"name":"Postman co ban","credits":3}`. **Mong đợi:** HTTP 201, có ID và dữ liệu đúng.

**Kết quả thực tế:** Tạo khóa học Postman co ban, credits = 3, ID = 2; HTTP 201; Test Results 2/2.

![TC02: POST tạo khóa học](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/02-post-create.png)

### TC03 — GET theo ID

**Mục đích:** đọc khóa học theo ID. **Phương thức:** GET. **URL:** `{{base_url}}/courses/{{course_id}}`. **Mong đợi:** HTTP 200, ID khớp biến `course_id`.

**Kết quả thực tế:** Đọc khóa học ID = 3, tên Postman co ban, credits = 3; HTTP 200; Test Results 2/2.

![TC03: GET theo ID](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/03-get-by-id.png)

### TC04 — PUT cập nhật

**Mục đích:** sửa tên và số tín chỉ. **Phương thức:** PUT. **URL:** `{{base_url}}/courses/{{course_id}}`. **Body:** `{"name":"Postman nang cao","credits":4}`. **Mong đợi:** HTTP 200, dữ liệu được cập nhật.

**Kết quả thực tế:** Cập nhật ID = 3 thành Postman nang cao, credits = 4; HTTP 200; Test Results 2/2.

![TC04: PUT cập nhật](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/04-put-update.png)

### TC05 — DELETE khóa học

**Mục đích:** xóa khóa học. **Phương thức:** DELETE. **URL:** `{{base_url}}/courses/{{course_id}}`. **Mong đợi:** HTTP 200, thông báo `Deleted`.

**Kết quả thực tế:** Xóa ID = 3, trả về Deleted; HTTP 200; Test Results 2/2.

![TC05: DELETE khóa học](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/05-delete.png)

### TC06 — GET sau xóa

**Mục đích:** kiểm tra khóa học đã xóa không còn truy xuất được. **Phương thức:** GET. **URL:** `{{base_url}}/courses/{{course_id}}`. **Mong đợi:** HTTP 404, thông báo `Course not found`.

**Kết quả thực tế:** Trả về Course not found; HTTP 404; Test Results 2/2. Đây là kết quả mong đợi sau khi xóa.

![TC06: GET sau xóa](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/06-get-deleted.png)

### TC07 — POST dữ liệu sai

**Mục đích:** kiểm tra việc từ chối dữ liệu sai. **Phương thức:** POST. **URL:** `{{base_url}}/courses`. **Body:** `{"name":"","credits":-1}`. **Mong đợi:** HTTP 400, có thông báo lỗi.

**Kết quả thực tế:** Từ chối dữ liệu không hợp lệ với thông báo name and positive integer credits required; HTTP 400; Test Results 2/2.

![TC07: POST dữ liệu sai](https://raw.githubusercontent.com/tuanbao205/postman-assignment/9c596f5c28acb21ad7b24eb1fa136eded4e0cd01/images/07-post-invalid.png)

## 5. Test script, kết quả và nhận xét

Mỗi request có hai test: kiểm tra status code và kiểm tra dữ liệu phản hồi. Ví dụ test của request POST tạo khóa học:

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

| Chỉ tiêu | Kết quả từ ảnh |
|---|---|
| Số kịch bản có ảnh kết quả | 7 |
| Kịch bản đạt | 7 |
| Kịch bản không đạt | 0 |
| Tổng số test đạt | 14/14 |
| Tỷ lệ kịch bản đạt | 100% |

Các ảnh cho thấy kết quả riêng lẻ phù hợp mong đợi. HTTP 404 và 400 ở TC06, TC07 xác nhận API xử lý đúng hai trường hợp lỗi.

**Ghi chú lần thực hành:** ảnh TC02 có ID = 2, còn TC03–TC05 có ID = 3, nên bộ ảnh chưa xác nhận một chuỗi thao tác liên tục trên cùng ID. Chưa có ảnh Collection Runner; số liệu trên được tổng hợp từ 7 ảnh request. Khi xác nhận lại toàn bộ luồng, chạy 01–07 theo đúng thứ tự với `course_id` do request 02 lưu.

Qua bài thực hành, sinh viên sử dụng được các phương thức HTTP cơ bản, biến Collection và test script. Phạm vi bài chưa bao gồm xác thực, kiểm thử tải hoặc truy cập đồng thời.

