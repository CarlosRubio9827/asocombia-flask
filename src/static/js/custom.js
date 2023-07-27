const validateLength = () => {
  const messageElement = document.getElementById("mensaje");
  let message = messageElement.value.trim();
  const count = message.length;

  if (count > 250) {
    alert("El mensaje no puede superar los 250 caracteres.");
    message = message.slice(0, 200); // Elimina el último carácter para que el mensaje tenga 200 caracteres
    messageElement.value = message; // Actualiza el valor del elemento con el mensaje modificado
  }
};
