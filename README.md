# Super-duper spam mailing
- This is a spam mailing with unlimited possibility to specify mails, with possibility to specify text header, text, bases with mails, etc.

## How to install
- Download the repository from the git hub:

```
https://github.com/Elkarapuzik/MAILS-spam-bot-PYTHON
```

- Python3 should already be installed. Then use pip(or pip3 if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
``` 
## Prepare to run
- Go to your email, open settings and in the settings get the application password or authentication password(token)
- Create `.env` file in the program folder
- The `.env` file should have the following form:
```
LOGIN=login from mail
PASSWORD=your token or application password
```
- Next, you should create a file with mails in the folder with the program in the following format
 `.json`, and also a file with mail in `.txt` format.

## How to run the program
- To run the program you need to enter in the command line:
```
python3 main.py --text "file_with_text" --emails "file_with_mails" --subject "subject_email"
```