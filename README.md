# Storage-service

Belf 서비스에서 사용되는 파일 등의 정적 데이터를 관리하는 서비스입니다.

1. 실제 파일 데이터가 저장되는 위치는 아래와 같습니다.
   1. 개발용
      1. Pycharm, Visual Studio Code: 개발 환경 디렉토리 내 upload 디랙토리
      2. docker: Docker container 에서 WORKING_DIR 으로 설정된 디렉토리 내부의 upload 디렉토리
   2. 서비스용
      1. K8S: Azure file service 내부

# Stack

1. **Python:v3.9(이상)**
2. Sanic web framework
3. Tortoise ORM
4. MySql:v5.7.16
5. VSCode
6. Pycharm
7. docker

> Belf 공식 개발 환경은 VSCode 이지만, 언어 특성상 편의를 위해 Pycharm을 사용 했습니다.
> VSCode 실행도 별 문제 없음을 확인 했습니다.
> 관련 내용은 빠른 시작 하위의 VSCode 부분을 참고하세요.
>
> 개발 OS로 Unix 계열인 MacOS, Linux 등을 추천하며 Windows 인 경우 WSL2 사용을 추천합니다.
>
> docker는 단순 테스트를 위한 Stack입니다. 실 서비스는 K8S 통해서 Azure 클라우드에서 제공됩니다.

# 빠른 시작

## 공통

1. Belf 개발용 DB 서비스를 Belf 프로젝트인 todo-service 에서 docker/mysql/README.md 파일을 참고해 구성한 다음 실행합니다.

> python3 명령어 실행 시 python 버전이 **python3.9** 이상인지 확인이 필요합니다.

## VSCode

1. storage-service 디렉토리를 열어줍니다.
2. python3 -m venv venv 명령어를 이용해 **python3.9** 가상 환경을 생성합니다.
3. 좌측의 벌레 모양 버튼을 눌러 디버깅 창으로 진입합니다.
4. Sanic:main.py 값을 드롭 박스에서 선택 후 상단의 초록 화살표 버튼을 클릭해 디버깅을 실행합니다.

> VSCode 터미널(쉘)에서 python --version 명령어로 python 버전을 확인하거나,
> 유닉스 계열의 OS 에서 which python 명령어를 시용해 2번에서 생성한 venv 경로가 정상적으로 잡히는지 확인이 가능합니다.
>
> 2번에서 venv 라는 이름으로 **python3.9** 가상 환경을 생성 한 경우 새로운 shell 창을 VSCode 내부에서 실행 했을 때 자동으로 python 명령어의 경로가
> venv 으로 잡힙니다. 관련 설정은 ./vscode/settings.json 내부에 존재합니다.
>
> VSCode 에서 3번의 디버깅 설정 관련 내용은 프로젝트 ./vscode/launch.json 내부에 존재합니다.
>
> 4번은 python main.py 명령어와 동일합니다.

## Pycharm

1. 프로젝트 디렉토리를 Pycharm을 사용해서 열어줍니다.
2. 상단 우측의 초록색 벌레 모양과 화살표 모양 좌측에 있는 프로젝트 시작 프리셋을 클릭 한 다음 Edit Configurations 내부로 들어갑니다.
3. script path 항목으로 storage-service 내부의 main.py 파일을 선택 해 줍니다.
4. Python interpreter 항목에 **python3.9** 이상의 python 인터프리터가 존재하지 않는 경우 Pycharm 기능을 사용해 생성 후 선택 합니다.
5. 실행 환경 설정 저장 후 해당 설정을 2번 프리셋 선택 창에서 선택 한 다음 상단 우측의 벌레 모양 아이콘을 클릭해서 디버깅 환경으로 진입합니다.

> Pycharm 개발 환경 상단의 View-Tool Windows-Python Console 을 클릭해서 python -version 등의 명령어로
> Pycharm 에서 인식한 python 버전 및 python 명령어 경로를 확인할 수 있습니다.

# 환경 변수

| Variable                    | dev | qa/prod |     Default     | Example                      | Usage                                                                                   |
| --------------------------- | :-: | :-----: | :-------------: | ---------------------------- | --------------------------------------------------------------------------------------- |
| STORAGE_SERVICE_APP_NAME    | ✅  |   ✅    | STORAGE_SERVICE | STORAGE_SERVICE              | storage service의 `Application Name` 을 설정하는 값입니다.                              |
| STORAGE_SERVICE_VERSION     | ✅  |   ✅    |       🤷‍♂️        | 0.1.1, 0.2.0                 | 실행 중인 storage service 서비스의 `Version`을 기입하는 값입니다.                       |
| STORAGE_SERVICE_HOST        | ✅  |   🚫    |    127.0.0.1    | www.belf-storage-service.xyz | storage service 서비스가 실행될 `IP` 혹은 `URL`을 설정하기 위한 값입니다.               |
| STORAGE_SERVICE_PORT        | ✅  |   🚫    |      3004       | 3004                         | storage service가 실행될 때 http 요청을 listen할 `Port`를 설정하기 위한 값입니다.       |
| STORAGE_SERVICE_SSL         | 🚫  |   🚫    |       ""        | ""                           | storage service가 실행될 때 `SSL` 설정을 위한 값입니다.(미사용)                         |
| STORAGE_SERVICE_ACCESS_LOG  | ✅  |   ✅    |      true       | true, false                  | storage service가 실행될 때 `Log` 사용 여부 설정을 위한 값입니다.                       |
| STORAGE_SERVICE_DB_HOST     | ✅  |   🚫    |    127.0.0.1    | 127.0.0.1                    | storage servicer가 실행될 때 접속할 `Master DB`의 `IP` 혹은 `URL` 설정을 위한 값입니다. |
| STORAGE_SERVICE_DB_PORT     | ✅  |   🚫    |      3306       | 3306                         | storage service가 실행될 때 접속할 `Master DB`의 `Port` 설정을 위한 값입니다.           |
| STORAGE_SERVICE_DB_NAME     | ✅  |   🚫    |      belf       | belf                         | storage service가 실행될 때 접속할 `DB`의 `DB Name` 설정을 위한 값입니다.               |
| STORAGE_SERVICE_DB_USER     | ✅  |   🚫    |      root       | root                         | storage service가 실행될 때 접속할 `DB`의 `User Name` 설정을 위한 값입니다.             |
| STORAGE_SERVICE_DB_PASSWORD | ✅  |   🚫    |     example     | example                      | storage service가 실행될 때 접속할 `DB`의 `User Password` 설정을 위한 값입니다.         |

# K8S 서비스 환경 구성

## Azure files 마운트

K8S 클러스터 내부에서 프로젝트가 실행되는 base directory 하위에 ./upload 폴더를 생성 후 이를 Azure와 mount 하면 됩니다.
예: ./upload/60d8e04e-38ef-4113-8fb9-322c9edb168b 형식으로 파일에 접근합니다.
