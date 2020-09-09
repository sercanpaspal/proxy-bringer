#Proxy Bringer
Python class that checks free proxy addresses periodically and brings up-to-date proxy.

##Usage
```python
proxy_bringer = ProxyBringer(debug=True, check_interval=60)
# start checking
proxy_bringer.start()
# get proxy when finished checking
proxy = proxy_bringer.get_proxy()
```

#####Defaults
```python
debug=True #print processes
check_interval=60 #second
```