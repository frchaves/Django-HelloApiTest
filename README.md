# Django HelloApiTest

## Description:
A RESTful API able to greet people. In the API it is possible to
pass in a name (for instance "John") and be greeted with a simple text saying "Hello,
John" (POST request). On another endpoint it is possible to see a report of which names were
given and how often they were greeted (GET request). Both endpoints are accessible at 
(_**http://localhost:8000/greetings/**_) 


### Tech Stack:
- PostgreSQL
- Python (Django, Django Rest Framework, Pytest)
- Docker


### Setup:
- Clone the project to a folder (_**https://github.com/frchaves/hello_api_test**_)
- Open the terminal in the project folder (/greetingsApp)
- Run the application with Docker Compose:
  - docker-compose build
  - docker-compose up 
  - Access the browsable DRF API @ _**localhost:8000**_
  - For more information, read the documentation (in Swagger, Redoc) 
  about available endpoints at (_**http://localhost:8000/api/schema/swagger-ui/**_), 
  (_**http://localhost:8000/api/schema/redoc/**_) or get the Open API schema at (_**http://localhost:8000/api/schema/**_)
    
  
- Test the application with Postman, curl or SwaggerUI:
  - Use the browsable API to test both the GET and POST endpoints at (_**http://localhost:8000/greetings/**_)
  - An example of a POST request would be
  {"name": "John"}. Where the response would be [
    "Hello,John"]
  - An example of a GET request would be {
        "name": "John",
        "number_greetings": 1
    }
   
### Run the Pytest tests inside Docker:
  - Access the django container with docker-compose exec web bash
  - Cd into /greetingsApp, run pytest (pytest tests -v)
  
