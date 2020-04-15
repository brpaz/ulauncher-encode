import logging
import base64
import urllib
import html
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

class EncodeExtension(Extension):

    def __init__(self):
        logger.info('init Encoding Extension')
        super(EncodeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        if event.get_argument() is None:
        	return

        base64Text = base64.encodebytes(event.get_argument().encode()).decode("utf-8") 
        urlEncoded = urllib.parse.quote_plus(event.get_argument())

        htmlEncoded = html.escape(event.get_argument())
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=base64Text,
                                         description='Base64 Encoded',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(base64Text)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=urlEncoded,
                                         description='URL Encoded',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(urlEncoded)
                                        ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=htmlEncoded,
                                           description='HTML Encoded',
                                           highlightable=False,
                                           on_enter=CopyToClipboardAction(
                                               htmlEncoded)
                                           ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    EncodeExtension().run()
