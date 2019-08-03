import librosa
import numpy as np
import matplotlib.pyplot as plt
from librosa import display

def mel_spec(f):
    y, sr = librosa.load('media/'+f.file.name)
    print('\033[92m'+"The length of uploaded file and its Sampling Rate, respectively, are:\n")
    print(len(y),sr)
    spect = librosa.feature.melspectrogram(y=y, sr=sr,n_fft=2048, hop_length=1024)
    spect = librosa.power_to_db(spect, ref=np.max)
    # spect = np.log(spect)
    print(spect.shape)
    print("Saving image file ...")
    def full_frame(width=None, height=None):
        plt.rcParams['savefig.pad_inches'] = 0
        figsize = None if width is None else (width, height)
        plt.figure(figsize=figsize,dpi=100)
        ax = plt.axes([0,0,1,1], frameon=False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.autoscale(tight=True)

    full_frame()
    librosa.display.specshow(spect, y_axis='mel', fmax=8000, x_axis='time')
    plt.axis('off');
    a = plt.savefig(f'media/{f.file.name}.png')
    # plt.show()
    plt.clf()
