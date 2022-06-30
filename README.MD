# telethon-duplicate-file

This script will go through all files (currently just `audio`) of a given group. Then send yourself a message if
possible duplicates were found.

The only criteria is `file_size`, which may not be unique. Thus, you have to review the result yourself.

## Usage

This script uses [Telethon](https://docs.telethon.dev/en/stable/) as a client. Replace `config.api_id`
and `config.api_hash` with your
own. You can get them [here](https://my.telegram.org).

## Contributions

Improvements to the code are welcome :)