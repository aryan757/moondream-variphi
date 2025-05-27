import moondream as md
from PIL import Image , ImageDraw

# Initialize for Moondream Cloud
model = md.vl(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiI2YzkyNTVjMy04YTY5LTQyODgtOGMwNi1mNzljNjJlODFjYmMiLCJvcmdfaWQiOiJmeWdKb1ZsS2l6SGF4dGkwTEk4YjFjcUlkV3ZLd3BDUyIsImlhdCI6MTc0ODMyOTkzMCwidmVyIjoxfQ.nmqSfQsExP_yxZ6ezicg1qCb8mSAfQdg5qlCjCDOgug")


# Load an image
image = Image.open("image.jpg")


# Generate a caption (normal length)
caption = model.caption(image,length="normal")["caption"]
print("Caption:", caption)


# Generate a caption (long length)
caption = model.caption(image,length="long")["caption"]
print("Caption:", caption)

# Generate a caption (short length)
caption = model.caption(image,length="short")["caption"]
print("Caption:", caption)





#Asking query
answer = model.query(image, "What is the text in the image?")
print("Answer:", answer)


# Detecting the object
img = Image.open("image.jpg")
boxes = model.detect(img, 'leters')['objects']

print(boxes)

#draw boxes on the image
ov = img.copy()
d = ImageDraw.Draw(ov)
w,h = ov.size

for b in boxes:
        d.rectangle([
        int(b['x_min'] * w),
        int(b['y_min'] * h),
        int(b['x_max'] * w),
        int(b['y_max'] * h)
    ], outline='red', width=3)

##save the annotated image
ov.save("annotated_image.jpg")
print("Annotated image saved as annotated_image.jpg")


# pointing the detected object .
img = Image.open("image.jpg")
points = model.point(img, 'leters')['points']
print(points)


# #Draw boxes and points on the image
# ov = img.copy()
# d = ImageDraw.Draw(ov)
# w, h = ov.size


for p in points:
    r = 4
    d.ellipse([
        int(p['x'] * w) - r, int(p['y'] * h) - r,
        int(p['x'] * w) + r, int(p['y'] * h) + r
    ], fill='blue')



#save the annotated image
ov.save("annotated_image_points.jpg")
print("Annotated image with points saved as annotated_image_points.jpg")









