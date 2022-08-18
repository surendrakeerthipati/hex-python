# serverless-python

poetry-pyenv project develops in hexagonal architecture style

pyenv - to manage python versions, 
poetry - dependency management

steps :

1.try to setup pyenv installation

once done with the installation, run below commands to make sure pyenv installed successfully:
  --> pyenv --version
  --> pyenv install -l (it will show all the available python versions for installation)
  --> now install python using pyenv
  example : pyenv install 3.10.2, then check below command
                                    --> python --version (now hopefully python installed)

2.install poetry 
  --> poetry --version
  --> poetry env use <python-version>
  now use this env based on project requirement
  
References for installation :
1. https://github.com/pyenv-win/pyenv-win#pyenv-for-windows
2. https://python-poetry.org/docs/

Executing the tests ::
  1.poetry run pytest 
  2.poetry run coverage run -m pytest

### SAM CLI Deployment

1. Install SAM CLI
2. `sam build`
3. `sam deploy`
4. To Delete - `sam delete`