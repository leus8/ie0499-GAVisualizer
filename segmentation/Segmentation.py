#!/usr/bin/python
import os
import subprocess
import string
import glob
import statistics
import sox
import time

class Segmentation(object):

    def __init__(self, inst_number, sil, snd, thd):
        # print("Creando instancias...")
        self.inst_number = inst_number
        self.durations_list = []
        self.std_dev = 0.0
        self.average = 0.0
        self.silence = sil
        self.sound = snd
        self.threshold = thd
        self.durations_dict = {}
        self.avg_duration = 0.0
        self.audios = 0
        # print("Instancias creadas")

    def segment_audio(self, file_name, dna_num):

        folder_name = ' splitted' + str(dna_num)

        if(os.path.exists('./'+ folder_name )==False):

            os.system("mkdir " + folder_name)
        subprocess.call('sox ' + file_name +   folder_name + '/out.wav silence ' + '1' + ' '
        + str(self.sound) + ' ' + str(self.threshold) + ' ' + '1' + ' ' + str(self.silence) + ' '
        + str(self.threshold) + ' : newfile : restart' , shell=True)



    def get_avg_duration(self, dna_num): #Obtener las duraciones de los segmentos, se guardan en datos.txt y se retorna una lista con las duraciones en orden
        # print("         Obteniendo duración de los audios...")

        all_files = sorted(glob.glob("./splitted" + str(dna_num) + "/out*"))
        self.durations_list = []


        for file in all_files:
            duration = subprocess.getoutput('soxi -D ' + file)
            self.durations_dict[file[11:]] = duration

            duration = float(duration)
            # time.sleep(0.6)

            self.durations_list.append(round(duration, 2))
            # if (duration.isnumeric()):
            #     self.durations_list.append(round(duration, 2))
            # else:
            #     print('MENSAJE ERRORRRRRRRRRRR DURATIONNNNNNNN')

            # duration = sox.file_info.duration(file)
            # if (duration == None):
            #     duration = 0.0
            # self.durations_list.append(round( float(duration) ,2))

        # print(self.durations_list)
        for duration in self.durations_list:
            self.avg_duration = self.avg_duration + duration
            self.audios = self.audios + 1
        self.avg_duration = self.avg_duration/self.audios
        # print("avg_duration", self.avg_duration)
        # print("         Duracion obtenida\n")

    def delete_audio(self, dna_num):
        # print("         Eliminando audios...")
        folder_name = ' splitted' + str(dna_num)
        os.system("rm ./splitted" + str(dna_num) + "/*")
        # print("         Audios eliminados!\n")
        os.system("rm -r" + folder_name)

    def get_std_dev(self): #Obtengo la desviacion estandar de las duraciones de los segmentos
        # print("         Obteniendo desviación estándar...")
        lista = self.durations_list
        self.std_dev = round(statistics.pstdev(lista),2)
        # print("         Desviación estándar obtenida y guardada!\n")
