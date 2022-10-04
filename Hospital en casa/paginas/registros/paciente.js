//const newPacienteUrl = 'https://apiclinicag9.herokuapp.com/newPacien';
const newPacienteUrl = 'http://127.0.0.1:8000/newPacien';

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
  const id = document.newPaciente.id.value;
  const direccion = document.newPaciente.direccion.value.trim();
  const ciudad = document.newPaciente.ciudad.value.trim();
  const fecha = document.newPaciente.fecha.value;
  const latitud = document.newPaciente.latitud.value;
  const longitud = document.newPaciente.longitud.value;

  // let result = validate_id(id);
  // if (result) {
  //   alert ("cedula no es valida");
  //   return;
  // }

  const paciente = {
    id: id,
    direccion: direccion,
    ciudad: ciudad,
    fecha: fecha,
    latitud: latitud,
    longitud: longitud,

  };
  console.log(paciente);
  const dataToSend = JSON.stringify(paciente);
  savePaciente(dataToSend);
}

function savePaciente(data) {
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


  fetch(newPacienteUrl, requestOptions)
    .then((response) => {response.text()})
    .then((result) => {
      if (result === "Paciente Agregada"){
        handleSuccess(result);
      } else if (
        result === "ya existe docuemnto "
      ){
        handleError(result);
      }
    });
}

function handleSuccess(){
   document.getElementById("formPaciente").remove();
   const message = document.createElement("p");
   message.innerText = "paciente  agregado";
   const info = document.getElementById("info");
   info.appendChild(message);
}

function handleError(){
   document.getElementById("formPaciente").remove();
   const message = document.createElement("p");
   message.innerText = "mo se pudo agregar el paciente";
   const info = document.getElementById("info");
   info.appendChild(message);
}



document.newPaciente.addEventListener("submit", recopilacionDatos);