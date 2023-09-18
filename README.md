# containerized-db-frontend
docker-compose build
docker-compose up
docker-compose down
localhost:5000 #frontend
localhost:8080 #adminer


# db data is being saved in volume and eventhough the container is being reinitialized or rebuild it is still persistent.
curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
