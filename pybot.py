from urllib.request import urlopen

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, Filters, MessageHandler, \
    CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, \
    BotCommand,bot,Bot
from datetime import datetime, timedelta, date, time
import  json, urllib
import requests


INPUT_TEXT = 0


def start(update, context):
    boton1 = InlineKeyboardButton(
        text='Rashid',
        callback_data='rashid')
    boton2 = InlineKeyboardButton(
        text='Share Exp',
        callback_data='share')
    boton3 = InlineKeyboardButton(
        text='Imbuements',
        callback_data='imbuements')
    boton4 = InlineKeyboardButton(
        text='1',
        url='www.tibia.com')
    boton5 = InlineKeyboardButton(
        text='2',
        url='www.tibia.com')
    boton6 = InlineKeyboardButton(
        text='3',
        url='www.tibia.com')
    # update.message.reply_text(f'Bienvenido Humano')

    update.message.reply_text(
        text='Selecciona una Opcion',
        reply_markup=InlineKeyboardMarkup([
            [boton1], [boton2],
            [boton3], [boton4],
            [boton5], [boton6]
        ])
    )



updater = Updater('1763562323:AAG2vkKIJXGMBo6koOWyaqQTbZ2ZCCWaeXk')


def guilds(update, context):
    update.message.reply_text('Probando funcionalidad del codigo QR')




