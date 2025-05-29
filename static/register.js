// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-analytics.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import {
  getDatabase,
  ref,
  set,
} from "https://www.gstatic.com/firebasejs/11.6.1/firebase-database.js";
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
const db = getDatabase(app);

function saveUserProfile(uid, email, name, contact , repasswordtext) {
  return set(ref(db, `users/${uid}`), {
    email: email,
    name: name,
    contact: contact,
    Pass: repasswordtext,
  });
}

const registerbtn = document.getElementById("registerbutton");

registerbtn.addEventListener("click", async (e) => {
  e.preventDefault();

  //get input values
  const email = document.getElementById("reemailtext").value.trim();
  const Nametext = document.getElementById("Nametext").value.trim();
  const repasswordtext = document.getElementById("repasswordtext").value.trim();
  const contacttext = document.getElementById("contacttext").value.trim();

  //check if all fields are filled
  if (
    email === "" ||
    Nametext === "" ||
    repasswordtext === "" ||
    contacttext === ""
  ) {
    alert("Please fill all fields");
    return;
  } else if (repasswordtext.length < 6) {
    alert("Password must be at least 6 characters");
    return;
  } else if (contacttext.length < 10) {
    alert("contact must be at least 10 characters");
    return;
  } else {
    // createUserWithEmailAndPassword(auth, email, repasswordtext)
    //   .then((userCredential) => {
    //     // Signed up
    //     const user = userCredential.user;
    //     alert("Registration successful!");
    //     window.location.href = "./Login.html";
    //     // ...
    //   })
    //   .catch((error) => {
    //     const errorCode = error.code;
    //     const errorMessage = error.message;
    //     alert(errorMessage);
    //     // ..
    //   });

    try {
      //Create user in Firebase Auth
      const userCredential = await createUserWithEmailAndPassword(
        auth,
        email,
        repasswordtext
      );
      const uid = userCredential.user.uid;

      //Save user profile in RTDB
      await saveUserProfile(uid, email, repasswordtext, contacttext , repasswordtext);

      alert("Registration successful!");
      window.location.href = "./login";
    } catch (error) {
      console.error("Registration error:", error);
      alert(error.message);
    }
  }
});
