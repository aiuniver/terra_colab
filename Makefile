PORT=9120
TUNNEL_USER=proxy_user@terra.neural-university.ru
RSA_KEY=./rsa.key

run:
	pip install -r ./requirements/colab.txt
	chmod 400 $(RSA_KEY)
	chmod +x ./manage.py
	./manage.py runserver 80 & ssh -i '$(RSA_KEY)' -o StrictHostKeyChecking=no -R $(PORT):localhost:80 $(TUNNEL_USER)
