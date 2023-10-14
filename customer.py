from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector as c
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

Window.size = (350, 580)

class Customer(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # Connect to the MySQL database
        database = c.connect(host="localhost", user="root", password="123456789", database="knock_app")
        cursor = database.cursor()

        user_data = locality_data = ''

        # Retrieve the data from the database
        v = "SELECT first_name, locality FROM customer where phone_no = 9305300206"
        cursor.execute(v)
        for row in cursor:
            user_data += str(row[0])
            locality_data += str(row[1])
            # for mare data use user_data += str(row[0]) + " " + str(row[1])

        # Assign the retrieved data to the app.data property
        self.data = user_data
        self.locality= locality_data

        # Load the Kivy file and return the screen manager
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("screens/customer.kv"))
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        return screen_manager

Customer().run()