# python_scripts

## Overview

This repository contains scripts for two tasks:

1. Fetching the data from an API endpoint and saving it to a CSV file.
2. Reading data from a CSV file and updating or creating records via a REST API endpoint.

## Prerequisites

. Ensure Python 3.x (python 3 or latest version) is installed on your system.

. Install the required Python libraries using pip:

   pip install requests or pip3 install requests

## Setup

## Task 1 Fetch data from an API endpoint and populates it into a CSV file

---

1. Clone this repository to your local machine

   git clone https://github.com/Fayaz1898/python_scripts.git

2. go to folder /python_scripts/task

3. For fetching data from an API endpoint and populates it into a CSV file run the following command

   python3 fetch_universities.py

## This will generate a .csv file with data fetched from the API.##

## Task 2 Reads data from a CSV file and updates it via a REST API endpoint

---

1. In same folder run update_universities.py by running below command

   python3 update_universities.py

## This will read the generated csv file which is mentioned in the script and update or add entries via a REST API endpoint if needed.And will fetch the data and print it to the console you can verify it by checking the csv file.
