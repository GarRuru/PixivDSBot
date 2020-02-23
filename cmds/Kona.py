import discord
from discord.ext import commands
from core.classes import cog_Extension
from bs4 import BeautifulSoup
import requests
import urllib
import random


class Kona(cog_Extension):

    @commands.command()
    async def s(self, ctx, *, keyword):  # Allow keyword w/ space
        val = { 'tags' : keyword}
        uri = urllib.parse.urlencode(val)   # Encode
        uri = 'http://konachan.net/post?' + uri    # Combine URL

        res = requests.get(uri)
        print(uri)
        if res.status_code == requests.codes.ok:
             soup = BeautifulSoup(res.text, 'html.parser')
        if soup.find_all("p", string="Nobody here but us chickens!"):
            await ctx.send("小精靈翻遍了整個網站 找不到任何結果QQ. Nothing found on the website.")

        else:
            PPList = soup.find_all("div", class_="inner")
            PICKUP = random.choice(PPList)
            #await ctx.send(PICKUP)
            print(PICKUP)       # Type: bs4.element.Tag
            choicePicThumb = str(PICKUP)
            cPTList = choicePicThumb.split('#pl')
            del cPTList[0]
            nextLink = "".join(cPTList) # Convert to String
            nextLink = nextLink[1:-17] # Remove character, Sample: " http://konachan.net/post/show/296680</span></a></div>"


            # To Detail Page: Download Photos!!
            res = requests.get(str(nextLink))
            if res.status_code == requests.codes.ok:
                soup = BeautifulSoup(res.text, 'html.parser')

            TargetURI = ""

            for a in  soup.find_all("a" , class_="original-file-changed"):
                print(a['href'])
                TargetURI = str(a['href'])
            await ctx.send(TargetURI)

    @commands.command()
    async def sr(self, ctx, *, keyword):
        val = {'tags': keyword}
        uri = urllib.parse.urlencode(val)  # Encode
        uri = 'http://konachan.com/post?' + uri  # Combine URL

        res = requests.get(uri)
        print(uri)
        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
        if soup.find_all("p", string="Nobody here but us chickens!"):
            await ctx.send("小精靈翻遍了整個網站 找不到任何結果QQ. Nothing found on the website.")

        else:
            PPList = soup.find_all("div", class_="inner")
            PICKUP = random.choice(PPList)
            # await ctx.send(PICKUP)
            print(PICKUP)  # Type: bs4.element.Tag
            choicePicThumb = str(PICKUP)
            cPTList = choicePicThumb.split('#pl')
            del cPTList[0]
            nextLink = "".join(cPTList)  # Convert to String
            nextLink = nextLink[
                       1:-17]  # Remove character, Sample: " http://konachan.net/post/show/296680</span></a></div>"

            # To Detail Page: Download Photos!!
            res = requests.get(str(nextLink))
            if res.status_code == requests.codes.ok:
                soup = BeautifulSoup(res.text, 'html.parser')

            TargetURI = ""

            for a in soup.find_all("a", class_="original-file-changed"):
                print(a['href'])
                TargetURI = str(a['href'])
            await ctx.send(TargetURI)

def setup(bot):
    bot.add_cog(Kona(bot))
