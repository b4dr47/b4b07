import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.slash_command(name="hello", description="Says hello")
async def hello(ctx: discord.ApplicationContext):
    member = ctx.author
    embed = discord.Embed(title="Hello!", color=discord.Color.blurple())
    embed.add_field(name="Greetings", value=f"Hello {member.mention}!", inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text="powered by b4")
    await ctx.respond(embed=embed)


@bot.slash_command(name="avatar", description="Get a user's avatar")
async def avatar(ctx: discord.ApplicationContext, member: discord.Member = None):
    if member is None:
        member = ctx.author
    avatar_url = member.display_avatar.url
    embed = discord.Embed(
        title=f"{member.display_name}'s Avatar", color=discord.Color.blurple()
    )
    embed.set_image(url=avatar_url)
    embed.set_footer(text="powered by b4")
    await ctx.respond(embed=embed)


@bot.slash_command(name="ping", description="Get server latency")
async def ping(ctx: discord.ApplicationContext):
    latency_ms = round(bot.latency * 1000)
    if latency_ms < 100:
        color = discord.Color.green()
    elif latency_ms < 200:
        color = discord.Color.orange()
    else:
        color = discord.Color.red()
    embed = discord.Embed(
        title="Pong!", description=f"Latency: {latency_ms} ms", color=color
    )
    embed.set_footer(text="powered by b4")
    await ctx.respond(embed=embed)


@bot.slash_command(name="mobai", description="mobai dalao")
async def mobai(ctx: discord.ApplicationContext, member: discord.Member):
    embed = discord.Embed(
        title=f"膜拜 {member.display_name} 電神",
        description="佬都不教",
        color=discord.Color.blurple(),
    )
    embed.set_footer(text="powered by b4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/emojis/1021398944779083806.webp?size=96&animated=true"
    )
    await ctx.respond(embed=embed)


@bot.slash_command(name="intro", description="Introduce me")
async def intro(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="b4dr47",
        description="Introduction",
        url="https://b4dr47.dev/",
        color=discord.Color.blurple(),
    )
    embed.set_footer(text="powered by b4")
    embed.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3llddq7WX0WXbbqF9uZv4ANWcvx4pS7apHw&s"
    )
    await ctx.respond(embed=embed)


if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable not set.")
bot.run(TOKEN)
