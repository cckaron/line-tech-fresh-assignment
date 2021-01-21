import os
import json
#line api
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, MessageAction

project_folder = os.path.dirname(os.path.abspath(__file__))

class helper:
    def __init__(self, line_bot_api):
        self.line_bot_api = line_bot_api

    def flushAllRichMenuThenCreateOne(self):
        #flush all existing menu
        rich_menu_list = self.line_bot_api.get_rich_menu_list()
        for rich_menu in rich_menu_list:
            self.line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
            print("old rich menu has deleted")

        #create default menu
        rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=1200, height=810),
        selected=True,
        name="Default menu",
        chat_bar_text="Tap here",
        areas=[
            RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=400, height=405),
            action=MessageAction(label='about_me', text='About me')),
            RichMenuArea(
            bounds=RichMenuBounds(x=400, y=0, width=400, height=405),
            action=MessageAction(label='leadership', text='Leadership')),
            RichMenuArea(
            bounds=RichMenuBounds(x=800, y=0, width=400, height=405),
            action=MessageAction(label='side_projects', text='Side Projects')),
            RichMenuArea(
            bounds=RichMenuBounds(x=0, y=405, width=400, height=405),
            action=MessageAction(label='contest_and_awards', text='Contests and Awards')),
            RichMenuArea(
            bounds=RichMenuBounds(x=400, y=405, width=400, height=405),
            action=MessageAction(label='work_experience', text='Work Experience')),
            RichMenuArea(
            bounds=RichMenuBounds(x=800, y=405, width=400, height=405),
            action=MessageAction(label='skillsets', text='Skillsets'))]
        )
        
        rich_menu_id = self.line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
        print("rich menu id:"+rich_menu_id)

        #upload image for menu
        with open(os.path.join(os.path.join(os.path.join(project_folder, 'assets'), 'image'), 'rich_menu.png'), 'rb') as f:
            self.line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)  
        print("successfully upload image")

        self.line_bot_api.set_default_rich_menu(rich_menu_id)
