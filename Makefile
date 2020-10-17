BUILD_DIR:=build
VENV:=${BUILD_DIR}/venv
PYTHON:=${VENV}/bin/python3
PIP:=${VENV}/bin/pip3

run: deps
	${PYTHON} -m src.stack

lint: deps
	${PYTHON} -m flake8 --exclude build/

test: deps
	${PYTHON} -m pytest tests/unit/ -s

clean:
	rm -rf ${BUILD_DIR}/
	find . -name "*.py[co]" -delete


venv:
	test -d ${VENV} || python3 -m venv ${VENV}/

deps:  venv requirements.txt
	${PIP} install -Ur requirements.txt