    #01234       #012345
s = "Hello"; t = "Python"              #string   #ไม่สามมารถเปลี่ยนค่าของStringได้
x = [1,3,5,7]; y = [5,6,7,8]           #list     #สามารถเปลี่ยนค่าของListได้
r = s + t                              
z = x + y
#length
print(len(s), len(r), len(x), len(z))  #len ช่วงระยะ
#index
print(s[1], x[2])
print(s[-1], s[-2], x[-1], x[-2])
# slice
print(s[0:3:1])   #[start:stop:step]   #แปลS โดยให้เริ่มตั้งแต่0-3โดยนับทีละ1
x[3] = 99
print (x[3])