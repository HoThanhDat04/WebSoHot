from django.db import models

class NguoiDung(models.Model):
    ho_ten = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mat_khau = models.CharField(max_length=255)
    dia_chi = models.TextField(blank=True, null=True)
    dang_nhap = models.BooleanField(default=True)

    def __str__(self):
        return self.ho_ten

class Admin(models.Model):
    nguoi_dung = models.OneToOneField(NguoiDung, on_delete=models.CASCADE)

class SanPham(models.Model):
    ten = models.CharField(max_length=255)
    gia = models.FloatField()
    mo_ta = models.TextField(blank=True, null=True)
    so_luong = models.IntegerField()

    def __str__(self):
        return self.ten

class DonHang(models.Model):
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    ngay_dat = models.DateField(auto_now_add=True)
    trang_thai = models.CharField(max_length=50)
    tong_tien = models.FloatField()

class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()
    don_gia = models.FloatField()

class GioHang(models.Model):
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)

class ChiTietGioHang(models.Model):
    gio_hang = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()

class ThanhToan(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    phuong_thuc = models.CharField(max_length=255)
    so_tien = models.FloatField()
    da_thanh_toan = models.BooleanField(default=False)

class DanhGia(models.Model):
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    so_sao = models.IntegerField()
    binh_luan = models.TextField(blank=True, null=True)
