import Genetics
import numpy as np
import csv
import time

def main():
    max_th = 2.0
    max_sil = 4.0
    max_snd = 4.0
    filename = str( input(f"Inserte el nombre del archivo a segmentar: ") )
    desired_time = float( input(f"Inserte el tiempo promedio deseado (s): ") )
    desired_audios = float( input(f"Indique la cantidad de audios deseada: ") )
    desired_std_dev = float( input(f"Inserte la desviación estándar máxima deseada: ") )
    start = time.perf_counter()
    max_pop = 10
    mutation = 0.3
    first = True
    population = Genetics.Population(max_pop, mutation, desired_time, desired_audios, desired_std_dev, filename)
    generations = np.array([])
    generation = 1
    eval = True

    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Generación", "Aptitud promedio", "Mejor Aptitud", "Segunda Mejor Aptitud", "Desviación estándar", "Duración Promedio (s)", "Cantidad de segmentos", "Silencio (s)", "Sonido (s)", "Umbral (s)"])
        file.flush()

        while (eval or first):
            print("\n********************************************************************")
            print("Generación:", generation)
            population.calculate_fitness()
           
            writer.writerow([generation, round(population.avg_fitness), population.pop[population.smallest].fitness, population.pop[population.second].fitness, 
                population.pop[population.smallest].std_dev, population.pop[population.smallest].avg_duration, population.pop[population.smallest].audios, 
                round(population.pop[population.smallest].genes[0],2), round(population.pop[population.smallest].genes[1],2) , round(population.pop[population.smallest].genes[2], 2) ])

            file.flush()

            eval = population.evaluate()
            population.next_generation()

            generation += 1
            first = False


if __name__ == '__main__':
    main()
