# Implementación de una interfaz de visualización para algoritmos genéticos en un sistema de segmentación de audios de larga duración

## Tabla de contenidos:

1. [Descripción breve](#descBreve)
2. [Objetivos](#objetivos)
3. [CHANGELOG y tareas a realizar](#changelog)
4. [Dependencias](#dependencies)
5. [Instalar el proyecto](#install)
6. [Notas hacia los profesores guía y lectores](#avisos)

## Descripción breve  <a name="descBreve"></a>

La utilización de audios de larga duración como fuente de información para el análisis del habla y el desarrollo de sistemas de síntesis y reconocimiento de voz ha recibido interés en la comunidad científica, dado el interés creciente en el desarrollo de asistentes virtuales y de aplicaciones que procesan la voz. Para aprovechar recursos como podcast o audiolibros disponibles en Internet para este fin, se deben segmentar los audio, lo cual usualmente se realiza de forma manual, o bien utilizando herramientas que detecten silencios. Esta detección requiere el ajuste de una serie de parámetros que pueden llevar a una buena o mala segmentación. Por esta razón se han propuesto estrategias como los algoritmos genéticos para automatizar el proceso de ajuste, pero no se cuenta con una interfaz que permita visualizar y verificar su funcionamiento, de manera que se pueda adoptar como una herramienta en procesos de investigación y de aprovechamiento de recursos de habla.

## Objetivos <a name="objetivos"></a>

### Objetivo general

Desarrollar una interfaz de visualización de los resultados de algoritmos genéticos para optimizar un conjunto de parámetros en un sistema de segmentación de audios de larga duración.

### Objetivos específicos

1. Analizar un sistema de segmentación de audios de larga duración para incorporar una etapa de visualización de resultados, usando algoritmos genéticos.
2. Comprender los conceptos asociados con algoritmos genéticos para problemas de optimización.
3. Desarrollar una interfaz en lenguaje Python para visualizar los resultados un proceso de algoritmos genéticos.
4. Definir un conjunto de datos de prueba para verificar los resultados y el funcionamiento del algoritmo.

## CHANGELOG y tareas a realizar <a name="changelog"></a>

El CHANGELOG es mantenido en el repositorio de GitHub.

### Tareas a realizar:

##### Académicas

* Capítulo I del avance del proyecto [En revisión por los profesores]

#### Desarrollo de software

* Determinar dependencias [En constante cambio todavía]

* Diagramas de flujo del programa

## Dependencias <a name="dependencies"></a>

Las dependencias están sujetas a cambios conforme se avanza en el proyecto, por el momento tales son:

- SoX
```
sudo apt-get install sox
```
- python3
```
sudo apt-get install python3
```
- python3-numpy
```
sudo apt-get install python3-numpy
```
- python3-pandas
```
sudo apt-get install python3-pandas
```

## Instalar el proyecto <a name="install"></a>

Clonar el repositorio del proyecto con:

```
git clone https://github.com/leus8/ie0499-GAVisualizer.git
```

> Para seguir con los siguentes pasos asegurarse que se han instalado todas las [Dependencias](#dependencies)

...

## Notas hacia los profesores guía y lectores <a name="avisos"></a>

En caso de dudas y recomendaciones pueden levantar un *issue* aquí en GitHub o me pueden contactar por correo/telegram.
