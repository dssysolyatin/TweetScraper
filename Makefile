# $(call build_lamda_function,lambda_function_name)
#   Build lambda function.
define build_lamda_function
	mkdir -p build/$(1)/app
	pip install -r lambda/$(1)/requirements.txt -t build/$(1)
	cp lambda/$(1)/* build/$(1)/app
	cp -R twitter build/$(1)
endef

build: build_hashtag_tweets build_users_tweets

build_hashtag_tweets:
	$(call build_lamda_function,hashtag_tweets)

build_users_tweets:
	$(call build_lamda_function,users_tweets)

start_api: build
	sam local start-api

unit_tests:
	python -m unittest discover

.PHONY: build build_hashtag_tweets build_users_tweets start_api unit_tests