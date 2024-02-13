# 0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter
## Concepts
=========================================================================================
## 0. What happens when you type `https://www.google.com` in your browser and press Enter
=========================================================================================
> - The browser checks the cache for a DNS record to find the IP address of `www.google.com`.
> - If the browser finds a cache, it stops and uses it.
> - If the browser does not find the DNS record in the cache, it will send a DNS request to the OS.
> - The OS will look at its cache, and if the record is found, it will be returned to the browser.
> - If the OS does not find the record, it will send a DNS request to the DNS server.
> - The DNS server looks at its cache, and if the record is found, it will be returned to the OS.
> - If the DNS server does not find the record, it will send a DNS request to the root server.
> - The root server will refer the DNS server to the `.com` TLD.
> - The DNS server will send a request to the `.com` TLD.
> - The TLD server will refer the DNS server to the `google.com` authoritative server.
> - The DNS server will send a request to the authoritative server for `google.com`.
> - The authoritative server will return the IP address for `www.google.com` to the DNS server.
> - The DNS server will return the IP address to the OS.
> - The OS will pass the IP address to the browser.
> - The browser will make a HTTP request to the IP address.
> - The server at the IP address will return the webpage to the browser.
=========================================================================================
