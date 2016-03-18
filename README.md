# Filter Proxy
#### An HTTPS proxy capable of filtering by URI domain and path
Intended to enable redirecting https traffic on for testing API development on existing apps without modifying client code.

## Installation
Install mitmproxy
```bash
brew install mitmproxy
```

Prepare your Mac to act as a transparent proxy, re-routing http and https traffic through mitmproxy
```bash
sudo pfctl -f filter_proxy/pf.conf
```

## Running filter proxy
Enable pf re-routing and start mitmproxy
```bash
sudo pfctl -e
mitmproxy -T --host -s 'filter_proxy/redirect.py api.example.com /apiPrefix localhost 3000'
```

## Shutdown
Disable http/https re-routing
```bash
sudo pfctl -d
```
