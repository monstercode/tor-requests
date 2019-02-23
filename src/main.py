import request_thread

proxies = {'http': 'socks5h://tor:9050', 'https': 'socks5h://tor:9050'}

threads = []
for x in range(0,10):
	threads.append(request_thread.RequestThread(x, proxies))

for t in threads:
    t.start()

for t in threads:
    t.join()
