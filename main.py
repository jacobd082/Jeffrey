import os
import discord
from keep_alive import keep_alive
import time


client = discord.Client()

sad_words = ["Kill my self", "suicide", "self harm", "hurt my self"]

myName = ["Jeffrey"]

no_no_word = ["fuck", "Fuck", "shit", "Shit", "bitch", "Bitch", "FUCK", "ass", "Ass", "ASS", "asshole", "Asshole", "ASSHOLE", "punch", "Punch", "PUNCH", "kill", "Kill", "KILL", "drugs", "Drugs", "DRUGS", "drug", "Drug", "DRUG", "BITCH", "SHIT", "bullshit", "Bullshit", "BULLSHIT", "dick", "Dick", "DICK", "dicks", "Dicks", "DICKS", "penis", "Penis", "PENIS", "pussy", "Pussy", "PUSSY", "vagina", "Vagina", "VAGINA", "Sex", "SEX", "faggot", "Faggot", "FAGGOT", "butt", "Butt", "BUTT", "cum", "Cum", "CUM", "cream", "Cream", "CREAM", "fuc", "a$$", "as$", "a$s", "FUC", "Porn", "porn", "PORN", "gayrate"]


iljy = ["I love Jeffrey"]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')
    print('Someone said hello!')

  if message.content.startswith('/how-is-it-going'):
    await message.channel.send('Is going good! beep bop boop beep!')
    print('Someone asked me how its going!')

  if message.content.startswith('/delete-this'):
    await message.channel.purge(limit=1)
    print('A person made me delete there message.')

  if message.content.startswith('/report-last'):
    await message.channel.purge(limit=2)
    print('A person made me delete the last message.')

  if message.content.startswith('/rules'):
    await message.channel.send('RULES:  1) No swearing.   2) No vilence    3) No harm to other users.   Most of these will be dectected by me and will be removed if not a Admin will remove it. If you are caught spaming or finding ways to avoid the word blocker, you will be banned.')
    print('A person asked for the rules.')

  if message.content.startswith('/about'):
    await message.channel.send('Hello! Im Jeffrey! Im a bot coded in Python by Jacob Drath! Heres my links: Website:https://sites.google.com/view/jeffrey-the-discord-bot   Privacy Policy: https://sites.google.com/view/jeffrey-the-discord-bot/privacy-policy     Currently Im Closed-Sourced. Ask my creater @jacobd082 for how to get me in your server!')
    print('A person asked for the about.')

  if message.content.startswith('/d'):
    await message.channel.purge(limit=2)
    print('A person made me delete the last message. (2)')

  if message.content.startswith('/ad10'):
    await message.channel.purge(limit=10)
    print('A person made me delete the last 10 messages.')

  if message.content.startswith('/c'):
    await message.channel.send('Heres my commands:  hello, how-is-it-going, delete-this, report-last, rules, about, c.')
    print('A person asked for help.')

  if message.content.startswith('/stay-awake'):
    await message.channel.purge(limit=1)
    print('ZZZZZZZ.... Im awake now')

  if message.content.startswith('/delete-my-data'):
    print('A DATA DELETION REQUSET HAS BEEN RECIVED.')
    await message.channel.send('Your data deletion request has been recived. Your data will be deleted in about 48 hours. The bot will remain working in this server.')
    

  msg = message.content

  if any(word in msg for word in sad_words):
    await message.channel.purge(limit=1)
    await message.channel.send('I sense harmfull words here. There is always someone willing to listen. Please call 800-273-8255 if you need to. :]')
    print('suicideal messages were found in chat.')

  if any(word in msg for word in myName):
    await message.channel.send('Hello! Did someone say my name?')
    print('Someone said my name!')

  if any(word in msg for word in iljy):
    await message.channel.send('Thanks!')
    print('Someone said they love me!')

  if any(word in msg for word in no_no_word):
    await message.channel.purge(limit=1)
    await message.channel.send('Inappropriate language has been detected. This type of language is not allowed under any circumstances.')
    print('A person swore in the chat')
    return

  
  Joke01 = ["/Joke:01"]
  if any(word in msg for word in Joke01):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!')
    await message.channel.send('What do you call a joke with no punchline?')
    time.sleep(5)
    await message.channel.send('This one!')
    print('I told them my punchline!')

  Joke02 = ["/Joke:02"]
  if any(word in msg for word in Joke02):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-02')
    await message.channel.send('What do you call a fake noodle?')
    time.sleep(5)
    await message.channel.send('IMPASTA')
    print('I told them my punchline!')

  Joke03 = ["/Joke:03"]
  if any(word in msg for word in Joke03):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-03')
    await message.channel.send('What did the grape do when he got stepped on?')
    time.sleep(5)
    await message.channel.send('He let out a little wine.')
    print('I told them my punchline!')

  Joke04 = ["/Joke:04"]
  if any(word in msg for word in Joke04):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-05')
    await message.channel.send('What do you call an elephant that doesnt matter?')
    time.sleep(5)
    await message.channel.send('An irrelephant.')
    print('I told them my punchline!')

  Joke05 = ["/Joke:05"]
  if any(word in msg for word in Joke05):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-05')
    await message.channel.send('I just watched a program about beavers.')
    time.sleep(5)
    await message.channel.send('It was the best dam program Ive ever seen.')
    print('I told them my punchline!')

  Joke06 = ["/Joke:06"]
  if any(word in msg for word in Joke06):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-06')
    await message.channel.send('How does a penguin build a house?')
    time.sleep(5)
    await message.channel.send('Igloos it together.')
    print('I told them my punchline!')

  Joke07 = ["/Joke:07"]
  if any(word in msg for word in Joke07):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-07')
    await message.channel.send('What do a tick and the Eiffel Tower have in common?')
    time.sleep(5)
    await message.channel.send('They are both Paris sites.')
    print('I told them my punchline!')


  Joke08 = ["/Joke:08"]
  if any(word in msg for word in Joke08):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-08')
    await message.channel.send('What do you call a fish wearing a bowtie?')
    time.sleep(5)
    await message.channel.send('So-fish-ticated')
    print('I told them my punchline!')

  Joke09 = ["/Joke:09"]
  if any(word in msg for word in Joke09):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-08')
    await message.channel.send('What did the janitor say when he jumped out of the closet?')
    time.sleep(5)
    await message.channel.send('Supplies!')
    print('I told them my punchline!')

  Joke10 = ["/Joke:10"]
  if any(word in msg for word in Joke10):
    await message.channel.send('Heres a joke!')
    print('A person asked for a joke!-08')
    await message.channel.send('What did one wall say to the other?')
    time.sleep(5)
    await message.channel.send('Ill meet you at the corner.')
    print('I told them my punchline!')
    time.sleep(10)
    await message.channel.send('You may notice I dont have that many jokes, give my creater jacobd082#8001 one to add.')

  

  #bot_test
  if message.content.startswith('/bot_test'):
    print('A bot test was requseted...')
    time.sleep(0.5)
    print('CTRL+C to stop...')
    time.sleep(0.5)
    print('Starting in 5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1.3)
    print('')
    print('')
    print('')
    print('A bot test has started...')
    await message.channel.send('A bot test has started.')
    print('Please wait...')
    time.sleep(10)
    print('Loading BOT_TEST_BOOT...')
    time.sleep(2)
    print('Finishing BOT_TEST_BOOT...')
    time.sleep(1)
    print('Installig BOT_TEST_BOOT...')
    time.sleep(3)
    print('Running BOT_TEST_BOOT...')
    time.sleep(4)
    print('Loading BOT_TEST_RUNNER...')
    time.sleep(2)
    print('Finishing BOT_TEST_RUNNER...')
    time.sleep(1.7)
    print('Installing BOT_TEST_RUNNER...')
    time.sleep(4.7)
    print('Running BOT_TEST_RUNNER...')
    time.sleep(9)
    print('BOT_TEST_RUNNER is being opened please wait..')
    time.sleep(13.9)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    time.sleep(1)
    print('running')
    time.sleep(27)
    print('BOT_TEST_DONE')
    await message.channel.send('The test is done! Veiw terminal for data!')
    time.sleep(3)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Loading BOT_TEST_DATA_END...')
    time.sleep(4)
    print('Finishing BOT_TEST_DATA_END...')
    time.sleep(1.2)
    print('Installig BOT_TEST_DATA_END...')
    time.sleep(5)
    print('Running BOT_TEST_DATA_END')
    time.sleep(2)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Loading...')
    time.sleep(18)
    print('___1___')
    print('200_RUN_c')



keep_alive()

client.run(os.environ['myKey'])