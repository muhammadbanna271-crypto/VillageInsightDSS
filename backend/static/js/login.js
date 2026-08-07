const btn=document.getElementById("showPassword");

const pass=document.getElementById("password");

btn.onclick=()=>{

if(pass.type==="password"){

pass.type="text";

btn.innerHTML='<i class="fa-solid fa-eye-slash"></i>';

}

else{

pass.type="password";

btn.innerHTML='<i class="fa-solid fa-eye"></i>';

}

}