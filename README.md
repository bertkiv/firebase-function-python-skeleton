# firebase-function-python-skeleton
Skeleton project of firebase function with python

### What included
- MyPy for python type checker
- Simple HTTP server with swagger for API documentation
- Various helpers scripts

## Requirements
- `python3.7`
- `setuptools`
- `gcloud` - https://cloud.google.com/sdk/docs/

## Installing
If you don't have `setuptools` installed
```bash
pip3 install setuptools
```

Open `scripts/deploy-prod` and change **{{YOUR PROJECT NAME}}** place holder to your project name.

Then
```bash
python3 setup.py install
```

## Developing
At root folder, run

```bash
start-dev
```

Then go to your favourite and navigate to http://127.0.0.1:5000

**port might be changed, please check in `flask` output**

also check this out https://cloud.google.com/functions/docs/concepts/python-runtime

## Testing
```bash
run-test
```

## Deploying
Run command below, you might need to do login to gcloud first with account that has access to your project.

```bash
deploy-prod
```