def rashid(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('Con esto veremos donde esta Rashid el dia de hoy')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Con esto veremos donde esta Rashid el dia de hoy")


    hoy = datetime.today()
    #print (hoy)
    ayer = hoy - timedelta(hours=3)
    #print( ayer)
    hoy=hoy.strftime("%Y-%m-%d %H:%M:%S.%f")

    day = date.weekday(ayer)
    dia = day

    #print("el dia es: " + str(dia))

    if dia == 0:
        #print('hoy es Lunes, Rashid está en Svargrond')
        #update.message.reply_text('hoy es Lunes, Rashid está en Svargrond')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Lunes, Rashid está en Svargrond")
    elif dia == 1:
        #print('hoy es Martes, Rashid está en Liberty Bay')
        #update.message.reply_text('hoy es Martes, Rashid está en Liberty Bay')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Martes, Rashid está en Liberty Bay")
    elif dia == 2:
        #print('hoy es Miercoles, Rashid está en Port Hope')
        #update.message.reply_text('hoy es Miercoles, Rashid está en Port Hope')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Miercoles, Rashid está en Port Hope")
    elif dia == 3:
        #print('hoy es Jueves, Rashid está en Ankrahmun')
        #update.message.reply_text('hoy es Jueves, Rashid está en Ankrahmun')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Jueves, Rashid está en Ankrahmun")
    elif dia == 4:
        #print('hoy es Viernes, Rashid está en Darashia')
        #update.message.reply_text('hoy es Viernes, Rashid está en Darashia')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Viernes, Rashid está en Darashia")
    elif dia == 5:
        #print('hoy es Sabado, Rashid está en Edron')
        #update.message.reply_text('hoy es Sabado, Rashid está en Edron')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Sabado, Rashid está en Edron")
    elif dia == 6:
        #print('hoy es Domingo, Rashid está en Carlin')
        #update.message.reply_text('hoy es Domingo, Rashid está en Carlin')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Domingo, Rashid está en Carlin")
    else:
        print('error')


def rashid_callback(update, context):
    query = update.callback_query
    query.answer()

    hoy = datetime.today()
    # print (hoy)
    ayer = hoy - timedelta(hours=3)
    # print( ayer)
    # hoy=hoy.strftime("%Y-%m-%d %H:%M:%S.%f")

    day = date.weekday(ayer)
    dia = day

    # print("el dia es: " + str(dia))

    if dia == 0:
        # print('hoy es Lunes, Rashid está en Svargrond')
        # update.message.reply_text('hoy es Lunes, Rashid está en Svargrond')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Lunes, Rashid está en Svargrond")
    elif dia == 1:
        # print('hoy es Martes, Rashid está en Liberty Bay')
        # update.message.reply_text('hoy es Martes, Rashid está en Liberty Bay')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Martes, Rashid está en Liberty Bay")
    elif dia == 2:
        # print('hoy es Miercoles, Rashid está en Port Hope')
        # update.message.reply_text('hoy es Miercoles, Rashid está en Port Hope')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Miercoles, Rashid está en Port Hope")
    elif dia == 3:
        # print('hoy es Jueves, Rashid está en Ankrahmun')
        # update.message.reply_text('hoy es Jueves, Rashid está en Ankrahmun')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Jueves, Rashid está en Ankrahmun")
    elif dia == 4:
        # print('hoy es Viernes, Rashid está en Darashia')
        # update.message.reply_text('hoy es Viernes, Rashid está en Darashia')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Viernes, Rashid está en Darashia")
    elif dia == 5:
        # print('hoy es Sabado, Rashid está en Edron')
        # update.message.reply_text('hoy es Sabado, Rashid está en Edron')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Sabado, Rashid está en Edron")
    elif dia == 6:
        # print('hoy es Domingo, Rashid está en Carlin')
        # update.message.reply_text('hoy es Domingo, Rashid está en Carlin')
        context.bot.send_message(chat_id=update.effective_chat.id, text="hoy es Domingo, Rashid está en Carlin")
    else:
        print('error')


def share(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('Que nivel Eres?')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Que Nivel Eres ???")

    return INPUT_TEXT


def share_callback(update, context):
    query = update.callback_query
    query.answer()
    #query.edit_message_text(text='Que Nivel Eres ???')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Que Nivel Eres ???")
    return INPUT_TEXT


def calc_share(update, context):
    text = update.message.text


    lvl = int(text)
    print(lvl)

    lvlmax = 0
    lvlmin = 0

   # update.message.reply_text('Compartes Experiencia con')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Compartes Experiencia con :")

    lvlmax = (lvl / 2) * 3
    lvlmax = round(lvlmax)
    lvlmin = (lvl / 3) * 2
    lvlmin = round(lvlmin)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nivel Maximo :" + str(lvlmax))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nivel Minimo :" + str(lvlmin))
    #update.message.reply_text('Max: ' + str(lvlmax))
    #update.message.reply_text('Min: ' + str(lvlmin))
    print(lvlmin)
    print(lvlmax)

    return ConversationHandler.END



def strike(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('20 Protective charms\n25 Sabretooth\n5 Vexclaw Talon')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Protective charms, 25 Sabretooth, 5 Vexclaw Talon")

def void(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('25 rope belts\n25 silencer claws\n5 Grimeleech Wings')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 rope belts, 25 silencer claws, 5 Grimeleech Wings")

def vampire(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text('25 vampire teeth\n15 bloody pincers\n5 piece of death brains ')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 vampire teeth, 15 bloody pincers, 5 piece of death brains ")

def mort(update, context):
    #update.message.reply_text('25 Pile of Grave Earth + \n20 Demonic Skeletal Hands + \n5 Petrified Screams')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Pile of Grave Earth, 20 Demonic Skeletal Hands, 5 Petrified Screams")

def mort_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Pile of Grave Earth + \n20 Demonic Skeletal Hands + \n5 Petrified Screams')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Pile of Grave Earth, 20 Demonic Skeletal Hands, 5 Petrified Screams")

def protec_mort(update, context):
    #update.message.reply_text('25 Flask of Embalming Fluid + \n20 Gloom Wolf Furs + \n5 Mystical Hourglasses')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Flask of Embalming Fluid, 20 Gloom Wolf Furs, 5 Mystical Hourglasses")

def protec_mort_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Flask of Embalming Fluid + \n20 Gloom Wolf Furs + \n5 Mystical Hourglasses')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Flask of Embalming Fluid, 20 Gloom Wolf Furs, 5 Mystical Hourglasses")

def energy(update, context):
    #update.message.reply_text('25 Rorc Feathers + 5 Peacock Feather Fans + 1 Energy Vein')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Rorc Feathers + 5 Peacock Feather Fans + 1 Energy Vein")

def energy_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Rorc Feathers + 5 Peacock Feather Fans + 1 Energy Vein')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Rorc Feathers + 5 Peacock Feather Fans + 1 Energy Vein")


def protec_energy(update, context):
    #update.message.reply_text('20 Wyvern Talismans + 15 Crawler Head Platings + 10 Wyrm Scales')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Wyvern Talismans + 15 Crawler Head Platings + 10 Wyrm Scales")

def protec_energy_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Wyvern Talismans + 15 Crawler Head Platings + 10 Wyrm Scales')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Wyvern Talismans + 15 Crawler Head Platings + 10 Wyrm Scales")

def tera(update, context):
    #update.message.reply_text('25 Swamp Grasses + 20 Poisonous Slimes + 2 Slime Hearts')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Swamp Grasses + 20 Poisonous Slimes + 2 Slime Hearts")

def tera_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Swamp Grasses + 20 Poisonous Slimes + 2 Slime Hearts')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Swamp Grasses + 20 Poisonous Slimes + 2 Slime Hearts")

def protec_tera(update, context):
    #update.message.reply_text('25 Piece of Swampling Wood + 20 Snake Skins + 10 Brimstone Fangss')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Piece of Swampling Wood + 20 Snake Skins + 10 Brimstone Fangss")

def protec_tera_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Piece of Swampling Wood + 20 Snake Skins + 10 Brimstone Fangss')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Piece of Swampling Wood + 20 Snake Skins + 10 Brimstone Fangss")

def fire(update, context):
    #update.message.reply_text('25 Fiery Hearts + 5 Green Dragon Scales + 5 Demon Horns')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Piece of Swampling Wood + 20 Snake Skins + 10 Brimstone Fangss")

def fire_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Fiery Hearts + 5 Green Dragon Scales + 5 Demon Horns')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Fiery Hearts + 5 Green Dragon Scales + 5 Demon Horns")

def protec_fire(update, context):
    #update.message.reply_text('20 Green Dragon Leathers + 10 Blazing Bones + 5 Draken Sulphurs')
    context.bot.send_message(chat_id=update.effective_chat.id,text="20 Green Dragon Leathers + 10 Blazing Bones + 5 Draken Sulphurs")

def protec_fire_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Green Dragon Leathers + 10 Blazing Bones + 5 Draken Sulphurs')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Green Dragon Leathers + 10 Blazing Bones + 5 Draken Sulphurs")

def ice(update, context):
    #update.message.reply_text('25 Frosty Hearts + 10 Seacrest Hairs + 5 Polar Bear Paws')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Frosty Hearts + 10 Seacrest Hairs + 5 Polar Bear Paws")

def ice_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Frosty Hearts + 10 Seacrest Hairs + 5 Polar Bear Paws')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Frosty Hearts + 10 Seacrest Hairs + 5 Polar Bear Paws")

def protec_ice(update, context):
    #update.message.reply_text('25 Winter Wolf Furs + 15 Thick Furs + 10 Deepling Warts')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Winter Wolf Furs + 15 Thick Furs + 10 Deepling Warts")

def protec_ice_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Winter Wolf Furs + 15 Thick Furs + 10 Deepling Warts')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Winter Wolf Furs + 15 Thick Furs + 10 Deepling Warts")

def protec_holy(update, context):
    #update.message.reply_text('25 Cultish Robes + 25 Cultish Masks + 20 Hellspawn Tails')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Cultish Robes + 25 Cultish Masks + 20 Hellspawn Tails")

def protect_holly_callback(update,context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Cultish Robes + 25 Cultish Masks + 20 Hellspawn Tails')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Cultish Robes + 25 Cultish Masks + 20 Hellspawn Tails")

def club_skill(update, context):
    #update.message.reply_text('20 Cyclops Toe + 15 Ogre Nose Rings + 10 Warmasters Wristguards')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Cyclops Toe + 15 Ogre Nose Rings + 10 Warmasters Wristguards")

def club_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Cyclops Toe + 15 Ogre Nose Rings + 10 Warmasters Wristguards')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Cyclops Toe + 15 Ogre Nose Rings + 10 Warmasters Wristguards")

def axe_skill(update, context):
    #update.message.reply_text('20 Orc Tooth + 25 Battle Stones + 20 Moohtant Horns')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Orc Tooth + 25 Battle Stones + 20 Moohtant Horns")

def axe_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Orc Tooth + 25 Battle Stones + 20 Moohtant Horns')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Orc Tooth + 25 Battle Stones + 20 Moohtant Horns")

def sword_skill(update, context):
    #update.message.reply_text('25 Lions Mane + 25 Moohtah Shells + 5 War Crystals')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Lions Mane + 25 Moohtah Shells + 5 War Crystals")

def sword_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Lions Mane + 25 Moohtah Shells + 5 War Crystals')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Lions Mane + 25 Moohtah Shells + 5 War Crystals")

def shield_skill(update, context):
    #update.message.reply_text('20 Piece of Scarab Shell + 25 Brimstone Shells + 25 Frazzle Skins')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Piece of Scarab Shell + 25 Brimstone Shells + 25 Frazzle Skins")

def shield_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Piece of Scarab Shell + 25 Brimstone Shells + 25 Frazzle Skins')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Piece of Scarab Shell + 25 Brimstone Shells + 25 Frazzle Skins")

def magic_skill(update, context):
    #update.message.reply_text('25 Elvish Talismans + 15 Broken Shamanic Staffs + 15 Strand of Medusa Hair')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Elvish Talismans + 15 Broken Shamanic Staffs + 15 Strand of Medusa Hair")

def magic_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Elvish Talismans + 15 Broken Shamanic Staffs + 15 Strand of Medusa Hair')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Elvish Talismans + 15 Broken Shamanic Staffs + 15 Strand of Medusa Hair")

def distance_skill(update, context):
    #update.message.reply_text('25 Elven Scouting Glasses + 20 Elven Hoofs + 10 Metal Spikes')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Elven Scouting Glasses + 20 Elven Hoofs + 10 Metal Spikes")

def distance_skill_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('25 Elven Scouting Glasses + 20 Elven Hoofs + 10 Metal Spikes')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 Elven Scouting Glasses + 20 Elven Hoofs + 10 Metal Spikes")

def backpack(update, context):
    #update.message.reply_text('20 Fairy Wings + 10 Little Bowl of Myrrhs + 5 Goosebump Leather')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Fairy Wings + 10 Little Bowl of Myrrhs + 5 Goosebump Leather")

def backpack_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Fairy Wings + 10 Little Bowl of Myrrhs + 5 Goosebump Leather')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Fairy Wings + 10 Little Bowl of Myrrhs + 5 Goosebump Leather")

def speed(update, context):
    #update.message.reply_text('15 Damselfly Wings + 25 Compasses + 20 Waspoid Wings')
    context.bot.send_message(chat_id=update.effective_chat.id, text="15 Damselfly Wings + 25 Compasses + 20 Waspoid Wings")

def speed_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('15 Damselfly Wings + 25 Compasses + 20 Waspoid Wings')
    context.bot.send_message(chat_id=update.effective_chat.id, text="15 Damselfly Wings + 25 Compasses + 20 Waspoid Wings")

def antiparalyze(update, context):
    #update.message.reply_text('20 Wereboar Hooves + 15 Crystallized Angers + 5 Quills')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Wereboar Hooves + 15 Crystallized Angers + 5 Quills")

def antiparalyze_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text('20 Wereboar Hooves + 15 Crystallized Angers + 5 Quills')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Wereboar Hooves + 15 Crystallized Angers + 5 Quills")

def imbuements(update, context):
    query_imb = update.callback_query
    query_imb.answer()

    boton7 = InlineKeyboardButton(
        text='Void',
        callback_data='void_callback')

    boton8 = InlineKeyboardButton(
        text='Life Leech',
        callback_data='vampire_callback')
    boton9 = InlineKeyboardButton(
        text='Critico',
        callback_data='strike_callback')
    boton10 = InlineKeyboardButton(
        text='Proteccion',
        callback_data='proteccion_callback')
    boton11 = InlineKeyboardButton(
        text='Daño',
        callback_data='dano_callback')
    boton12 = InlineKeyboardButton(
        text='Aumento Skills',
        callback_data='skill')
    boton13 = InlineKeyboardButton(
        text='Otros',
        callback_data='otros_callback')

    query_imb.edit_message_text(
        text='Imbuements',
        reply_markup=InlineKeyboardMarkup([
            [boton7],
            [boton8],
            [boton9],
            [boton10],
            [boton11],
            [boton12],
            [boton13]
        ])
    )

def proteccion_callback (update, context):
    query_imb = update.callback_query
    query_imb.answer()

    boton14 = InlineKeyboardButton(
        text='Mort',
        callback_data='protec_mort_callback')

    boton15 = InlineKeyboardButton(
        text='Holy',
        callback_data='protec_holy_callback')
    boton16 = InlineKeyboardButton(
        text='Fire',
        callback_data='protec_fire_callback')
    boton17 = InlineKeyboardButton(
        text='Ice',
        callback_data='protec_ice_callback')
    boton18 = InlineKeyboardButton(
        text='Tera',
        callback_data='protec_tera_callback')
    boton19 = InlineKeyboardButton(
        text='Energy',
        callback_data='protec_energy_callback')


    query_imb.edit_message_text(
        text='Proteccion Elemental',
        reply_markup=InlineKeyboardMarkup([
            [boton14],
            [boton15],
            [boton16],
            [boton17],
            [boton18],
            [boton19]
        ])
    )

def dano_callback(update, context):
        query_imb = update.callback_query
        query_imb.answer()

        boton20 = InlineKeyboardButton(
            text='Mort',
            callback_data='mort_callback')
        boton21 = InlineKeyboardButton(
            text='Fire',
            callback_data='fire_callback')
        boton22 = InlineKeyboardButton(
            text='Ice',
            callback_data='ice_callback')
        boton23 = InlineKeyboardButton(
            text='Tera',
            callback_data='tera_callback')
        boton24 = InlineKeyboardButton(
            text='Energy',
            callback_data='energy_callback')

        query_imb.edit_message_text(
            text='Daño Elemental',
            reply_markup=InlineKeyboardMarkup([
                [boton20],
                [boton21],
                [boton22],
                [boton23],
                [boton24]

            ])
        )


def skill_callback(update, context):
    query_imb = update.callback_query
    query_imb.answer()

    boton25 = InlineKeyboardButton(
        text='Axe',
        callback_data='axe_skill_callback')
    boton26 = InlineKeyboardButton(
        text='Club',
        callback_data='club_skill_callback')
    boton27 = InlineKeyboardButton(
        text='Sword',
        callback_data='sword_skill_callback')
    boton28 = InlineKeyboardButton(
        text='Shielding',
        callback_data='shield_skill_callback')
    boton29 = InlineKeyboardButton(
        text='Magic Level',
        callback_data='magic_skill_callback')
    boton30 = InlineKeyboardButton(
        text='Distance',
        callback_data='distance_skill_callback')

    query_imb.edit_message_text(
        text='Daño Elemental',
        reply_markup=InlineKeyboardMarkup([
            [boton25],
            [boton26],
            [boton27],
            [boton28],
            [boton29],
            [boton30]
        ])
    )
def otros_callback(update, context):
    query_imb = update.callback_query
    query_imb.answer()

    boton31 = InlineKeyboardButton(
        text='BackPack Capacity',
        callback_data='backpack_callback')
    boton32 = InlineKeyboardButton(
        text='Aumento Speed',
        callback_data='speed_callback')
    boton33 = InlineKeyboardButton(
        text='Antiparalyze',
        callback_data='antiparalyze_callback')


    query_imb.edit_message_text(
        text='Otros Imbuements',
        reply_markup=InlineKeyboardMarkup([
            [boton31],
            [boton32],
            [boton33]

        ])
    )

def vampire_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text(text='25 vampire teeth\n15 bloody pincers\n5 piece of death brains')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 vampire teeth\n15 bloody pincers\n5 piece of death brains")


def void_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text(text='25 rope belts\n25 silencer claws\n5 Grimeleech Wings')
    context.bot.send_message(chat_id=update.effective_chat.id, text="25 rope belts\n25 silencer claws\n5 Grimeleech Wings")


def strike_callback(update, context):
    query = update.callback_query
    query.answer()

    #query.edit_message_text(text='20 Protective charms\n25 Sabretooth\n5 Vexclaw Talon')
    context.bot.send_message(chat_id=update.effective_chat.id, text="20 Protective charms\n25 Sabretooth\n5 Vexclaw Talon")

print('estamos dentro')

updater.dispatcher.add_handler(CommandHandler('guilds', guilds))

updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('rashid', rashid),
                  CallbackQueryHandler(pattern='rashid', callback=rashid_callback)
                  ],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('share', share),
                  CallbackQueryHandler(pattern='share', callback=share_callback)],
    states={
        INPUT_TEXT: [MessageHandler(Filters.text, calc_share)]

    },
    fallbacks=[])
)

updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('strike', strike),
                  CallbackQueryHandler(pattern='strike', callback=strike_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('void', void),
                  CallbackQueryHandler(pattern='void', callback=void_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('vampire', vampire),
                  CallbackQueryHandler(pattern='vampire', callback=vampire_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern='imbuements', callback=imbuements)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern='proteccion', callback=proteccion_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern='dano', callback=dano_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern='skill', callback=skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern='otros', callback=otros_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('mort', mort),
                  CallbackQueryHandler(pattern='mort', callback=mort_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('tera', tera),
                  CallbackQueryHandler(pattern='tera', callback=tera_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('energy', energy),
                  CallbackQueryHandler(pattern='energy', callback=energy_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('fire', fire),
                  CallbackQueryHandler(pattern='fire', callback=fire_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('ice', ice),
                  CallbackQueryHandler(pattern='ice', callback=ice_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_mort', protec_mort),
                  CallbackQueryHandler(pattern='protec_mort', callback=protec_mort_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_energy', protec_energy),
                  CallbackQueryHandler(pattern='protec_energy', callback=protec_energy_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_tera', protec_tera),
                  CallbackQueryHandler(pattern='protec_tera', callback=protec_tera_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_fire', protec_fire),
                  CallbackQueryHandler(pattern='protec_fire', callback=protec_fire_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_ice', protec_ice),
                  CallbackQueryHandler(pattern='protec_ice', callback=protec_ice_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('protec_holy', protec_holy),
                  CallbackQueryHandler(pattern='protec_holy', callback=protect_holly_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('club_skill', club_skill),
                  CallbackQueryHandler(pattern='club_skill', callback=club_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('axe_skill', axe_skill),
                  CallbackQueryHandler(pattern='axe_skill', callback=axe_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('sword_skill', sword_skill),
                  CallbackQueryHandler(pattern='sword_skill', callback=sword_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('shield_skill', shield_skill),
                  CallbackQueryHandler(pattern='shield_skill', callback=shield_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('magic_skill', magic_skill),
                  CallbackQueryHandler(pattern='magic_skill', callback=magic_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('distance_skill', distance_skill),
                  CallbackQueryHandler(pattern='distance_skill', callback=distance_skill_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('backpack', backpack),
                  CallbackQueryHandler(pattern='backpack', callback=backpack_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('speed', speed),
                  CallbackQueryHandler(pattern='speed', callback=speed_callback)],
    states={},
    fallbacks=[])
)
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('antiparalyze', antiparalyze),
                  CallbackQueryHandler(pattern='antiparalyze', callback=antiparalyze_callback)],
    states={},
    fallbacks=[])
)
updater.start_polling()
updater.idle()
