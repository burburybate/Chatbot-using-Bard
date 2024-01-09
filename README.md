
# Purvi_Chatbot

For you to use it you must do the following

## Cloning and Intallation

1.)Creating a virtual environment and installing the dependancies 

```
python venv -m Venv_Name /pathofyourvenv
```
Venv_name can be like python 3.11 myChatbotEnvironment

Activate that venv in your editor like VsCode using this command

```
/pathofyourvenv/Scripts/Activate.ps1
```
Then install the dependancies using these commands

```
pip install bardapi
pip install tk
```

Also recommended to have a pythin version 3.6 and above

2.)Clone this github repo using the command

```
git clone https://github.com/burburybate/Chatbot-using-Bard
```

after this run the files 


## Token Collection

From token collection open 

```
bard.google.com
```
Press F12 function button on the keyboard and explore to

```
Application>Cookies>Copy tokens
```

Tokens to be copied are
``` 
__Secure-1PSID
__Secure-1PSIDCC
__Secure-1PSIDTS
```
Then paste them in the UI 

## Working of tkinterApp

There are blank spaces in the app for token to be pasted in. Press 'submit and next' to open the chatbot.
In the chatbot type your query in the space and press send. The Query will be answered by the chatbot acoordingly.
You can press the 'New Token' for changing of token as token keep changing after about 20 min.
In case of any kind of error it is expected to start over with new tokens.

## Requirements
python --version >= 3.6.13

tkinter library should be present in the venv

bardapi version >= 0.1.38 should be present in the venv

## Useful links

For bard related information
```
https://pypi.org/project/bardapi/
```

For Tkinter related information
```
https://www.geeksforgeeks.org/python-gui-tkinter/
```

You may have to signin/signup in some of links.