# Authorization Proyect

#### Ivan Raitman
  
## PING

With this application the possibility of authorizing endpoints through middleware is stated

- **URL:**
    `/ping`

- **Method**
    `GET`
  
- **Response:**
    **Code:** 200 <br />
        **Content:**
        
        "pong"

    **Code:** 403 <br />
        **Content:**
        
        "unauthorized"

# Run this project

If you want to run this code locally, you should run the following commands:

* Being inside the project folder, build the container:

      docker build -t test_app .

* After that, you are able to run the code

      docker run -it --publish 8081:8081  test_app
 
It is important to have the local_settings file to run this code correctly.
