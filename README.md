## Mini analizador léxico:

En este archivo .py que es un analizador léxico como se indica su nombre, actualmente identifica los siguientes tokens (identificador, entero o real):

Identificadores:

En la variable codigo que está ubicado casi al final del archivo si escribo Hola2, al momento de correr el programa saldrá un mensaje el cual el token ya sea identificador, entero o real, el tipo y valor declaro en la variable.
 
![image](https://github.com/JosGpe/Compiladores/assets/100324579/753125e6-408d-4add-bdf6-6c44b48f1389)

Enteros:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/9080665f-a7ec-49ed-9dfe-9a0942cacfcf)

Reales:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/004d7955-a942-41a6-8d18-3b325ba558de)

Si escribo un carácter, símbolo o token que no esté declarado en el analizador, saltara una excepción con un mensaje.  

![image](https://github.com/JosGpe/Compiladores/assets/100324579/30e73238-a7d9-4056-b8fe-964a3388e8bd)

## Analizador léxico completo

En comparación del mini analizador, esta versión reconoce más símbolos (los que se requiere en el archivo), ahora el funcionamiento del código es el siguiente: 

En la función analizador léxico toma el código fuente como entrada y produce una lista de tokens. Los tokens se almacenan como tuplas en la lista tokens, y cada tupla tiene tres elementos: el símbolo del token, el código y el valor asociado.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/4229925d-1ccf-44d4-a4b5-a24c3acb6693)

Después en la función agregar_token se utiliza para agregar un nuevo token a la lista de tokens utilizando como entrada los valores que se mencionan en los tokens.  Además, utiliza un bucle while para iterar a través de cada carácter en el código fuente y dependiendo del estado actual del analizador léxico, se realizan acciones específicas para reconocer y clasificar los tokens.  

![image](https://github.com/JosGpe/Compiladores/assets/100324579/6970b51a-3990-4535-bbf9-9f74247f38fb)

El analizador utiliza un enfoque basado en estados para reconocer diferentes tipos de tokens.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/a4e54418-cc5c-4584-82cf-861f6a089e83)

Y, por último, para mostrar los resultados ahora uso una librería que es tabulate para imprimir los tokens en forma de tabla.

![image](https://github.com/JosGpe/Compiladores/assets/100324579/9c6de79c-f79e-4722-a3d0-b9b305371e06)

Resultados:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/446a7d70-8940-4826-920e-bd4530c354ec)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/56356ca6-189f-4cd7-9239-3122fb375544)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/d3cfb209-ed51-4b3a-a121-aba63b5aab52)

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
