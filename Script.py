class script(object):
    START_TXT = """👋 Hey Welcome {},
My name is <a href=https://t.me/{}>{}</a> I am a Cinema World Auto Filter Bot with some more Features... 🌺

👉 Add me in a Your Group and promote me as Admin to let me get in action!

Press /help to see all the Commands and how they Work. Stay Safe & Enjoy!"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """◇ мʏ ɴᴀмᴇ : {}
◇ cʀᴇᴀтoʀ : <a href=https://t.me/Cinema_World_Owner>ʟᴀsιтн cнᴀмικᴀ</a>
◇ ʟιʙʀᴀʀʏ : ᴘʏʀoԍʀᴀм
◇ ʟᴀɴԍuᴀԍᴇ : ᴘʏтнoɴ 3
◇ ᴅᴀтᴀ ʙᴀsᴇ : мoɴԍo ᴅʙ
◇ ʙoт sᴇʀvᴇʀ : нᴇʀoκu
◇ ʙuιʟᴅ sтᴀтus : v1.0.2 [ ʙᴇтᴀ ]

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""



    PRIVATEBOT_TXT = """<b>𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙱𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄</b>
<b>›› 𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙰 𝙱𝙾𝚃 𝚂𝙰𝙼𝙴 𝙻𝙸𝙺𝙴 𝚃𝙷𝙸𝚂</b>
<b>›› 𝚆𝙸𝚃𝙷 𝙰𝙻𝙻 𝚈𝙾𝚄𝚁 𝙲𝚁𝙴𝙳𝙸𝚃𝚂</b>
<b>›› 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽𝙴𝚁𝚂𝙷𝙸𝙿</b>
<b>›› coɴтᴀcт мᴇ <a href=https://t.me/Cinema_World_Owner>ʟᴀsιтн cнᴀмικᴀ</a></b>"""

    SOURCE_TXT = """<b>Donation</b>>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

<b>━━━━━━━━━᚜ ᴘᴀʏмᴇɴт мᴇтнoᴅs ᚛━━━━━━━━━

◇ BANK ( ANY BANK )
◇ DIALOG
◇ MOBITEL
◇ GOOGLE PAY

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/Cinema_World_Owner><b>ʟᴀsιтн cнᴀмικᴀ</b></a> ᚛━━━━━━━━━━━━"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and Cinema World will respond whenever a keyword is found the Message

<b>⚠️️ NOTE:</b>
1. Cinema World should have admin Privillage.
2. Only admins can add filters in a Chat.
3. Alert buttons have a limit of 64 Characters.

<b>Commands and Usage:</b>
ᗚ /filter - <code>add a filter in chat</code>
ᗚ /filters - <code>list all the filters of a chat</code>
ᗚ /del - <code>delete a specific filter in chat</code>
ᗚ /delall - <code>delete the whole filters in a chat (chat owner only)</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline Buttons.

<b>⚠️️ NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is Mandatory.
2. Supports buttons with any telegram Media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Cinema_World_Sri_Lanka)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>⚠️️ NOTE:</b>
1. Make me the Admin of your Channel if It's Private.
2. Make sure that your Channel does not contains <b>Camrips, Porn and Fake Files.</b>
3. Forward the last message to me with Quotes.

I'll add all the files in that channel to My DB.

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for Managing Filters 
- It helps to avoid spamming in Groups.

<b>⚠️️ NOTE:</b>
1. Only admins can add a Connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ᗚ /connect  - <code>connect a particular chat to your PM</code>
ᗚ /disconnect  - <code>disconnect from a chat</code>
ᗚ /connections - <code>list all your connections</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>⚠️️ NOTE:</b>
These are the Extra Features.

<b>Commands and Usage:</b>
ᗚ /id - <code>get id of a specifed user.</code>
ᗚ /info  - <code>get information about a user.</code>
ᗚ /imdb  - <code>get the film information from IMDb source.</code>
ᗚ /search  - <code>get the film information from various sources.</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>⚠️️ NOTE:</b>
This module only works for Bot Creator.

<b>Commands and Usage:</b>
ᗚ /logs - <code>to get the rescent errors</code>
ᗚ /stats - <code>to get status of files in db.</code>
ᗚ /delete - <code>to delete a specific file from db.</code>
ᗚ /users - <code>to get list of my users and ids.</code>
ᗚ /chats - <code>to get list of the my chats and ids </code>
ᗚ /leave  - <code>to leave from a chat.</code>
ᗚ /disable  -  <code>do disable a chat.</code>
ᗚ /ban  - <code>to ban a user.</code>
ᗚ /unban  - <code>to unban a user.</code>
ᗚ /channel - <code>to get list of total connected channels</code>
ᗚ /broadcast - <code>to broadcast a message to all users</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    STATUS_TXT = """◇ тoтᴀʟ ғιʟᴇs : <code>{}</code>
◇ тoтᴀʟ usᴇʀs : <code>{}</code>
◇ тoтᴀʟ cнᴀтs : <code>{}</code>
◇ usᴇᴅ sтoʀᴀԍᴇ : <code>{}</code>
◇ ғʀᴇᴇ sтoʀᴀԍᴇ : <code>{}</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
◇ 𝐆𝐫𝐨𝐮𝐩 ›› {}(<code>{}</code>)
◇ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ›› <code>{}</code>
◇ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ›› {}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
◇ 𝐈𝐃 ›› <code>{}</code>
◇ 𝐍𝐚𝐦𝐞 ›› {}
"""
    CARBON_TXT = """Help: <b>Carbon Module</b>
    
- You can Beautify your Codes by using this Feature.

<b>⚠️️ NOTE:</b>
This Feature works on the Both Group & Bot PM.

<b>Commands and Usage:</b>
ᗚ /carbon - <code>reply to any text message.</code>

<b>Credits ››</b> <a href=https://t.me/Cinema_World_Sri_Lanka>Cinema-World</a></b>"""

