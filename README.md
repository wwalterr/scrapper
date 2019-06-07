### Scrapper

🏤 Scrapper that download CSV files using Selenium and Scrapy to run trough web pages, make login, open subpages, assign fields, etc.

> Warning: A scrapper can break if the page (s) the scrapper is crawling has been changed, for that its necessary to update some HTML element selector (s). To update some selectors you can manually find the classes, ids, tags, etc; or use the [xPath Finder](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph) extension on Google Chrome, to easily find the xPath pattern

#### Setup

This tutorial assumes that the OS is based on Unix / Linux.

<details>
<summary>Python 3</summary>
  
Install the Python 3 interpreter, to run the scripts present in repository:

```sh
# Add Python PPA
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
```
</details>

<details>
<summary>Venv</summary>
  
Create a virtual environment to run the code present in this repository in a sandbox:

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
</details>

#### Credits

Developed by [Sphinxs](https://github.com/Sphinxs).