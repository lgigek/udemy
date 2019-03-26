# Section 2, 3 and 4

This application is build by Docker compose and contain some basic endpoints.

## Running 

It is necessary to start the docker-compose to run the application:

`docker-compose build`

`docker-compose up`

The application will be running on port 5000.

## Routes

 - `/visit`
 
    CURL: `curl --request GET \
             --url http://localhost:5000/visit`
            
- `/add`

    CURL: `curl --request POST \
             --url http://localhost:5000/add \
             --header 'content-type: application/json' \
             --data '{
           	"x": 2,
           	"y": 10
           }'`

- `/subtract`

    CURL: `curl --request POST \
             --url http://localhost:5000/subtract \
             --header 'content-type: application/json' \
             --data '{
           	"x": 10,
           	"y": 2
           }'`

- `/multiply`
  
    CURL: `curl --request POST \
             --url http://localhost:5000/multiply \
             --header 'content-type: application/json' \
             --data '{
           	"x": 20,
           	"y": 10
           }'`

- `/divide`
  
    CURL: `curl --request POST \
             --url http://localhost:5000/divide \
             --header 'content-type: application/json' \
             --data '{
           	"x": 10,
           	"y": 5
           }'`