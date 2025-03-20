

# Register your models here.
from django.contrib import admin
from .models import NguoiDung, Admin, SanPham, DonHang, ChiTietDonHang, GioHang, ChiTietGioHang, ThanhToan, DanhGia

# Đăng ký model đơn giản (cách nhanh nhất)
admin.site.register(NguoiDung)
admin.site.register(Admin)
admin.site.register(SanPham)
admin.site.register(DonHang)
admin.site.register(ChiTietDonHang)
admin.site.register(GioHang)
admin.site.register(ChiTietGioHang)
admin.site.register(ThanhToan)
admin.site.register(DanhGia)

