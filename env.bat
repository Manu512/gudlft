@ECHO ON

SET FLASK_APP=server.py
SET PYTHONPATH=%cd%
SET COVERAGE_RCFILE=%PYTHONPATH%\tests\.coveragerc
SET LOCUST_LOCUSTFILE=%PYTHONPATH%\tests\locustfile.py