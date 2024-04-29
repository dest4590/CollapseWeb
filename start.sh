screen -S "collapseweb" -d -m
screen -r "collapseweb" -X stuff $'python manage.py runserver --insecure\n'
echo Started CollapseWeb in dedicated screen
