# Validation of _stfX_

The validation scripts assume the totality of the stfX environment is running locally, using the `docker-compose`.

Therefore, please do not forget to run `sh docker.sh` before proceeding with the validation.

However, to run the experiments that depends on a mock PSR service, you must run the application locally and run the mock server available in folder `/validation/psr-mock`. After, run `sh experiments_with_mock.sh` to run the experiments that support mock data.

# Contents

The main contents of the validation tests are: 

| Content | Responsibility |
|:-|:-|
| Resources | Directory containing the resources necessary for running the tests | 
| validate.py | ... |