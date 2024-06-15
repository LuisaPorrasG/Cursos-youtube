//FUNCION SIMPLE SIN ARGUMENTOS
function mostrarMensaje(){
    console.log("Hola Mundo")
}

mostrarMensaje();
mostrarMensaje();

//FUNCION CON ARGUMENTOS 
function sumar(a,b){
    var suma = a+b;
    console.log("la suma de "+ a + " + "+ b+ " es :" +  suma);

}


sumar(5,3);
sumar(5,5);

var x = 5;
var y= 10;
sumar(x,y);

function concatenarCadenas(cadena1, cadena2, cadena3){
    console.log(cadena1 + " " + cadena2 + " " + cadena3)
}

concatenarCadenas("Luisa", "Fernanda", "Porras");
//--------------------------------------------------------------------------------------------------------
//TIPOS DE VARIABLES

//global, esta definida en la parte principal del código
var edad = 23; //global

function miEdad(){
    console.log(edad);
}

miEdad();
//---------------------------------------------------------------------------------------------------------
//RETORNO DE FUNCIONES
function sumatoria (a,b){
    return a+b;
}

console.log(sumatoria(5,2));

//ASIGNACIÓN DE RETURN DE FUNCION A UNA VARIABLE

function resta(a,b){
    return a -b;
}

var resultado = resta(5,3);
console.log(resultado);


//ejemlo2

function crearCadenaConMeta(lenguajeProgramacion){
    return "mi meta es aprender: " + lenguajeProgramacion;
}

crearCadenaConMeta("javaScript");
var resultado = crearCadenaConMeta("javaScript");
console.log(resultado);

