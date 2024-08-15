# text-summarization-llm-app
License: (Apache 2.0), Copyright (C) 2024, Author Phil Chen (nethacker)

## Description

This repo is an example app showing text summarization leveraging <a href="https://mistral.ai/" target="_blank">Minstral Large model available from </a> <a href="https://aws.amazon.com/bedrock/" target="_blank">AWS Bedrock</a>. For the frontend UI <a href="https://streamlit.io/" target="_blank">Streamlit</a> is being used.

## Prerequisites

* <a href="https://aws.amazon.com" target="_blank"> Amazon Web Services Account</a>
* AWS CLI
* AWS user with Bedrock Access (Specifically Mistral-Large) see: <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html" target="_blank">Manage access to Amazon Bedrock foundation models</a>
* Python 3.8 or higher
* Anaconda or Miniconda installed for Local Setup
* Virtualenv for Server Setup

**Required Python Packages**

```
awscli
streamlit
boto3
```

## AWS Resource Cost

As with most AWS services you will incur costs for usage. 

* Pricing:
  * https://aws.amazon.com/bedrock/pricing/

## Local Setup

```
conda create -n "text-summarization-llm-app" python=3.11.0

git clone git@github.com:VSKIP/text-summarization-llm-app.git

cd text-summarization-llm-app

pip install -r requirements.txt
```

## Run Local Setup

To run text summarization leveraging AWS Bedrock (Mistral-Large)

```
streamlit run text-summarization-llm-app.py
```

You can reach the app at `http://localhost:8501/`

## EC2 Ubuntu Linux Instance Setup Steps
(assumes you have a ubuntu user with /home/ubuntu)

### Install some dependencies
```
sudo apt -y update

sudo apt -y install build-essential openssl

sudo apt -y install libpq-dev libssl-dev libffi-dev zlib1g-dev

sudo apt -y install python3-pip python3-dev

sudo apt -y install nginx

sudo apt -y install virtualenvwrapper
```

### Clone the GIT Repository
```
cd /home/ubuntu

git clone git@github.com:nethacker/text-summarization-llm-app.git
```

### Setup the Python Environment
```
virtualenv text-summarization-llm-app_env

source text-summarization-llm-app_env/bin/activate
```

### Install the Text Summarization LLM APP package dependencies
```
cd /home/ubuntu/text-summarization-llm-app

pip install -r requirements.txt
```

### Setup systemd to daemonize the Text Summarization LLM APP (Port 8080)
```
sudo cp systemd/text-summarization-llm-app.service /etc/systemd/system/

sudo systemctl start text-summarization-llm-app

sudo systemctl enable text-summarization-llm-app.service
```

### Install NGINX to help with connections (Port 80)
```
sudo vim /etc/nginx/sites-available/nginx_text-summarization-llm-app.conf

sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /etc/nginx/sites-available/nginx_text-summarization-llm-app.conf /etc/nginx/sites-enabled

sudo systemctl restart nginx
```
