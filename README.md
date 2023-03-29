# ECOIN_Project
## Bootcamp Zero KeepCoding final project.

AppWeb of balance of income and expenese of crypto with Flask, API and JS.

## User laucnch

1. Create a virtual environment

    ```Shell
    # Windows
    python -m venv env

    # Mac / Linux
    python3 -m venv env
    ```

2. Activate the virtual environment

    ```Shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate
    ```

3. Install dependencies

    ```Shell
    pip install -r requirements.txt
    ```

4. Make a copy of the file `.env_template` as `.env`

    ```Shell
    # Windows
    copy .env_template .env

    # Mac / Linux
    cp .env_template .env
    ```

5. Edit the file `.env` and change the necesary environment values. For security reasons, leave the variable `DEBUG` as False.

6. Make a copy of the file `config_sample.py` as `config.py`

    ```shell
    # Windows
    copy config_sample.py config.py

    # Mac / Linux
    cp config_sample.py config.py
    ```

7. Edit the `config.py` file and change the `SECRET_KEY` value.

8. With the virtual environment active, launch the app.

    ```Shell
    flask run
    ```

## Launch as a dev.
1. Create virtual environment

    ```Shell
    # Windows
    python -m venv env

    # Mac / Linux
    python3 -m venv env
    ```

2. Activate virtual environment
    ```Shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate
    ```

3. Install dependencies
    ```Shell
    pip install -r requirements.dev.txt
    ```

4. Make a copy of the file `.env_template` as `.env`

    ```shell
    # Windows
    copy .env_template .env

    # Mac / Linux
    cp .env_template .env
    ```

5. Edit the `.env` file and change (or not) the value of `DEBUG` (True/False)

6. Make a copy of the file `config_sample.py` as `config.py`

    ```shell
    # Windows
    copy config_sample.py config.py

    # Mac / Linux
    cp config_sample.py config.py
    ```

7. Edit the `config.py` file and change the `SECRET_KEY` value.