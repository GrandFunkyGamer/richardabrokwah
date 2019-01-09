PROJECT_ID:=richard-abrokwah
VERSION:=test

.PHONY: all
all: test

.PHONY: deploy
deploy:
	gcloud app deploy --project $(PROJECT_ID)

.PHONY: test
test:
	gcloud app deploy --no-promote --project $(PROJECT_ID) --version $(VERSION)

.PHONY: init
init:
	gcloud app create --project $(PROJECT_ID) --region us-central

.PHONY: browse
browse:
	gcloud app browse --project $(PROJECT_ID)