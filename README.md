# Django-docker-test-app

### Testing on Ubuntu 16.04, python 2.7
### How run app:
1. ```$ git clone https://github.com/AlexeyLog/Django-docker-test```
2. Install Docker - https://docs.docker.com/engine/installation/linux/ubuntulinux/
3. Install Docker Compose - https://docs.docker.com/compose/install/
4. run command ```$ docker-compose build``` (if get errors try with 'sudo')
5. run command ```$ docker-compose up```

### Setting
In settings.py set credentials:
1. GOOGLE_OAUTH2_CLIENT_ID 
2. GOOGLE_OAUTH2_CLIENT_SECRET