from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget

class MainApp(MDApp):
    def on_start(self):
        # Set colors
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '900'

        # Add messages
        self.new_message("ERIK SANDBERG", "Hello World", "woman.png")
        self.new_message("ERIK Danberg", "Hello World", "woman.png")
        self.new_message("Danny Erikberg", "Hello World", "woman.png")
        self.new_message("KivyMD NotSandberg", "Hello World", "woman.png")
        self.new_message("Whats App", "Hello World", "woman.png")
        self.new_message("Me Myself", "Hello World", "woman.png")
        self.new_message("Pewdiepie", "Hello World", "woman.png")

    def new_message(self, name, message, image_name):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(ImageLeftWidget(source=image_name))
        self.root.ids.list.add_widget(new_message)


    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        pass



class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''



MainApp().run()