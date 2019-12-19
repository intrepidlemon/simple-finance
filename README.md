# simple finance

Personal tooling to figure out how much I'm spending per month, and how much to have ready in my checking account to pay off my statement balance each month.

I use a free trial developer account from [Yodlee](https://developer.yodlee.com/) to access my own personal credit card data.

## setup

- go to [Yodlee](https://developer.yodlee.com/) to get a developer account. The trial membership should be fine. Log on to your own personal credit card accounts through their portal. You should log in to all account under one user.
- install `requirements.txt` in a venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- set environment variables including ISSUER_ID, and YODLEE_USER (the assigned yodlee user name)
- save private key to `key.pem` file issued by Yodlee

## run
```bash
make stats
```
