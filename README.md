# CLI Diki Translator
` A lightweight command-line interface tool written in Python that fetches English word translations directly from [diki.pl](https://www.diki.pl/).`

## Screenshots

<table>
  <tr>
    <td align="center"><img src="./screenshots/1.png" width="250"/><br/>1. Invoke diki</td>
    <td align="center"><img src="./screenshots/2.png" width="250"/><br/>2. Prompt your phrase</td>
    <td align="center"><img src="./screenshots/3.png" width="250"/><br/>3. Get Results</td>
  </tr>
</table>

## Features
- Direct Web Scraping: *Uses `requests` and `BeautifulSoup` to parse dictionary entries seamlessly.*
- Terminal Color Support: *Formats CLI output with ANSI color codes.*
- Error Handling:\*\* Gracefully handles non-200 HTTP statuses and network timeouts.

## Requirements
-   `Python 3.x`
-   `requests`
-   `beautifulsoup4`
-   `soupsieve==4.1`
-   `cx_Freeze==8.7.4`

## Installation
1. Clone or download the repository.
2. Install the required dependencies:
```bash
 pip install -r requirements.txt
```

3. Run
```bash
python diki.py
```

4. Compile diki.py to exe
```bash
python ./setup.py build
```
5. Add ./build directory to path in your OS
<table>
  <tr>
    <td align="center"><img src="./screenshots/4.png" width="450"/><br/></td>
    <td align="center"><img src="./screenshots/5.png" width="450"/><br/></td>
  </tr>
  <td align="center"><img src="./screenshots/6.png" width="750"/><br/></td>
  <tr>
    
     
</table>

```bash
# click <new> and
# paste the absolute path of your directory where */build/*/diki.exe is located
```
<table>
  <tr>
    <td align="center"><img src="./screenshots/7.png" width="500"/><br/></td>
  </tr>
</table>

6. `Diki` works now!
<table>
  <tr>
    <td align="center"><img src="./screenshots/1.png" width="750"/><br/></td>
  </tr>
</table>
