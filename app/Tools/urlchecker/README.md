# URL Checker
A python script for checking the status of web pages and any links stored on the web pages.

## Language
python3

## Dependencies
native python libraries:<br />
**requests** <br />
**json** <br />
**re (regular expression)**

## Setup
1. Set up configuration in 'URLChecker.config' file.
```json
{
  "URL_List": ["https://www.jamauni.com"],
  "regExpressions": ["href=\"(.*?)\"", "src=\"(.*?)\""],
  "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"},
  "URLsToSkip": ["javascript:void(0)", "www.tiktok.com", "www.linkedin.com"]
}
```
* **URL_List:** An array of urls as strings.
* **regExpressions:** An array of regular expressions stored as strings.
* **headers:** JSON header object for http(s) request. Without it some links will reflect "Not working".
* **URLsToSkip:** An array of urls the URLChecker will skip

2. Run URL checker script.
```bash
python3 CheckURL.py
```
3. The script will then recursively check any links found on any URL_List set up during configuration.
```json
{
    "https://www.jamauni.com": "Working",
    "https://www.jamauni.com/css/fonts.css": "Working",
    "https://www.jamauni.com/css/index.css": "Working",
    "https://www.jamauni.com/css/header.css": "Working",
    "https://www.jamauni.com/css/footer.css": "Working",
    "https://www.jamauni.com/css/userMessage.css": "Working",
    "https://www.jamauni.com/css/menu.css": "Working",
    "https://www.jamauni.com/index.html": "Working",
    "https://www.jamauni.com/work.html": "Working",
    "https://www.jamauni.com/contact.html": "Working",
    "https://www.jamauni.com/js/menu.js": "Working",
    "https://www.jamauni.com/css/icons/menu.svg": "Working",
    "https://www.jamauni.com/css/imgs/ProfilePic.jpg": "Working",
    "https://www.jamauni.com/css/imgs/blank.jpeg": "Working",
    "https://www.jamauni.com/css/work.css": "Working",
    "https://www.jamauni.com/job.html?jobID=0": "Working",
    "https://www.jamauni.com/job.html?jobID=1": "Working",
    "https://www.jamauni.com/job.html?jobID=2": "Working",
    "https://www.jamauni.com/job.html?jobID=3": "Working",
    "https://www.jamauni.com/job.html?jobID=4": "Working",
    "https://www.jamauni.com/css/contact.css": "Working",
    "https://www.jamauni.com/js/contact.js": "Working",
    "https://www.jamauni.com/js/Message.js": "Working",
    "https://www.jamauni.com/css/job.css": "Working"
}
```
* Upon completion, the URL Checker will print a JSON object to the console detailing the results of it's operation.

## Output
Upon success, the URL checker prints a JSON object detailing what links are "Work(returned 200 http status code)" and what links are "Not Working(did not return 200 http status code)".
```json
{
    "https://www.jamauni.com": "Working",
    "https://www.jamauni.com/css/fonts.css": "Working",
    "https://www.jamauni.com/css/index.css": "Working",
    "https://www.jamauni.com/css/header.css": "Working",
    "https://www.jamauni.com/css/footer.css": "Working",
    "https://www.jamauni.com/css/userMessage.css": "Working",
    "https://www.jamauni.com/css/menu.css": "Working",
    "https://www.jamauni.com/index.html": "Working",
    "https://www.jamauni.com/work.html": "Working",
    "https://www.jamauni.com/contact.html": "Working",
    "https://www.jamauni.com/js/menu.js": "Working",
    "https://www.jamauni.com/css/icons/menu.svg": "Working",
    "https://www.jamauni.com/css/imgs/ProfilePic.jpg": "Working",
    "https://www.jamauni.com/css/imgs/blank.jpeg": "Working",
    "https://www.jamauni.com/css/work.css": "Working",
    "https://www.jamauni.com/job.html?jobID=0": "Working",
    "https://www.jamauni.com/job.html?jobID=1": "Working",
    "https://www.jamauni.com/job.html?jobID=2": "Working",
    "https://www.jamauni.com/job.html?jobID=3": "Working",
    "https://www.jamauni.com/job.html?jobID=4": "Working",
    "https://www.jamauni.com/css/contact.css": "Working",
    "https://www.jamauni.com/js/contact.js": "Working",
    "https://www.jamauni.com/js/Message.js": "Working",
    "https://www.jamauni.com/css/job.css": "Working"
}
```