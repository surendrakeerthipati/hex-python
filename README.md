# serverless-python

Full Explanation available here - https://medium.com/p/79eb05477a09

poetry-pyenv project develops in hexagonal architecture style

pyenv - to manage python versions,
poetry - dependency management

## Steps 

1. Setup `pyenv` 

once done with the installation, run below commands to make sure pyenv installed successfully:
  --> `pyenv --version`
  --> `pyenv install -l` (it will show all the available python versions for installation)
  --> now install python using pyenv
  example : `pyenv install 3.9.12`, then check below command
  --> `python --version` (now hopefully python installed)

2.install poetry
  --> `poetry --version`
  --> `poetry env use <python-version>`
  now use this env based on project requirement

References for installation :
1. https://github.com/pyenv-win/pyenv-win#pyenv-for-windows
2. https://python-poetry.org/docs/

Executing the tests ::
  1.`poetry run pytest`
  2.`poetry run coverage run -m pytest`
   for Test Reports : poetry run coverage report -m

pre-commit check ::
  1. `poetry run pre-commit run -a`

### Deploy & Test using SAM CLI:

1. [Install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
2. `sam build` - Build 
3. `sam deploy` - deploys to the AWS account configured 
4. To Delete the stack - `sam delete`

### Testing API app - 

1. Invoke the Rest API endpoint (output of the sam deploy command) - `<rest-api-endpoint>/weather-info?stateCd=CA`
2. Invoke the Event Handler using by posting the below event onto the Eventbdige `default` bus, this will write records into the dynamo-db
   ``` json
   {
        "version": "0",
        "id": "1a582f25-eaa6-2862-adc6-bf4014f78627",
        "detail-type": "Weather Alert",
        "source": "muthu",
        "account": "684805258957",
        "time": "2022-08-18T04:49:10Z",
        "region": "us-east-1",
        "resources": [],
        "detail": {
            "stateCd": "CA",
            "onset": "2022-08-17T14:00:00-07:00",
            "expires": "2022-08-18T08:00:00-07:00",
            "ends": "2022-08-18T08:00:00-07:00",
            "status": "Actual",
            "messageType": "Alert",
            "category": "Met",
            "severity": "Severe",
            "certainty": "Likely",
            "urgency": "Expected",
            "event": "Red Flag Warning",
            "sender": "w-nws.webmaster@noaa.gov",
            "senderName": "NWS Reno NV",
        },
    }
    ```

