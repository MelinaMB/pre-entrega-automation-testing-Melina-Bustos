import pytest
#va a tener los archivos de las pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito"
]

pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)