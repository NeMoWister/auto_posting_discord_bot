# Discord Auto Posting Bot
This Discord bot selects random images from predefined folders and sends them to a specified channel.

## How to Use

1. Install all the necessary dependencies by executing:

    ```
    pip install -r requirements.txt
    ```

2. Specify the bot settings in the config.py file, such as:
    
    ```python
    # config.py
    token = 'your discord token'
    my_list = [('name', 'path', chance, max_cache_size)]
    channel_id = int # your discord channel id
    ```
    I recommend setting max_cache_size close to the total number of files in the folder. 
    You can also set max_cache_size to 'auto,' in which case the maximum value will be 90% of the total number of files in the folder. 
    I do not recommend using this when the total number of files is less than 20.

3. Run the bot using:

    ```
    python bot.py
    ```
  
The bot will randomly select 10 images from the specified folders and send them to the designated channel.

## Caching Settings
The bot automatically caches sent images to avoid re-sending in the same session. The cache is stored separately for each folder.

## Configuration
In the `config.py` file, you can configure the list of folders, their paths, weights for random selection, and the maximum cache value.

License
This project is distributed under the [CC0 (Creative Commons Zero)](LICENSE).
