rm -f allu/*
pytest --alluredir=allu
allure serve allu
