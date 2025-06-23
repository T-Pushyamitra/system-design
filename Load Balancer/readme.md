## To Run the application 

- Need a docker desktop
- Run command `docker-compose up --build -d`
- Now, The nginx will be running on 8080 port


## Access the backend server

- open `localhost:8080`, You need to see `{"message": f"Hello, FastAPI from {os.getenv('APP_NAME')}"}`
- refersh/send request again the server number in response should be changing