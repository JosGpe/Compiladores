## Mini analizador sintáctico 

En esta practica se genera un algoritmo para analizar los códigos. Primero se define una clase con constantes que representan diferentes categorías y luego una clase llamada Stack que implementa una pila. 

![image](https://github.com/JosGpe/Compiladores/assets/100324579/76660549-d5d1-44ea-a602-1053c6f16046)

También se declara unas funciones para los ejercicios que procesan las cadenas de entrada ("hola+mundo$" y "a+b+c+d+e+f$") de acuerdo con reglas sintácticas específicas. Utilizan una instancia de la clase Stack para realizar un seguimiento de la pila durante el procesamiento y generan datos que se utilizan para mostrar una tabla que representa la pila, la entrada y la acción realizada en cada paso.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/ab085043-af53-4dc5-b3c5-46f4a438b10c)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/ff87855c-5841-4e6c-a665-7b348dea8891)

Para los resultados utilizo la biblioteca tabulate para mostrar los datos en forma de tabla.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/d1c1c219-61ba-4115-b6b8-a60125823591)

Y en el main hace el llamado de las funciones y muestra los resultados. 

![image](https://github.com/JosGpe/Compiladores/assets/100324579/e1d93592-3d19-492b-8325-7487501b3485)

Resultados: 

![image](https://github.com/JosGpe/Compiladores/assets/100324579/4566b23a-5046-445f-8f90-57cec24c9398)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/82e2f971-a3fc-4e0a-81e3-422319c7b37c)

## Analizador sintáctico con objetos

En el código se hace modificaciones al analizador, modificando el tipo de la pila para implementar el uso de objetos.  Las modificaciones que se hicieron fueron la declaración de varias clases que son la terminal, no terminal y estado, incluyendo su constructor. Esto para representar distintos tipos de elementos en la pila de manera más clara.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/65877bc3-9b9f-40cb-a57d-41461f7d6102)

El cambio de nombre de clases, además se creó una función obtener pila en la clase pila para obtener una representación de la pila en forma de lista de cadenas.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/dd911dc5-2887-41e5-a9ba-74b8c7348909)

Y en las funciones de los ejercicios se utiliza instancias de las clases pila, terminal, no terminal, y estado para representar elementos en la pila.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/34210488-dafa-4ee3-80c0-807bba11df64)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/78b4281c-5a19-416d-97a1-c1ef3936895c)

Resultados: 

![image](https://github.com/JosGpe/Compiladores/assets/100324579/3eb9a38d-b8e5-46bb-a0a2-8c446fc36eca)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/02bf281d-0544-43a5-9469-f3db65eb6a6e)
