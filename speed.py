import speedtest
import json

results_file = open("results.txt", "a")
verbose_results = open("verbose.txt", "a")

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()

print(results_dict)

download_speed = results_dict['download']/1000000
upload_speed = results_dict['upload']/1000000
ping = results_dict['ping']
timestamp = results_dict['timestamp']

dump_string = f"\n\nRUN AT: {timestamp}\nDOWNLOAD SPEED: {download_speed} Mbps\nUPLOAD SPEED: {upload_speed} Mbps\nPING: {ping} ms\n---------------------"

results_file.write(dump_string)
verbose_results.write(json.dumps(results_dict)+"\n-------------\n")