cm selenoid stop
cm selenoid start --browsers 'firefox:78.4;chrome:86.0'
rm debug22.log
pytest --browser chrome
pytest --browser firefox
