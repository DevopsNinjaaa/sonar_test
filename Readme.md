$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ pip3 install coverage
$ pip3 install pytest

* Method-1
	$ cd code
	$ coverage run -m pytest
	$ coverage report -m pytest *.py
	$ coverage xml *.py

* Method-1
	
	$ ls
		# code Readme.md
	$ coverage run -m pytest code/*.py
	$ coverage report -m pytest code/*.py
	$ coverage xml -m code/*.py
