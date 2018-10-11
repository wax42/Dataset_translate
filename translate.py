# -*-coding:utf-8 -*
import os
from textblob import TextBlob
import pprint
import io

def load_dataset():
    """ Telecharge le fichier et le decompresse
    http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz """
    if os.path.isfile("save.tar.gz") == False:
        os.system("curl -S http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz > save.tar.gz")
        print('\033[92m Dataset successful load\033[0m')
    else:
        print('\033[93m Dataset already load\033[0m')
    if os.path.isdir("aclImdb") == False:
        os.system("tar -zxvf save.tar.gz")
        print('\033[92m Tar successful uncompress\033[0m')
    else:
        print('\033[93m Tar already uncompress\033[0m')


def copy_directory(directory, copy_directory):
    list = os.listdir(directory)
    for i in list:
        if os.path.isdir(directory + '/' + i):
            if os.path.isdir(copy_directory + '/' + i) == False:
                os.mkdir(copy_directory + '/' + i)
                print('\033[92m Folder {} created \033[0m'.format(copy_directory + '/' + i))
            else:
                print('\033[93m Warning folder {} already created \033[0m'.format(copy_directory + '/' + i))
            list2 = os.listdir(directory + '/' + i)
            for l in list2:
                if os.path.isdir(directory + '/' + i + '/' +  l):
                    if os.path.isdir(copy_directory + '/' + i + '/' + l) == False:
                        os.mkdir(copy_directory + '/' + i  + '/' + l)
                        print('\033[92m Folder {} created \033[0m'.format(copy_directory +  "/" + i + "/" + l))
                    else:
                        print('\033[93m Warning folder {} already created \033[0m'.format(copy_directory +  "/" + i + "/" + l))
                else:
                    pass
        else:
            pass
            # print("jack")

def decrypt_textblob(blob):
    encrypted_blob = base64.b64decode(blob)
    decrypted_text = data_protector.decrypt_text(encrypted_blob)
    print(decrypted_text)

def translate(directory_to_translate, copy_directory):
    """"" Translate in the same filename"""
    list = os.listdir(directory_to_translate)
    for i in list:
        if os.path.isfile(copy_directory + '/' + i) == False:
            with open(directory_to_translate + '/' +  i ,'r') as handle:
                print('\033[92m {}\033[0m'.format(directory_to_translate + '/' +  i ))
                text = handle.read()
                blob = TextBlob(text)
                text_translate = blob.translate(to='fr')  # type: object
                with open(copy_directory + '/' + i, 'w') as jack:
                    jack.write(str(text_translate))
        else:
            print('\033[93m {} already translate \033[0m'.format(directory_to_translate + '/' + i))


def create_copy():
    if os.path.isdir("aclImdb_fr") == False:
        os.mkdir("aclImdb_fr")
        print('\033[92m Folder aclImdb_fr successful created \033[0m')
    else:
        print('\033[93m Folder aclImdb_fr already created\033[0m')
    copy_directory("aclImdb", "aclImdb_fr")




def main():
    print('\n\033[92mWorking directory : {}\033[0m'.format(os.getcwd()))
    load_dataset()
    create_copy()
    translate("aclImdb/train/pos", "aclImdb_fr/train/pos")
    translate("aclImdb/train/neg", "aclImdb_fr/train/neg")
    translate("aclImdb/train/neg", "aclImdb_fr/test/pos")
    translate("aclImdb/train/neg", "aclImdb_fr/test/neg")
    translate("aclImdb/train/unsup", "aclImdb_fr/train/unsup")


if __name__ == "__main__":
    main()
