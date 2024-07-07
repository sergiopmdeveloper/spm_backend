docker build -t spm-backend-service .
docker run --rm --name spm-backend-service -p 8000:8000 spm-backend-service
