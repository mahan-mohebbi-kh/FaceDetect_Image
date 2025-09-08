import cv2

#بارگذاری مدل تشخیص چهره (فایل مدل باید در کنار کد موجود باشه)
model = cv2.CascadeClassifier("model.xml")

#نمایش پیام راهنما و دریافت مسیر تصویر از کاربر
print("<< example : D:\Folder\image.jpg >>")
image_path = input("Enter the image path : ")

#خواندن تصویر ورودی
img = cv2.imread(image_path)

while True:

    #ایجاد یک کپی از تصویر برای رسم مستطیل ها
    img_copy = img.copy()

    #تشخیص چهره ها در تصویر
    faces = model.detectMultiScale(img , 1.1 , 4)

    #حلقه روی تمام چهره های پیدا شده
    for (x , y , w , h) in faces:

        #رسم مستطیل دور هر چهره شناسایی شده
        cv2.rectangle(img_copy , (x,y) , (x+w , y+h) , (255 , 0 , 0) , 2)

    #نمایش تصویر با چهره های شناسایی شده
    cv2.imshow("Face Detect" , img_copy)

    #زده شد، از حلقه خارج شود esc اگر کلید
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#بستن تمام پنجره های باز شده توسط کتابخانه
cv2.destroyAllWindows()
