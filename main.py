from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
import re
from vendor import *
import mysql.connector as c
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window


Window.size = (350, 580)

class ElementCard:
    string = StringProperty()

class LoginPage(MDApp):

    database = c.connect(host="localhost", user="root", password="123456789", database="knock_app")
    regex = r"\b(0|91)?[-\s]?[6-9][0-9]{9}\b"
    cursor = database.cursor()
    # data = area = l1 = l2 = l3 = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        
    def build(self):
        
        # Load the Kivy file and return the screen manager
        global screen_manager

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("screens/home-splash.kv"))
        screen_manager.add_widget(Builder.load_file("screens/home_page.kv"))
        screen_manager.add_widget(Builder.load_file("screens/login.kv"))
        screen_manager.add_widget(Builder.load_file("screens/register.kv"))
        screen_manager.add_widget(Builder.load_file("screens/reg_customer.kv"))
        screen_manager.add_widget(Builder.load_file("screens/reg_user.kv"))
        #screen_manager.add_widget(Builder.load_file("screens/customer.kv"))         
        screen_manager.add_widget(Builder.load_file("screens/vendor.kv"))
        
        return screen_manager

    def user_page(self,c):

        v = f"SELECT first_name, area, locality_1, locality_2, locality_3 FROM user where phone_no = {c.text}"
        c.text=''

        self.cursor.execute(v)
        for row in self.cursor:
            self.a += str(row[0])
            self.data += str(row[1])
            self.l1+= str(row[2])
            self.l2 += str(row[3])
            self.l3 += str(row[4])
            # for mare data use user_data += str(row[0]) + " " + str(row[1])

        # # Assign the retrieved data to the app.data property
        # self.data = user_data
        # self.area= area_data
        # self.l1 = locality_1
        # self.l2 = locality_2
        # self.l3 = locality_3

        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="If you want to send notification to customers then click on 'Send Notification' below, otherwise Click on 'Cancel'",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="SEND NOTIFICATION", on_release=lambda *args: self.do_something()
                    ),
                    MDFlatButton(
                        text="CANCEL", on_release = lambda *args: self.dialog.dismiss()
                    ),

                ],
            )
        self.dialog.open()

    def log_out(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="To Logout click on 'LOGOUT', otherwise Click on 'CANCEL'",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="LOGOUT", on_release=lambda *args: self.do_something()
                    ),
                    MDFlatButton(
                        text="CANCEL", on_release=lambda *args: self.dialog.dismiss()
                    ),

                ],
            )
        self.dialog.open()

    def do_something(self):
        name = self.dialog.content_cls.text
        print(f"Hello, {name}!")
        self.dialog.dismiss()


    # def authenticate_login(self, phone, password):
    #     self.cursor.execute(f"SELECT password FROM login WHERE phone = '{phone}'")
    #     result = self.cursor.fetchone()
    #
    #     if result is None:
    #         # phone number not found in database
    #         self.root.get_screen("login").ids.phone.error = True
    #         self.root.get_screen("login").ids.phone.helper_text = "Phone number not found"
    #         return
    #
    #     if result[0] != password:
    #         # password doesn't match
    #         self.root.get_screen("login").ids.password.error = True
    #         self.root.get_screen("login").ids.password_.helper_text = "Incorrect password"
    #         return


    def send_data(self, phone, password):

        if re.fullmatch(self.regex, phone.text):
            self.cursor.execute(f"insert into login values('{phone.text}','{password.text}')")
            self.database.commit()
            phone.text = ""
            password.text = ""
        else:
            print("Invalid Data")

    def recieve_data(self, phone, password):
        self.cursor.execute("select * from login")
        ph_list = []
        for i in self.cursor.fetchall():
            ph_list.append(i[0])
        if phone.text in ph_list and phone.text != "":
            self.cursor.execute(f"select password from login where phone = '{phone.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    print("you have successfully Logged In")
                else:
                    print("Incorrect password")
        else:
            print("Incorrect phone no.")

    def cust_info(self,a,b,c,d,e,f,g,h,i,j):

        v = self.cursor.execute(f"insert into customer values('{a.text}','{b.text}','{c.text}',"
                                f"'{d.text}','{e.text}','{f.text}','{g.text}','{h.text}','{i.text}','{j.text}')")
        a.text = b.text = c.text = d.text = e.text = f.text = g.text = h.text = i.text = j.text = ""
        self.database.commit()
        if v:
            print("data sent")
        else:
            print("Give all required data")

    def user_info(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
        v = self.cursor.execute(f"insert into user values('{a.text}','{b.text}','{c.text}',"
                                f"'{d.text}','{e.text}','{f.text}','{g.text}','{h.text}','{i.text}','{j.text}','{k.text}','{l.text}','{m.text}','{n.text}','{o.text}')")

        a.text = b.text = c.text = d.text = e.text = f.text = g.text = h.text = i.text = j.text = k.text = l.text = m.text = n.text = o.text = ""
        self.database.commit()
        if v:               
            print("data sent")
        else:
            print("error in sending data")

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        screen_manager.current = "main"

LoginPage().run()

