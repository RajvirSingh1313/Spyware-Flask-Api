# Spyware-Flask-Api 🕵️

## Why & What
This is a little tiny api for my brother so i could sneek into his pc. I am creating this repo for demostration if you want to use it you would have to host it on heroku or pythoneverywhere, etc. And I am not responsible if your brother give you reply with a new spyware so I am out of family matters hehe. Just Kidding.

## How it Works?
![How it works](https://github.com/RajvirSingh1313/Spyware-Flask-Api/blob/main/How%20it%20works.png)

### Client.py
Takes Screenshot every 10 second or as you wish but remember the pictures can be alot as time pass so I have function which will automatically deletes data after 1 hour so our api don't suffer from less data space. After taking screenshot it saves the image in jpg format as it is low size format, also we uses pillow to decrease quality as we care more about size then quality and then converts into binary and then sends it in json post request to the api.

### Server/App.py
It have two end points one is ``/`` which is only POST and second one is ``/data`` which is GET endpoint for our reader script to fetch data. So when client script sends a post request on the ``/`` endpoint, We first checks whether the existing data is been more than hour or so if yes then we clear the table and then we again fill it, then the app.py or api converts it again into binary from json string and then stores it into sqlite database with low quality as we need to make them as compact as possible. Now when me or the spy wants to see the images, we need to fetch data, so api provides a get endpoint for that, when reader makes a get request we just read the binary from the database and then decode it with utf-8. Then we return data with json reponse.

### Reader.py
It fetches the latest image from the api and then writes the binary to a bin file and then writes that bin file's content into jpg image.

## Have good day folks!
