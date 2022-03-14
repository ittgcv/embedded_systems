<!DOCTYPE html>
<html lang="es">
<head>
<title>Hola, que tal {{nombre}}</title>
<meta charset="utf-8" />
</head>
<body>
    <header>
       <h1>Mi sitio web</h1>
       <p>Mi sitio web creado en html5</p>
    </header>
    <h2>Vamos a saludar</h2>
    % if nombre=="Mundo":
      <p> Hola <strong>{{nombre}}</strong></p>
    %else:
      <h1>Hola {{nombre.title()}}!</h1>
      <p>¿Cómo estás?
    %end
</body>
</html>
