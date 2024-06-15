//Proximo en la fila

/**
 * defina una funcion proximoEnLaFila que tome un arreglo (arreglo) y un numero (elemento) como argumentos.
 * Agrega el numero al final del arreglo y luego elinima el primer elemento del arreglo.La función proximo
 * en la Fla debe retornar el elemento que removio
 */
var arreglo = [1,2,3,4,5]; 

function proximoEnLaFila (arreglo, elemento){

  arreglo.push(elemento); //agregar elemento al final del arreglo
  return arreglo.shift(); //no toma ningun argumento ya que elimina el primer elemto del arreglo
  //shift es el metodo que va a eliminar el primer elemento del arreglo
  
}

console.log("Antes: " + JSON.stringify(arreglo)); //JSON.stringify es una funcion que me permite mostar arrreglos
                                                   // de una forma mas presentable
console.log(proximoEnLaFila(arreglo,6)); //retorna el valorremovido
console.log("Despues: " + JSON.stringify(arreglo));
