# -*- coding: utf-8 -*-

import random
import numpy as np
import os
import glob
import time
from Segmentation import Segmentation
from multiprocessing import Pool

class Cromosome(object):
    genes = np.array([])
    fitness = 0
    std_dev = 0
    avg_duration = 0
    audios = 0
    def __init__(self):
        temp_genes = np.array(random.sample(range(4), 3))

        t_p1 = random.sample(range(4),1)
        t_p2 = random.sample(range(2),1)
        t_p3 = random.sample(range(2),1)
        p1 = t_p1[0] + random.random()
        p2 = t_p2[0] + random.random()
        p3 = t_p3[0] + random.random()
        self.genes = np.array([p1,p2,p3])

    def mutate(self, parentA, parentB, mutation_rate):
        newGenes = np.zeros(parentA.genes.shape[0])
        midPoint = random.randint(0,parentA.genes.shape[0])
        cross_direction = bool(random.getrandbits(1))
        for ix in range(len(self.genes)):

            if random.random() < mutation_rate:
                if ix == 0:
                    temp = random.sample(range(4),1)
                if ix == 1:
                    temp = random.sample(range(2),1)
                if ix == 2:
                    temp = random.sample(range(2),1)
                newGenes[ix] = temp[0] + random.random()

            else:
                if cross_direction:
                    newGenes[ix] = parentA.genes[ix] if ix < midPoint \
                                                else parentB.genes[ix]
                else:
                    newGenes[ix] = parentB.genes[ix] if ix < midPoint \
                                                else parentA.genes[ix]

        self.genes = newGenes

class Population(object):
    pop = np.array([])
    def __init__(self, max_pop, mutation, desired_time, desired_audios, desired_std_dev, filename):
        self.max_pop = max_pop
        self.smallest = 10000000
        self.avg_fitness = 0
        self.mutation_rate = mutation
        self.desired_time = desired_time
        self.desired_audios = desired_audios
        self.desired_std_dev = desired_std_dev
        self.filename = filename

        while self.pop.shape[0] < max_pop:
            self.pop = np.append(self.pop, Cromosome())


    def segmentation_fun(self, list):
        list[0].segment_audio(self.filename, list[1])
        list[0].get_avg_duration(list[1])
        list[0].get_std_dev()
        # list[0].delete_audio(list[1])
        results = np.array([None,None,None,None])

        self.pop[list[1]].fitness = abs( (list[0].avg_duration - self.desired_time)) + list[0].std_dev + abs( list[0].audios - self.desired_audios)
        results[0] = self.pop[list[1]].fitness 
        
        results[2] = list[0].avg_duration
        results[1] = list[0].std_dev
        time.sleep(1)
        results[3] = list[0].audios
        return results

    def calculate_fitness(self):
        self.smallest = 0
        self.second = 1
        self.avg_fitness = 0
        results = []
        seg_list = []
        for ix in range(self.pop.shape[0]):
            print('____________________________________________________________________')
            print('Genes del cromosoma #', ix , self.pop[ix].genes)
            seg_list.append( [ Segmentation(ix,self.pop[ix].genes[0],self.pop[ix].genes[1],self.pop[ix].genes[2]), ix] )

        with Pool(20) as p:
            results = p.map(self.segmentation_fun, seg_list)

        for ix in range(self.pop.shape[0]):
            print("Valor de aptitud # ", ix, " : ", round( results[ix][0]) )
            self.pop[ix].fitness = results[ix][0]
            self.pop[ix].avg_duration = results[ix][2]
            self.pop[ix].audios = results[ix][3]
            self.avg_fitness = self.avg_fitness + self.pop[ix].fitness
            self.pop[ix].std_dev = results[ix][1]
            seg_list[ix][0].delete_audio(ix)
            
        self.avg_fitness = self.avg_fitness/self.pop.shape[0]
        

        for ix in range(self.pop.shape[0]):
            if self.pop[ix].fitness < self.pop[self.smallest].fitness:
                self.second = self.smallest
                self.smallest = ix

            elif self.pop[ix].fitness < self.pop[self.second].fitness or ix == 1:
                if self.pop[ix].fitness != self.pop[self.smallest].fitness:
                    self.second = ix


    def next_generation(self):
        parentA = self.pop[self.smallest]
        parentB = self.pop[self.second]
        for ix in range(self.pop.shape[0]):
            child = Cromosome()
            child.mutate(parentA, parentB, self.mutation_rate)
            self.pop[ix] = child

    def evaluate(self):
        print("Mejor aptitud (Cromosoma #", self.smallest, "): ", round( self.pop[self.smallest].fitness, 2) )
        print("Segunda mejor aptitud (Cromosoma #", self.second, "): " , round( self.pop[self.second].fitness, 2) )
 
        # self.avg_fitness = self.avg_fitness / self.max_pop
        print("Aptitud promedio: ", round( self.avg_fitness, 2) )
        limit = self.desired_std_dev + self.desired_time*0.3 + self.desired_audios*0.3*4
        if (self.pop[self.smallest].fitness <= limit and self.pop[self.smallest].avg_duration > self.desired_time*0.7 
            and self.pop[self.smallest].audios > self.desired_audios*0.7):
            seg_final = Segmentation(self.smallest, self.pop[self.smallest].genes[0],self.pop[self.smallest].genes[1],self.pop[self.smallest].genes[2])
            seg_final.segment_audio(self.filename, 90000)
            seg_final.get_avg_duration(90000)
            seg_final.get_std_dev()
            print("************************* Solución óptima *************************")
            print('Desviación Estándar: ', round( seg_final.std_dev) )
            print('Duración promedio: ', round( seg_final.avg_duration) )
            print('Cantidad de audios: ', round( seg_final.audios) )
            print('Aptitud: ', round( self.pop[self.smallest].fitness) )
            return False
        else:
            return True
