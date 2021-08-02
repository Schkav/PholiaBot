# bot.py

import os
import random
import pycountry
from weapon_skills import WeaponSkills
from gacha import Gacha
from gwbox import GwBox
from dotenv import load_dotenv
from googletrans import Translator

# 1
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='%', case_insensitive=True)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='spark', help='Calculate spark')
async def spark(ctx, crystal=0, ten_draws=0, single_draw=0):
    crystal_rolls = crystal//300
    ten_draws_rolls = ten_draws * 10
    total_rolls = crystal_rolls + ten_draws_rolls + single_draw
    percentage = (total_rolls / 300) * 100
    response = "You have {} rolls available ({:.1f}% complete)".format(total_rolls, percentage)
    await ctx.send(response)


@bot.command(name='wepskill', help='Return values of weapon skills', aliases=['ws'])
async def wepskill(ctx, skill_type):
    weapon_skill = WeaponSkills()
    table = weapon_skill.get_table(skill_type)
    await ctx.send(table)


@bot.command(name='roll?', help='Return 50:50 yes or no')
async def roll(ctx):
    yes_or_no = ['Yes, YOLO!', 'No, save up', 'Yes, do a 10', 'No, not worth it']
    response = random.choice(yes_or_no)
    await ctx.send(response)


@bot.command(name='choice', help='Return random choice from input')
async def choice(ctx, *choices):
    choice_list = []
    for item in choices:
        choice_list.append(item)
    response = random.choice(choice_list).title()
    await ctx.send(response)


@bot.command(name='roll', help='Do a 10 roll and hope you get bol')
async def roll(ctx, *banners):
    message = []
    gacha = Gacha()
    gacha.set_pool(banners)
    results = gacha.get_ten()

    for draw in results:
        if draw in gacha.ssr_summon_pool:
            message.append("""```yaml
You got {}```""".format(*draw))

        elif draw in gacha.ssr_chara_pool or draw in gacha.limited_pool:
            message.append("""```yaml
You got the {}
{} joined your party!
```""".format(*draw))

        elif draw in gacha.sr_pool:
            message.append("""```You got {}```""".format(draw))

        else:
            message.append("""```brainfuck
You got {}```""".format(draw))

    await ctx.send(''.join(message))


@bot.command(name='rollspark', help='Do a 300 roll and hope you get your spark target')
async def rollspark(ctx, *banners):
    message = []
    gacha = Gacha()
    gacha.set_pool(banners)
    results = gacha.get_spark()

    message.append("""```css\n
You got {} SSR in 300 rolls
Including the following limiteds:```""".format(len(results)))

    for draw in results:
        if draw in gacha.limited_pool or draw in gacha.limited_pool:
            message.append("""```yaml
{}
```""".format(draw[1]))

    await ctx.send(''.join(message))


@bot.command(name='feedback', help='Send feedback or bug report message to bot owner', aliases=['bugreport'], pass_context=True)
async def feedback(ctx, *messages):
    feedback_message = " ".join(messages)
    response = """
Your feedback has been sent to Schkav#9999.
Thank you for your feedback!"""
    await bot.get_user(209998612594294784).send("{} from {}".format(feedback_message, ctx.message.author))
    await ctx.send(response)


@bot.command(name='player', help='Search for player by [ID]')
async def player(ctx, id):
    link = ["http://game.granbluefantasy.jp/#profile/", id]
    response = ''.join(link)
    await ctx.send(response)


@bot.command(name='crew', help='Search for crew by [ID]')
async def crew(ctx, id):
    link = ["http://game.granbluefantasy.jp/#guild/detail/", id]
    response = ''.join(link)
    await ctx.send(response)
    

@bot.command(name='translate', help='Translate [text] > [language]. Default is translate to English if without ">" sign', aliases=['tl'])
async def translate(ctx, *texts):
    translator = Translator()
    joined_text = " ".join(texts).lower()
    lan_choice = False
    for text in texts:
        if text.lower() == ">":
            lan_choice = True
    if lan_choice:
        split_text = joined_text.split('>')
        language_code = pycountry.languages.get(name=split_text[-1].strip())
        language = language_code.alpha_2
        if split_text[-1].strip().lower() == "chinese":
            language = "zh-CN"
        text_to_translate = split_text[0]
    else:
        language = "english"
        text_to_translate = joined_text
    translated_text = translator.translate(str(text_to_translate), dest=str(language))
    await ctx.send(translated_text.text)


@bot.command(name='gwbox', help='Calculate how many boxes you can open by [tokens]', aliases=['box'])
async def gwbox(ctx, tokens: int):
    box = GwBox()
    boxes_count = box.calculate_box(tokens)
    response = "You can open {} boxes with {} tokens left".format(boxes_count[0], boxes_count[1])
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send('Invalid parameters. See %help for correct parameters.')


bot.run(TOKEN)

