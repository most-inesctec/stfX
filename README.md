# ___stfX_: A SpatioTemporal Features eXtractor__

Since this server was developed as a set of microservices, this microservices are added to this repository as sub-modules.

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
git pull --recurse-submodules
```

To add new submodules use the command:
```shell
git submodule add <submudole link>
```
