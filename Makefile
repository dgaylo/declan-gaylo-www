PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/build
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PUBLISHCONF_DEV=$(BASEDIR)/publishconf_dev.py

ICON_SVG=$(INPUTDIR)/images/logo.svg

SSH_HOST=Scripts
SSH_PORT=22
SSH_USER=dgaylo
SSH_TARGET_DIR=~/web_scripts/home
SSH_TARGET_DIR_DEV=~/web_scripts/dev/home

DEV ?= 0
ifeq ($(DEV), 1)
	PUBLISHCONF=$(PUBLISHCONF_DEV)
	SSH_TARGET_DIR=$(SSH_TARGET_DIR_DEV)
endif

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make sftp_upload                    upload the web site via SFTP       '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -b 0.0.0.0

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
#	$(MAKE) purify
	$(MAKE) icons
	$(MAKE) $(OUTPUTDIR)/commit.txt

ssh_upload: publish
	if [ -f ~/.scripts/krbSetup_MIT ]; then  ~/.scripts/krbSetup_MIT; fi
	scp -P $(SSH_PORT) -r "$(OUTPUTDIR)"/* "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)"
sftp_upload: publish
	printf 'put -r $(OUTPUTDIR)/*' | sftp $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)


rsync_upload: publish
	if [ -f ~/.scripts/krbSetup_MIT ]; then  ~/.scripts/krbSetup_MIT; fi
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --include tags --cvs-exclude --delete "$(OUTPUTDIR)"/ "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)"


.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload

# icons
.PHONY: icons
icons: $(OUTPUTDIR)/icon-80.png $(OUTPUTDIR)/icon-120.png $(OUTPUTDIR)/icon-180.png  

$(OUTPUTDIR)/icon-%.png: $(ICON_SVG)
	convert -density 2400 -resize $*x$* $< -strip $@

# note the commit hash
.PHONY: $(OUTPUTDIR)/commit.txt

$(OUTPUTDIR)/commit.txt:
	python -c "import sys; import git; sys.stdout.write(git.Repo().head.object.hexsha)" >  $@

# run purify
.PHONY: purify
purify: $(OUTPUTDIR)/theme/css/style.min.css $(shell find $(OUTPUTDIR) -name '*.html') $(shell find $(OUTPUTDIR) -name '*.js')
	purifycss $^ -m -o $<
