#!/bin/bash

./manage.py sqlflush | ./manage.py dbshell
./manage.py migrate
./manage.py loaddata genesis_identity genesis_invite

#Genesis invite message
MESSAGE_FILE="./API/Mock/messages/7JDrh8YM1jYfPAdakw6sjoyFuFCcBo4fRKD9mK2FU6jy"
CONTENT="QgO46Himh8a5fLBmZ1ypILJN3e1Zxzgsd72imyvOr8qrQb6xZafKpztc9atwv8sQbpXjLWzTIESpereGL2LQlYvdIkee226REmX3C8u02JH3gieNLSXGTrs0gIcHle/AYIgDxbmDqSpWX+QmY0YigffC/xw9exRnJVdakiHN6FEd2o1cF8nUzQP2d+H1WmowDE1qwB5QclGIblg8FPug81JntbHscnPI1RQpg7O+WkWKzI2tUR/11NZ1a+x6bSHOypInHMHNNzRfOhw9DxCXauBJg58wBWvLkL7mraSaUYI6OtCmMke3SboY3iYDavYRXaz6v/h3OUkq0r+kM8r7FZ+f0U9w39P7Zk7MJ9CVMA5KwZkaMeyeHpOMOasbu1azIshTKcmTSMbhofGX/Apa+NYKp+8bMukaQ6PTRhwnWb2NEG75n7DY090hZL2G45W4kie+zlzlfhu+g8Pn8UjMGg90OY7yqtyDrpiUPcxgiMLVSyIrNfTJ+uQpLXJFzZovcN9xJ6B/Nvb8g+V/GSmZ0GwHzS1lz5uvoTpDjgOj2gA5JC+ntejFcyTnXv9qBgLfY9TKHsNfCOlKxFHbbbEfDCpCCE9fXqX3qVp8ThD2+JLwvezICHuytL/bstyzGSN9CL+zyLaxfaglYcfzS3tIml9ebaGZjJISAlu7uNf0exXB/NumRPjpGNLt1TKcx5o1VClz67j5mPZJf7Ht7aftS+1U+EUGl8IWarK2DOsUBSiSjf2+NN2JK0iBzp30FtMyCvV19cdd1wiqT0KGyOZ9q7ozz1fzKmcyk2NnezAySIc="
echo "$CONTENT" > $MESSAGE_FILE