import os

import discord
import time
import config
import post


class myClient(discord.Client):
    async def on_ready(self):
        files = []
        current_date = time.strftime("%d_%m_%Y")
        current_time = time.strftime("%H_%M")
        folder_path = os.path.join('logs', current_date)
        os.makedirs(folder_path, exist_ok=True)

        log_filename = os.path.join(folder_path, f'log_{current_time}.txt')
        #print('Logged on as {0}.'.format(self.user))

        channel = client.get_channel(config.channel_id)
        result = post.start_posting()
        with open(log_filename, 'w') as f:
            for i in result[1]:
                f.write(i + '\n')
                files.append(discord.File(i))
        #print(files)
        await channel.send(files=files)
        await client.close()


client = myClient(intents=discord.Intents.default())
client.run(config.token)
