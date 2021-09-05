import pandas as pd
import collections
import re

inputFile = "sre-challenge.log"

def parser(pattern, file_name):
    arr=[]
    response_ms_list=[]
    bytes_list=[]
    line_regex = re.compile(r".*" + pattern +".*$")
    with open(inputFile) as f:
        for line in sorted(f):
            if (line_regex.search(line)):
                print(line)

                # Using regular expression to search log for specific values and then save value to list
                response_time = re.search('reponseTime::(.+?)ms', line)
                if response_time:
                    found = response_time.group(1)
                    response_ms_list.append(found)

                print('Response Time: ' + found + 'ms')

                # Using regular expression to search log for specific values and then save value to list
                no_bytes = re.search('bytes::(.+?) ', line)
                print(no_bytes)
                if no_bytes:
                    found = no_bytes.group(1)
                    print(found)
                    bytes_list.append(found)

                print('Bytes: ' + found)
                
                # Find sum of occurences text 'status::*' is found in list 'arr'
                error_403_count = sum('status::403' in s for s in arr)
                error_500_count = sum('status::500' in s for s in arr)
                success_200_count = sum('status::200' in s for s in arr)
               
                my_string = line.replace("method::", "")
                my_string = my_string.replace("path::/", "")
                my_string = my_string.replace("host::", "")
                my_string = my_string.replace("reponseTime::", "")
                my_string = my_string.replace("protocol::", "")
                arr.append(my_string)

         # Map list str to list int in order to perform sum function
        response_ms_list = list(map(int, response_ms_list))
        total_response_ms = sum(response_ms_list)
        print("Total Response time for service: " + str(total_response_ms) + "ms")

        # Map list str to list int in order to perform sum function
        bytes_list = list(map(int, bytes_list))
        total_bytes = sum(bytes_list)
        print(total_bytes)
        print("Total number of bytes for service: " + str(total_bytes))

        print(pattern + " application has a total count of 403 errors: " + str(error_403_count))
        print(pattern + " application has a total count of 500 errors: " + str(error_500_count))
        print(pattern + " application has a total count of 200 success: " + str(success_200_count))
        print("\n")

    with open(file_name,'w') as file:
        for line in arr:
            new_string = line.replace("status::", "")
            new_string = new_string.replace("bytes::", "")

            if (line_regex.search(line)):
                file.write(new_string)
                file.write('\n')


    df = pd.read_csv(file_name, header=None, delimiter=' ')
    df['total 403 errors'] = pd.Series([error_403_count])
    df['total 500 errors'] = pd.Series([error_500_count])
    df['total 200 success'] = pd.Series([success_200_count])
    df['total no bytes'] = pd.Series([total_bytes])
    df['total response time(ms)'] = pd.Series([total_response_ms])
    df.rename(columns={0: 'timestamp', 1: 'method', 2: 'path', 3: 'host', 4: 'responseTime', 5: 'status', 6: 'bytes', 7: 'protocol'}, inplace=True)
    df.to_csv(file_name, index=False) # save to new csv file


# parse inputFile = sre-challenge.log and pass service name/pattern to create a file for eg. ($service, filename.csv)
parser("facebook", "output/facebook.csv")
parser("instagram", "output/instagram.csv")
parser("weather", "output/weather.csv")
parser("profile", "output/profile.csv")
parser("upload-media", "output/upload-media.csv")
parser("profle", "output/profle.csv")