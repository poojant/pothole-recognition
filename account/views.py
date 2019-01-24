from django.http import HttpResponse
from django.shortcuts import render
from account.restore_model_code import ModelSignature
import array as arr
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyrebase
config = {
  "apiKey": "AIzaSyDhw586_yQeeNM_bEyopI275pEgmV9OjkQ",
  "authDomain": "ezcommuter.firebaseapp.com",
  "databaseURL": "https://ezcommuter.firebaseio.com",
  "storageBucket": "ezcommuter.appspot.com",
  "serviceAccount": "C:/Users/Poojan/Downloads/ezcommuter-8d0be99c1e2a.json"
}
firebase = pyrebase.initialize_app(config)
def index(request):

    pnum_get = request.GET.get('pnum')
    pnum_token = request.GET.get('token')
    db = firebase.database()
    #if pnum_get is not None and pnum_get != '':
    #args = {'pnum': pnum_get}


    m = ModelSignature("Signature_Test", output_folder=None)
    print(type(m))

    m.load("C:/Users/Poojan/Desktop/Projects/ETL Django/potholerecog/account/checkpoints/restoreModel")

    """images3 = []
    path = sorted(list(paths.list_images("drive/My Drive/CommuterSafetyCapsules/TestDataSet")))
    # Read all image into the folder
    for imagePath in path:
      image = cv2.imread(imagePath.replace("\\",""))
      image = cv2.resize(image,(64, 64),3)
      plt.imshow(image)
      plt.show()
      image = np.array(image) / 255
      images3.append(image)

    predictions=m.predict(images3)

    print(predictions[1])
    """
    #run the next 3 blocks for predictions
        
    a = arr.array('i',[1,2,3])#,4,5,6,7,8,9,10,11,12])
    predicted_id_to_user = ["001","002","Pothole"]#,"004","005","006","007","008","009","010","011","012"]

    images1 = []
    """path = sorted(list(paths.list_images("drive/My Drive/CommuterSafetyCapsules/TestDataSet")))
    # Read all image from the folder
    for imagePath in path:
      image = cv2.imread(imagePath.replace("\\",""))
      image = cv2.resize(image,(64, 64),3)
      plt.imshow(image)
      plt.show()
      image = np.array(image) / 255
      images1.append(image)
    """
    import urllib
    #path = pnum_get#"C:/Users/Poojan/Desktop/Projects/ETL Django/potholerecog/account/static/trainchat.png"#imgurl
    import cv2
    import urllib.request
    import urllib.parse
    import numpy as np

    #pnum_get = urllib.parse.quote_plus(pnum_get)
    imt = pnum_get+"&token="+pnum_token
    imt = imt.replace('2/','2%2F')
    print("HELLLLLLLLLLLO ",pnum_get)
    print("KOKOKOKOKOKOKOK",pnum_token)
    print("POPOPOPOPOPO",imt)
    #imt = urllib.parse.quote_plus(imt)
    req = urllib.request.urlopen(imt)
    #"https://firebasestorage.googleapis.com/v0/b/csmvscommunity.appspot.com/o/0Siae2fwxwhTWPSJfSrlwp8s3Z42%2F1546077224722?alt=media&token=5a36fb08-84e0-4867-b25a-68fffe75f30d")
    ar = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(ar, -1) # 'Load it as it is'

    #image = cv2.imread(path.replace("\\",""))
    image = img
    print(image.shape)
    image = cv2.resize(image,(64, 64),3)
    image = np.array(image).reshape(1, 64,64,3)
    plt.imshow(image[0])
    #plt.show()
    image = np.array(image) / 255
    #images1.append(image)
    # Get the prediction
    predictions_for_setting_range = m.predict(image)

    # Plot the result
    fig, axs = plt.subplots(36, 2, figsize=(10, 150))

    axs = axs.ravel()
    print(predictions_for_setting_range)
    for i in range(1):
        if i%2 == 0:
            axs[i].axis('off')
            axs[i].imshow(image[0])
            if predictions_for_setting_range[0][np.argmax(predictions_for_setting_range[0])] > 60:
                #lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
                db.child("accept").set(1)
            else:
                #flag = 0
                db.child("accept").set(0)

            axs[i].set_title("Prediction: %s" % predictions_for_setting_range[0][np.argmax(predictions_for_setting_range[0])] )
        else:
            axs[i].bar(a, predictions_for_setting_range[0])
            axs[i].set_ylabel("Softmax")
            axs[i].set_xlabel("Labels")
    #a = {"flag":flag}
    plt.show()
    return HttpResponse(2)
    #return render(request,'index.html', args)
