token:
	python3 generate.py --key=key.pem --issuer-id=$(ISSUER_ID) --username=$(YODLEE_USER) > user.jwt

stats: token
	python3 run.py
