# Terra Colab

Terra Colab contains methods for working in a Colaboratory notebook.


## Production

### Создаем новый ноутбук колаба
https://colab.research.google.com/#create=true

### Устанавливаем пакет
Через `github.com`
```
!pip install git+https://github.com/aiuniver/terra_colab.git
```

Через `pypi.org`
```
!pip install terra_colab
```

### Запускаем веб-сервис
```
!terra_colab_web
```  
Так же данная команда может принимать аргумент `-b` или `--branch` - имя ветки репозитория проекта TerraGUI:
```
!terra_colab_web --branch dev
```

### Summary
Т.о. для запуска в ноутбуке колаба достаточно выполнить следующий код
```
!pip install terra_colab
!terra_colab_web
```


## Development

Для работы необходимо запустить 2 веб-сервиса `TerraAI` и `TerraGUI`

### Запуск `TerraAI`

#### Устанавливаем пакет
```
python ./setup.py install
```
Данную установку **ОБЯЗАТЕЛЬНО!** необходимо выполнять, если были какие-то изменения в проекте.

#### Создаем в `./cyber_kennel` файл `.env` со следующим содержанием (все переменные должны быть определены)
```
DJANGO_SECRET=
EMAIL_PASSWORD=
EMAIL_ADDRESS=
```

#### Запускаем веб-сервис
```
python ./cyber_kennel/manage.py localhost:8080
```
Вместо `localhost:8080` естественно ставим свои данные, далее этот сервис понадобится указать в окружении сервиса `TerraGUI`

### Запуск `TerraGUI`

#### Создаем в `./` файл `.env` со следующим содержанием (все переменные должны быть определены)
```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=*
TERRA_AI_DATA_PATH=./TerraAI
TERRA_AI_EXCHANGE_API_URL=http://localhost:8080/api/v1/exchange
```
`TERRA_AI_DATA_PATH` - путь к файлам, которые используются для хранения датасетов и других файлов проекта  
`TERRA_AI_EXCHANGE_API_URL` - API-url к запущенному веб-сервису `TerraAI`, а именно здесь нужно поменять `localhost:8080` на свой, который был указан при запуске веб-сервиса `TerraAI`. Ну и конечно же мы здесь можем указать адрес production-версии проекта `TerraAI` - `terra.neural-university.ru`, т.о. у нас пропадает необходимость в запуске своего веб-сервиса `TerraAI`, но не советую его использовать, т.к. зачастую production-версия различается с development-версией.

#### Запускаем веб-сервис
```
python ./manage.py localhost:8000
```
Вместо `localhost:8000` естественно ставим свои данные
