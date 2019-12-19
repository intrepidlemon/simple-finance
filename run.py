import requests
import pprint
import datetime
import pandas

statements = "https://sandbox.api.yodlee.com/ysl/statements"
accounts = "https://sandbox.api.yodlee.com/ysl/accounts"

with open("user.jwt", "r") as f:
    jwt = f.read().strip()

headers = {
    "Api-version": "1.1",
    "Authorization": "Bearer {}".format(jwt),
}

statements_data = requests.get(statements, headers=headers).json().get('statement', list())
accounts_data = requests.get(accounts, headers=headers).json().get('account', list())

accounts_dict = dict()
for a in accounts_data:
    accounts_dict[a.get('id')] = dict(
            id=str(a.get('id')),
            provider=a.get('providerName'),
            name=a.get('accountName'),
            number=a.get('accountNumber'),
            total_balance=a.get('balance', dict()).get('amount', -1),
        )

statements_list = list()
for s in statements_data:
    statements_list.append(dict(
        date=datetime.datetime.strptime(s.get("statementDate", "1970-01-01"), "%Y-%m-%d"),
        **accounts_dict.get(s.get("accountId"), dict()),
        statement_balance=s.get("amountDue", dict()).get("amount"),
    ))

df = pandas.DataFrame(statements_list)
df = df[df.provider != "Dag Site"]

print(df.append(df.sum(numeric_only=True), ignore_index=True))
print("Over the past 30-day statement period, you have spent {} per day".format(df.statement_balance.sum()/30))
