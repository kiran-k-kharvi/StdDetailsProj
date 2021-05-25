// ********************Button disabled************************
document.getElementById("subBtn").disabled = true

//**************************add event listener to elements********************************/

var last_name = document.getElementById("id_Last_Name").addEventListener("change",alt);
var first_name = document.getElementById("id_First_Name").addEventListener("change",alt);
var password = document.getElementById("id_Password").addEventListener("change",alt);
var email = document.getElementById("id_Email").addEventListener("change",alt);
var img = document.getElementById("id_profile_pic").addEventListener("change",alt);




function alt()
{   
    document.getElementById("subBtn").disabled = true
    var avoid = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~\d]/;
    var last_name = document.getElementById("id_Last_Name").value
    var first_name = document.getElementById("id_First_Name").value
    var password = document.getElementById("id_Password").value
    var email = document.getElementById("id_Email").value
    var img = document.getElementById("id_profile_pic").files
    if(last_name.length>0 && avoid.test(last_name)  || first_name.length>0 && avoid.test(first_name))
    {
        alert("Invalid character in first name or last name field.\n (only A-Z a-z allowed...) ")
    }
    else if (last_name.length<0||first_name.length<0)
    {
        alert("first name and last name required")

    }
    else if(password.length <8 && password.length>0)
    {
        alert("password should be atleast 8 character long...")
    }
    else if(last_name.length>0 && first_name.length>0 && password.length>0)
    {
        document.getElementById("subBtn").disabled = false
    }
    
}

const btn = document.querySelector('#subBtn');
btn.addEventListener("click", alt);



// const h2 = document.querySelector('#msg');
// btn.addEventListener("change", reg);


// let observer = new MutationObserver(reg);
  
//   // observe everything except attributes
//   observer.observe(msg, {
//     childList:true,
//     subtree:true,
//     characterData : true
//   });





// **********************************Registration successful********************
$(document).ready(function() {
    $( "#msg" ).after( setTimeout(reg, 6000));
    );
    
   });


function reg()
{
alert("REGISTRATION SUCCESSFULL...");
window.location.replace("http://facebook.com");
}