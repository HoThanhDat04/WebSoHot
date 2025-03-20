from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# ViewSet cho Người Dùng
class NguoiDungViewSet(viewsets.ModelViewSet):
    queryset = NguoiDung.objects.all()
    serializer_class = NguoiDungSerializer

# ViewSet cho Sản Phẩm
class SanPhamViewSet(viewsets.ModelViewSet):
    queryset = SanPham.objects.all()
    serializer_class = SanPhamSerializer

# ViewSet cho Đơn Hàng
class DonHangViewSet(viewsets.ModelViewSet):
    queryset = DonHang.objects.all()
    serializer_class = DonHangSerializer

# ViewSet cho Chi Tiết Đơn Hàng
class ChiTietDonHangViewSet(viewsets.ModelViewSet):
    queryset = ChiTietDonHang.objects.all()
    serializer_class = ChiTietDonHangSerializer

# ViewSet cho Thanh Toán
class ThanhToanViewSet(viewsets.ModelViewSet):
    queryset = ThanhToan.objects.all()
    serializer_class = ThanhToanSerializer

# ViewSet cho Giỏ Hàng
class GioHangViewSet(viewsets.ModelViewSet):
    queryset = GioHang.objects.all()
    serializer_class = GioHangSerializer

# ViewSet cho Chi Tiết Giỏ Hàng
class ChiTietGioHangViewSet(viewsets.ModelViewSet):
    queryset = ChiTietGioHang.objects.all()
    serializer_class = ChiTietGioHangSerializer
