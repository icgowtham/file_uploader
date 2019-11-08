# File Uploader
* Python based application to upload a file to the server.

### Introduction
* `file_uploader` is a Python based application to upload a file to the server. The files having extension as `.txt` are supported. This can be changed by editing `webapp/config.py`.

### Technology
`file_uploader` is developed using Python 3 and makes use of:
* `Flask` - A Python based micro web framework. 
* `Bootstrap` - For rendering the components of the HTML page.

### Sample usage:
* On a terminal run the application:
```bash
$ python3 run.py
```
* Open a web browser and navigate to http://<your machine's ip>:5000.
    * For e.g., if the machine IP is 192.168.1.111, then type http://192.168.1.111:5000
    * NOTE: Ingress and egress traffic on port 5000 should be enabled to view the application.


### Development
Clone the git repo and follow the steps below on any linux  machine.

    git clone https://github.com/icgowtham/file_uploader.git
    cd file_uploader

Setup python virtual environment.

    make setup-env
    source env3/bin/activate


### Compliance

To validate compliance, complexity and coverage:

    make compliance <code_path>

