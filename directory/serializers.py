from rest_framework import serializers

from .models import *


class DirectoryListSerializers(serializers.ModelSerializer):
    # список справочников
    class Meta:
        model = Directory
        fields = "__all__"


class DirectoryDetailListSerializers(serializers.ModelSerializer):
    # список элементов справочника
    class Meta:
        model = ElementDirectory
        fields = "__all__"
