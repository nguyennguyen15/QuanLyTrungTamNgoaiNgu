# Tổ chức thư mục

Tài khoản
    admin@gmail.com
    hocvien@gmail.com
    giaovien@gmail.com
    nhanvien@gmail.com

Mật khẩu: `TTNN@2026`

## Thư mục chính

TTNGapp/
├── __init__.py       # Tạo app, cấu hình, đăng ký route
├── index.py          # Chạy chương trình
├── models.py         # Model và thao tác database
├── decorators.py     # Kiểm tra quyền người dùng
├── routes/           # Các đường dẫn web
├── services/         # Xử lý nghiệp vụ
├── templates/        # Các trang HTML
└── static/           # CSS, JavaScript, hình ảnh

## Routes

- `auth.py`: đăng nhập, đăng xuất, đăng ký.
- `student.py`: chức năng học viên.
- `teacher.py`: chức năng giảng viên.
- `employee.py`: chức năng nhân viên.
- `admin.py`: chức năng admin.
- `report.py`: thống kê và báo cáo.

## Services

- `account_service.py`: tạo tài khoản và hồ sơ theo vai trò.
- `enrollment_service.py`: đăng ký lớp, kiểm tra sĩ số.
- `grade_service.py`: tính điểm trung bình, Đạt/Không đạt.
- `invoice_service.py`: xử lý hóa đơn và thanh toán.
- `report_service.py`: lấy dữ liệu báo cáo.

## Templates

- `base.html`: khung chung, thanh điều hướng, nút đăng nhập/đăng ký/đăng xuất.
- `index.html`: nội dung trang chủ.

- `auth/`: các trang xác thực.
  - `login.html`: form đăng nhập bằng email và mật khẩu.
  - `register.html`: form học viên đăng ký tài khoản.

- `student/`: các trang dành cho học viên.
  - `courses.html`: xem danh sách khóa học và đăng ký lớp.
  - `enrollments.html`: xem các lớp đã đăng ký.
  - `grades.html`: xem điểm và kết quả học tập.
  - `profile.html`: xem mã học viên, họ tên và email.

- `teacher/`: các trang dành cho giảng viên.
  - `classes.html`: xem các lớp được phân công.
  - `attendance.html`: điểm danh học viên.
  - `grades.html`: nhập điểm thành phần.

- `employee/`: các trang dành cho nhân viên.
  - `students.html`: tra cứu và quản lý học viên.
  - `invoices.html`: lập và quản lý hóa đơn học phí.

- `admin/`: các trang dành cho admin.
  - `users.html`: tạo và quản lý tài khoản.
  - `courses.html`: quản lý khóa học.
  - `classes.html`: quản lý lớp học và phân công giảng viên.
  - `regulations.html`: cập nhật học phí, sĩ số và quy định.

- `reports/`: các trang báo cáo.
  - `dashboard.html`: số học viên, tỷ lệ đạt và doanh thu.
