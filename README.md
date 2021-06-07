Website Checker
===============

Checks a website for changes every *n* seconds.  
Plays alarm when website has changed.

### Install

```bash
$ pip3 install -r requirements.txt
```

### Running

```bash
$ python3 <URL> [--interval <interval>]
```

### Example

Checks `https://apple.com/mac` every 5 seconds:

```bash
$ python3 main.py https://apple.com/mac --interval 5
```
