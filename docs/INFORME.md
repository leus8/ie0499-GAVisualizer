# Informe de Implementación de una interfaz de visualización para algoritmos genéticos en un sistema de segmentación de audios de larga duración


 ## Tabla de contenidos:

 1. [Capítulo 1 - Introducción](#cap1)
 2. [Capítulo 2 - Teoría del trabajo de investigación](#cap2)
 3. [Capítulo 3 - Diseño](#cap3)
 4. [Capítulo 4 - Arquitectura de software](#cap4)
 5. [Capítulo 5 - Resultados](#cap5)
 6. [Capítulo 6 - Conclusiones y recomendaciones](#cap6)

 ## Capítulo 1 - Introducción <a name="cap1"></a>
 
 La utilización de audios de larga duración como fuente de información para el análisis del habla y el desarrollo de sistemas de síntesis y reconocimiento de voz ha recibido interés en la comunidad científica, dado el interés creciente en el desarrollo de asistentes virtuales y de aplicaciones que procesan la voz. Si se quiere aprovechar recursos como podcast o audiolibros disponibles en Internet para este fin, se deben segmentar los audios, lo cual usualmente se realiza de forma manual, o bien utilizando herramientas que detecten silencios. Esta detección requiere el ajuste de una serie de parámetros que pueden llevar a una buena o mala segmentación. Por esta razón se han propuesto estrategias como los algoritmos genéticos para automatizar el proceso de ajuste, pero no se cuenta con una interfaz que permita visualizar y verificar su funcionamiento, de manera que se pueda adoptar como una herramienta en procesos de investigación y de aprovechamiento de recursos de habla.
 
 Los algoritmos genéticos reciben unos parámetros de entrada que les permite optimizar un proceso aplicando métodos muy similares a los que se encuentran en la genética y la selección natural, por esto surge el interés de tener una herramienta en el que se pueda visualizar cada una de las etapas de la evolución para poder verificar el rendimiento de los parámetros de entrada dados al algoritmo. Sumado a esto el contar con una interfaz de usuario permitirá al investigador enfocarse en el perfeccionamiento del algoritmo que está estudiando ya que no tendrá que desperdiciar tiempo en la elaboración de gráficos para poder visualizar los resultados.
 
 Se utilizará el lenguaje de programación Python para el desarrollo de la interfaz de visualización de los resultados del proceso de optimización del algoritmo genético. Este lenguaje cuenta con una comunidad amplia y en constante crecimiento de herramientas de análisis de datos y creación de interfaces de usuario que facilitará las secciones del proyecto destinadas al desarrollo del software.
 
 ### Alcance
 
 El propósito de este proyecto es desarrollar una interfaz de visualización de resultados de algoritmos genéticos de manera que facilite la optimización de un conjunto de parámetros en un sistema de segmentación de audios de larga duración.
 
 En el proyecto no se estará realizando un nuevo algoritmo genético para segmentación de audios de larga duración sino que se analizará uno ya existente de manera que se pueda incorporar una interfaz de visualización de los resultados de la optimización realizada por el algoritmo. Esto permite dirigir el enfoque del trabajo de investigación al desarrollo de la interfaz y a la verificación de su funcionamiento.
 
 La interfaz de usuario para la visualización de los resultados de la optimización de los parámetros del algoritmo genético será desarrollada en el lenguaje de programación Python. Se utilizará el paradigma de la programación orientada objetos así como las herramientas de análisis datos y creación de interfaces de usuario que cuenta el lenguaje utilizado de manera que simplifiquen las secciones del trabajo destinadas al desarrollo del software.
 
 ### Justificación
 
 Mediante este proyecto se pretende crear una herramienta que asista al investigador en el proceso de segmentación de audios de larga duración automatizado mediante algoritmos genéticos para que pueda visualizar el progreso y los resultados obtenidos del algoritmo en cada una de sus etapas de manera que se pueda agilizar la verificación de los parámetros utilizados.
 
 Con esta herramienta se pretende que el usuario limite su uso de la terminal del computador y tenga a disposición una interfaz de usuario que simplifique su trabajo de manera que no tenga que desperdiciar tiempo creando gráficos para poder visualizar los resultados obtenidos.
 
 ### Problema
 
 La utilización de algoritmos genéticos para la segmentación de audios de larga duración permite automatizar una gran parte proceso de adjuste de parámetros pero no se cuenta con una herramienta que permita visualizar ni verificar los resultados obtenidos de la segmentación. Actualmente los usuarios de estos sistemas solo cuentan con un programa funcional que corre en una terminal de computador que presenta los datos obtenidos de una manera difícil de visualizar y por lo tanto deben construir sus propios gráficos que les permita observar los resultados obtenidos. De lo anterior sale la necesidad de una herramienta que permita automatizar este proceso de manera que el investigador pueda dedicar el tiempo que actualmente invierte en estas tareas avanzando y mejorando su trabajo de investigación.
 
 ### Objetivo General
 
 Desarrollar una interfaz de visualización de los resultados de algoritmos genéticos para optimizar un conjunto de parámetros en un sistema de segmentación de audios de larga duración.
 
 ### Objetivos específicos
 
 1. Analizar un sistema de segmentación de audios de larga duración para incorporar una etapa de visualización de resultados, usando algoritmos genéticos.
 2. Comprender los conceptos asociados con algoritmos genéticos para problemas de optimización.
 3. Desarrollar una interfaz en lenguaje Python para visualizar los resultados un proceso de algoritmos genéticos.
 4. Definir un conjunto de datos de prueba para verificar los resultados y el funcionamiento del algoritmo.
 
 ### Metodología
 
 La metodología a seguir en el proyecto consiste en una serie de actividades que satisfacen los objetivos específicos. A continuación se describen las actividades a realizar en el proyecto:
 
 - Revisión del sistema de segmentación de audios de larga duración de manera que se pueda comprender y verificar su funcionamiento.
 
 - Determinar la manera en que se puede integrar la interfaz de visualización de resultados al sistema de segmentación de audios de larga duración.
 
 - Revisión bibliográfica sobre tecnologías del habla y segmentación de audios de larga duración.
 
 - Investigación sobre algoritmos genéticos y su implementación en sistemas de segmentación de audios de larga duración.
 
 - Determinar herramientas de Python útiles y que simplifiquen el proceso de desarrollo de la interfaz de visualización de resultados.
 
 - Diseño de diagramas de flujo e integración de la interfaz de visualización de resultados al sistema de segmentación de audios de larga duración.
 
 - Procesar un conjunto de datos de prueba que permita validar el funcionamiento del sistema.
 
 El informe realizado está divido en una serie de capítulos que tratan los distintos temas relacionadas al trabajo de investigación. En el capítulo 2 se presenta la teoría relacionada a sistemas de segmentación de audios de larga duración, algoritmos genéticos y interfaces de usuario. En el capítulo 3 se describe el diseño del sistema de segmentación de audios de larga duración con una interfaz de visualización de resultados mientras que en el capítulo 4 se presenta la arquitectura de software realizada. En el capítulo 5 se analizan los resultados de la segmentación de audios de larga duración con una interfaz de visualización. Finalmente en el capítulo 6 se presentan las conclusiones y recomendaciones del proyecto realizado.
 
 ## Capítulo 2 - Teoría del trabajo de investigación <a name="cap2"></a>
 
 ## Capítulo 3 - Diseño <a name="cap3"></a>
 
 ## Capítulo 4 - Arquitectura de software <a name="cap4"></a>
 
 ## Capítulo 5 - Resultados <a name="cap5"></a>
 
 ## Capítulo 6 - Conclusiones y recomendaciones <a name="cap6"></a>
 
