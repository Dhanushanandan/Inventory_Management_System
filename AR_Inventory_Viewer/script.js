
  const firebaseConfig = {
    apiKey: "AIzaSyB0zhVa_qGrfOLtdt9QMkdtBvTJAwqwsD8",
    authDomain: "supermarket-inventory-e6ed7.firebaseapp.com",
    databaseURL: "https://supermarket-inventory-e6ed7-default-rtdb.firebaseio.com",
    projectId: "supermarket-inventory-e6ed7",
    storageBucket: "supermarket-inventory-e6ed7.appspot.com",
    messagingSenderId: "980166513047",
    appId: "1:980166513047:web:5bf3f72202a5be8a40b4d2",
    measurementId: "G-2HE3ETGSPE"
  };

  firebase.initializeApp(firebaseConfig);
  const db = firebase.database();

  window.addEventListener("DOMContentLoaded", () => {
    const markers = ["milk-marker", "bread-marker"];

    markers.forEach((markerId) => {
      const marker = document.querySelector(`#${markerId}`);
      const info = document.querySelector(`#${markerId.replace("-marker", "Info")}`);

      marker.addEventListener("markerFound", () => {
        const productRef = db.ref("products/" + markerId);
        productRef.once("value").then((snapshot) => {
          const data = snapshot.val();
          if (data) {
            info.setAttribute("value", `${data.name}\nPrice: $${data.price}\nStock: ${data.quantity}`);
          } else {
            info.setAttribute("value", "Product not found");
          }
        });
      });

      marker.addEventListener("markerLost", () => {
        info.setAttribute("value", "");
      });
    });
  });
