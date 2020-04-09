#!/bin/sh
cd core/stfXCore
./mvnw package && java -jar target/sftx-core.jar
cd ../..
docker-compose up