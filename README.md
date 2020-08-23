для запуска
	python manage.py runserver

доступ к админ панеле
	логин: admin
	пароль: password


/api/v1/directory/<numberPage> - возвращает список справочников 10 штук на страницу (numberPage >= 1)
/api/v1/directory/<idDirectory>/<numberPage> - возвращает список элементов справочника по id (idDirectory - id справочника)
/api/v1/directory/<idDirectory>/<version>/<numberPage> - возвращает элементы заданного справочника указанной версии
/api/v1/directory/<idDirectory>/current/<numberPage> - возвращает элементы заданного справочника текущей версии
/api/v1/directory/<date>/<numberPage> - возвращает список справочников, актуальных на указанную дату (date - yyyy-mm-dd)
/api/v1/directory/create - добавить новый справочник
/api/v1/element/create - добавить новый элемент в справочник
