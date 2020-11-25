## Set up

- Needs a psql db called "houses" set up.
- Set up virtual env `python3 -m venv env`
- Activate env: `source env/bin/activate`
- Install packages with: `pip install -r requirements.txt`

## Test

- `cd <root dir of project> && python3 -m pytest tests` <- Use this to make sure the relative imports work.
