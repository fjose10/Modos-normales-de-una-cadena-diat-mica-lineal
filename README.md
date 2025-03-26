# Contextualización y análisis

Este script surge del análisis dinámico de una cadena lineal diatómica de masas M1 y M2 (con M1 siendo mayor a M2), con separación entre cada vecino igual a "a" y modelando las fuerzas interatómicas como resortes de constante C y con interacciones solo entre los vecinos más inmediatos.
El análisis dinámico y la solución del sistema de ecuaciones brinda una frecuencia de oscilación que depende de las constantes del sistema y del valor de un vector de onda "k", creándose dos "ramas" de vibración posibles en el sistema, conocidas como
rama acústica y rama óptica. 
En el análisis dinámico, cada átomo tiene una posición fija "x0" y la solución que encontramos de las leyes de Newton nos brinda u(t), en lugar de x(t), siendo u(t) el desplazamiento respecto a la posición de equilibrio de cada átomo. Así, la posición de cada átomo 
en el tiempo está dada por x(t) = u(t) + x0.
Como un aspecto importante antes de realizar la animacion, atendiendo a la rama que se grafique, el comportamiento de u(t) de cada atomo va a variar de acuerdo a si uno es mas masivo que el otro. Del análisis dinámico, se encuentra la siguiente relación entre las amplitudes
de oscilación de los átomos M1 y M2,

![image](https://github.com/user-attachments/assets/6b294b76-3ef6-4da7-8fde-6b1d9ed4da9b)

De las cuales solo se toma la parte real de esta ecuación. 

En la rama acustica, que se caracteriza por poseer frecuencias bajas, los atomos más pesados van a experimentar fuerzas más pequeñas, lo que se traduce en que su movimiento es prácticamente oscilatorio sin ningún tipo de afectación. En caso contrario, los átomos más ligeros sufren la inercia también de los pesados y es por esto por lo que el desplazamiento u(t) de los átomos ligeros adquiere una forma más compleja que cuantifica la interacción con los átomos pesados. 

En la rama óptica, las frecuencias son altas, lo que se traduce en oscilaciones más "fuertes". Esto implica que los átomos de menor masa van a tener una amplitud de oscilación la cual va a estar prácticamente determinada por la fuerza externa del movimiento
y no por las interacciones con los átomos pesados, por lo que su movimiento es oscilatorio simple. Contrariamente, los átomos pesados sí sufren la interacción con los ligeros, por lo que su desplazamiento u(t) es más complejo. 

El gráfico de los "modos normales" surge de condiciones matemáticas a los valores posibles del vector de onda "k" que se imponen al sistema para evitar problemas en los "bordes" de la cadena. Estas condiciones, en este caso siendo las de Born-Von Karmann, llevan a que
solo se puedan tener vectores de onda k iguales a un múltiplo entero de 2pi/N. 

# Lógica del código

Habiendo hecho ya el análisis físico, el paso a código es bastante directo, puesto que poseemos soluciones u(t) para cada átomo en cada rama, por lo que es una mera cuestión de calcularlas en cada instante para un determinado intervalo, algo que podemos hacer
con ciclos for sobre listas que definan tanto el intervalo de tiempo y su paso temporal "dt", así como listas que contengan la posición de cada átomo en la cadena. 
El desplazamiento del enésimo átomo en la cadena en el instante t, se almacena en un array de dimensiones T x N (Con T siendo el número de pasos en el tiempo y N el número de átomos), cuyas filas detallan cada instante en el tiempo y cuyas columnas son la posición
del n-esimo átomo en ese instante. Esto se grafica con matplotlib con ayuda de la función "scatter" y de librerías de animación. 
Para observar la animación, se introducen las constantes del sistema, M1, M2, C, a y el valor de k (recordando que SOLO SE ADMITEN valores enteros de 2pi/N) y se procede a correr el código. 

# Interpretación del resultado

La representación visual de las soluciones permite obtener una idea intuitiva del resultado, el cual regularmente posee una expresión matemática que no es sencilla de interpretar. Lo que observamos en el código son los diferentes valores de k, los cuales corresponden a las formas más "básicas" de vibración del sistema, es decir, determinan las frecuencias posibles a las que el sistema puede oscilar. En particular, estos tipos de vibración son de interés puesto que con estas frecuencias, se puede determinar la energía interna del sistema y por medio de otras relaciones matemáticas, propiedades como la capacidad calorífica, conductividad eléctrica y térmica se pueden predecir. 
