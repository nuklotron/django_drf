1. docker build -t <b>django_drf</b> . # создаем образ
2. docker run <b>--network host</b> -p 8002:80 <b>django_drf</b> # запускаем контейнер
3. docker exec -it <b>priceless_shtern</b> psql -U postgres -d <b>postgres</b>  # создать бд в контейнере