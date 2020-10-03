run:
	pipenv run python -m goat_tweet_analyzer

build-image:
	docker build -t goat-twitter-analyzer .

run-docker:
	docker run -d goat-twitter-analyzer

deploy:
	@make build-image
	@make run-docker

