# Storage-service

## Quick start

### Docker

#### Create container

```
docker-compose up -d
```

Run above command to create docker image and docker container.

After that, restart `storage-service` container.

> The reason to restart is it can be occured problem when `storage-service` try to connect to uncompleted mysql server. It's not a permanet solution however, let's handle the problem like this way in development environment.

### Delete container

```
docker-compose down
```

Run the above command to delete the container.

### Request API

#### ping

http://localhost:3004/api/v1/default/ping

#### etc

Please reference the subpart of the file in the api-gateway document of Notion.

#### Environment variable

See **environment** part inside of **docker-compose.yml** file.

## Summary

This is a service to handle static data like a file in Belf service.

## Special note

1. Path where actual file data is stored
   1. dev
      1. Pycharm, Visual Studio Code: Path of project directory + `STORAGE_SERVICE_UPLOAD_PATH` value in Config/local/upload_config.json file
      2. docker: `STORAGE_SERVICE_UPLOAD_PATH` environment variable in docker-compose.yml
   2. QA/production
      1. K8S: value of STORAGE_SERVICE_UPLOAD_PATH environment variable

## Stack

1. **Python:v3.9(greater than)**
2. Sanic web framework
3. Tortoise ORM
4. MySql:v5.7.16
5. VSCode
6. Pycharm
7. docker

> Offical development environment of Belf is VSCode, but we used Pycharm for language convenience.
> We checked VSCode can be used for the development environment.
> If you are interested, Please check the VSCode section below.
>
> Due to Python package errors, we recommend Unix-like MacOS, Linux, etc. as the development OS, and for Windows, we recommend using WSL2 + VSCode.
>
> Docker is a Stack for a simple test. Real production is served by K8S in the Azure cloud.

## Start

### Common

1. Run the `mysql` service from the oauth service or run the `mysql` service from the `docker-compose.yml` file to launch DB.

### VSCode

1. Open the storage-service directory.
2. Create **python3.9** virtual environemnt by python3 -m venv venv command.
3. Install Python packages by `pip install -r requirements.txt`
4. Go into debug window by clicking the left bug-shaped icon.
5. Select Sanic:main.py value from the drop box and launch debug by the green arrow button on the above of VSCode.

> You can check Python version by `python --version` command in VSCode terminal(Shell).
> You can check the path of venv which created no.2 by the `which python` command in Unix-based OS
>
> If you create a **python3.9** virtual environment named venv in number 2, the python command is automatically routed to venv when you run a new shell window inside VSCode.
> The relevant settings exist inside ./vscode/settings.json.
>
> In VSCode, the information about setting up debugs for number 3 exists inside the project ./vscode/launch.json.
>
> Number 4 is as same as the `python main.py` command.

### Pycharm

1. Open the project directory using Pycharm.
2. Click the Project Start Preset on the left side of the green worm and arrow shapes on the top right, and then go inside Edit Configurations.
3. Select the main.py file inside the storage-service as the script path item.
4. If there is no python interpreter greater than **python3.9** in the Python interpreter item, use the Pycharm function to create and select it.
5. Use the command `pip install -r requirements.txt` to install the Python package.
6. Save the execution environment settings, select them in the 2nd Preset Selection window, then click the worm icon on the top right to enter the debugging environment.

> Click View-Tool Windows-Python Console at the top of the Pycharm development environment to view the python version and
> path of the python command recognized by Pycharm with commands such as `python -version`.

## Environment variable

### Environment Variable Table Legend

| Component     | Explanation                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------- |
| Variable      | Name of the environment variable                                                               |
| dev           | Whether environment variable is used in the development environment                            |
| qa/prod       | Whether environment variable is used in qa, production environment                             |
| Default value | Default value when no environment variable is determined using the system environment variable |
| Example       | Array of examples can be used as environment variables                                         |
| Explanation   | Explanation about environment variable                                                         |

### Table of environmental variables

| Variable                        | dev | qa/prod | Default value | Example                                 | Explanation                                                                                                              |
| ------------------------------- | :-: | :-----: | :-----------: | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| STORAGE_SERVICE_IS_PROD         | 🚫  |   ✅    |               | true                                    | Value to distinguish whether it is a `K8S` deployment environment.                                                       |
| STORAGE_SERVICE_PORT            | ✅  |   🚫    |     8000      | 8000, 3004                              | Value to set `HTTP listen port`.                                                                                         |
| STORAGE_SERVICE_SSL             | 🚫  |   🚫    |      ""       |                                         | Value to set `SSL`(Unused)                                                                                               |
| STORAGE_SERVICE_ACCESS_LOG      | ✅  |   ✅    |     true      | true, false                             | Value for setting `Log`.                                                                                                 |
| STORAGE_SERVICE_IS_USING_DOCKER | ✅  |   🚫    |     true      | true                                    | Value for setting whether to drive locally using `Docker`.                                                               |
| STORAGE_SERVICE_UPLOAD_PATH     | ✅  |   ✅    |    /upload    | /upload, /mnt/mount/azure/files/storage | Input a `relative path` for local development or input absolute path of `directory` which be mounted with `Azure Files`. |
| STORAGE_SERVICE_DB_HOST         | ✅  |   ✅    |   127.0.0.1   | 127.0.0.1, host.docker.internal         | Value for setting about `IP` of `Master DB` to connect or `URL`.                                                         |
| STORAGE_SERVICE_DB_PORT         | ✅  |   ✅    |     3306      | 3306, 3307                              | Value for setting about `Port` of `Master DB` to connectPort`.                                                           |
| STORAGE_SERVICE_DB_NAME         | ✅  |   ✅    |     belf      | belf                                    | Value for setting about `DB Name` of `DB` to connect.                                                                    |
| STORAGE_SERVICE_DB_USER         | ✅  |   ✅    |     root      | root                                    | Value for setting about `User Name` of `DB` to connect.                                                                  |
| STORAGE_SERVICE_DB_PASSWORD     | ✅  |   ✅    |    example    | example                                 | Value for setting about `User Password` of `DB` to connect.                                                              |

### Simple test

Open `./test/index.html` via a web browser like Chrome and added some functions for a simple test.

#### Priorities

In the local environment, Storage Service should be launched in port number 3004 and OAuth Server should be connected in port number 3001. (Including Gin)

#### How to test

1. Select the server you want to test and check the login function by login test.
2. Send a request after uploading the file. Detail information is printed log in below and the file_id input field is filled automatically when you succeed.
3. File information, deleting, downloading images, etc like a spec of server can be requested easily.
