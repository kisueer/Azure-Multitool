from Config.Util import *
from Config.Config import *
try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import time
except Exception as e:
   ErrorModule(e)

Title("Username Tracker")

try:
    sites = {
        "Roblox Trade": "https://rblx.trade/p/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Instagram": "https://www.instagram.com/{}",
        "Paypal": "https://www.paypal.com/paypalme/{}",
        "GitHub": "https://github.com/{}",
        "Giters": "https://giters.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Telegram": "https://t.me/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Blogger": "https://{}.blogspot.com",
        "Tumblr": "https://{}.tumblr.com",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Keybase": "https://keybase.io/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Behance": "https://www.behance.net/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "Patreon": "https://www.patreon.com/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Disqus": "https://disqus.com/by/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Weebly": "https://{}.weebly.com",
        "YouTube": "https://www.youtube.com/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "Mix": "https://mix.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Strava": "https://www.strava.com/athletes/{}",

        "Internet Archive": "https://archive.org/search?query={}",
        "Twitter Archive": "https://web.archive.org/web/*/https://twitter.com/{}/status/*",
        "Linktree": "https://linktr.ee/{}",
        "Xbox": "https://www.xboxgamertag.com/search/{}",
        "Twitter": "https://twitter.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Goodreads": "https://www.goodreads.com/{}",
        "VK": "https://vk.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Dribbble": "https://dribbble.com/{}",
        "AngelList": "https://angel.co/{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Tidal": "https://tidal.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",  
        "Ello": "https://ello.co/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "VK": "https://vk.com/{}",
    }

    def SiteException(username, site, page_content):
        if site == "Paypal":
            page_content = page_content.replace(f'slug_name={username}', '').replace(f'"slug":"{username}"', '').replace(f'2F{username}&amp', '')
        elif site == "TikTok":
            page_content = page_content.replace(f'\\u002f@{username}"', '')
        return page_content

    number_site = 0
    number_found = 0
    sites_and_urls_found = []

    Slow(osint_banner)
    username = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")
    Censored(username)

    username = username.lower()

    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Scanning..")

    session = requests.Session()

    for site, url_template in sites.items():
        try:
            number_site += 1
            url = url_template.format(username)
            try:
                response = session.get(url, timeout=3)
                if response.status_code == 200:
                    page_content = re.sub(r'<[^>]*>', '', response.text.lower().replace(url, "").replace(f"/{username}", ""))
                    page_content = SiteException(username, site, page_content)

                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_text = soup.get_text().lower().replace(url, "")
                    page_title = soup.title.string.lower() if soup.title else ""

                    found = username in page_title or username in page_content or username in page_text

                    if found:
                        number_found += 1
                        sites_and_urls_found.append(f"{site}: {white + url}")
                        print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} {site}: {white + url}")
                    else:
                        print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} {site}:{white} Not Found")

                else: 
                    print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} {site}:{white} Not Found")

            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {site}: {white + e}")
        except:
            pass

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Total Found:{reset}")
    for site_and_url_found in sites_and_urls_found:
        time.sleep(0.5)
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} {site_and_url_found}")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Total Website: {white}{number_site}{red} Total Found: {white}{number_found}{red}")
    Continue()
    Reset()

except Exception as e:
    Error(e)