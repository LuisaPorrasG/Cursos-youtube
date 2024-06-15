//arreglo simplre
var miArreglo =[ "Jhon", 24];
//arreglo anidado
var listaEstudiantes = [["luisa", 23],["Claudia", 26]];
console.log(listaEstudiantes);

var listaDeProductos = [["camisa", 5.67, "S134"], ["celular", 250, "S356"], ["zapatos", 36.7, "S7678"]];
console.log(listaDeProductos);

console.log(listaDeProductos[0][0])

listaDeProductos [1][1] = "hola";
console.log(listaDeProductos[1][1]);

//METODO PUSH

var estaciones = ["inviero", "otoño", "primavera"];
estaciones.push("verano"); //agrega el elemento al final del arreglo
console.log(estaciones);

//METODO POP

var dias = ["lunes", "martes", "miercoles"];
diaEliminado = dias.pop(); //remueve el ultimo elemento del arreglo
console.log(dias);
console.log(diaEliminado);

//METODO SHIFT

var meses =["enero", "febrero", "marzo"];
meses.shift(); //remueve el primer elemento del array
console.log(meses);

//METODO UNSHIFT

var numeros=[1,2,3,4];
numeros.unshift("no es un numero"); //agrego un elemento al inicio del arrreglo
console.log(numeros);

//LISTAS ANIDADAS
var milistasDeCompras=[["cereal", 3],["leche", 2], ["galletas",4],["pan", 5], ["refresco",5], ["pollo", 7]];
console.log("voy a comprar "+ milistasDeCompras[0][1]+ " unidadaes de "+ milistasDeCompras[0][0]);
console.log("voy a comprar "+ milistasDeCompras[1][1]+ " unidadaes de "+ milistasDeCompras[1][0]);
console.log("voy a comprar "+ milistasDeCompras[2][1]+ " unidadaes de "+ milistasDeCompras[2][0]);
console.log("voy a comprar "+ milistasDeCompras[3][1]+ " unidadaes de "+ milistasDeCompras[3][0]);
console.log("voy a comprar "+ milistasDeCompras[4][1]+ " unidadaes de "+ milistasDeCompras[4][0]);
console.log("voy a comprar "+ milistasDeCompras[5][1]+ " unidadaes de "+ milistasDeCompras[5][0]);



 