// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-analytics.js";
import {
  getAuth,
  signInWithEmailAndPassword ,
} from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC-pLnAIMclS6QgEVRD3mC0Mvx6UtUSSQ0",
  authDomain: "inventory-management-sys-560b1.firebaseapp.com",
  projectId: "inventory-management-sys-560b1",
  storageBucket: "inventory-management-sys-560b1.firebasestorage.app",
  messagingSenderId: "771187231984",
  appId: "1:771187231984:web:fab69a3ab1af7405490635",
  measurementId: "G-Q5LK8QQKCB",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app); 

const loginbutton = document.getElementById("loginbutton");

loginbutton.addEventListener("click", (e) => {
    e.preventDefault();

  //get input values
  const email = document.getElementById("emailtext").value.trim();
  const repasswordtext = document.getElementById("passwordtext").value.trim();

  //check if all fields are filled
  if (
    email === "" ||
    repasswordtext === ""
  ) {
    alert("Please fill all fields");
    return;
  } else if (repasswordtext.length < 6) {
    alert("Password must be at least 6 characters");
    return;
  } else {
    signInWithEmailAndPassword(auth, email, repasswordtext)
      .then((userCredential) => {
        // Signed in
        const user = userCredential.user;
        // Set session in Flask
        fetch("/set_session", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: email })
        })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            alert("Login successful!");
            if(email === "danushanandan1@gmail.com" && repasswordtext === "123456"){
              window.location.href = "./dashboard";
            } else {
              window.location.href = "./customerdashboard";
            }
          } else {
            alert("Session error!");
          }
        });
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        alert(errorMessage);
        // ..
      });
  }
});
