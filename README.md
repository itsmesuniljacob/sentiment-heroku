# sentiment

Install Python 3 and PIP

## Step 1: Create Python 3.6 virtualenv
To use Flair you need Python 3.6. We will start by creating a Python 3.6 virtualenv

```
$ python3.6 -m venv pyeth
```
Next, we activate the virtualenv
```
$ source pyeth/bin/activate
```
Next, you can check Python version
```
(pyeth) $ python --version
Python 3.6.1
```
## Step 2: Install flair and flask package

```
pip install flair flask
```

Run
`python3 app.py`

Sample curl request

```
curl --request POST \
  --url http://localhost:5000/api/v1/analyzeSentiment \
  --header 'content-type: application/json' \
  --data '{
    "message":"I could watch The Marriage over and over again. At 90 minutes, it'\''s just so delightfully heartbreaking."
}'
```

