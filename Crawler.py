import nltk

class Crawler:
    def __init__(self):
        self.url = []
        self.topic = []

    def checkReqPackage(self):
        requirements=['punkt', 'universal_tagset', 'averaged_perceptron_tagger']
        pack = nltk.downloader.Downloader()
        if(pack.is_installed(mod) for mod in requirements):
            print("All Set!!\n")
        else:
            print("Not all the required nltk packages are installed!\n")
            if(pack.is_installed(info_or_id=requirements)==False):
                print("Downloading uninstalled content....\n")
                pack.download(info_or_id=requirements)
                print("Download complete!\n")


 #   def checkFilePath(self):
