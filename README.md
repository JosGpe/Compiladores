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
