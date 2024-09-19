[![Pylint](https://github.com/nethacker/text-summarization-llm-app/actions/workflows/pylint.yml/badge.svg)](https://github.com/nethacker/text-summarization-llm-app/actions/workflows/pylint.yml)
# Text Summarization LLM APP
* License: (MIT), Copyright (C) 2024, Author Phil Chen
  * This is a example application the author of this repository is not liable for damages or losses arising from your use or inability to use the code.

### Description

This repo is an example app showing text summarization leveraging <a href="https://mistral.ai/" target="_blank">Minstral Large model available from </a> <a href="https://aws.amazon.com/bedrock/" target="_blank">AWS Bedrock</a>. For the frontend UI <a href="https://streamlit.io/" target="_blank">Streamlit</a> is being used.

### Prerequisites for macOS local setup

* <a href="https://aws.amazon.com" target="_blank"> Amazon Web Services Account</a>
* AWS CLI <a href="https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html" target="_blank">installed</a>
* AWS CLI user with Bedrock Access (Specifically Mistral-Large) see: <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html" target="_blank">Manage access to Amazon Bedrock foundation models</a>
* Verified on Python 3.10, 3.11, 3.12
* Anaconda or Miniconda installed 
* AWS Default Region is set to us-east-1 you can change the region in the `text_summarization_llm_app.py` file under `region_name='us-east-1'`

### Prerequisites for EC2 Ubuntu Linux instance setup
* <a href="https://aws.amazon.com" target="_blank"> Amazon Web Services Account</a>
* Enable Amazon Bedrock Access (Specifically Mistral-Large) see: <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html" target="_blank">Manage access to  Amazon Bedrock foundation models</a>
* EC2 Instance Role with AmazonBedrockFullAccess Policy Attached (note you can make this more secure by making a custom policy)
* Verified on Python 3.10, 3.11, 3.12
* Verified on EC2 Instance Ubuntu 22.04 and Ubuntu 24.04
* Virtualenv
* AWS Default Region is set to us-east-1 you can change the region in the `text_summarization_llm_app.py` file under `region_name='us-east-1'`

### AWS Resource Cost

As with most AWS services you will incur costs for usage. 

* Pricing:
  * https://aws.amazon.com/bedrock/pricing/
  * https://aws.amazon.com/ec2/pricing/on-demand/

### macOS laptop local setup

```
conda create -n "text-summarization-llm-app" python=3.11.0

git clone git@github.com:nethacker/text-summarization-llm-app.git

cd text-summarization-llm-app

pip install -r requirements.txt
```

### Run macOS laptop local setup

To run text summarization leveraging AWS Bedrock (Mistral-Large)

```
streamlit run text_summarization_llm_app.py
```

You can reach the app at `http://localhost:8501/`

### EC2 Ubuntu linux instance setup steps
(assumes you have a ubuntu user with /home/ubuntu)

#### Install some dependencies
```
sudo apt -y update

sudo apt -y install build-essential openssl

sudo apt -y install libpq-dev libssl-dev libffi-dev zlib1g-dev

sudo apt -y install python3-pip python3-dev

sudo apt -y install nginx

sudo apt -y install virtualenvwrapper
```

#### Clone the GIT Repository
```
cd /home/ubuntu

git clone https://github.com/nethacker/text-summarization-llm-app.git
```

#### Setup the Python environment
```
virtualenv text-summarization-llm-app_env

source text-summarization-llm-app_env/bin/activate
```

#### Install the Text Summarization LLM application package dependencies
```
cd /home/ubuntu/text-summarization-llm-app

pip install -r requirements.txt
```

#### Setup systemd to daemonize the Text Summarization LLM application (Port 8080)
```
sudo cp systemd/text-summarization-llm-app.service /etc/systemd/system/

sudo systemctl start text-summarization-llm-app

sudo systemctl enable text-summarization-llm-app.service
```

#### Install NGINX to help scale and handle connections (Port 80)
```
sudo cp nginx/nginx_text-summarization-llm-app.conf /etc/nginx/sites-available/nginx_text-summarization-llm-app.conf

sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /etc/nginx/sites-available/nginx_text-summarization-llm-app.conf /etc/nginx/sites-enabled

sudo systemctl restart nginx
```

You can reach the app at `http://{yourhost}`.

### Notes

* Make sure to open up port 80 in your EC2 Security Group associated to the instance.
* For HTTPS (TLS) you can use AWS ALB or AWS CloudFront
* This application does not take into consideration security controls, that is your responsibility.
* Please read <a href="https://aws.amazon.com/bedrock/faqs/" target="_blank">Amazon Bedrock FAQ's</a> for general questions about AWS LLM resources used.
