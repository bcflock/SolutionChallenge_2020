docker-compose down
docker volume prune -f
docker network prune -f
docker image prune -f
docker container prune -f