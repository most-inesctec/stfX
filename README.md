# ___stfX_: SpatioTemporal Features eXtractor__

The __SpatioTemporal Features eXtractor (_stfX_)__ is the prototype implementation of the conceptual framework detailed in chapter 4 of the __corresponding [thesis](docs/thesis.pdf)__.
Thus, the _stfX_ focuses on the quantification of the features of interest occurring over user-inputted spatiotemporal phenomena. The _stfX_ is capable of quantifying a subset of the spatiotemporal change features identified in the literature review, namely: translations, rotations, uniform scaling, changes of direction, moment in time and duration.


The SpatioTemporal Features eXtractor (_stfX_) is a server-side application utilising the microservices architectural approach, thus emphasising self-management, lightweightness, scalability, and autonomy.
In the _stfX_, each microservice represents a component responsible for the quantification of a given category of spatiotemporal change features.
The developed microservices were added to this repository as sub-modules.
Below we can visualise the _stfX_ current architecture:

<img width="702" alt="Screenshot 2020-07-31 at 18 27 18" src="https://user-images.githubusercontent.com/22712373/89060906-b9bedf00-d35b-11ea-92f2-f7dfa2b61a90.png">

The _stfX_'s API can be consulted in the __[corresponding Swagger](https://app.swaggerhub.com/apis-docs/EdgarACarneiro/thesis/2.1.1)__.

Chapter 5 of the __corresponding [thesis](docs/thesis.pdf)__ contains a more detailed description of the _stfX_.

# Functionalities

The current _stfX_ version supports the following functionalities:
- [x] Receives as input both the spatiotemporal dataset modelled as a sequence of temporal snapshots and the thresholds that express the end-user interests;
- [x] Extracts both the shapes and associated timestamps from each temporal snapshot;
- [x] For each temporal snapshot, quantifies the rigid transformations that occurred (translation, uniform scaling and rotation);
- [x] From the identified movement derived features, computes change of direction (the motive behind solely considering the change of direction is explained in section 5.2.2.1 in the __[thesis](docs/thesis.pdf)__);
- [x] Filters the identified spatiotemporal change features according to the user-inputted thresholds;
- [x] Computes, from the identified temporal features, duration and moment in time, even though no thresholds are provided for these features of interest;
- [x] Indexes the identified features of interest by temporal range.

# Repository Folder Overview

| __Folder__ | __Description__ |
|:-|:-|
| `/configs` | Contains necessary configurations for the deployment of the _stfX_. |
| `/core` | [Core microservice](https://github.com/EdgarACarneiro/stfXCore). |
| `/CPD-service` | [CPD microservice](https://github.com/EdgarACarneiro/CPD-service). The CPD is the used point set registration algorithm in this service. Represents the PSR service of the above figure. |
| `/docs` | Contains the associated documents, namely the corresponding __[thesis](docs/thesis.pdf)__. |
| `/PR-GLS-service` | Attempt of developing a microservice employing non-rigid registration. Ended up using the [CPD microservice](https://github.com/EdgarACarneiro/CPD-service). |
| `/swagger` | Contains the `json` file describing the [Swagger](https://app.swaggerhub.com/apis-docs/EdgarACarneiro/thesis/2.1.1) corresponding to the _stfX_. |
| `/utils` | Contains some utility python scripts, such as the parser of `.wkt`to `.json` and extracting the `.json` dataset from an animation modelled as a set of `.obj` files. |
| `/validation` | Contains the resources, the results, and the code necessary to validate the _stfX_. See chapter 6 of the corresponding __[thesis](docs/thesis.pdf)__ for more information. |

# Getting started

To download stfX with the latest micro-services versions run:
* As one step:
```shell
git clone --recursive https://github.com/EdgarACarneiro/stfX.git
```
* Two steps - first cloning repository and then updating sub-modules:
```shell
git clone https://github.com/EdgarACarneiro/stfX.git
git submodule update --init --recursive
```

To update the submodules use the command:
```shell
git submodule foreach git pull origin master
```

To add new submodules use the command:
```shell
git submodule add <submudole link>
```

To run the application, using Docker (one must have it installed), run:
```shell
docker-compose up
```
