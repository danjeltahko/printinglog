# Simple Logging Module

I've been using pythons built-in logging for my previous projects, but i discovered that it doesn't work as expected when running cronjobs in docker containers. The logger fails to write to the specified file because cronjobs operate in a limited environment with different permissions. They often capture standard output and error to a default file, usually ```cron.log``` in my case. While there might be ways to fix this, as a coder, it feels much better to write my own logging module; it would be a disgrace otherwise. So with this module, i can read the logs from cron.log since it uses print statements with logging formatting.

### Install
Install the module with:
```bash
pip install printinglog
```

### Usage
To start using `printinglog`, initialize the logger with:
```python
from printinglog import Logger

logger = Logger()

logger.info("This is a INFO log")
```

You can also change how much detail you want to show in your log:
```python
logger = Logger(format="simple")
logger.info("This is a INFO log")
>> INFO: This is a INFO log

logger = Logger(format="logging")
logger.info("This is a INFO log")
>> 2024-07-26 22:55:28 - INFO: This is a INFO log

logger = Logger(format="detailed")
logger.info("This is a INFO log")
>> 2024-07-26 22:55:28 @main - INFO: This is a INFO log

logger = Logger(format="long")
logger.info("This is a INFO log")
>> INFO: This is a INFO log
2024-07-26 22:55:28 @main<test_function> - INFO: This is a INFO log
```

To change the colors for each log type, you can also specify that:
```python
default_colors = {
    "info": "green",
    "error": "red",
    "warning": "yellow",
    "debug": "blue",
}
logger = Logger(colorscheme=default_colors)
```

Colors to choose from:
* black
* red
* green
* yellow
* blue
* magneta
* cyan
* white

