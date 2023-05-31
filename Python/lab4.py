#ask the user for three sensor values
sensor1 = input("Enter the value of sensor 1: "))
sensor2 = input("Enter the value of sensor 2: "))
sensor3 = input("Enter the value of sensor 3: "))
#create a dictionary, list, and tuple to store the values
sensor_dict = {"sensor1": sensor1,
               "sensor2": sensor2, 
               "sensor3": sensor3}
sensor_list = [sensor1, sensor2, sensor3]
sensor_tuple = (sensor1, sensor2, sensor3)
#print the values stored in the dictionary, list, and tuple
print("dictionary: ", sensor_dict)
print("list: ", sensor_list)
print(" tuple: ", sensor_tuple)