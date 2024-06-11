import speedtest

wifi = speedtest.Speedtest()

print("Download Speed: ", round(wifi.download()/1048576), " Mbps")
print("Upload Speed: ", round(wifi.upload()/1048576), " Mbps")
