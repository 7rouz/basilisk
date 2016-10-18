# Basilisk

This project helps to download songs from a youtube playlist in mp3 format.
TODO: More details about the project description

## Installation

This project uses selenium and selenium needs a webdriver. Here is where and how to insatll it.
 We have chosen Firefox: 
 1. Find here the latest release of gecko: https://github.com/mozilla/geckodriver/releases
 2. Download the tar file that matches your operating system
 3. extract it some where using this command :
  ```
  tar zxvf /path/to/downloaded/geckodriver-vx.x.x-os.tar.gz
  ```
 4. move geckodriver to /usr/local/bin using this command :
 ```
  sudo mv geckodriver /usr/local/bin
 ```
 last step is needed so that geckodriver could be found in PATH (you can add its path to PATH instead)
 
TODO: Describe the installation process

## Usage
 To get the list of videos in a playlist 
```
python3 parse.py [YOUTUBE_playlist_url]
```

 To download a song :
For this one we will need to create a virtual env to messing up you environment. To do so follow these steps:
1. create the virtual env:
 ```
 virtualenv -p /usr/bin/python3 py3env
 ```
2. activate the virtual env:
```
source py3env/bin/activate
```
Then we need to install selenium in our virtual env
```
pip install selenium
```
now we can run downloader using this command:
```
python3 downloader.py 
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license

## Authors

* **Rafik Harzi** - *Initial work* - [7rouz](https://github.com/7rouz)
