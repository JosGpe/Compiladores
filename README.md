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

## Gramática del compilador:

En este programa se realizó en el lenguaje de programación de Python, en la versión 3.12.0. Este programa consiste en un compilador con las fases del léxico junto con la fase del sintáctico y además trabaja con las tablas. A continuación, se describe el propósito y el flujo principal del código: 

Definición de Clases:
Se definen varias clases como ElementoPila, Terminal, NoTerminal, y Estado que se utilizan para representar diferentes elementos en el análisis léxico y sintáctico.

Análisis Léxico:
Se implementa un analizador léxico que recibe una cadena de entrada y devuelve una lista de objetos Estado que representan los tokens y símbolos encontrados en la cadena.

Tabla LR:
Se define una tabla LR que se utiliza en el parser LR para determinar las acciones a realizar (desplazar, reducir, aceptar) en función del estado actual y el símbolo de entrada.

Reglas de Producción:
Se definen reglas de producción (Regla) que se utilizan en el parser LR(1) durante las reducciones.
Implementación del Parser LR(1):
Se implementa un parser LR(1) que utiliza la tabla tlr1 para analizar la cadena de tokens generada por el analizador léxico. El parser mantiene una pila (pila) que se actualiza según las acciones de desplazamiento, reducción o aceptación. Las acciones y el estado de la pila se registran en las variables acciones y data para su posterior visualización.

Presentación de Resultados:
Al final, se presenta la salida del análisis léxico en forma tabular (usando la biblioteca tabulate), mostrando el tipo, fuente y mensaje asociado a cada token.
También se presenta la ejecución del parser LR, mostrando la pila, la entrada y las acciones realizadas. Si en resultado del léxico se encuentra una carácter no declarado/definido en una parte antes del $ se detiene con la información disponible hasta ese punto. Esto es porque se rompe el bucle principal y no se completa la exploración de la cadena de entrada.

Ejemplos:

Ejemplo 1

![image](https://github.com/JosGpe/Compiladores/assets/100324579/7e222524-fe7d-4e86-8632-ecbde8ac743a)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/34d3c854-1832-44f0-963c-60550bfa992d)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/7166c5b2-8d47-4664-8f80-d40dcc31c2a2)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/403b34d8-e8fa-4f85-9216-4eb772f125cb)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/3cbd0cce-726b-4a55-8b06-94c69500d70e)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/76c316e5-11bf-4b0b-915c-1c1fc6e073d6)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/78814e38-687b-480b-aef2-d777826039f2)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/df26749b-6399-4ec0-86ee-adae8605b2ec)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/a704cd49-129e-4b9f-a0e7-9f5a5883166e)

Ejemplo 2:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/8b91577b-3154-4b42-8487-ae499402b422)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/40551482-707b-4847-a240-eeac0061aa5d)

Ejemplo 3:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/113b6abb-964c-4eba-83e1-81e5cbeb58c6)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/5c570c90-4846-4e97-8e50-dc156071b328)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/3cf967c5-9788-4e4b-b6f1-3ac011ab58cc)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/2610ec46-3a3f-4939-91c4-2df747e08d3c)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/75ac3d43-5c98-467f-af13-c5a7c1baf8f7)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/ec387dde-dd1b-4b9c-8589-bd0a8eb0c595)

Ejemplo 4:

![image](https://github.com/JosGpe/Compiladores/assets/100324579/54c4eb92-e1f9-4d19-875d-a9d39e590f64)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/1ea24674-78a4-4886-bfb8-2d874f7a3d89)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/b5b17aff-ba87-4b5c-8c6c-bb98cd521cc9)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/106019e5-720e-495a-aa51-42fbcbd3e038)
