from rest_framework import serializers
from .models import Department, Item


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    departament = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    departament_detail = DepartmentSerializer(source="departament", read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "departament",
            "departament_detail",  # Вложенный объект департамента только для чтения
            "number",
            "seal_number",
            "user",
            "head_of_department",
            "warehouse_manager",
            "type",
            "motherboard",
            "motherboard_model",
            "CPU",
            "generation",
            "frequency",
            "HDD",
            "SSD",
            "disk_type",
            "RAM_type",
            "RAM_size",
            "GPU",
            "ipadresss",
            "mac_adress",
            "printer",
            "scaner",
            "type_webcamera",
            "model_webcam",
            "monitor",
        ]

    def create(self, validated_data):
        # Создаем объект Item с валидированными данными
        return Item.objects.create(**validated_data)
