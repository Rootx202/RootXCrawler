# RootXCrawler

**RootXCrawler** is a powerful web crawler and security scanner designed for deep website reconnaissance, penetration testing, and security auditing.

> Crawling deep. Seeing everything.

## Features

- **Deep Web Crawling** — Multi-threaded crawling with configurable depth, delay, and concurrency
- **Historical URL Discovery** — Fetches archived URLs from [archive.org (Wayback Machine)](https://web.archive.org)
- **DNS Enumeration** — Subdomain discovery using DNS dumpster and DNS resolution
- **Secret Key Scanning** — Detects exposed API keys, tokens, credentials, and secrets in page content
- **Regex Filtering** — Include or exclude URLs using regular expressions
- **Export Formats** — Export results to CSV, JSON, HTML, or SQLite
- **Website Cloning** — Download and mirror websites for offline analysis
- **Proxy Support** — HTTP/HTTPS/SOCKS proxy support (including authentication)
- **Cookie Support** — Authenticated crawling with session cookies
- **User-Agent Rotation** — Custom User-Agent header with rotation support
- **Custom Seed URLs** — Additional starting points for crawling
- **Sitemap & Robots.txt** — Automatic parsing of sitemap.xml and robots.txt

## Installation

### Option 1: Direct (Linux / macOS)

```bash
git clone https://github.com/rootx/RootXCrawler.git
cd RootXCrawler
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Option 2: Docker

```bash
git clone https://github.com/rootx/RootXCrawler.git
cd RootXCrawler
docker build -t rootxcrawler .
docker run rootxcrawler -u https://example.com
```

## Usage

```
python rootxcrawler.py -u <URL> [options]
```

### Basic Crawl

```bash
python rootxcrawler.py -u https://example.com
```

### Crawl with Depth, Threads, and Delay

```bash
python rootxcrawler.py -u https://example.com -l 3 -t 10 -d 1
```

### Export Results

```bash
python rootxcrawler.py -u https://example.com -e json -o ./output
```

### Using a Proxy

```bash
python rootxcrawler.py -u https://example.com -p 127.0.0.1:8080
```

### Authenticated Crawl with Cookies

```bash
python rootxcrawler.py -u https://example.com -c "sessionid=abc123; token=xyz"
```

### Regex Filtering and Exclusions

```bash
python rootxcrawler.py -u https://example.com -r "\.php" --exclude "\.css|\.png"
```

### Full Reconnaissance

```bash
python rootxcrawler.py -u https://example.com -l 5 -t 20 -e csv --dns --keys --wayback --verbose
```

### Website Cloning

```bash
python rootxcrawler.py -u https://example.com --clone --headers
```

### Extract URLs Only

```bash
python rootxcrawler.py -u https://example.com --only-urls -o ./urls
```

### Load Configuration from JSON

```bash
python rootxcrawler.py --config config.json
```

## Arguments

### Options

| Argument | Description |
|----------|-------------|
| `-u`, `--url` | Root URL to begin crawling from |
| `-c`, `--cookie` | HTTP cookie header value for authenticated requests |
| `-r`, `--regex` | Regular expression to filter or match URLs |
| `-e`, `--export` | Output format: `csv`, `json`, `html`, `sqlite` |
| `-o`, `--output` | Output directory for results |
| `-l`, `--level` | Maximum crawl depth (default: unlimited) |
| `-t`, `--threads` | Number of concurrent threads (default: 10) |
| `-d`, `--delay` | Delay in seconds between requests |
| `-v`, `--verbose` | Enable detailed logging |
| `-s`, `--seeds` | Additional seed URLs |
| `--stdout` | Print output variables to stdout |
| `--user-agent` | Custom User-Agent header(s) — use `\|\|` separator for rotation |
| `--exclude` | Regex pattern to exclude URLs |
| `--timeout` | HTTP request timeout in seconds (default: 10) |
| `-p`, `--proxy` | Proxy server (IP:PORT or DOMAIN:PORT) |
| `--config` | Load configuration from JSON file |

### Switches

| Argument | Description |
|----------|-------------|
| `--clone` | Clone website content locally |
| `--headers` | Include HTTP headers in requests/output |
| `--dns` | Enumerate subdomains and DNS information |
| `--keys` | Scan for exposed secret keys and credentials |
| `--update` | Update RootXCrawler to the latest version |
| `--only-urls` | Extract URLs only (no content analysis) |
| `--wayback` | Fetch historical URLs from archive.org |

## Configuration File

You can load settings from a JSON file with `--config`:

```json
{
  "root": "https://example.com",
  "level": 3,
  "threads": 20,
  "export": "json",
  "output": "./results",
  "dns": true,
  "keys": true,
  "wayback": true,
  "verbose": true
}
```

## Directory Structure

```
RootXCrawler/
├── rootxcrawler.py          # Main entry point
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build file
├── core/
│   ├── colors.py            # Terminal color definitions
│   ├── config.py            # Configuration defaults
│   ├── flash.py             # Flash message handler
│   ├── mirror.py            # Website cloning module
│   ├── prompt.py            # Interactive prompt handler
│   ├── regex.py             # Regular expression patterns
│   ├── requester.py         # HTTP request handler
│   ├── updater.py           # Update mechanism
│   ├── user-agents.txt      # User-Agent strings database
│   ├── utils.py             # Utility functions
│   └── zap.py               # robots.txt & sitemap parser + Wayback
└── plugins/
    ├── dnsdumpster.py       # DNS enumeration plugin
    ├── exporter.py          # Results export (CSV/JSON/HTML/SQLite)
    ├── find_subdomains.py   # Subdomain discovery
    └── wayback.py           # Archive.org integration
```

## Dependencies

- Python 3.2+
- `requests` — HTTP library
- `requests[socks]` — SOCKS proxy support
- `urllib3` — HTTP connection pooling
- `tld` — Top-level domain extraction

## License

MIT License

## Author

**rootx**
