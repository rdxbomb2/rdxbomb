import os
import argparse

# Create the parser
my_parser = argparse.ArgumentParser(description='user pass and api token')

# Add the arguments
my_parser.add_argument('user', metavar='user',type=str, help='user')
# my_parser.add_argument('pass', metavar='pass',type=str, help='pass')
my_parser.add_argument('api_token', metavar='api_token',type=str, help='api_token')



# Execute the parse_args() method
args = my_parser.parse_args()

username = args.user
api_token = args.api_token


os.system("cd rdxbomber")
os.system("rm .git -rf")
os.system("dir")


# os.environ["HEROKU_API_KEY"] = api_token
# os.environ["GOOGLE_CHROME_BIN"] = r"/app/.apt/usr/bin/google-chrome"
# os.environ["CHROMEDRIVER_PATH"] = r"/app/.chromedriver/bin/chromedriver"
#
# os.system(f"heroku create {username}rdxbomber0")
#
# os.system(f"heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome -a {username}rdxbomber0")
# os.system(f"heroku buildpacks:add heroku/python -a {username}rdxbomber0")
# os.system(f"heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a {username}rdxbomber0")
#
#
# os.system('git config --global user.name "rdxbombauto"')
# os.system('git config --global user.email "rdxbombauto@gmail.com"')
# os.system("git init")
# os.system(f"heroku git:remote -a {username}rdxbomber0")
# os.system("git add .")
# os.system('git commit -am "make it better"')
# os.system('git push heroku master')