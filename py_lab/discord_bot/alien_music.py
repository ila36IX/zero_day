#!/bin/python3
import discord
from yt import download_mp3, is_youtube_link, random_meme
from yt import yt_search
from discord.ext import commands
import asyncio
import re

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
intents.messages = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ww(ctx, q1=None, q2=None, q3=None):
    global voice_client
    if q1 is None:
        await ctx.send('Rak nsiti link! katmergen biya Wa9ila?')
        return

        # await play_audio(ctx, str(video))

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = channel
        await ctx.message.add_reaction('⏳')
        try:
            await channel.connect()
        except Exception as e:
            pass
        # await ctx.send("OK")
        if is_youtube_link(q1):
            await play_audio(ctx, q1)
        else:
            video = yt_search(q1, q2, q3)
            # await ctx.send(video.thumbnail_url)
            await play_audio(ctx, video.watch_url)
    else:
        await ctx.send('Dkhel chi voice? fin bghitini ntele9 hadchi SMA?')

@bot.command()
async def ply(ctx):
    await ctx.message.add_reaction('⏳')
    global voice_client
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = channel
        try:
            await channel.connect()
        except Exception as e:
            pass
        # await ctx.send(random_meme())
        await play_audio(ctx, random_meme())
    else:
        await ctx.send('Dkhel chi voice? fin bghitini ntele9 hadchi f\'SMA?')

@bot.command()
async def xx(ctx):
    global voice_client
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = channel
        try:
            await channel.connect()
        except Exception as e:
            pass
        # await ctx.send(random_meme())
        await play_audio(ctx, "https://www.youtube.com/watch?v=ivezrbNVJ00")
    else:
        await ctx.send('Dkhel chi voice? fin bghitini ntele9 hadchi f\'SMA?')
@bot.command()
async def xn(ctx):
    global voice_client
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = channel
        try:
            await channel.connect()
        except Exception as e:
            pass
        # await ctx.send(random_meme())
        await play_audio(ctx, "https://www.youtube.com/watch?v=nA_caNpqxRQ")
    else:
        await ctx.send('Dkhel chi voice? fin bghitini ntele9 hadchi f\'SMA?')

@bot.command()
async def ja(ctx):
    global voice_client
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = channel
        try:
            await channel.connect()
        except Exception as e:
            pass
        if ctx.voice_client:
            ctx.voice_client.stop()
            voice_client = ctx.voice_client
            ctx.voice_client.play(discord.FFmpegPCMAudio("files/ja_lkeleb.mp3"))
            await ctx.message.remove_reaction('⏳', bot.user)
            await ctx.message.add_reaction('✅')
        while voice_client and voice_client.is_playing():
            await asyncio.sleep(1)
        if voice_client:
            await ss(ctx)
    else:
        await ctx.send('Dkhel chi voice? fin bghitini ntele9 hadchi f\'SMA?')

@bot.command()
async def ss(ctx):
    global voice_client
    voice_client = None
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.guild.voice_client.disconnect()

@bot.command()
async def skot(ctx):
    global voice_client
    voice_client = None
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.guild.voice_client.disconnect()

async def play_audio(ctx, link):
    global voice_client
    print(link)
    audio_source = download_mp3(link)
    if ctx.voice_client:
        ctx.voice_client.stop()
        voice_client = ctx.voice_client
        ctx.voice_client.play(discord.FFmpegPCMAudio(audio_source))
        await ctx.message.remove_reaction('⏳', bot.user)
        await ctx.message.add_reaction('✅')
    while voice_client and voice_client.is_playing():
        await asyncio.sleep(1)
    if voice_client:
        await ss(ctx)
        # await ctx.guild.voice_client.disconnect()


async def play_for_me(id, member, before, after, sound):
    global voice_client
    if str(member.id) == id:
        if before.channel is None and after.channel is not None:
            voice_client = await after.channel.connect()
            audio_source = discord.FFmpegPCMAudio("./files/" + sound)
            voice_client.play(audio_source)
            while voice_client and voice_client.is_playing():
                await asyncio.sleep(1)
            if voice_client:
                await voice_client.disconnect()
                voice_client = None

@bot.event
async def on_voice_state_update(member, before, after):
    global voice_client
    # Play audie if I owner joined a voice
    # if str(member.id) == "592180944983556096":
    #     if before.channel is None and after.channel is not None:
    #         voice_client = await after.channel.connect()
    #         audio_source = discord.FFmpegPCMAudio("./files/alien_soundeffect.mp3")
    #         voice_client.play(audio_source)
    #         while voice_client and voice_client.is_playing():
    #             await asyncio.sleep(1)
    #         if voice_client:
    #             await voice_client.disconnect()
    #             voice_client = None
    await play_for_me("592180944983556096", member,before, after, "alien_soundeffect.mp3")
    await play_for_me("1159576461880066230", member,before, after, "hassan_enters.mp3")
    await play_for_me("963503666734710784", member,before, after, "rida_enters.mp3")
    await play_for_me("688808986539327505", member,before, after, "carry_the_boat.mp3")
    if member == bot.user and before.channel != after.channel:
        voice_channel = after.channel
        if voice_channel is None and voice_client is not None:
            voice_client.stop()
            await before.channel.send("### Malek m3essb STA3MEL: `!ss` Please!")
            await voice_client.disconnect()
            voice_client = None

bot.run('token_goes_here')
