from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import customer

Window.size = (350, 580)
class LoginPage(MDApp):

    def build(self):


        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("home-splash.kv"))
        screen_manager.add_widget(Builder.load_file("home_page.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("reg_customer.kv"))
        cus = customer.customer_page()
        cus.next()
        cus.next1()
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.login, 3)


    def login(self, *args):
        screen_manager.current = "main"


if __name__ == "__main__":
    LoginPage().run()