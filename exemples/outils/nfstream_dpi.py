from nfstream import NFStreamer
my_awesome_streamer = NFStreamer(source="wlp3s0") # or network interface (source="eth0")
for flow in my_awesome_streamer:
   print(flow)  # print it, append to pandas Dataframe or whatever you want :)!
