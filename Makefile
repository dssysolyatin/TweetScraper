# $(call build_lamda_function,lambda_function_function_name)
#   Build lambda_function_function function.
define build_lamda_function
	mkdir -p build/$(1)/app
	pip install -r lambda_function/$(1)/requirements.txt -t build/$(1)
	cp -R lambda_function/$(1)/* build/$(1)/app
	cp -R twitter build/$(1)
	cp -R lambda_helper build/$(1)
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