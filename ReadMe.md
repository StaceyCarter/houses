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
