const newRegistroUrl = 'https://apiclinicag9.herokuapp.com/newRegistro';
//const newRegistroUrl = 'http://127.0.0.1:8000/newRegistro';

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
  const id = document.newRegistro.id.value;
  const contrase = document.newRegistro.contrase.value.trim();
  

  // let result = validate_id(id);
  // if (result) {
  //   alert ("cedula no es valida");
  //   return;
  // }

  const registro = {
    id: id,
    contrase: contrase,  

  };
  console.log(registro);
  const dataToSend = JSON.stringify(registro);
  saveRegistro(dataToSend);
}

function saveRegistro(data) {
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


   fetch(newRegistroUrl, requestOptions)
     .then((response) => {response.text()})
     .then((result) => {
       if (result === "Registro Exitoso"){
         handleSuccess(result);
       } else if (
         result === "ya existe docuemnto "
       ){
         handleError(result);
       }
     });
    // fetch(newRegistroUrl, requestOptions)
    //     .then(response => response.text())
    //     .then(result => console.log(result))
    //     .catch(error => console.log('error', error));
}

function handleSuccess(){
   document.getElementById("formRegistro").remove();
   const message = document.createElement("p");
   message.innerText = "Registro  agregado";
   const info = document.getElementById("info");
   info.appendChild(message);
}

function handleError(){
   document.getElementById("formRegistro").remove();
   const message = document.createElement("p");
   message.innerText = "mo se pudo registrar la persona";
   const info = document.getElementById("info");
   info.appendChild(message);
}



document.newRegistro.addEventListener("submit", recopilacionDatos);