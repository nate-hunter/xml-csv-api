# API FOR A PROJECT TO CONVERT MULTIPLE XML FILES TO A CSV FILE

## TECHNOLOGY USED:
- Vagrant

### Setting up a Vagrant file and connecting to a Vagrant Box
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