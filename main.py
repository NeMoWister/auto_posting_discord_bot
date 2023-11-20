import os
import sys

import discord
import time
import config
import post


class myClient(discord.Client):
    async def on_ready(self):
        for i in range(json_data['number_of_starts']):
            for _ in json_data['channel_id']:
                await self.post_them_all(_['id'])
        await client.close()

    async def post_them_all(self, ch_id):
        files = []
        current_date = time.strftime("%d_%m_%Y")
        current_time = time.strftime("%H_%M")
        folder_path = os.path.join('logs', current_date)
        os.makedirs(folder_path, exist_ok=True)

        log_filename = os.path.join(folder_path, f'log_{current_time}.txt')
        # print('Logged on as {0}.'.format(self.user))
        channel = client.get_channel(ch_id)
        result = post.start_posting(json_data)
        with open(log_filename, 'w') as f:
            for i in result[1]:
                f.write(i + '\n')
                files.append(discord.File(i))
        # print(files)
        await channel.send(files=files)


name = sys.argv[1] if len(sys.argv) > 1 else "config"

json_data = config.json_parse(name)
if name != 'config':
    config.json_delete(name)


client = myClient(intents=discord.Intents.default())
client.run(json_data['token'])
