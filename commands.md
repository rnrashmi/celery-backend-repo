pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker exec -t django /bin/sh