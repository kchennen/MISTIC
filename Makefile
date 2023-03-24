## .PHONY defines parts of the makefile that are not dependant on any specific file
## This is most often used to store functions
.PHONY = help activate init_venv develop

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

PROJECT_NAME = MISTIC
project_name = $(shell echo $(PROJECT_NAME) | tr A-Z a-z)
PROJECT_PATH = $(shell cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
ROOT_DATA_PATH = "$(PROJECT_PATH)/data"
DATA_DIRS := $(ROOT_DATA_PATH)/0_external $(ROOT_DATA_PATH)/1_raw $(ROOT_DATA_PATH)/3_processed


help:
	@python -c "import pyfiglet,termcolor; termcolor.cprint(text=pyfiglet.figlet_format(text='$(project_name)',font='standard'),color='magenta',attrs=['bold'],)"
	@echo "-----------------------------------HELP-----------------------------------"
	@echo "* init		- Initialize project running environment."
	@echo "* init_data	- Initialize project data repositories."
	@echo "* init_venv	- Initialize virtual environment."
	@echo "* activate	- Activate virtual environment."
	@echo "* develop	- Install application in dev mode."
	@echo "* install	- Install the package."
	@echo "--------------------------------------------------------------------------"


## init_data - Initialize project data repositories.
init_data:
	mkdir -p $(DATA_DIRS)

init: init_data
	python -m venv venv
	bash --rcfile "venv/bin/activate"

# Init virtual environment
init_venv:
	pip install --upgrade pip
	pip install -r requirements.txt

# Activate virtual environment
activate:
	@./bin/activate_venv.sh

# Install application in dev mode, i.e that updates with the code change without having to reinstall the package.
develop:
	pip install -e .


# Install the application
install:
	pip install .
