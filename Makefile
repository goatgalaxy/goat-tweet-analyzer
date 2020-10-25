run:
	pipenv run python -m goat_tweet_analyzer

build-image:
	docker build -t goat-tweet-analyzer .

tag-image:
	docker tag goat-tweet-analyzer localhost:5000/goat-tweet-analyzer

push-image:
	docker push localhost:5000/goat-tweet-analyzer

run-docker:
	docker run -d goat-tweet-analyzer

deploy:
	@make build-image
	@make tag-image
	@make push-image
	kubectl apply -f deployment.yml --record

