--- git clone code
git clone git@github.com:shreyashankar/gpt3-sandbox.git
mv                                     gpt3-sandbox/ shreyashankar--gpt3-sandbox
cd shreyashankar--gpt3-sandbox/                    # shreyashankar--gpt3-sandbox/

------

--- get :python3 3.9.x via pyenv
pyenv install 3.9 ; pyenv local 3.9

--- get pipenv latest of current :python3
python3 -m ensurepip --upgrade
python3 -m       pip install --upgrade pipenv

--- install python pkg w/ pipenv
python3 -m pipenv install -r api/requirements.txt  # should fail; but we get generated Pipfile
    : make packages in Pipfile to have version = "*" eg flask = "*"
    python3 -m pipenv install  # reinstall again this time w/ Pipfile all "*"

python3 -V ; python3 -m pipenv --venv  # should see 3.9.16 ; .../.venv

------

--- get :node v19.4 via nvm
nvm install v19.4
nvm use v19.4

--- get yarn of chosen :node
npm install -g yarn

--- install nodejs pkg w/ yarn
yarn install

------

--- openai secret
echo 'OPENAI_KEY=yoursecret' > openai.cfg
export     OPENAI_CONFIG=`pwd`/openai.cfg

--- run sample app
PYTHONPATH=`pwd` python3 -m pipenv run  python examples/run_latex_app.py

NOTE may get this error
    Error: error:0308010C:digital envelope routines::unsupported
    ...
    at /home/namgivu/code/l/gpt3_sql/shreyashankar--gpt3-sandbox/node_modules/babel-loader/lib/index.js:59:103 {
      opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
      library: 'digital envelope routines',
      reason: 'unsupported',
      code: 'ERR_OSSL_EVP_UNSUPPORTED'
    }
fix by  ref. https://stackoverflow.com/a/69746937
export NODE_OPTIONS=--openssl-legacy-provider

== final run sample
NODE_OPTIONS=--openssl-legacy-provider \
OPENAI_CONFIG=`pwd`/openai.cfg \
PYTHONPATH=`pwd` python3 -m pipenv run \
  python examples/run_latex_app.py


FIXME progress now
[2023-03-14 12:47:21,711] ERROR in app: Exception on /translate [POST]
Traceback (most recent call last):
  File "/home/namgivu/code/l/gpt3_sql/shreyashankar--gpt3-sandbox/.venv/lib/python3.9/site-packages/flask/app.py", line 2528, in wsgi_app
    response = self.full_dispatch_request()

--- about sample examples/run_latex_app.py
in docstring in the code
