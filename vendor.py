from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector as c
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

Window.size = (350, 580)

class Vendor(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.dialog = None

    def build(self):
        # Connect to the MySQL database
        database = c.connect(host="localhost", user="root", password="123456789", database="knock_app")
        cursor = database.cursor()

        user_data = area_data = locality_1 = locality_2 = locality_3 = ''

        # Retrieve the data from the database
        v = "SELECT first_name, area, locality_1, locality_2, locality_3 FROM user where phone_no = 9893380753"
        cursor.execute(v)
        for row in cursor:
            user_data += str(row[0])
            area_data += str(row[1])
            locality_1+= str(row[2])
            locality_2 += str(row[3])
            locality_3 += str(row[4])
            # for mare data use user_data += str(row[0]) + " " + str(row[1])

        # Assign the retrieved data to the app.data property
        self.data = user_data
        self.area= area_data
        self.l1 = locality_1
        self.l2 = locality_2
        self.l3 = locality_3

        # Load the Kivy file and return the screen manager
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("screens/vendor.kv"))
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        return screen_manager

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



