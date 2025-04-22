# Sonar scanner testing

This repository contains code sample in Python to validate SonarSource code scanner, with known problems.

## Demo

To run the application server, execute:

```shell
docker compose up
```

To hammer the server and generate an OOM:

```shell
while curl http://localhost:5000/\?event\=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c64;echo;) ; do echo "."; done
```

_Need to find another `uuidgen` command._

## Sonar scan

```shell
uv run pysonar-scanner
```

## Local admin account

`E_FD7hytFTom-qO8mL-xwDZEXQVdB8EA`
