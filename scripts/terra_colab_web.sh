#!/usr/bin/env bash

CONTENT_PATH=/content


cd $(CONTENT_PATH)
ls -la

#pip install -r ./requirements/colab.txt
#chmod 400", response.get("data").get("rsa")])
#self.__run_shell(["chmod +x ./manage.py"])
#self.__run_shell(
#    [
#        "./manage.py",
#        "runserver",
#        "80",
#        "&",
#        "ssh",
#        "-i",
#        response.get("data").get("rsa"),
#        "-o",
#        "StrictHostKeyChecking=no",
#        "-R",
#        f'{response.get("data").get("port")}:localhost:80',
#        response.get("data").get("user"),
#    ]
#)
