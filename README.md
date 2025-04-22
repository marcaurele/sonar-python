# Sonar scanner testing

This repository contains code sample in Python to validate SonarSource code scanner, with known problems.

> [!NOTE]
> Secrets are only working on my local setup. You will have to generate new ones for:
>
> - SonarQube admin account
> - CLI API token which is set in `pyproject.toml`

## Demo

To run the application server and sonarqube, execute:

```shell
docker compose up
```

SonarQube interface is available at <http://localhost:9000/>.

To hammer the application endpoint and generate an OOM (the app is limited to 16MB):

```shell
while curl http://localhost:5000/\?event\=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c64;echo;) ; do echo "."; done
```

## Sonar scan

```shell
uv run pysonar-scanner
```

## Local admin account

`E_FD7hytFTom-qO8mL-xwDZEXQVdB8EA`
