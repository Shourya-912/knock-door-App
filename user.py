from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 580)

KVU = """
MDFloatLayout:
    MDCard:
        size_hint: .9, .9
        pos_hint: {'center_x':.5, 'center_y':.5}
        Carousel:
            id: slide
            MDFloatLayout:
                MDTextField:
                    hint_text:"First Name"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.57}
                MDTextField:
                    hint_text:"Last Name"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.46}
                MDTextField:
                    hint_text:"Aadhar No."
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.26}
                MDTextField:
                    hint_text:"Phone Number"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.36}

                MDRaisedButton:
                    text: "next"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.13}
                    on_release:
                        app.next()
            MDFloatLayout:

                MDTextField:
                    hint_text:"Goods/Services 1"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.57}
                MDTextField:
                    hint_text:"Goods/Services 2"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.46}
                MDTextField:
                    hint_text:"Goods/Services 3"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.36}
                MDTextField:
                    hint_text:"Goods/Services 4"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.26}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x:.39
                    pos_hint: {'center_x':.3, 'center_y':.15}
                    on_release: 
                        app.previous()
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x:.39
                    pos_hint: {'center_x':.7, 'center_y':.15}
                    on_release: 
                        app.next1()
            MDFloatLayout:

                MDTextField:
                    hint_text:"Locality"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.57}
                MDTextField:
                    hint_text:"Locality"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.46}
                MDTextField:
                    hint_text:"Locality"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.36}
                MDTextField:
                    hint_text:"Locality"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.26}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x:.39
                    pos_hint: {'center_x':.3, 'center_y':.15}
                    on_release: 
                        app.previous1()
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x:.39
                    pos_hint: {'center_x':.7, 'center_y':.15}
                    on_release: 
                        app.next2()
                        
            MDFloatLayout:

                MDTextField:
                    hint_text:"Password"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.57}
                    password: True
                MDTextField:
                    hint_text:"Confirm Password"
                    size_hint_x:.8
                    pos_hint: {'center_x':.5, 'center_y':.46}
                    password: True

                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x:.39
                    pos_hint: {'center_x':.3, 'center_y':.2}
                    on_release: 
                        app.previous2()

                MDRaisedButton:
                    text: "SUBMIT"
                    size_hint_x:.39
                    pos_hint: {'center_x':.7, 'center_y':.2}
                    on_release: 
                        app.submit()

    MDLabel:
        text: "Register as User"
        bold: True
        pos_hint: {'center_x':.75, 'center_y':.85}
        font_style:"H5"

    MDLabel:
        id: info
        text:"Information"
        pos_hint:{'center_x':.58, 'center_y':.7}
        font_size:"13sp"
        bold:True
        theme_text_color: "Custom"
    MDIconButton:
        id: icon
        icon:"numeric-1-circle"
        pos_hint:{'center_x':.18,'center_y':.65}
        user_font_size:"35sp"
        theme_text_color: "Custom"
    MDProgressBar:
        id: progress 
        size_hint:.12, .009
        pos_hint:{'center_x':.275,'center_y':.65}
    MDLabel:
        id: goods
        text:"Items"
        pos_hint:{'center_x':.83, 'center_y':.7}
        font_size:"13sp"
        bold:True
        theme_text_color: "Custom"
    MDIconButton:
        id: icon1
        icon:"numeric-2-circle"
        pos_hint:{'center_x':.37,'center_y':.65}
        user_font_size:"35sp"
        theme_text_color: "Custom"
    MDProgressBar:
        id: progress1 
        size_hint:.13, .009
        pos_hint:{'center_x':.47,'center_y':.65}
    MDLabel:
        id: local
        text:"Localities"
        pos_hint:{'center_x':.99, 'center_y':.7}
        font_size:"13sp"
        bold:True
        theme_text_color: "Custom"
    MDIconButton:
        id: icon2
        icon:"numeric-3-circle"
        pos_hint:{'center_x':.57,'center_y':.65}
        user_font_size:"35sp"
        theme_text_color: "Custom"
    MDProgressBar:
        id: progress2
        size_hint:.125, .009
        pos_hint:{'center_x':.67,'center_y':.65}
    MDLabel:
        id: finish
        text:"Finish"
        pos_hint:{'center_x':1.23, 'center_y':.7}
        font_size:"13sp"
        bold:True
        theme_text_color: "Custom"
    MDIconButton:
        id: icon3
        icon:"numeric-4-circle"
        pos_hint:{'center_x':.77,'center_y':.65}
        user_font_size:"35sp"
        theme_text_color: "Custom"


"""


class user(MDApp):

    def build(self):
        kv = Builder.load_string(KVU)
        return kv

    def next(self):
        self.root.get_screen('customer')..ids.slide.load_next(mode="next")
        self.root.get_screen('customer').ids.info.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.progress.value = 100
        self.root.get_screen('customer').ids.icon.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.icon.icon = "check-decagram"

    def next1(self):
        self.root.get_screen('customer').ids.slide.load_next(mode="next")
        self.root.get_screen('customer').ids.goods.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.progress1.value = 100
        self.root.get_screen('customer').ids.icon1.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.icon1.icon = "check-decagram"

    def next2(self):
        self.root.get_screen('customer').ids.slide.load_next(mode="next")
        self.root.get_screen('customer').ids.local.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.progress2.value = 100
        self.root.get_screen('customer').ids.icon2.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.icon2.icon = "check-decagram"

    def submit(self):
        self.root.get_screen('customer').ids.slide.load_next(mode="next")
        self.root.get_screen('customer').ids.finish.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.icon3.text_color = self.theme_cls.primary_color
        self.root.get_screen('customer').ids.icon3.icon = "check-decagram"

    def previous(self):
        self.root.get_screen('customer').ids.slide.load_previous()
        self.root.get_screen('customer').ids.info.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.icon.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.progress.value = 0
        self.root.get_screen('customer').ids.icon.icon = "numeric-1-circle"

    def previous1(self):
        self.root.get_screen('customer').ids.slide.load_previous()
        self.root.get_screen('customer').ids.goods.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.icon1.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.progress1.value = 0
        self.root.get_screen('customer').ids.icon1.icon = "numeric-2-circle"

    def previous2(self):
        self.root.get_screen('customer').ids.slide.load_previous()
        self.root.get_screen('customer').ids.local.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.icon2.text_color = 0, 0, 0, 1
        self.root.get_screen('customer').ids.progress2.value = 0
        self.root.get_screen('customer').ids.icon2.icon = "numeric-3-circle"


if __name__ == "__main__":
    user().run()