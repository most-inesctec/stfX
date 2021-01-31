# Validation of _stfX_

The purpose of the `/validation` subfolder is none other less than to validate the _stfX_, by containing all the necessary resources to run the experiments and recreate the results documented.

Some important nuances:
1. The validation scripts assume the totality of the stfX environment is running locally, using `docker-compose`.
2. Therefore, please do not forget to run `docker-compose up`, on stfX main folder, before proceeding with the validation.
3. However, to run the experiments that depend on the mock PSR service, you must run the `stfXCore` microservice in a standalone manner (e.g. using _IntelliJ_), and run the mock server available in folder `/validation/psr-mock` (you must not have the original `cpd-service` running, as both server - the mock and the original - run in the same port on localhost). Afterwards, run `sh experiments_with_mock.sh` to run the experiments that support mock data.
4. Before running the validations scripts, remember you have to install the requirements, available on the `/validation`folder, using `pip install -r requirements.txt`. It is suggested to first create a [virtual environment](https://docs.python.org/3/library/venv.html) and activate it.

<details>
<summary><code>utils/</code></summary>
  <br>
  Contains Metrics M1 and M2:
  <ul>
    <li><strong>M1</strong>
      <ul>
        <li>metric that consists of comparing the ground truth final representation with the representation obtained by applying the transformations outputted by the <em>stfX</em>. The goal is to identify if the transformations recognised by the <em>stfX</em> result in equivalent representations to the ground truth.
        </li>
      </ul>
    </li>
    <li><strong>M2</strong>
      <ul>
        <li>metric that consists of analysing the similarity between the set of transformations outputted by the tool and the ground truth transformations. The goal is to identify how similar are both sets of transformations and, therefore, how effective is the devised solution.</li>
      </ul>
    </li>
  </ul> 
</details>

<details>
<summary><code>experiment_mock.sh</code></summary>
  <br>
  This script is in charge of running the mock microservice that runs the algorithm point set registration.
</details>



<details>
  <summary><code>validate.py</code> & <code>validate_all.py</code></summary>
<br>
  <ul>
    <li>
      <code>validate.py</code> Script to validate a test-scenario the stfX tool. Usage:
      <code>

      usage: validate.py [-h] -d DIR [-e ENDPOINT]

      Script to validate a test-scenario the stfX tool.

      optional arguments:
        -h, --help            show this help message and exit
        -d DIR, --dir DIR     The directory containing the resources necessary for this test. The output is also written to
                              this directory, in file result.txt
        -e ENDPOINT, --endpoint ENDPOINT
                              The endpoint running stfX. Default is http://localhost:0080/stfx
  </code>
    </li>
    <li>
      <code>validate_all.py</code> Script to validate all the test-scenario, in the given directory, using the stfX tool. Usage:
      <code>

      usage: validate_all.py [-h] -d DIR [-o OUT_DIR] [-e ENDPOINT]

      Script to validate all the test-scenario, in the given directory, using the stfX tool.

      optional arguments:
        -h, --help            show this help message and exit
        -d DIR, --dir DIR     The directory containing the test-scenarios.
        -o OUT_DIR, --out_dir OUT_DIR
                              The directory where the output of the test-scenario will be written to. If the directory does
                              not exist, it is created. Defaults to './results'
        -e ENDPOINT, --endpoint ENDPOINT
                              The endpoint running stfX. Default is http://localhost:0080/stfx
  </code>
    </li>
  </ul>
</details>

<details>
  <summary><code>results/</code></summary>
  <br>
  Contains the results under the denomination <code><em><name_of_the_test></em>.json</code>. 
  <br><br>
  The json files have both the obtained results, the metric scores, and the differences between what was accomplish and what was expected for the M2 metric.
  <br>
  As for the files under the denomination <code><em><name_of_the_test></em>_m1.png</code>, they exhibit the representation of the <strong>convex hulls</strong> and the phenomena used in the M1 metric.
</details>

<details>
  <summary><code>psr-mock</code></summary>
  <br>
  Contains the imperative code to run the mock microservice.
</details>

<details>
  <summary><code>experiments</code></summary>
  <br>
  Encloses folders for each experiment. As for each experiment, it consists of:
  <ul>
    <li>
      <code>dataset.json</code>: the dataset that characterizes the spatiotemporal phenomena.
    </li>
    <li>
      <code>expected_result.json</code>: the expected result for the M2 metric (changes that effectively affect the phenomenon). 
    </li>
    <li>
      <code><em>name</em>.blend</code>: blender file used to create the experience (phenomenon + geometric transformations applied).
    </li>
    <li>
      <code>thresholds.json</code>: thresholds adopted for the detection of changes that affect the spatiotemporal phenomenon.
      <ul>
        <li>
          Sometimes it happens to exist more than one file for <code>thresholds.json</code> inside an experiment. This occurs because some experiments made with the same dataset adopt different thresholds so that the impact of bad and good thresholds in the quality of the results can be appraised.
        </li>
      </ul>
    </li>
  </ul>
</details>