BASEDIR = $(shell pwd)
PROJECT_ID=$(shell gcloud config list project --format="value(core.project)")

image_repo_name := finetuned-bert-classifier
image_uri := gcr.io/${PROJECT_ID}/${image_repo_name}
image_tag := v0.1

REPOSITORY_NAME=

print:
	@echo "project_id: ${PROJECT_ID}"
	@echo "image_repo_name: ${image_repo_name}"
	@echo "image_uri: ${image_uri}:${image_tag}"

build:
	docker build -f Dockerfile -t "${image_uri}:${image_tag}" ../python_package

training:
	# When running with machine with GPUs, you can use --gpus all command line flag.
	@echo "Run the container locally in detached mode to test."
	docker run --gpus all -it --rm "${image_uri}:${image_tag}"

push:
	docker push "${image_uri}:${image_tag}" 
