from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NguoiDungViewSet, SanPhamViewSet, DonHangViewSet, ChiTietDonHangViewSet,
    ThanhToanViewSet, GioHangViewSet, ChiTietGioHangViewSet
)

# Tạo router
router = DefaultRouter()
router.register(r'nguoidung', NguoiDungViewSet, basename="nguoidung")
router.register(r'sanpham', SanPhamViewSet, basename="sanpham")
router.register(r'donhang', DonHangViewSet, basename="donhang")
router.register(r'chitietdonhang', ChiTietDonHangViewSet, basename="chitietdonhang")
router.register(r'thanhtoan', ThanhToanViewSet, basename="thanhtoan")
router.register(r'giohang', GioHangViewSet, basename="giohang")
router.register(r'chitietgiohang', ChiTietGioHangViewSet, basename="chitietgiohang")

# Khai báo urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Kết hợp tất cả các routes từ router
]

