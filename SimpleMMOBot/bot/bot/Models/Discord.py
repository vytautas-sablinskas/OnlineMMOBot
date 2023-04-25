from discord_webhook import DiscordWebhook

class Discord:
    def __init__(self, token, webhook_url):
        self.token = token
        self.webhook_url = webhook_url

    def send_message_to_discord_server(self, message):
        webhook = DiscordWebhook(url=self.webhook_url, content=message)
        webhook.execute()