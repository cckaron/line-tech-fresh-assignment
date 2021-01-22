from flask import Flask, request, abort
from config import Config as config
from messages.flex import flex
from helper import helper
import sys
import tempfile
import json
import os

# line api
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

# start web server
app = Flask(__name__)

# specify db config
app.config.from_object(config())

# specify path
project_folder = os.path.dirname(os.path.abspath(__file__))

# get line channel config
channel_secret = config.LINE_CHANNEL_SECRET
channel_access_token = config.LINE_CHANNEL_ACCESS_TOKEN

# Confirm configs
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

# chatbot init
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# init helper
helper = helper(line_bot_api)

# Create rich menu at the first time
# helper.flushAllRichMenuThenCreateOne()


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text == 'Quick' or text == 'quick':
        text_message = TextSendMessage(
            text='Hi, 我是Aaron, 感謝你的加入!\n請點擊選單取得更多資訊\n輸入"Quick"可以再次開啟快速回覆列表',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(
                    label='關於我', text='About me')),
                QuickReplyButton(action=MessageAction(
                    label='我的社群帳號', text='Social Networks'))
        ]))

        line_bot_api.reply_message(
                event.reply_token,
                text_message
        )
    elif text == 'About me':
        flexObj = flex("about_me")
        message = FlexSendMessage(
            alt_text="projects", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Leadership':
        flexObj = flex("leadership")
        message = FlexSendMessage(
            alt_text="leadership", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Side Projects':
        flexObj = flex("side_projects")
        message = FlexSendMessage(
            alt_text="side_projects", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Contests and Awards':
        flexObj = flex("contest_and_award")
        message = FlexSendMessage(
            alt_text="contest_and_award", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Work Experience':
        flexObj = flex("work_experience")
        message = FlexSendMessage(
            alt_text="work_experience", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Skillsets':
        flexObj = flex("skillsets")
        message = FlexSendMessage(
            alt_text="skillsets", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'Social Networks':
        flexObj = flex("social_networks")
        message = FlexSendMessage(
            alt_text="social_networks", contents=flexObj.readFile())
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    label = event.postback.label

@handler.add(FollowEvent)
def handle_join(event):
    print("follow")
    text_message = TextSendMessage(
        text='Hi, 我是Aaron, 感謝你的加入!\n請點擊選單取得更多資訊\n輸入"Quick"可以再次開啟快速回覆列表',
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(
                label='關於我', text='About me')),
            QuickReplyButton(action=MessageAction(
                label='我的社群帳號', text='Social Networks'))
    ]))

    line_bot_api.reply_message(
                event.reply_token,
                text_message
    )

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=True)
