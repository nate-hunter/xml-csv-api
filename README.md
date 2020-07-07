# API FOR A PROJECT TO CONVERT MULTIPLE XML FILES TO A CSV FILE

## TECHNOLOGY USED:
- Vagrant
- Python virtual environment (venv)
- Django
- Django Restframework

### To set up a Vagrant file and connect to a Vagrant Box:
In terminal:
```bash
	$ vagrant init ubuntu/bionic64
	$ vagrant up
	$ vagrant ssh		
```

### To test if Vagrant is synchronized with the project's folder:
In terminal:
```bash
	$ cd /vagrant
	$ touch test.py
```

In `test.py`:
```python
	print('...Test Python file in Vagrant Box...')
```

In terminal:
```bash
	$ python test.py
```

### To create a Python virtual environment:
In terminal, in `/vagrant`:
```bash
	$ python -m venv ~/env
	$ source ~/env/bin/activate
	=> (env) vagrant@ubuntu-bionic:/vagrant$
```

To deactivate the virtual environment:
```bash
	$ deactivate
```

### To install the project's packages:
In terminal:
```bash
	$ pip install -r requirements.txt
```

### To test Django server:
In terminal:
```bash
	$ python manage.py runserver 0.0.0.0:8000
```

### To run initial migrations in the project:
In terminal:
```bash
	$ python manage.py migrate
```


