# Generated by Django 5.1.6 on 2025-03-13 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NguoiDung",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ho_ten", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("mat_khau", models.CharField(max_length=255)),
                ("dia_chi", models.TextField(blank=True, null=True)),
                ("dang_nhap", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="SanPham",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ten", models.CharField(max_length=255)),
                ("gia", models.FloatField()),
                ("mo_ta", models.TextField(blank=True, null=True)),
                ("so_luong", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="GioHang",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nguoi_dung",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.nguoidung"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonHang",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ngay_dat", models.DateField(auto_now_add=True)),
                ("trang_thai", models.CharField(max_length=50)),
                ("tong_tien", models.FloatField()),
                (
                    "nguoi_dung",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.nguoidung"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nguoi_dung",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.nguoidung"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DanhGia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("so_sao", models.IntegerField()),
                ("binh_luan", models.TextField(blank=True, null=True)),
                (
                    "nguoi_dung",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.nguoidung"
                    ),
                ),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.sanpham"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChiTietGioHang",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("so_luong", models.IntegerField()),
                (
                    "gio_hang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.giohang"
                    ),
                ),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.sanpham"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChiTietDonHang",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("so_luong", models.IntegerField()),
                ("don_gia", models.FloatField()),
                (
                    "don_hang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.donhang"
                    ),
                ),
                (
                    "san_pham",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.sanpham"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ThanhToan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phuong_thuc", models.CharField(max_length=255)),
                ("so_tien", models.FloatField()),
                ("da_thanh_toan", models.BooleanField(default=False)),
                (
                    "don_hang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.donhang"
                    ),
                ),
            ],
        ),
    ]
