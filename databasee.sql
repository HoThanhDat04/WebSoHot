CREATE DATABASE sohot;
USE sohot;

-- Bảng Người Dùng
CREATE TABLE NguoiDung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    mat_khau VARCHAR(255) NOT NULL,
    dia_chi TEXT,
    dang_nhap BOOLEAN DEFAULT FALSE
);

-- Bảng Admin
CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nguoi_dung_id INT UNIQUE,
    FOREIGN KEY (nguoi_dung_id) REFERENCES NguoiDung(id)
);

-- Bảng Sản Phẩm
CREATE TABLE SanPham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(255) NOT NULL,
    gia FLOAT NOT NULL,
    mo_ta TEXT,
    so_luong INT NOT NULL
);

-- Bảng Giỏ Hàng
CREATE TABLE GioHang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nguoi_dung_id INT,
    FOREIGN KEY (nguoi_dung_id) REFERENCES NguoiDung(id)
);

-- Bảng Chi Tiết Giỏ Hàng
CREATE TABLE ChiTietGioHang (
    gio_hang_id INT,
    san_pham_id INT,
    so_luong INT NOT NULL,
    PRIMARY KEY (gio_hang_id, san_pham_id),
    FOREIGN KEY (gio_hang_id) REFERENCES GioHang(id),
    FOREIGN KEY (san_pham_id) REFERENCES SanPham(id)
);

-- Bảng Đơn Hàng
CREATE TABLE DonHang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nguoi_dung_id INT,
    ngay_dat DATE NOT NULL,
    trang_thai VARCHAR(50) NOT NULL,
    tong_tien FLOAT NOT NULL,
    FOREIGN KEY (nguoi_dung_id) REFERENCES NguoiDung(id)
);

-- Bảng Chi Tiết Đơn Hàng
CREATE TABLE ChiTietDonHang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    don_hang_id INT,
    san_pham_id INT,
    so_luong INT NOT NULL,
    don_gia FLOAT NOT NULL,
    FOREIGN KEY (don_hang_id) REFERENCES DonHang(id),
    FOREIGN KEY (san_pham_id) REFERENCES SanPham(id)
);

-- Bảng Thanh Toán
CREATE TABLE ThanhToan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    don_hang_id INT,
    phuong_thuc VARCHAR(255) NOT NULL,
    so_tien FLOAT NOT NULL,
    da_thanh_toan BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (don_hang_id) REFERENCES DonHang(id)
);

-- Bảng Đánh Giá
CREATE TABLE DanhGia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    san_pham_id INT,
    nguoi_dung_id INT,
    so_sao INT CHECK(so_sao BETWEEN 1 AND 5),
    binh_luan TEXT,
    FOREIGN KEY (san_pham_id) REFERENCES SanPham(id),
    FOREIGN KEY (nguoi_dung_id) REFERENCES NguoiDung(id)
);
