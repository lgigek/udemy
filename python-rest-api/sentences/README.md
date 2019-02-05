# Section 5

This application is build by Docker and contain some endpoints to register an user and store a sentence for the user.

## Running 
It is necessary to start the docker-compose to run the application:

`docker-compose build`

`docker-compose up`

The application will be running on port 5000.

## Routes
- `/user`

   CURL: `curl --request POST \
     --url http://localhost:5000/user \
     --header 'content-type: application/json' \
     --data '{
   	"username": "teste",
   	"password": "teste1234"
   }'`

- `/sentence`

   CURL: `curl --request POST \
     --url http://localhost:5000/sentence \
     --header 'content-type: application/json' \
     --data '{
   	"username": "gigek",
   	"password": "teste1234",
   	"sentence": "teste"
   }'`
   
   CURL: `curl --request GET \
     --url http://localhost:5000/sentence \
     --header 'content-type: application/json' \
     --data '{
   	"username": "gigek",
   	"password": "teste1234"
   }'`