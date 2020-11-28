# Set up

- Needs a psql db called "houses" set up.
- Set up virtual env `python3 -m venv env`
- Activate env: `source env/bin/activate`
- Install packages with: `pip install -r requirements.txt`

# Test

- `cd <root dir of project> && python3 -m pytest tests` <- Use this to make sure the relative imports work.

Alternatively there's also a hack directly in the test script too so you can run it normally if you want to.

# Run

To run the script, cd to the root directory and do one of the following options:

- `python3 main.py` - will collect & dump data from yesterday
- `python3 main.py --date <date you want>` - get data from a specific date. Date is in format yyyy-mm-dd (you can also see this info by doing `python3 main.py --help`)

# AWS stuff

- Connect to psql with: `sudo -u postgres psql`
- To connect to remote psql db running on ec2:
  Need to set up host config in ~/.ssh/config with the public address, user and point to the secret key file.

Users:
postgres password = postgres
ec2-user password = ec2user

If we need to make changes to postgres permissions they live in:

- `/var/lib/pgsql/data/pg_hba.conf`
- `/var/lib/pgsql/data/postgresql.conf`

eg.

```
Host ec2-houses
  HostName ec2-18-191-15-163.us-east-2.compute.amazonaws.com
  StrictHostKeyChecking No
  User ec2-user
  IdentityFile ~/.ssh/stacey_mac.pem

```

```
# Setup the ssh tunnel to the db & leave this running in a different tab.
ssh -v ec2-houses -L 5432:127.0.0.1:5432

# Connect to the db through the runnel in a different tab with:
psql postgresql://ec2-user:ec2user@localhost:5432/houses
```
