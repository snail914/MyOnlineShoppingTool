from price_checker import Stores, PriceChecker
from discord_bot import DiscordBot


urls = {
        Stores.John_Lewis: "https://www.johnlewis.com/sonos-beam-compact-smart-sound-bar-with-voice-control/black/p3585331",
        Stores.Argos: "https://www.argos.co.uk/product/8153368?clickSR=slp:term:sonos%20beam:2:18:1",
        Stores.Currys: "https://www.currys.co.uk/gbuk/tv-and-home-entertainment/dvd-blu-ray-and-home-cinema/home-cinema-systems-and-sound-bars/sonos-beam-compact-sound-bar-with-amazon-alexa-google-assistant-black-10181783-pdt.html"
}

DiscordBot.send(PriceChecker.get_john_lewis_price(urls[Stores.John_Lewis]))
DiscordBot.send(PriceChecker.get_argos_price(urls[Stores.Argos]))
DiscordBot.send(PriceChecker.get_currys_price(urls[Stores.Currys]))
