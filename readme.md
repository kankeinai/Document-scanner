Works only for white paper (A4) with more or less constrast background.

– converter.py converts .heic images to .jpg, usage: python converter.py dir_name

– transform.py contains function four_point_transform(image, pts) that apply perspective transformation of the document

– scan.py saves transformed images to the folder "scanned" and creates output.pdf file with all images from your dir_name folder, usage: python scan.py dir_name

Before usage create virtual environment and install needed libraries: img2pdf, imutils, pyheif (for converter), cv2, skimage

Example:
<div>
  <div width="50%">
    <img src="https://user-images.githubusercontent.com/56974757/111684968-921c7880-8851-11eb-9fbf-8d37ca730fca.png" height="450">
  </div>
  <div width="50%">
    <img src="https://user-images.githubusercontent.com/56974757/111685045-a95b6600-8851-11eb-94a0-16cf0e9da3fe.png" height="450">
  </div>
</div>
