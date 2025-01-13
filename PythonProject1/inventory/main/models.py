from platform import mac_ver
from unittest.mock import mock_open

from django.db import models


# Create your models here.


class Item(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    seal_number = models.CharField(max_length=255, verbose_name='Номер пломбы')
    departament = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Цех')
    user = models.CharField(max_length=255, verbose_name='Пользователь')
    head_of_department = models.CharField(max_length=255, verbose_name='Руководитель подразделения')
    warehouse_manager = models.CharField(max_length=255, verbose_name='Зав. склада')
    type = models.CharField(max_length=255, verbose_name='Тип орг.техники')
    motherboard = models.CharField(max_length=255, verbose_name='Производитель МП')
    motherboard_model = models.CharField(max_length=255, verbose_name='Модель МП')
    CPU = models.CharField(max_length=255, verbose_name='Процессор')
    generation = models.CharField(max_length=255, verbose_name='Поколение процессора')
    frequency = models.CharField(max_length=255, verbose_name='Частота процессора')
    HDD = models.IntegerField(default="-", verbose_name='Диск  HDD')
    SSD = models.IntegerField(verbose_name='Диск  SSD')
    disks = [
        (0, 'sata-1'),
        (1, 'sata-2'),
        (2, 'sata-3'),
        (3, 'NVmE'),
        (4, 'M2'),
    ]
    disk_type = models.IntegerField(choices=disks, verbose_name='Тип диска')
    RAM = [
        (1, 'DDR1'),
        (2, 'DDR2'),
        (3, 'DDR3'),
        (4, 'DDR4'),
        (5, 'DDR5'),
    ]
    RAM_type = models.IntegerField(choices=RAM, verbose_name='Тип оперативки')
    RAM_size = models.IntegerField(verbose_name='Размер оперативной памяти')
    GPU = models.CharField(max_length=255, verbose_name='Видеокарта')
    ipadresss = models.CharField(max_length=255, verbose_name='IPv4 адрес')
    mac_adress = models.CharField(max_length=255, verbose_name='Физический(MAC) адрес')
    printer = models.CharField(max_length=255, verbose_name='Принтер', default='Нет')
    scaner = models.CharField(max_length=255, verbose_name='Сканер', default='Нет')
    type_webcamera = models.CharField(max_length=255, verbose_name='Тип вебкамера', default='Нет')
    model_webcam = models.CharField(max_length=255, verbose_name='Модель вебкамеры', default='Нет')
    monitor = models.CharField(max_length=255, verbose_name='Монитор')

    def __str__(self):
        return self.user


class Department(models.Model):
    number = models.IntegerField(verbose_name='Номер цеха')
    name = models.CharField(max_length=255, verbose_name='Название цеха')
    bolishi = models.CharField(max_length=255, verbose_name='Руководитель цеха')

    def __str__(self):
        return self.name
