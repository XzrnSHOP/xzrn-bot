# 這段程式碼必須存在於您的 bot.py 最上方
from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleKeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"Bot is Active")

def run_web_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), SimpleKeepAliveHandler)
    server.serve_forever()

import threading
threading.Thread(target=run_web_server, daemon=True).start()
import os
import discord
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from discord.ext import commands

# 輕量保活 (避免 Render 休眠)
class KeepAlive(BaseHTTPRequestHandler):
    def do_GET(self): self.send_response(200); self.end_headers(); self.wfile.write(b"OK")
threading.Thread(target=lambda: HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), KeepAlive).serve_forever(), daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 新機器人已就緒: {bot.user}")

# 簡單功能範例
@bot.command()
async def ping(ctx):
    await ctx.send("系統運作中，穩定連線！")

bot.run(os.environ.get("TOKEN"))
