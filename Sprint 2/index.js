const pagos = [];
const usuarios = [];
const lista = document.querySelector("#list-group");
const resultados = document.querySelector("#total");
const usuario = document.querySelector("#nombre")
const pago = document.querySelector("#pago")

function repartir(){
    agregarGasto();
    ultimoAPantalla();
    mostrarPago();
}

function agregarGasto(){
    usuarios.push(usuario.value);
    pagos.push(pago.value);
}

function ultimoAPantalla(){
    const li = document.createElement("li");
    const text = document.createTextNode(`${usuario.value}: Pagó $${pago.value}`);
    li.classList.add("list-group-item");
    li.appendChild(text);
    lista.appendChild(li);
}

function sumarValores(pagos){
    let suma = 0;
    for (let pago of pagos){
        suma += parseInt(pago);
    }
    return suma;
}

function mostrarPago(){
    const total = sumarValores(pagos);
    const aporteIndividual = total/usuarios.length;
    resultados.innerText = `Total: ${total}
                            A cada uno le toca aportar: ${aporteIndividual.toFixed(2)}`;
    
}