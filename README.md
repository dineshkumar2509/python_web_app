This is an example of web server implementation with uwsgi python backend, connected to Postgres DB and accessed using NGINX. The app is accessible from port 4567 and has two endoints - 'option1' and 'option2'.

Fast setup:
docker-compose up --build
curl --request GET http://localhost:4567/option1?param1=value
curl --request GET http://localhost:4567/option2?param1=value
