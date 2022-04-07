from platform import platform
import random
import time
import os
import sys
import webbrowser

class computer():
    def __init__(self):
        self.on = True
        self.filecounter = 0
        #actions
        self.actions = {'oa': self.oa, 'ca': self.ca, 'exit': self.exit, 'help': self.help, 'search': self.search, 'note': self.note, 'of': self.of}
        #enter username
        # errors
        self.errors = {'usernametaken': '(error: username taken, enter a new username to continue)','applicationnotfound': '(error: application not found, enter a valid application name to continue)'}
        self.name = input("> Enter Username: ")
        self.name = self.name.capitalize()
        # if self.name is empty or a space, ask again
        while self.name == "" or self.name == " ":
            self.name = input("> Enter Username: ")
            self.name = self.name.capitalize()
        self.startup()

    #startup
    def startup(self):
        time.sleep(1)
        print('> Monkey Startup, booting...')
        time.sleep(1)
        print('> Booting complete.')
        time.sleep(1)
        print('> Welcome to Monkey Computer, ' + self.name + '.')
        self.main()

    def main(self):
        while self.on:
            self.action = input("> ")
            if self.action in self.actions:
                self.actions[self.action]()
            else:
                self.help()
              
    def oa(self):
        self.application = input("> Enter application name: ")
        os.system("open -a " + self.application)
        # if application is not found, ask again
        if self.application not in os.listdir():
            pass
    
    
    def ca(self):
        self.application = input("> Enter application name: ")
        os.system("osascript -e 'quit app \"" + self.application + "\"'")
        #if self.application is not open, print error
        while self.application not in platform():
            pass

    def exit(self):
        print('> Goodbye, ' + self.name + '.')
        time.sleep(1)
        # check if notepad file exists
        if self.filecounter == 1:
            os.remove('notepad.txt')
        else:
            pass
        sys.exit()
    
    def search(self):
        self.search = input("> Search: ")
        self.search.replace(" ", "+")
        # open google search
        webbrowser.open('https://www.google.com/search?q=' + self.search)
    
    def note(self):
        print('> Launching Notepad...')
        time.sleep(1)
        self.text = input('> Enter text: ')
        # save input to .txt file
        if self.filecounter == 0:
            print('> Saving file...')
            time.sleep(1)
            print('> File saved to notepad.txt.')
            with open('notepad.txt', 'w') as f:
                f.write(self.text)
                self.filecounter = 1
        elif self.filecounter == 1:
            print('> Warning: file already exists, if continued, file will be overwritten.')
            self.overwrite = input('> Continue? (y/n): ')
            if self.overwrite == 'y':
                print('> Saving file...')
                time.sleep(1)
                print('> File saved to notepad.txt.')
                with open('notepad.txt', 'w') as f:
                    f.write(self.text)
                    self.filecounter = 1
            elif self.overwrite == 'n':
                pass
            else:
                print('> Error: invalid input.')
                pass
    def of(self):
        self.openfile = input('> Enter the name of the file you want to open: ')
        # open the file
        with open(self.openfile, 'r') as f:
            print(f.read())
        # if file is not found, print error
        if self.openfile not in os.listdir():
            print('> Error: file not found.')
            pass
    def help(self):
        print('> Error: invalid input.')
        time.sleep(0.3)
        print('> oa: open application')
        time.sleep(0.3)
        print('> ca: close application')
        time.sleep(0.3)
        print('> note: write a notepad file')
        time.sleep(0.3)
        print('> of: open file')
        time.sleep(0.3)
        print('> exit: exit')
        time.sleep(0.3)
        print('> search: search')
        time.sleep(0.3)
        print('> help: show help')
        
computer()

if __name__ == '__main__':
    monkeycomputer = computer()