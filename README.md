# Microservices_in_python

The backend is composed of two Apps; 
1. Admin App - (Django)
2. Main App - (Flask) 

both applications run in the docker container and is connected with their own Database (mysql). They communicate with eachother using Rabbitmq events.