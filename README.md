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

Ejemplo 1:
![image](https://github.com/JosGpe/Compiladores/assets/100324579/7e222524-fe7d-4e86-8632-ecbde8ac743a)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/34d3c854-1832-44f0-963c-60550bfa992d)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/7166c5b2-8d47-4664-8f80-d40dcc31c2a2)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/403b34d8-e8fa-4f85-9216-4eb772f125cb)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/3cbd0cce-726b-4a55-8b06-94c69500d70e)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/76c316e5-11bf-4b0b-915c-1c1fc6e073d6)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/78814e38-687b-480b-aef2-d777826039f2)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/df26749b-6399-4ec0-86ee-adae8605b2ec)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/a704cd49-129e-4b9f-a0e7-9f5a5883166e)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/8b91577b-3154-4b42-8487-ae499402b422)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/40551482-707b-4847-a240-eeac0061aa5d)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/113b6abb-964c-4eba-83e1-81e5cbeb58c6)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/5c570c90-4846-4e97-8e50-dc156071b328)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/3cf967c5-9788-4e4b-b6f1-3ac011ab58cc)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/2610ec46-3a3f-4939-91c4-2df747e08d3c)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/75ac3d43-5c98-467f-af13-c5a7c1baf8f7)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/ec387dde-dd1b-4b9c-8589-bd0a8eb0c595)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/54c4eb92-e1f9-4d19-875d-a9d39e590f64)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/1ea24674-78a4-4886-bfb8-2d874f7a3d89)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/b5b17aff-ba87-4b5c-8c6c-bb98cd521cc9)

![image](https://github.com/JosGpe/Compiladores/assets/100324579/106019e5-720e-495a-aa51-42fbcbd3e038)
