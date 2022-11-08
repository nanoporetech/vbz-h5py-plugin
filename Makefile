SHELL = /bin/bash
PYTHON ?= python3.8

envDir = venv
envPrompt ?= "vbz"

.PHONY: clean update install wheel plugin venv

# Clean the python virtual environment
clean: 
	rm -rf ${envDir}

# Create a python virtual environment
venv:
	${PYTHON} -m venv ${envDir} --prompt=${envPrompt}

# install the python project in the current venv
update: 
	source ${envDir}/bin/activate \
	&& pip install --upgrade pip \
	&& pip install -e .[dev] \
	&& pre-commit install 

# Completely re-install the python environment for development
install: clean venv update
	@echo "To activate your new environment:  source ${envDir}/bin/activate"

# Build the python wheel for this project
wheel: venv update
	source ${envDir}/bin/activate \
	&& pip install --upgrade build \
	&& python -m build

	@echo "Build outputs in dist/"
