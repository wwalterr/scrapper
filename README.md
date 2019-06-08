### Scrapper

🏤 Scrapper that download CSV files using Selenium and Scrapy.

> Warning: A scrapper can break if the page (s) the scrapper is crawling has been changed. To update some selectors you can manually find the classes, ids, tags, etc; or use the [xPath Finder](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph) extension on Google Chrome, to easily find the xPath pattern

If this file it's not formated, try to open it using the [Slack Edit](https://stackedit.io/) or [Dillinger](https://dillinger.io/).

#### Setup

This tutorial assumes that the OS is based on Unix / Linux.

<details>
<summary>Google Chrome Drive</summary>
  
The Google Chrome drive is already present in this repository, but if you want to update the driver, follow this tutorial.

> The driver needs to match the browser version installed. If you want to run a specific version of Google Chrome, see [this](https://superuser.com/questions/936432/how-do-i-install-a-previous-version-of-chrome) thread

Open the [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and select the driver version you want to install, choose the OS and save the file in this repository.

```sh
# Unzip (apt install unzip) the driver
$ unzip driver-name

# Rename the driver
$ unzip driver-name chromedriver

# Grant the permissions to the driver
$ chmod a+x  chromedriver
```

Let the driver in the base of this repository.
</details>

<details>
<summary>Python 3</summary>
  
Install the Python 3 interpreter:

```sh
# Add the Python PPA
$ sudo add-apt-repository ppa:deadsnakes/ppa

# Update the OS packages
$ sudo apt update

# Install the Python 3.6
$ sudo apt install python3.6
```
</details>

<details>
<summary>Pip 3</summary>
  
Install the Pip 3 package manager:

```sh
# Install the Pip 3
$ sudo apt -y install python3-pip

# Update the Pip 3
$ pip3 install --upgrade pip
```
</details>

<details>
<summary>Venv</summary>
  
Create a virtual environment to run the code:

```sh
# Create a virtual environment called venv based on Python 3.6 
$ python3.6 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Deactivate the virtual environment:

```sh
$ deactivate
```

Remove the virtual environment:

```sh
$ rm -rf venv
```
</details>

<details>
<summary>Dependencies</summary>
  
Install dependencies of this project, inside the virtual environment:

```sh
$ pip install -r requirements.txt
```

For more details of [Selenium](https://www.seleniumhq.org/docs/) and [Scrapy](https://docs.scrapy.org/en/latest/), check its documentations.
</details>

#### Run

To run the available scripts you need to be inside the virtual environment with all dependencies installed, you have this setup you can follow the next steps, otherwise go to the [setup](#setup) section.

> Before run the scripts, go to each one and change the data required, e.g username and password in the login.py and the query in the data.py

```sh
# Make login in the platform
$ scrapy runspider login.py

# Download CSV files from the platform / specific query
$ scrapy runspider login.py
```

Or run all the available scrappers through the *main.py* file.

```sh
# Run all scrappers
$ python main.py
```

See the [examples](./examples). For the *data.py*, read the [data.md](./data.md) documentation.

#### Debug

<details>
<summary>xPath</summary>
  
To check if a xPath pattern was found in a specific page, use the [XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)
</details>

<details>
<summary>Scrapy</summary>

There are a few ways to debug the Scrapy code:

- Shell

```sh
# Start a web page in the Scrapy interactive Shell
$ scrapy shell 'url'
```

This will return a `response` object, which you can do everything like if it was your real application.

```sh
# See the response body
>>> view(response)
```

This will open the `response` body in the browser.

- Log

```python
# Print messages inside a Scrapy class
self.log('message')
```

- IPDB

```python
import ipdb; ipdb.set_traec()
```

This will stop the execution and start a shell with all the variables and functions inside the Python import table.

- VSCode

You can also debug via VSCode debug, this is a great tool and offers a lot of functionalities.
</details>

#### Style Guide

This repository uses the [Auto PEP 8](https://github.com/hhatto/autopep8) tool that automatically formats Python code to conform to the PEP 8 style guide, along with the [Prettier](https://github.com/prettier/prettier-vscode) VSCode extenssion to format code, normally using auto PEP 8, [Pylint](https://www.pylint.org/) or [Yapf](https://github.com/google/yapf).

Consider to use the tools to maintain a concise code base.

#### Credits

Developed by [Sphinxs](https://github.com/Sphinxs).