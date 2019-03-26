# Section 1

This application uses flask that contains just one route.

## Running

It's necessary to run the file "app.py": `python app.py`

The application will be running on port 5000.

## Routes

- `/add_two_routes`
        
    CURL: `curl --request POST \
              --url http://localhost:5000/add_two_numbers \
              --header 'content-type: application/json' \
              --data '{
                "x": 1,
                "y": 1
            }'`
 