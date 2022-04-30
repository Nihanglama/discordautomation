import time
from discord_webhook import DiscordWebhook


def UC60():
    if page == 1:
        # SUB_Gaming ko 60 pins ko url
        url = "https://discord.com/api/webhooks/969880942091051029/KZpzwuEVQ0fIDvks-dMi0A9BHBE979IYl3DxUgfZVPoDG6q9H6qMmM55QuAbzgDc3qbB"
    elif page==2:
        #MRL_ko 60 pins ko url
        url=''
    elif page==3:
        # ADV presents ko 60 pins ko url
        url=''
    else:
        print("Wrong choice")
        exit()        
    pins = open('60pins.txt', 'r')
    count=0
    for pin in pins:
        post_request = DiscordWebhook(url, content='```'+pin+'```')
        response = post_request.execute()
        count+=1
        time.sleep(5)
        if count%10==0:
            # url = "https://discord.com/api/webhooks/969880942091051029/KZpzwuEVQ0fIDvks-dMi0A9BHBE979IYl3DxUgfZVPoDG6q9H6qMmM55QuAbzgDc3qbB"
            post_request = DiscordWebhook(url, content="```Total:"+str(count)+'```')
            response = post_request.execute()

def UC325():
    if page == 1:
        # SUB_Gaming ko 60 pins ko url
            url = "https://discord.com/api/webhooks/969881094692429875/uiu6f50L76SyiHHtwM7Wg1h9YO-enVEqrlxUEFwqCrEXBoMe9yf-obBRnGR0kFXi9oLz"
    elif page==2:
        #MRL_ko 60 pins ko url
        url=''
    elif page==3:
        # ADV presents ko 60 pins ko url
        url=''
    else:
        print("Wrong choice")
        exit()  
    pins = open('325pins.txt', 'r')
    count=0
    for pin in pins:
        # url = "https://discord.com/api/webhooks/969881094692429875/uiu6f50L76SyiHHtwM7Wg1h9YO-enVEqrlxUEFwqCrEXBoMe9yf-obBRnGR0kFXi9oLz"
        post_request = DiscordWebhook(url, content='```'+pin+'```')
        response = post_request.execute() 
        count+=1
        time.sleep(5)
        if count%10==0:
                # url = "https://discord.com/api/webhooks/969881094692429875/uiu6f50L76SyiHHtwM7Wg1h9YO-enVEqrlxUEFwqCrEXBoMe9yf-obBRnGR0kFXi9oLz"
                post_request = DiscordWebhook(url, content="```Total:"+str(count)+'```')
                response = post_request.execute()

def UC660():
    if page == 1:
        # SUB_Gaming ko 60 pins ko url
            url = "https://discord.com/api/webhooks/969879128675328080/XdNekek60pwkboZnHDfhpYfioxffHlT9wRLoz2hHAKUwTdLusOnOQAHyZvwcbyn2rkET"
    elif page==2:
        #MRL_ko 60 pins ko url
        url=''
    elif page==3:
        # ADV presents ko 60 pins ko url
        url=''
    else:
        print("Wrong choice")
        exit()  
    pins = open('660pins.txt', 'r')
    count=0
    for pin in pins:
        # url = "https://discord.com/api/webhooks/969879128675328080/XdNekek60pwkboZnHDfhpYfioxffHlT9wRLoz2hHAKUwTdLusOnOQAHyZvwcbyn2rkET"
        post_request = DiscordWebhook(url, content='```'+pin+'```')
        response = post_request.execute()
        count+=1
        time.sleep(5)
        if count%10==0:
                # url = "https://discord.com/api/webhooks/969879128675328080/XdNekek60pwkboZnHDfhpYfioxffHlT9wRLoz2hHAKUwTdLusOnOQAHyZvwcbyn2rkET"
                post_request = DiscordWebhook(url, content="```Total:"+str(count)+'```')
                response = post_request.execute()




if __name__== '__main__':
    print("1:SUB Gaming\n2:MRL Shop\n:ADV Present")
    page=int(input("Choose page: "))

    print("1:60UC\n2:325UC\n3:660UC")

    choose_pins=int(input("Choose pin: "))
    if choose_pins==1:
        UC60()
    elif choose_pins==2:
        UC325()
    elif choose_pins==3:
        UC660()
    else:
        print("Wrong")
        exit()

