Terra Colab contains methods for working in a Colaboratory notebook.

Production
==========

Создание нового ноутбука колаба
-------------------------------
https://colab.research.google.com/#create=true

Установка пакета
----------------
Через ``github.com``

.. code-block:: bash

   !pip install git+https://github.com/aiuniver/terra_colab.git

Через ``pypi.org``

.. code-block:: bash

   !pip install terra_colab

Инициализация веб-сервиса
-------------------------

.. code-block:: bash

    !tc-init

Данная команда запрашивает доступ к ``Google.Drive`` и авторизацию в сервисе ``TerraAI``

Запуск веб-сервиса
------------------

.. code-block:: bash

    !tc-web

Если авторизация не была выполнена до этой команды, то автоматически будет запущена команда ``tc-init``

Так же данная команда может принимать аргумент ``-b`` или ``--branch`` - имя ветки репозитория проекта ``TerraGUI``:

.. code-block:: bash

   !tc-web --branch dev

Summary
-------
Т.о. для запуска в ноутбуке колаба достаточно выполнить следующий код

.. code-block:: bash

   !pip install terra_colab
   !tc-web


Development
===========

Для работы необходимо запустить 2 веб-сервиса ``TerraAI`` и ``TerraGUI``

Запуск ``TerraAI``
------------------

Установка пакета
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python ./setup.py install

Данную установку **ОБЯЗАТЕЛЬНО!** необходимо выполнять, если были какие-то изменения в проекте.


Переменные окружения
~~~~~~~~~~~~~~~~~~~~
Создаем в ``./cyber_kennel`` файл ``.env`` со следующим содержанием (все переменные должны быть определены)

.. code-block:: shell

   DJANGO_SECRET=
   EMAIL_PASSWORD=
   EMAIL_ADDRESS=

Запускаем веб-сервис
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python ./cyber_kennel/manage.py runserver localhost:8080

Вместо ``localhost:8080`` естественно ставим свои данные, далее этот сервис понадобится указать в окружении сервиса ``TerraGUI``

Запуск ``TerraGUI``
-------------------

Переменные окружения
~~~~~~~~~~~~~~~~~~~~
Создаем в ``./`` файл ``.env`` со следующим содержанием (все переменные должны быть определены)

.. code-block:: bash

   SECRET_KEY=
   DEBUG=True
   ALLOWED_HOSTS=*
   TERRA_AI_DATA_PATH=./TerraAI
   TERRA_AI_EXCHANGE_API_URL=http://localhost:8080/api/v1/exchange

``TERRA_AI_DATA_PATH`` - путь к файлам, которые используются для хранения датасетов и других файлов проекта
``TERRA_AI_EXCHANGE_API_URL`` - API-url к запущенному веб-сервису ``TerraAI``, а именно здесь нужно поменять ``localhost:8080`` на свой, который был указан при запуске веб-сервиса ``TerraAI``. Ну и конечно же мы здесь можем указать адрес production-версии проекта ``TerraAI`` - ``terra.neural-university.ru``, т.о. у нас пропадает необходимость в запуске своего веб-сервиса ``TerraAI``, но не советую его использовать, т.к. зачастую production-версия различается с development-версией.

Запускаем веб-сервис
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python ./manage.py runserver localhost:8000

Вместо ``localhost:8000`` естественно ставим свои данные
