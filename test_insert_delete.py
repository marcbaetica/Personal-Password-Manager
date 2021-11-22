import subprocess


subprocess.run('python --version')
# subprocess.run('python insert_credentials.py some_site_1 some_user_1 some_password_1 public_key')

subprocess.run('python retrieve_credentials.py some_site_1')
subprocess.run('python retrieve_credentials.py lalala')
