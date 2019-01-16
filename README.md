SoSmart
=======

So Smart is a flask project inspired from this [reddit thread](https://www.reddit.com/r/Python/comments/aghpxp/riamsosmartpy/)
Implements a form for generating "I-am-so-smart" like sentences, using flask

Deployment without Docker
-------------------------

1. Requires Python3.7 so install Python3.7

2. Create a virtual environment inside your project

```bash
python3 -m venv venv
```

3. Activate the virtual environment

```bash
source ./venv/bin/activate
```

4. Install the requirements needed

```bash
pip install -r requirements.txt
```

5. Start the HTTP service `./run.sh`


Deployment with Docker
----------------------


1. Install [Docker](https://www.docker.com/).

2. Install [docker-compose](https://docs.docker.com/compose/install/).

3. Create a docker network

```bash
sudo docker network create so-smart-network
```

4. Create a docker network
```bash
sudo docker-compose up --build -d
```