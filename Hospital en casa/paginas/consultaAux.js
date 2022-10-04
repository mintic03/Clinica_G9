const getCustomersUrl = 'https://apiclinicag9.herokuapp.com/getAllPacientes';
//const getCustomersUrl = 'http://127.0.0.1:8000/getAllCustomers';

customer = [];

function getCustomers() {
  // Petición HTTP
  fetch(getCustomersUrl)
    .then(response => {
      console.log(response);
      if (response.ok)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
       console.log("Datos: " + data);
       customer = JSON.parse(data);
      handleCustomers();
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handleCustomers() {
  const divs = [];
  customer.forEach((cust) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3>id: ${cust.id}</h3>
      <h3>nombre: ${cust.nombre}</h3>
      <h3>apellido: ${cust.apellido}</h3>
      <h3>telefono: ${cust.telefono}</h3>
      <h3>genero: ${cust.genero}</h3>
      <h3>direccion: ${cust.direccion}</h3>
      <h3>ciudad: ${cust.ciudad}</h3>
      <h3>fechaNacimiento: ${cust.fecha_Nacimiento}</h3>
      <h3>latitud: ${cust.latitud}</h3>
      <h3>longitud: ${cust.longitud}</h3>
      `;
    divs.push(div);
  });
  
 
  const info = document.getElementById("Hola Juliana Vargas");
  divs.forEach(div => info.appendChild(div));
  
}
function handleError() {
    
    const message = document.createElement("p");
    message.innerText = "No se pudo cargar la información. Intente más tarde.";
    const info = document.getElementById("Hola Juliana Vargas");
    info.appendChild(message);
    
  }
  
  //-----------------------------------
  
document.addEventListener("DOMContentLoaded", getCustomers);