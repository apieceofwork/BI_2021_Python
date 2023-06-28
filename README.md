Hi there!
Welcome to my homework on virtual environments

## Here is the algorithm for running "pain.py"
Python version used: Python 3.11.3

OS version: MacOS Ventura 13.3.1

In my repository you will find a file called "requirements.txt". It contains all the packages needed for running the file — "pain.py"

**So, the steps are the following:**
1) Create and activate a new virtual environment by using conda or virtualenv:

*For virtualenv:*

- virtualenv (insert your virtual_env name)
- source virtual_env name/bin/activate

*For conda:*
- conda create --name (insert your virtual_env name)
- conda activate (insert your virtual_env name)

3) After you've activated your new virtual environment, you need to install all the packages listed in "requirements.txt"

*For virtualenv:*

run this command "pip install -r requirements.txt" 
   
*For conda:*

- while the command "pip install -r requirements.txt" usually works, conda doesn’t support this option directly

- Instead use this command: "while read requirement; do conda install --yes $requirement; done < requirements.txt"

It will install the needed packages in your virtual environment.

4) Now when the packages have been installed, you can run "pain.py"
   
Use this command: python pain.py

5) Great! Everything works! Here is the output of pain.py:
