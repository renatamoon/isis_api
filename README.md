# isis_api

<hr>

<p align="center">
  <a href="#projeto">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">How to install</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#execução">How to execute it</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#response">Response</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
</p>

## <a id="projeto"> 💻 ABOUT THE PROJECT </a>

This is a microservice able to accept RESTFUL requests receiving as parameter either city name or lat long 
coordinates and returns a playlist (only track names is fine) suggestion according to the current temperature.`.

Some functionalities present on this project:

    * Route to return musics of a playlist according to weather city;
    * Spotify Developer API consummer;
    * Weather Map API consummer;

🟩 PROJECT STATUS: <b>STILL IN DEVELOPMENT ... </b> <br>

<hr>

## <a id="tecnologias"> 🧪 TECHNOLOGIES </a>

- Python
- FAST API
- Playwright
- Pydantic

<hr>

## <a id="instalacao"> 🔴 HOW TO INSTALL IT </a> 

<b>- Clone the repo with the following command:</b> `https://github.com/renatamoon/isis_api.git` <br>

<hr> 

#### On Windows

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: If for any reason occurs and error:</b> on powershell execute the following command: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>- Execute requirements with the command: </b>`pip install -r requirements.txt`<br>

<hr> 

#### On Linux:

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment:</b> `source venv/bin/activate`<br>
<b>- Execute requirements with the command:</b> `pip install -r requirements.txt`<br>

<hr>

Create a project root `.env` file and change your local strings connections to do the properly connection <br>

```commandline
MONGO_CONNECTION_URL=
MONGODB_DATABASE_NAME=
MONGODB_COLLECTION=
```

<hr>

## <a id="execução"> 🔴 EXECUTE HYPERCORN </a> 

- To Execute the application run the command: `uvicorn main:app --reload`

<hr>

## <a> 🔴 USING THE SWAGGER (NATIVE FOR FAST API) </a> 

- To user the FastAPI user the router: `http:{your-host}/get_playlist_weather/docs`

## <a> 🔴 REQUISITION ROUTER </a> 

- Use the router on your Postman/Insomnia/Swagger: `http:{your-host}/get_playlist_weather` ;

<hr>

## <a id="response"> 🔴 API RESPONSES: </a> 

- Expected return of the route `/get_playlist_weather` :
