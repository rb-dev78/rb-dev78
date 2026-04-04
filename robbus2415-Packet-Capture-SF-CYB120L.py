########################################
## Assessment: Packet Capture Starter ##
##         ROBBUS2415 - CYB120L       ##
########################################


#############################
## Part 1: Writing to File ##
#############################

## 1. Predict ##
## On Document

## 2. Observe ##
#with open("packet_summary.txt", "w") as file:
#    file.write("2025-08-22 10:01:33, 192.168.1.20 -> 10.0.0.5, TCP, 512\n")
#    file.write("2025-08-22 10:01:35, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")

## 3. Analyze ##
##with open("packet_summary.txt", "w") as file:
##    file.write("2025-08-22 10:01:33, 192.168.1.20 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:35, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")
##    file.write("2025-08-22 10:02:00, 192.168.1.25 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:12, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")

## 4. Experiment ##

##with open("packet_summary.txt", "a") as file:
##    file.write("2025-08-22 10:01:33, 192.168.1.20 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:35, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")
##    file.write("2025-08-22 10:02:00, 192.168.1.25 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:12, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")

## 5. Challenge Thinking ##

##with open("packet_summary.txt", "w") as file:
##    file.write("2025-08-22 10:01:33, 192.168.1.20 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:35, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")
##    file.write("2025-08-22 10:02:00, 192.168.1.25 -> 10.0.0.5, TCP, 512\n")
##    file.write("2025-08-22 10:01:12, 10.0.0.5 -> 192.168.1.0, UDP, 128\n")

## 6. Extend ##

##data = input("Enter packet data (timestamp, source -> destination, protocol, size): ")
##with open("packet_summary.txt", "a") as file:
##    file.write(data + "\n")
##print("Packet data added.")


#################################
## Part 2. Reading from a File ##
#################################

## 1. Predict ##
## On document

## 2. Observe ##
##with open("Packet_summary.txt", "r") as file:
##    for line in file:
##        print(line.strip())

## 3. Analyze ##
##with open("packet_summary.txt", "r") as file:
##          for line in file:
##              print(line.strip())
          
## 4. Experiment ##

##with open("packet_summary.txt", "r") as file:
##    for line in file:
##        parts = line.strip().split(",")
##        size = int(parts[-1])
##        if size >= 500:
##            print(line.strip())


## 5. Challenge Thinking ##
## On document

## 6. Extend ##

##pcount = {}
##with open("packet_summary.txt", "r") as file:
##    for line in file:
##        parts = line.strip().split(",")
##        prot = parts[2].strip()
##        if prot in pcount:
##            pcount[prot] += 1
##        else:
##            pcount[prot] = 1
##print(pcount)

############################################
## Part 3. Creating a Summary Report File ##
############################################

## 1. Predict ##
## On document

## 2. Observe ##
##with open("pcap_report.txt", "x") as file:
##          file.write("Packet Summary Report\n")

## 3. Analyze ##

##count = 0
##with open("packet_summary.txt", "r") as file:
##          for line in file:
##              count += 1
##with open("pcap_report.txt", "w") as file:
##          file.write("Total packets:" + str(count))

## 4. Experiment ##
##from datetime import datetime 
##now = datetime.now()
##with open("pcap_report.txt", "a") as file:
##    file.write("\nReport Time: " +str(now))

## 5. Challenge Thinking ##
## On document

## 6. Extend ##

pcount = {}
lcount = 0
with open("packet_summary.txt", "r") as file:
    for line in file:
        parts =  line.strip().split(",")
        ptype = parts[2].strip()
        size = int(parts[-1])
        if ptype in pcount:
            pcount[ptype] += 1
        else:
            pcount[ptype] = 1
        if size >= 500:
            lcount += 1
with open("pcap_report.txt", "a") as file:
    file.write("\nTotal packets by protocol:\n")
    for p in pcount:
        file.write(f"{p}: {pcount[p]}\n")
    file.write(f"\nTotal packets with size > 500: {lcount}\n")
               

    

          
                  
