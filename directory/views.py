from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Directory, ElementDirectory
from .serializers import DirectoryListSerializers, DirectoryDetailListSerializers


class DirectoryListView(APIView):
    # вывод списка справочников
    def get(self, requests, page):
        directories = Directory.objects.all()
        serializer = DirectoryListSerializers(directories, many=True)
        if len(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11]):
            return Response(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11])
        else:
            return Response(status=404)


class DirectoryCreateView(APIView):
    # добавление справочника
    def post(self, requests):
        directory = DirectoryListSerializers(data=requests.data)
        if not directory.is_valid():
            return Response(status=403)

        directory.save()
        return Response(status=201)


class ElementDirectoryCreateView(APIView):
    # добавление элемента в справочник
    def post(self, requests):
        element = DirectoryDetailListSerializers(data=requests.data)
        if not element.is_valid():
            return Response(status=403)

        element.save()
        return Response(status=201)


class DirectoryDetailListView(APIView):
    # вывод элементов справочника
    def get(self, requests, pk, page):
        try:
            # наличие справочника с таким id
            parent = Directory.objects.get(id=pk)
        except:
            return Response(status=404)

        elementsDirectory = ElementDirectory.objects.filter(parentId=parent)
        serializer = DirectoryDetailListSerializers(elementsDirectory, many=True)

        if len(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11]):
            return Response(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11])
        else:
            return Response(status=404)


class DirectoryVersionDetailListView(APIView):
    # вывод элементов справочника текущей версии
    def get(self, requests, pk, version, page):
        try:
            # наличие справочника с таким id
            parent = Directory.objects.get(id=pk, version=version)
        except:
            return Response(status=404)

        elementsDirectory = ElementDirectory.objects.filter(parentId=parent)
        serializer = DirectoryDetailListSerializers(elementsDirectory, many=True)

        if len(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11]):
            return Response(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11])
        else:
            return Response(status=404)


class DirectoryDateListView(APIView):
    # вывод списка справочников на указанную дату
    def get(self, requests, date, page):
        directorys = Directory.objects.filter(date=date)
        serializer = DirectoryListSerializers(directorys, many=True)

        if len(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11]):
            return Response(serializer.data[(page - 1) * 10:(page - 1) * 10 + 11])
        else:
            return Response(status=404)


