id=$(docker run -d -t ubuntu)
docker cp "./server.py" "$id:/"
echo "Started: $id"
docker exec -it $id "/bin/bash"