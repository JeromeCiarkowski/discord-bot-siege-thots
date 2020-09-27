# standard library
import os
import random

# third-party
from discord.ext import commands
from dotenv import load_dotenv
from nanoleafapi import discovery
from nanoleafapi import Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, WHITE

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
NANOLEAF_IP_ADDRESS = os.getenv('NANOLEAF_IP_ADDRESS')
NANOLEAF_AUTH_TOKEN = os.getenv('NANOLEAF_AUTH_TOKEN')

ON = 'on'
OFF = 'off'
TOGGLE = 'toggle'

bot = commands.Bot(command_prefix='!')

@bot.command(name='nanoleaf_connect', help='Performs functionality related to connectiono')
async def nanoleaf_connect(ctx, ip_address):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    # TODO everything

@bot.command(name='nanoleaf_identify', help='Performs functionality related to identification')
async def nanoleaf_identify(ctx):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    # TODO everything

@bot.command(name='nanoleaf_power', help='Performs functionality related to power')
async def nanoleaf_power(ctx, arg):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg == ON:
        nl.power_on()
    elif arg == OFF:
        nl.power_off()
    elif arg == TOGGLE:
        nl.toggle_power()
    else:
        temp = 'orary'
        # TODO error handling

    status = f'Nanoleaf is powered on.' if nl.get_power() else f'Nanoleaf is powered off.'
    await ctx.send(status)

@bot.command(name='nanoleaf_color', help='Performs functionality related to color')
async def nanoleaf_color(ctx, *args):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if len(args) == 1:
        if args[0] == 'red':
            nl.set_color(RED)
        elif args[0] == 'orange':
            nl.set_color(ORANGE)
        elif args[0] == 'yellow':
            nl.set_color(YELLOW)
        elif args[0] == 'green':
            nl.set_color(GREEN)
        elif args[0] == 'light_blue':
            nl.set_color(LIGHT_BLUE)
        elif args[0] == 'blue':
            nl.set_color(BLUE)
        elif args[0] == 'pink':
            nl.set_color(PINK)
        elif args[0] == 'purple':
            nl.set_color(PURPLE)
        elif args[0] == 'white':
            nl.set_color(WHITE)
        else:
            temp = 'orary'
            # TODO error handling
    elif len(args) == 3:
        try:
            nl.set_color((int(args[0]), int(args[1]), int(args[2])))
        except Exception as e:
            temp = 'orary'
            # TODO error handling
    else:
        temp = 'orary'
        # TODO error handling


    status = f'Nanoleaf color is {args[0]}' if len(args) == 1 else f'Nanoleaf color is ({args[0]}, {args[1]}, {args[2]}).'
    await ctx.send(status)

@bot.command(name='nanoleaf_brightness', help='Performs functionality related to brightness')
async def nanoleaf_brightness(ctx, arg=None):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg == None:
        nl.get_brightness()
    else:
        try:
            nl.set_brightness(int(arg))
        except Exception as e:
            temp = 'orary'
            # TODO error handling

    status = f'Nanoleaf brightness is {nl.get_brightness()}'
    await ctx.send(status)

@bot.command(name='nanoleaf_hue', help='Performs functionality related to hue')
async def nanoleaf_hue(ctx, arg=None):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg == None:
        nl.get_hue()
    else:
        try:
            nl.set_hue(int(arg))
        except Exception as e:
            temp = 'orary'
            # TODO error handling

    status = f'Nanoleaf hue is {nl.get_hue()}.'
    await ctx.send(status)

@bot.command(name='nanoleaf_saturation', help='Performs functionality related to saturation')
async def nanoleaf_saturation(ctx, arg=None):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg == None:
        nl.get_saturation()
    else:
        try:
            nl.set_saturation(int(arg))
        except Exception as e:
            temp = 'orary'
            # TODO error handling

    status = f'Nanoleaf saturation is {nl.get_saturation()}.'
    await ctx.send(status)

@bot.command(name='nanoleaf_color_temperature', help='Performs functionality related to color temperature')
async def nanoleaf_color_temperature(ctx, arg=None):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg == None:
        nl.get_color_temp()
    else:
        try:
            nl.set_color_temp(int(arg))
        except Exception as e:
            temp = 'orary'
            # TODO error handling

    status = f'Nanoleaf color temperature is {nl.get_color_temp()}.'
    await ctx.send(status)

@bot.command(name='nanoleaf_effects', help='Performs functionality related to effects')
async def nanoleaf_effects(ctx, arg=None):
    # TODO convert to class to become functional and to allow multiple bot instances
    nl = Nanoleaf(NANOLEAF_IP_ADDRESS, NANOLEAF_AUTH_TOKEN)

    if arg:
        try:
            breakpoint()
            nl.set_effect(arg)
        except Exception as e:
            temp = 'orary'
            # TODO error handling

    status = f'Nanoleaf current effect:\n{nl.get_current_effect()}\n\nNanoleaf available effects:\n' + '\n'.join(effect for effect in nl.list_effects())
    await ctx.send(status)

bot.run(TOKEN)

# TODO genercize similar functions
# brightness, hue, saturation, and color temperature share the same patterrn
# conditional statement to function object assignment
# getter = blah
# setter = blah

# increment_*(value), get_color_mode(), effect_exists(name), and write_effect(effect_dict) intentionally ommitted

# TODO requirements.txt