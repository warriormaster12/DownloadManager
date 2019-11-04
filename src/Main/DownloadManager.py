import os 


os.system("./Updater.sh")
store_status= os.system("cat Updater.sh | grep check_updates")
print(store_status)
