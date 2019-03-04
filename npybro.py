import npyscreen
import datetime
import threading
from time import sleep

class BroController(npyscreen.NPSAppManaged):
    """The controller makes sure to run forms. MAIN will be the first that runs"""
    def onStart(self):
        #npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.registerForm("MAIN", MainForm())

class MainForm(npyscreen.SplitForm):
    def create(self):
        self.name = "BroIRC"
        self.OK_BUTTON_TEXT = "Send"
        #self.new_menu(name="test") # must be npyscreen.FormWithMenus
        #self.chat = self.add(npyscreen.TitleText, name="Chat Widget")
        for i in range(1,18):
            exec('self.l'+str(i)+' = self.add(npyscreen.FixedText, value = "line '+str(i)+'")')
        #self.nextrely += 1 #increase space for the next element position
        self.draw_line_at = 20 # the position the line split should be drawn at
        self.nextrely = 21
        self.chatMessage = self.add(npyscreen.Textfield, value = "Enter here...")
        self.display()
        self.chatMessage.edit()
        #thread_time = threading.Thread(target=self.update_time,args=())
        #thread_time.daemon = True
        #thread_time.start()

    # def update_time(self):
    #     counter = 0
    #     while True:
    #        counter += 1
    #        exec('self.l'+str(counter)+'.value = "changed'+str(counter)+'"')
    #        self.display()
    #        sleep(1)

    def afterEditing(self):
        self.chatMessage.value = ""
        self.display()
        self.chatMessage.edit()
        #self.parentApp.setNextForm("MAIN")

    #def resize(self):
    #    print("just happened a resize")

    def set_value(self):
        return "Tom"

if __name__ == "__main__":
    App = BroController()
    App.run()
