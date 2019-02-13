# Hedera

This is a minimalistic project that just has basic account features and a simple, static reader [or will—this is a work in progress].

For the full Scaife Viewer running the Perseus Digital Library in production, see <https://github.com/scaife-viewer/scaife-viewer>.

## Getting Started

```
npm install
pipenv run pip install pip==18.0
pipenv install
pipenv shell
./manage.py migrate
./manage.py loaddata sites cana livy tolstoy gnt80 morphgnt-lemmatization
npm start
```

Leave the first Terminal window (above) running. Open a second Terminal window and run:

```
cd <path to hedera>
pipenv shell
./manage.py runserver
```

Browse to http://localhost:8000/ or http://localhost:8000/read/1/
