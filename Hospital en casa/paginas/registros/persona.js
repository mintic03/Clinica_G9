const newPersonaUrl = 'https://apiclinicag9.herokuapp.com/newPersona';
//const newPersonaUrl = 'http://127.0.0.1:8000/newPersona';

//customer = [];

function validate_name(val){
  const letters = /^[A-Z-a-z]+$/;
  if (val.match(letters)) return true;
  else return false;
}

// function validate_id(val){
//   if (Number(val) > 1000){
//     if (Number(val <= 99999999999)) return true;
//   } else return false;
// }

function recopilacionDatos(evt){
  evt.preventDefault();
  const id = document.newPersona.id.value;
  const nombre = document.newPersona.nombre.value.trim();
  const apellido = document.newPersona.apellido.value.trim();
  const telefono = document.newPersona.telefono.value;
  const genero = document.newPersona.genero.value;

  // let result = validate_id(id);
  // if (result) {
  //   alert ("cedula no es valida");
  //   return;
  // }

  const persona = {
    id: id,
    nombre: nombre,
    apellido: apellido,
    telefono: telefono,
    genero: genero,

  };
  console.log(persona);
  const dataToSend = JSON.stringify(persona);
  savePersona(dataToSend);
}

function savePersona(data) {
  // Petición HTTP

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = data;

  
  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow',
  };


  fetch(newPersonaUrl, requestOptions)
    .then((response) => {response.text()})
    .then((result) => {
      if (result === "Persona Agregada"){
        handleSuccess(result);
      } else if (
        result === "ya existe docuemnto "
      ){
        handleError(result);
      }
    });
}

function handleSuccess(){
   document.getElementById("formPersona").remove();
   const message = document.createElement("p");
   message.innerText = "persona  agregado";
   const info = document.getElementById("info");
   info.appendChild(message);
}

function handleError(){
   document.getElementById("formPersona").remove();
   const message = document.createElement("p");
   message.innerText = "mo se pudo agregar la persona";
   const info = document.getElementById("info");
   info.appendChild(message);
}



document.newPersona.addEventListener("submit", recopilacionDatos);